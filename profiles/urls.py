from django.urls import path
from .views import (
	signup, rating_view, revenue_view, InstallView, AdminView, add_app, role_update, CarrierSearch
)

app_name = 'profiles'

urlpatterns = [
	path('', signup, name='profile-signup'),
	path('rating/', rating_view, name='profile-rating'),
	path('revenue/', revenue_view, name='profile-revenue'),
	path('installs/', InstallView.as_view(), name='profile-install'),
	path('admin_setting/', AdminView.as_view(), name='profile-admin'),
	path('user_list/', role_update, name='profile-role'),
	path('add_app/', add_app, name='add_app'),
	path('search/<str:query>', CarrierSearch.as_view(), name='search_install'),
]
