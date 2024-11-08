from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from .forms import RegisterNewUser
from .forms import EditProfile
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
#- for recaptcha setting -#
import requests
from django.conf import settings
#- decorator -#
from .decorator import user_is_logged_in



#---------------$ home function $---------------#
def home_func(req):
    #- show or hide homemessages bar -#
    messages_order = HomeMessages.objects.all()

    #- show latest (newest) added products by date -#
    if 'jeans' in req.POST:
        all_products = Products.objects.filter(category='Jeans')
    elif 'tshirt' in req.POST:
        all_products = Products.objects.filter(category='T-Shirt')
    elif 'jacket' in req.POST:
        all_products = Products.objects.filter(category='Jacket')
    else:
        all_products = Products.objects.all()

    #> get just latest 8 new added items <#
    products = list(reversed(all_products))[:8]

    ctx = {
        'home_messages':messages_order,
        'products':products
    }
    return render(req, 'home.html', ctx)



#---------------$ register function $---------------#
def register_func(req):
    form = RegisterNewUser()
    if req.method == 'POST':
        email=req.POST.get('email')
        exist_email = User.objects.filter(email=email).exists()

        if exist_email:
            messages.error(req, 'This Email Already Exist!')
        else:
            form = RegisterNewUser(req.POST)
            if form.is_valid():

                #- confirm recaptcha befor save -#
                recaptcha_response = req.POST.get('g-recaptcha-response')
                data = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response':recaptcha_response
                }
                r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
                result = r.json()
                if result['success']:
                    form.save()
                    return redirect('login_page')
                else:
                    messages.error(req, 'Invalid Recaptcha! Try Again')

    ctx = {'registerForm':form}
    
    return render(req,'register.html',ctx)



#---------------$ login function $---------------#
def login_func(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        
        user = authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('home_page')
        else:
            messages.error(req, 'Invalid username or password.')
            return redirect('login_page')

    return render(req,'login.html')


#---------------$ logout function $---------------#
def logout_func(req):
    logout(req)
    return redirect('login_page')



#---------------$ product details [all users] function $---------------#
@user_is_logged_in(['user','admin'])
def product_details_func(req, product_id):
    selected_product = get_object_or_404(Products,id=product_id)

    #- get 4items from same gategory to show as RELATED PRODUCTS in produt details page -#
    #> reversed for getting newest added products by date <#
    all_products_by_category = Products.objects.filter(category=selected_product.category)
    related_products = list(reversed(all_products_by_category))[:4]
    
    ctx = {
        'product':selected_product,
        'related_products':related_products
    }
    return render(req, 'product_details.html', ctx)



#---------------$ add product to cart function $---------------#
@user_is_logged_in(['user','admin'])
def add_to_cart_func(req, product_id):
    selected_product = get_object_or_404(Products,id=product_id)
    exist_cart = get_object_or_404(Cart,user=req.user)

    if req.method == 'POST':

        #- check if this product exist in cartitem or not
        cart_item, created = CartItem.objects.get_or_create(cart=exist_cart, products=selected_product)

        #- get quantity (peaces) [mostbe integer] -#
        quantity_value = int(req.POST.get('quantity', 1))

        #- if same product exist just add +1 quantity dont add new same product -# 
        if not created:
            cart_item.quantity += quantity_value
        else:
            cart_item.quantity = quantity_value

        cart_item.save()

        messages.success(req,
        f'{quantity_value} Peaces Of [ {selected_product.name} ] Added To Cart Successfully.')

    else:
        messages.error(req,'Somthing Going Wrong, Try Again!')

    #- redirect to this page with product id -#
    return redirect('product_details_page', product_id=product_id)



#---------------$ shop page $---------------#
show_list = [16]
def shop_func(req):
    #- filter -#
    if 'jeans' in req.POST:
        products = Products.objects.filter(category='Jeans')
        title = 'Jeans'
    elif 'jacket' in req.POST:
        products = Products.objects.filter(category='Jacket')
        title = 'Jacket'
    elif 'tshirt' in req.POST:
        products = Products.objects.filter(category='T-Shirt')
        title = 'T-Shirt'
    else:
        products = Products.objects.all()
        title = 'All'

    end_items = False
    message = ''
    products_count = products.count()

    #- when load more button clicked add 4 items more -#
    if req.method == 'POST':
        if products.count() <= show_list[-1]:
            all_produts = products
            end_items = True
            message = 'END'
        else:
            show_list.append(show_list[-1] + 16)
            all_produts = list(products)[:show_list[-1]]

    else:
        #- if open page first time get just 8 items -#
        if len(show_list) > 1:
            show_list.clear()
            show_list.append(16)
        all_produts = list(products)[:16]

    ctx = {
        'products_count':products_count,
        'all_produts':all_produts,
        'end':end_items,
        'message':message,
        'title':title
    }
    return render(req, 'shop.html', ctx)



#---------------$ user proile function $---------------#
@user_is_logged_in(['user','admin'])
def user_profile_func(req, user_id):
    user = get_object_or_404(User,id=user_id)
    cart = get_object_or_404(Cart,user=req.user)
    #- added items in cart -#
    cart_items_count = CartItem.objects.filter(cart=cart).count()

    
    ctx = {
        'user':user,
        'cart_items_count':cart_items_count
    }
    return render(req, 'user_profile.html', ctx)



#---------------$ user cart items function $---------------#
@user_is_logged_in(['user','admin'])
def cart_items_func(req):
    cart = get_object_or_404(Cart,user=req.user)
    #- added items in cart -#
    cart_items = CartItem.objects.filter(cart=cart)
    cart_items_count = cart_items.count()
    

    ctx = {
        'cart_items':cart_items,
        'cart_items_count':cart_items_count
    }
    return render(req, 'cart_items.html', ctx)



#---------------$ edit profile function $---------------#
@user_is_logged_in(['user','admin'])
def edit_profile_func(req, user_id):
    user = get_object_or_404(User,id=user_id)
    profile = get_object_or_404(Profile,user=user)
    form = EditProfile(instance=profile)

    #- update informatons -#
    if req.method == 'POST':
        form = EditProfile(req.POST,req.FILES, instance=profile)
        if form.is_valid():
            form.save()
            
            return redirect('user_profile_page', user_id=user_id)
        
    ctx = {
        'form':form
    }
    
    return render(req, 'edit_profile.html', ctx)



#---------------$ contact page $---------------#
def contact_func(req):
    message = ''
    if req.method == 'POST':
        first_name = req.POST.get('firstname')
        last_name = req.POST.get('lastname')
        email = req.POST.get('email')
        subject = req.POST.get('subject')
        body = req.POST.get('body')
        full_name = f'{first_name} {last_name}'

        if first_name and last_name and email and subject and body:
            indexbox = IndexBox(name=full_name,
                            email=email,
                            title=subject,
                            message=body)
            indexbox.save()
            #- if message saved in model successfully send message to admin for check inbox -#
            email_message_body = f'''
            username : {full_name}
            email : {email}
            title : {subject}
            body : {body}
            '''
            send_mail(
                f"Message From Contact Section (techhubStore)",
                email_message_body,
                "djangodjngo@gmail.com",
                ['doomxmass1@gmail.com',], #> most be a list <#
                fail_silently=False,
            )

            #- message sended successfully -#
            message = f'Dear {full_name} your Message Has Been Sended Successfuly.'

        else:
            #- message unsended (error) -#
            message = 'Somthing Going Wrong! Try Again.'

    return render(req, 'contact.html', {'message':message})



#---------------$ error 404 function $---------------#
def error_404_func(req):
    return render(req, 'error/error_404.html')