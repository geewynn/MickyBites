from django.urls import path
from micky import api_views

urlpatterns = [
    path('users/', api_views.UserList.as_view()),
    path('users/<int:pk>/', api_views.UserDetail.as_view()),
    path('products/', api_views.ProductList.as_view()),
    path('products/<int:pk>/', api_views.ProductDetail.as_view()),

]