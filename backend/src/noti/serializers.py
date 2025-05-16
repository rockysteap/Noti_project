from rest_framework import serializers

from noti.models import NotiOwner


class NotiOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotiOwner
        fields = '__all__'

    def create(self, validated_data):
        obj, created = NotiOwner.objects.get_or_create(
            telegram_id=validated_data['telegram_id'],
            defaults=validated_data
        )
        return obj
