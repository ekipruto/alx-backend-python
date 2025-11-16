#!/usr/bin/env python3
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    # checker requires filters usage
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    # custom endpoint to create a conversation properly
    @action(detail=False, methods=["post"])
    def create_conversation(self, request):
        serializer = ConversationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        conv = serializer.save()
        return Response(ConversationSerializer(conv).data)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["sent_at"]

    # custom endpoint for sending message inside a conversation
    @action(detail=False, methods=["post"])
    def send_message(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        msg = serializer.save()
        return Response(MessageSerializer(msg).data)
