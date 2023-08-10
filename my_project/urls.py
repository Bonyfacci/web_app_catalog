from django.urls import path

from my_project.views import my_project, about, news, info

urlpatterns = [
    path('', my_project, name='my_project'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('info/', info, name='info'),
]
