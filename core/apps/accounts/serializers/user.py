from django.contrib.auth import get_user_model
from rest_framework import serializers

from .address.district import ListRegionSerializer
from .address.region import ListCountrySerializer


class UserSerializer(serializers.ModelSerializer):
    qrcode = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    country = ListCountrySerializer()
    region = ListRegionSerializer()

    def get_qrcode(self, obj):
        return obj.profile.qrcode.url

    def get_balance(self, obj):
        return obj.profile.balance

    class Meta:
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_active",
            "phone",
            "role",
            "country",
            "region",
            "balance",
            "qrcode",
        ]
        model = get_user_model()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "region",
            "country",
        ]
