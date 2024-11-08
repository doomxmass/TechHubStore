from django.urls import path
from . import views
from .custom_reset_password_forms import *
from . import adminViews
#- change passwword view -#
from django.contrib.auth import views as authViews

urlpatterns = [
    #- home page -#
    path('', views.home_func, name='home_page'),
    #- resgister -#
    path('register/', views.register_func, name='register_page'),
    #- login -#
    path('login/', views.login_func, name='login_page'),
    #- log-out -#
    path('logout/', views.logout_func, name='logout_page'),
    #- change password link AMDIN PAGE -#
    # path('password/reset', authViews.PasswordResetView.as_view(), name='password_reset'),
    # path('password/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #: my custom reset password page :#
    path('password/reset', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #> after this dont forget to go to admin dashboard and in sites section change example.com to localhost:8000 <#
    #---------------$ Dashboard $---------------#
    #- dashboard -#
    path('dashboard/', adminViews.dashboard_func, name='dashboard_page'),
    #---------------$ product [admin] section $---------------#
    #- add product -#
    path('product/add/', adminViews.add_product_func, name='add_product_page'),
    #- show a product -#
    path('product/info/<str:product_id>/', adminViews.show_product_func, name='product_info_page'),
    #- delete a product -#
    path('product/delete/<str:product_id>-<str:name>/', adminViews.delete_product_func, name='delete_product_page'),
    #- edit a product -#
    path('product/edit/<str:product_id>/', adminViews.edit_product_func, name='edit_product_page'),
    #---------------$ user [admin] section $---------------#
    #- add new user -#
    path('user/add/', adminViews.add_user_func, name='add_user_page'),
    #- show a user -#
    path('user/info/<str:user_id>/', adminViews.show_user_func, name='user_info_page'),
    #- delete a user -#
    path('user/delete/<str:user_id>-<str:name>/', adminViews.delete_user_func, name='delete_user_page'),
    #- edit a user -#
    path('user/edit/<str:user_id>/', adminViews.edit_user_func, name='edit_user_page'),
    #---------------$ tags [admin] section $---------------#
    #- add tag -#
    path('tags/add/', adminViews.add_tag_func, name='add_tag_page'),
    #- delete tag -#
    path('tags/delete/<str:tag_id>_<str:name>', adminViews.delete_tag_func, name='delete_tag_page'),
    #---------------$ home messages [admin] section$---------------#
    #- add message -#
    path('home/messages/add/', adminViews.home_messages_func, name='home_messages_page'),
    #---------------$ product [for All users] section $---------------#
    #- product details -#
    path('product/details/<str:product_id>/', views.product_details_func, name='product_details_page'),
    #- add product to CART -#
    #: EMPTY LINK (no HTML page) just link to get infos :#
    path('product/add/cart/<str:product_id>/', views.add_to_cart_func, name='add_to_cart'),
    #---------------$ shop section $---------------#
    #- shop page -#
    path('shop/', views.shop_func, name='shop_page'),
    #---------------$ user profile section $---------------#
    #- profile page -#
    path('user/profile/<str:user_id>/', views.user_profile_func, name='user_profile_page'),
    #- cart added items page -#
    path('user/profile/cart/items/', views.cart_items_func, name='cart_items_page'),
    #- edit prfile page -#
    path('user/profile/edit/<str:user_id>/', views.edit_profile_func, name='profile_edit_page'),
    #---------------$ Contact us page $---------------#
    #- contact page -#
    path('contact/', views.contact_func, name='contact_page'),
    #---------------$ error page $---------------#
    path('error/404', views.error_404_func, name='error_404_page'),
]
