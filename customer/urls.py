from . import views
from django.urls import path

app_name ='customer'

urlpatterns = [
    path('',views.home,name='home'),
    path('viewproduct/<int:id>',views.viewproduct,name='viewproduct'),
    path('timeout/<int:id>',views.timeout,name='timeout'),
]