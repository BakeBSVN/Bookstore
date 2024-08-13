from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # path('cart_update_ajax/', views.cart_update_ajax, name='cart_update_ajax'),
]

