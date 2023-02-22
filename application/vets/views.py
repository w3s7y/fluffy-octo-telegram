from rest_framework import mixins, generics
from vets import models
from vets import serializers


class ClientList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientDetail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class VetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Vet.objects.all()
    serializer_class = serializers.VetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VetDetail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = models.Vet.objects.all()
    serializer_class = serializers.VetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PetDetail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AppointmentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AppointmentDetail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AddressList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AddressDetail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SurgeryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Surgery.objects.all()
    serializer_class = serializers.SurgerySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SurgeryDetail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = models.Surgery.objects.all()
    serializer_class = serializers.SurgerySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
