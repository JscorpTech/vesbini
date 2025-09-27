from rest_framework import serializers

from core.apps.payment.models import HistoryModel


class BaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModel
        fields = [
            "id",
            "amount",
            "type",
            "comment",
        ]


class ListHistorySerializer(BaseHistorySerializer):
    class Meta(BaseHistorySerializer.Meta): ...


class RetrieveHistorySerializer(BaseHistorySerializer):
    class Meta(BaseHistorySerializer.Meta): ...


class CreateHistorySerializer(BaseHistorySerializer):
    class Meta(BaseHistorySerializer.Meta):
        fields = [
            "id",
            "name",
        ]
