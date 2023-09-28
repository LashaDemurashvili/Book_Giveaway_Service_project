from django.urls import path

from . import views

urlpatterns = [
    path('home', views.homepage, name="home"),
    path('reg', views.reg, name="reg"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),
]
