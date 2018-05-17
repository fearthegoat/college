from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('sign/', views.sign, name='sign'),
	path('landingpage/', views.landingpage, name='landingpage')
]