from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_new_password, register_confirm, \
    VerifiedEmailView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),

    # Функция сменить пароль на рандомный
    path('profile/genpassword', generate_new_password, name='generate_new_password'),

    # Верификация почты
    path('verified_email/', VerifiedEmailView.as_view(), name='verified_email'),
    path('register_confirm/<str:token>/', register_confirm, name='register_confirm'),
]
