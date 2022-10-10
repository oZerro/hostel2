from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

from .serializers import (
    ProfileSerializer,
    RoomSerializer,
    DeparturesSerializer,
    PaymentsSerializer,
    RefundsSerializer,
    SpendingAdminSerializer,
    SpendingBossSerializer,
    SpendingHostelSerializer,

)
from otchet.models import (
    Profile,
    Room,
    Departures,
    Payments,
    Refunds,
    SpendingAdmin,
    SpendingBoss,
    SpendingHostel
)


# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser, )

    @action(methods=['get'], detail=False)  # если нужно добавить кастомную ссылку в api
    def rooms(self, request):
        rooms_all = Room.objects.all()
        return Response({'rooms': [r.number for r in rooms_all]})


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminUser, )


class DeparturesViewSet(viewsets.ModelViewSet):
    queryset = Departures.objects.all()
    serializer_class = DeparturesSerializer
    permission_classes = (IsAdminUser, )


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = (IsAdminUser, )


class RefundsViewSet(viewsets.ModelViewSet):
    queryset = Refunds.objects.all()
    serializer_class = RefundsSerializer
    permission_classes = (IsAdminUser, )


class SpendingAdminViewSet(viewsets.ModelViewSet):
    queryset = SpendingAdmin.objects.all()
    serializer_class = SpendingAdminSerializer
    permission_classes = (IsAdminUser, )


class SpendingBossViewSet(viewsets.ModelViewSet):
    queryset = SpendingBoss.objects.all()
    serializer_class = SpendingBossSerializer
    permission_classes = (IsAdminUser, )


class SpendingHostelViewSet(viewsets.ModelViewSet):
    queryset = SpendingHostel.objects.all()
    serializer_class = SpendingHostelSerializer
    permission_classes = (IsAdminUser, )


# class ProfileAPIList(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileAPIUpdate(generics.UpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


# class ProfileAPIView(APIView):
#     def get(self, request):
#         lst = Profile.objects.all()
#         return Response({'customers': ProfileSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = ProfileSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'customer': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUD not allowed"})
#
#         try:
#             instance = Profile.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#
#         serializer = ProfileSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"customer": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Метод удаления не может быть выполнет.. нет такого PK"})
#         try:
#             Profile.objects.get(pk=pk).delete()
#         except:
#             return Response({"error": "Метод удаления не может быть выполнет.. нет такого PK"})
#
#         return Response({"customer": f"удалили посетителя {pk}"})








# class ProfileAPIView(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer