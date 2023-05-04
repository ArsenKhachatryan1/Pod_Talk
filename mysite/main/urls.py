from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('listing-page/', views.listing_page, name = 'listing-page'),
    path('detail-page/', views.detail_page, name = 'detail-page'),
    path('contact/', views.contact, name = 'contact'),
]