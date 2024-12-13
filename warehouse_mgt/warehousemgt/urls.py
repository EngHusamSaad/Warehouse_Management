from django.urls import path



from . import views     
    
urlpatterns = [
    path('', views.index),
    path('login', views.login ,name='login'),
    path('customers', views.customers ,name='customers'),
    
    path('add_item', views.add_item ,name='add_item'),
    path('delete_item', views.delete_item ,name='delete_item'),
    path('edit_item', views.edit_item ,name='edit_item'),
    
    
    
    
    
    
    
    
    
    
    
    
    
]
