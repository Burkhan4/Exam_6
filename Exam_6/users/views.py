from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from random import randint
from django.core.mail import send_mail
from os import getenv
from dotenv import load_dotenv
from django.http import HttpResponse
from .forms import UserUpdateForm


from users.forms import CustomUserCreationForm
from users.models import CustomUser, EmailVerifycationCodes

load_dotenv()


class CreateUserView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def confirm_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email, pk = request.user.id)
            code = f"{randint(100, 999)}-{randint(100, 999)}"
            try:
                EmailVerifycationCodes.objects.create(code=code, user=user, email=email)
                send_mail(
                    subject="Confirm your email",
                    message=f"iltimos bu qo'dni kiriting: {code}",
                    from_email=getenv('EMAIL_HOST_USER'),
                    recipient_list=[email]
                )
                return render(
                    request,
                    template_name='registration/confirm_send_email.html'
                )
            except Exception as e:
                print(e)
                return render(request, 'registration/confirm_mail.html', {'error': 'Nomalum hato'})
        except CustomUser.DoesNotExist:
            return render(request, 'registration/confirm_mail.html', {'error': 'Email topilmmadi'})
    else:
        return render(request, 'registration/confirm_mail.html')

@login_required
def verify_email(request):
    if request.methot == 'POST':
        code = f"{request.POST.get('num1')}-{request.POST.get('num2')}"
        obj = EmailVerifycationCodes.objects.get(code=code, status = True)
        if obj is None:
            return render(request, 'registration/confirm_send_email.html')
        obj.status=False
        obj.save()
        CustomUser.objects.filter(email=obj.email).update(email_verified = True)
        resp = """<h3>
                    Email succesfully confirmed.
                    <script>
                        setTimeout(function() {
                            window.location.href = '/';
                        }, 3000);
                    </script>
                </h3>"""
        return HttpResponse(resp)
    else:
        return redirect('/')
    
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'registration/profile_update.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')