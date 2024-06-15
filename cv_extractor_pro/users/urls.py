
from django.urls import path
from . import views

urlpatterns = [
    #path('',views.upload_cv,name='upload_cv'),
    path('', views.upload_folder,name='upload_folder'),
    #path('upload_folder/',views.upload_folder,name='upload_folder'),
    
]

