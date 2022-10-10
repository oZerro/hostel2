from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

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


# class ProfileModel:
#     def __init__(self, name, room, phone_number):
#         self.name = name
#         self.room = room
#         self.phone_number = phone_number

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class DeparturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departures
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class RefundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refunds
        fields = '__all__'


class SpendingAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingAdmin
        fields = '__all__'


class SpendingBossSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingBoss
        fields = '__all__'


class SpendingHostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingHostel
        fields = '__all__'





# name = serializers.CharField(max_length=255)
# room_id = serializers.IntegerField()
# phone_number = serializers.CharField(max_length=12)
#
# def create(self, validated_data):
#     return Profile.objects.create(**validated_data)
#
#
# def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.room_id = validated_data.get('room_id', instance.room_id)
#     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
#     instance.save()
#     return instance


# def encode():
#     model = ProfileModel('qwerrty', '5', '79876778987')
#     model_sr = ProfileSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
