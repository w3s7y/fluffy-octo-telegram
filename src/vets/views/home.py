import django.forms
from django.views.generic import FormView

from vets.models import Client, Appointment, Vet, Surgery


class HomeForm(django.forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class HomeView(FormView):
    form_class = HomeForm
    template_name = "home.html"

