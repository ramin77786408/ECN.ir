from django.urls import path
from . import views

app_name ='store'

urlpatterns = [
    path('',views.storehome,name='storehome'),
    path('<int:pk>/',views.good_details,name='good_details'),
    path('about/',views.about,name='about'),
]