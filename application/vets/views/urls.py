from django.urls import path
from vets.views import home, welcome

urlpatterns = [
    path('home/', home.HomeView.as_view()),
    path('welcome/', welcome.WelcomeView.as_view())
]
