from django.urls import path
from . import views     
    
urlpatterns = [
    path('', views.index),
    path('login', views.login ,name='login'),
    path('customers', views.customers ,name='customers'),
    
    path('add_item', views.add_item ,name='add_item'),
    path('delete_item', views.delete_item ,name='delete_item'),
    
    path('add_customer', views.add_customer ,name='add_customer'),
    path('delete_customer', views.delete_customer ,name='delete_customer'),
    path('customers_view', views.customers_view, name='customers_view'),

    
    
    path('get_item_data/', views.get_item_data, name='get_item_data'),
    path('view_item_data/<int:item_id>/', views.view_item_data, name='view_item_data'),

    path('update_item/', views.update_item, name='update_item'),
    path('select_customer/', views.select_customer, name='select_customer'),
    
    path('rest_password/', views.rest_password, name='rest_password'),
    path('rest_password_in', views.rest_password_in, name='rest_password_in'),



    
    
    
    
    
    
    
    
    
    
    
    
    
]
