from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')
    target_object = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_object', 'timestamp', 'read']

    def get_target_object(self, obj):
        return str(obj.target)
