import logging

from rest_framework import mixins, generics, permissions, viewsets
from vets import models
from vets import serializers

logger = logging.getLogger(__name__)


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()
    permission_classes = [permissions.IsAdminUser]


class ClientList(mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ClientDetail(mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   generics.GenericAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        logger.debug(f"Writing {kwargs} to Clients")
        return self.update(request, *args, **kwargs)


class VetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VetSerializer
    queryset = models.Vet.objects.all()
    permission_classes = [permissions.IsAdminUser]


class VetList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = models.Vet.objects.all()
    serializer_class = serializers.VetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class VetDetail(mixins.RetrieveModelMixin,
                generics.GenericAPIView):
    queryset = models.Vet.objects.all()
    serializer_class = serializers.VetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PetViewSet(viewsets.ModelViewSet):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer
    permission_classes = [permissions.IsAdminUser]


class PetList(mixins.ListModelMixin,
              generics.GenericAPIView):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PetDetail(mixins.RetrieveModelMixin,
                generics.GenericAPIView):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [permissions.IsAdminUser]


class AppointmentList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AppointmentDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAdminUser]


class AddressList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AddressDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class SurgeryViewSet(viewsets.ModelViewSet):
    queryset = models.Surgery.objects.all()
    serializer_class = serializers.SurgerySerializer
    permission_classes = [permissions.IsAdminUser]


class SurgeryList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = models.Surgery.objects.all()
    serializer_class = serializers.SurgerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SurgeryDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = models.Surgery.objects.all()
    serializer_class = serializers.SurgerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
