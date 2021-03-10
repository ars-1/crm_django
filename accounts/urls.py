from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home),
    path('products/', views.products),
    path('customer/<str:pk_test>/', views.customer),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),

    path('create_order/', views.createOrder, name="create_order"),
    path('create_orderC/<str:pk>/', views.createOrderC, name="create_orderC"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]