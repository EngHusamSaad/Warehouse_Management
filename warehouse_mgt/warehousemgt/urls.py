from django.urls import path



from . import views     
    
urlpatterns = [
    path('', views.index),
    path('login', views.login ,name='login'),
    path('customers', views.customers ,name='customers'),
    
    path('add_item', views.add_item ,name='add_item'),
    
    
    
    
    
    
    
]
