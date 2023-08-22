from django.urls import path
from  . import views
urlpatterns = [
    path('shipping/',views.index1,name='index1')
]
