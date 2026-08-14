"""
Main URL configuration for fitness_website project.
Delegates all page routes to the 'fitness' app, and serves
static files during development.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),
    path('', include('fitness.urls')),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Custom 404 handler -> renders our styled 404 page
handler404 = 'fitness.views.error_404'
