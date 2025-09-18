from rest_framework import serializers

from core.apps.api.models import FeedbackModel


class BaseFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = [
            "id",
            "message",
            "answer",
        ]


class ListFeedbackSerializer(BaseFeedbackSerializer):
    class Meta(BaseFeedbackSerializer.Meta): ...


class RetrieveFeedbackSerializer(BaseFeedbackSerializer):
    class Meta(BaseFeedbackSerializer.Meta): ...


class CreateFeedbackSerializer(BaseFeedbackSerializer):
    def create(self, validated_data):
        validated_data["user"] = self.context.get("request").user
        return super().create(validated_data)

    class Meta(BaseFeedbackSerializer.Meta):
        fields = [
            "id",
            "message",
        ]
