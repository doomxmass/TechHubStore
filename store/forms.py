from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm




#---------------$ upgrade exist user form $---------------#
class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    #- customize form style -#
    def __init__(self, *args, **kwargs):
        super(UpdateUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})




#---------------$ register fom $---------------#
class RegisterNewUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    #- customize form style -#
    def __init__(self, *args, **kwargs):
        super(RegisterNewUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})


#---------------$ EditProfle form $---------------#
class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

    #- customize form style -#
    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'description'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Image'})




#---------------$ product form $---------------#
class AddProduct(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'


    #- customize form style -#
    def __init__(self, *args, **kwargs):
        super(AddProduct, self).__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'class': 'form-control-choices', 'placeholder': 'Tags'})
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Category'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'price'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file', 'placeholder': 'Upload an image'})



#---------------$ tags form $---------------#
class AddTags(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ['name']

    #- customize form style -#
    def __init__(self, *args, **kwargs):
        super(AddTags, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})



#---------------$ home messages form $---------------#
class AddHomeMessages(forms.ModelForm):

    class Meta:
        model = HomeMessages
        fields = '__all__'

    #- customize form style -#
    def __init__(self, *args, **kwargs):
        super(AddHomeMessages, self).__init__(*args, **kwargs)

        self.fields['left_message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Left message'})
        self.fields['middle_message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Middle message'})
        self.fields['right_message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Right message'})
        self.fields['show'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Show Messages Bar'})



#> reset password forms section <#
#---------------$ password reset form $---------------#
#- reset password email form (enter email page) -#
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your email address',
            'style': 'width: 100%',
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Optionally add custom validation logic
        return email
    


#- reset password confirm form (enter new pass and confirm pass) -#
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm new password"
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user', None)  # Get the user from kwargs
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # Call the parent save method to save the new password
        return super().save(commit=commit)
