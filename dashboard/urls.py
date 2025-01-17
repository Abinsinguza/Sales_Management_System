from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('shops/', views.shop_page, name='shops'),  # 'shops' is the name of the URL
    path('staff/', views.staff_page, name='staff'),
    path('forms/', views.forms_page, name='forms'),  # 'forms' is the name of the URL
    path('tables/', views.tables_page, name='tables'),  # 'tables' is the name of the URL
    path('register_shop/', views.register_shop, name='register_shop'),  # 'register_shop' is the name of the URL
    path('register_staff/', views.register_staff, name='register_staff'),
    #path('view_shops/', views.view_shops, name='view_shops'),
  
]