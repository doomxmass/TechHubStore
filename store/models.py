import os
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from main.settings import BASE_DIR




#---------------$ tags model $---------------#
class Tags(models.Model):
    name = models.CharField(max_length=15,null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name



#---------------$ products model $---------------#
class Products(models.Model):
    CHOICES = {
        'Jeans':'Jeans',
        'T-Shirt':'T-Shirt',
        'Jacket':'Jacket'
    }

    tags = models.ManyToManyField(Tags,blank=True,default='Unknown')
    name = models.CharField(max_length=15,null=True)
    description = models.TextField(max_length=100,null=True,blank=True,default='No Description!')
    category = models.CharField(max_length=25,null=True,choices=CHOICES)
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    image = models.ImageField(upload_to='products/%Y%b%d',
                              default='default_files/default_product.png')
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    



#---------------$ profile model $---------------#
#- Function to generate dynamic file path
def user_directory_path(instance, filename):
    #> File will be uploaded to MEDIA_ROOT/<username>/<year><month>/<filename> <#
    username = instance.user.username  #- Assuming there's a user foreign key in your model
    date_path = datetime.now().strftime('%Y-%b-%d')  #- Format as %Y%b%d (like  2024-OCT-01)
    return f'{username}/{date_path}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=18,null=True,blank=True,default='+* *** *** ****')
    description = models.TextField(max_length=500,null=True,blank=True,default='No Description!')
    image = models.ImageField(upload_to=user_directory_path,
                              default='default_files/default_user.png')
    
    def __str__(self):
        return self.user.username
    


#---------------$ cart model $---------------#
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


#---------------$ cart items model $---------------#
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"USER :( {self.cart.user.username} ), PRODUCT : ( {self.products.name} )"
    




#---------------$ home messages [reklams] model $---------------#
class HomeMessages(models.Model):
    SHOW_CHOICES = {
        True:'YES',
        False:'NO'
    }   

    left_message = models.TextField(max_length=35,blank=True, null=True)
    middle_message = models.TextField(max_length=35,blank=True, null=True)
    right_message = models.TextField(max_length=35,blank=True, null=True)
    show = models.BooleanField(default=False,null=True,choices=SHOW_CHOICES)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.left_message} - {self.date}'




#---------------$ index box [for contact] messages $---------------#
class IndexBox(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=60, null=True)
    title = models.CharField(max_length=30, null=True)
    message = models.TextField(max_length=1000, null=True)
    sened_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.email} - title : {self.title}'
        