from django.urls import path

from .views import (
	home,
	users_view,
	user_update,
	companies_view,
	company_update,
	ad_update,
	admin_login,
	admin_logout,
	admin_update
)

app_name = 'dashboard'
urlpatterns = [
	path('', home, name='home'),
	path('users/', users_view, name='users'),
	path('user/<int:id>/', user_update, name='user-update'),
	path('companies/', companies_view, name='companies'),
	path('company/<int:id>/', company_update, name='company'),
	path('ad/<int:id>/', ad_update, name='ad-update'),
	path('login/', admin_login, name='login'),
	path('profile-update/', admin_update, name='profile-update'),
	path('logout/', admin_logout, name='logout')
]