from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('dash', views.my_dashboard, name="dash"),
    path('add/', views.add, name="add"),
    path("addrec/", views.addrec, name="addrec"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update"),
    path('update/uprec/<int:id>/', views.uprec, name="uprec"),

    path('search/', views.Search.as_view(), name="search"),
]

