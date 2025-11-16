#!/usr/bin/env python3
"""DRF serializers for chats app."""

from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # use user_id (UUID) instead of pk for external references
        fields = (
            "user_id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "role",
            "created_at",
        )
        read_only_fields = ("user_id", "created_at")


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )  # optional if set from request.user
    conversation = serializers.PrimaryKeyRelatedField(
        queryset=Conversation.objects.all()
    )

    class Meta:
        model = Message
        fields = ("message_id", "sender", "conversation", "message_body", "sent_at")
        read_only_fields = ("message_id", "sent_at")


class ConversationSerializer(serializers.ModelSerializer):
    # nested messages (read-only)
    messages = MessageSerializer(many=True, read_only=True)
    # participants are referenced by their user_id
    participants = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )

    class Meta:
        model = Conversation
        fields = ("conversation_id", "participants", "created_at", "messages")
        read_only_fields = ("conversation_id", "created_at")

    def create(self, validated_data):
        """Handle creation of conversation and attaching participants."""
        participants = validated_data.pop("participants", [])
        conversation = Conversation.objects.create(**validated_data)
        if participants:
            conversation.participants.set(participants)
        return conversation
