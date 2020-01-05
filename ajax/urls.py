from django.urls import path
from . import views

app_name = 'ajax'

urlpatterns = [

	path('', views.home, name = 'home'),
	path('save_book', views.save_book, name = 'save_book'),
]