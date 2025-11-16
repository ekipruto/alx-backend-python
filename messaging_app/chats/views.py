#!/usr/bin/env python3
"""ViewSets for chats app."""

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """List, retrieve and create Conversations."""
    queryset = Conversation.objects.all().prefetch_related("participants", "messages")
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Optionally restrict to conversations the user participates in
        user = self.request.user
        if user.is_authenticated:
            return self.queryset.filter(participants=user).distinct()
        return Conversation.objects.none()


class MessageViewSet(viewsets.ModelViewSet):
    """List and create messages for conversations."""
    queryset = Message.objects.all().select_related("sender", "conversation")
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Ensure sender is set to request.user (if authenticated). If the
        request doesn't provide sender, use request.user.
        """
        data = request.data.copy()

        # If request user is authenticated, set sender to that user
        if request.user and request.user.is_authenticated:
            data["sender"] = request.user.user_id  # UUIDField primary key
        # else allow client to pass sender (not recommended for production)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """Optionally filter messages by conversation via query param."""
        qs = super().get_queryset()
        conv_id = self.request.query_params.get("conversation")
        if conv_id:
            qs = qs.filter(conversation__conversation_id=conv_id)
        return qs
