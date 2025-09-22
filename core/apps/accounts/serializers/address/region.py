from rest_framework import serializers

from core.apps.accounts.models import CountryModel


class BaseCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = [
            "id",
            "name",
            "flag",
            "code",
        ]


class ListCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class RetrieveCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class CreateCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta):
        fields = [
            "id",
            "name",
        ]
