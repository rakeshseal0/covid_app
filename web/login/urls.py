from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login_page'),
    path('check', views.checker, name='check_creds')

]
