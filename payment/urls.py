from django.urls import path

from .views import pay_create, payments


app_name = 'payment'
urlpatterns = [
	path('create/', pay_create),
	path('payments/', payments),
]