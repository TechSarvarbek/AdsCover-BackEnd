from django.urls import path

from .views import (
	register,
	login,
	activate,
	UserProfileView,
)


app_name = 'users'
urlpatterns = [
	path('register/', register, name='register'),
	path('login/<str:email>/<str:password>/', login, name='login'),
	path('active/<str:code>/', activate, name='user-activate'),
	path('profile/', UserProfileView.as_view(), name='user-profile')
]