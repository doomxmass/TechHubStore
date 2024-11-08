from .forms import (CustomPasswordResetForm,
                    CustomSetPasswordForm)
#- to customize password reset form -#
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
#- decorator -#
from .decorator import user_is_logged_in
#- important for decorator to return class not function -#
from django.utils.decorators import method_decorator


#> IMPORTANT <#
#---------------$ reset password function $---------------#
#- reset password main page -#
# @method_decorator(user_is_logged_in(['user','admin']), name='dispatch')
class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'change_pass_temps/change_password.html'


#- reset password done page -#
# @method_decorator(user_is_logged_in(['user','admin']), name='dispatch')
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'change_pass_temps/change_password_done.html'


#- reset pssword confirm page -#
# @method_decorator(user_is_logged_in(['user','admin']), name='dispatch')
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'change_pass_temps/change_password_confirm.html'


#- reset pssword complete page -#
# @method_decorator(user_is_logged_in(['user','admin']), name='dispatch')
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'change_pass_temps/change_password_complete.html'

