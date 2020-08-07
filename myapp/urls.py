from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    # path('product_list/<str:product_slug>/', views.products, name='products'),
    path('category_list/<str:category_slug>/', views.product_list_with_same_category, name='product_list_with_same_category'),
    path('sign_up/', views.sign_up, name='signup' ),
    ]

