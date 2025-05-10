from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import CreateUserView, logout_view, confirm_email, verify_email, profile_update, profile_view

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('confirm-email/', confirm_email, name='confirm-email'),
    path('verify-email/', verify_email, name='verify-email'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',
        success_url='/accounts/password-change/done/'
    ), name='password_change'),
    
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'
    ), name='password_change_done'),
    path('profile/edit/', profile_update, name='profile_update'),
    path('profile/', profile_view, name='profile'),
]