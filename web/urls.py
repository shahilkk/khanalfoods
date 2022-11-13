from . import views
from django.urls import path

app_name ='web'

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.log_in,name='login'),
    path('logout',views.log_out,name='logout'),
    path('register',views.register,name='register'),
    path('productlist',views.productlist,name='productlist'), 
    path('addproduct',views.addproduct,name='addproduct'), 
    path('customerlist',views.customerlist,name='customerlist'),
    path('viewhistory/<int:id>',views.viewhistory,name='viewhistory'), 
    
    
]