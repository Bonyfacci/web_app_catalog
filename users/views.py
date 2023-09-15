import random

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    token = None

    def form_valid(self, form):

        new_user = form.save()

        if new_user.is_verified is False:
            user_token = user_token_verification()
            form.instance.code_verification = user_token

            confirm_link = self.request.build_absolute_uri(
                reverse_lazy(
                    "users:register_confirm", kwargs={"token": user_token}
                )
            )

            self.token = user_token

            send_mail(
                subject='Поздравляем с регистрацией',
                message=f'Вы зарегистрировались на нашей платформе!'
                        f'\n\nВаш код верификации: {user_token}'
                        f'\n\nИли перейдите по ссылке {confirm_link}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )
            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:verified_email')


def user_token_verification():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])


def register_confirm(request, token):
    """
    Не получилось реализовать. Как автоматически залогинить пользователя?
    """
    user_info = token

    print(user_info)

    if user_id := user_info:
        print(user_id)
        user = get_object_or_404(User, code_verification=user_id)
        user.is_verified = True
        user.save()
        return redirect(to=reverse_lazy("users:login"))
    else:
        return redirect(to=reverse_lazy("users:register"))


class VerifiedEmailView(View):
    template_name = 'users/verified_email.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        verification_code = request.POST.get('verification_code')
        User = get_user_model()
        try:
            user = User.objects.get(code_verification=verification_code)
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return redirect('users:login')
        except User.DoesNotExist:
            pass
        return redirect('users:login')


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = get_random_string(length=12)
    request.user.set_password(new_password)
    request.user.save()

    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    return redirect(reverse('users:login'))



