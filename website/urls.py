from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('gallery/', views.gallery, name='gallery'),
    path('stats/', views.stats_dashboard, name='stats'),
    path('fees/', views.fees, name='fees'),
    path('notifications/', views.notifications_page, name='notifications'),
    path('contact/', views.contact, name='contact'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('faculty/', views.faculty, name='faculty'),
]
