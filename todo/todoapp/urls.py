from django.urls import path
from todoapp import views

urlpatterns = [
   
    path('dashboard',views.dashboard_page),
    path('home',views.home_page),
    path('about',views.about_page),
    path('product',views.product_page),
    path('add_task',views.add_task),
    path('dtl',views.dtl),
    path('delete/<rid>',views.delete_task),
    path('edit/<rid>',views.edit_task),
    path('complete/<rid>',views.mark_completed),
]