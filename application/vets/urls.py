from django.urls import path, include
from django.contrib import admin
from vets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('vets/', views.VetList.as_view()),
    path('vets/<int:pk>/', views.VetDetail.as_view()),
    path('appointments/', views.AppointmentList.as_view()),
    path('appointments/<int:pk>', views.AppointmentDetail.as_view()),
    path('address/', views.AddressList.as_view()),
    path('address/<int:pk>/', views.AddressDetail.as_view()),
    path('surgery/', views.SurgeryList.as_view()),
    path('surgery/<int:pk>/', views.SurgeryDetail.as_view()),
    path('pets/', views.PetList.as_view()),
    path('pets/<int:pk>', views.PetDetail.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]

urlpatterns = format_suffix_patterns(urlpatterns)
