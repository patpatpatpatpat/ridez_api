from rest_framework import serializers
from .models import User, Ride, RideEvent
from datetime import timedelta
from django.utils.timezone import now

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        read_only_fields = ('username', 'email')


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'auth_token',)
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = [
            "id",
            "description",
            "created_at",
        ]


class RideSerializer(serializers.ModelSerializer):
    rider = UserSerializer()
    driver = UserSerializer()
    todays_ride_events = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = [
            "id",
            "status",
            "rider",
            "driver",
            "pickup_latitude",
            "pickup_longitude",
            "dropoff_latitude",
            "dropoff_longitude",
            "pickup_time",
            "todays_ride_events",
        ]

    def get_todays_ride_events(self, obj):
        time_threshold = now() - timedelta(hours=24)
        recent_events = obj.rideevent_set.filter(created_at__gte=time_threshold)

        return RideEventSerializer(recent_events, many=True).data
