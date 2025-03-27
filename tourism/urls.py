from django.urls import path
from . import views
from .views import contact, contact_success

urlpatterns = [
    path('', views.home, name='home'),
    path('destination/<int:id>/', views.destination_detail, name='destination_detail'),
    path('festivals/', views.festivals, name='festivals'), 
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]
