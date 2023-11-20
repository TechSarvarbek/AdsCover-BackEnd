from django.urls import path

from .views import (
	create_company,
	DetailCompanyView,
	user_companies,
)

app_name = 'company'
urlpatterns = [
	path('create/', create_company, name='create'),
	path('detail/<int:id>/', DetailCompanyView.as_view(), name='detail-company'),
	path('companies/', user_companies, name='user-companies'),
	
]