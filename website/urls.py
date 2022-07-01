from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    # path('accounts/', include('allauth.urls')),
]

urlpatterns += [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
