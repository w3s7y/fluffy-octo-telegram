from django.urls import path, include
from django.contrib import admin
from vets import admin_views as views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# Create a simple router for the rest api
rest_router = routers.SimpleRouter()

# Bind our basic admin views to it.
rest_router.register(r'clients', views.ClientViewSet)
rest_router.register(r'vets', views.VetViewSet)
rest_router.register(r'appointments', views.AppointmentViewSet)
rest_router.register(r'address', views.AddressViewSet)
rest_router.register(r'surgery', views.SurgeryViewSet)
rest_router.register(r'pets', views.PetViewSet)

# Add binds to the auth framework and admin site.
urlpatterns = [
    path('', include('vets.views.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += rest_router.urls
