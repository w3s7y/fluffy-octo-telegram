from django.urls import path
from vets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('vets/', views.VetList.as_view()),
    path('vets/<int:pk>/', views.VetDetail.as_view()),
    path('appointments/', views.AppointmentList.as_view()),
    path('appointments/<int:pk>', views.AppointmentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
