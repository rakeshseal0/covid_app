from django.urls import path

from . import views

urlpatterns = [
    path('top', views.top_news, name='latest_news'),
    path('', views.landing_page, name='landing_page'),
    path('user_data', views.user_data, name='user_data')

]
