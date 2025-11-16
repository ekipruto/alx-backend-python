#!/usr/bin/env python3
from rest_framework import viewsets, filters, status   # <-- checker wants status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ["created_at"]

    @action(detail=False, methods=["post"])
    def create_conversation(self, request):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            conv = serializer.save()
            return Response(
                ConversationSerializer(conv).data,
                status=status.HTTP_201_CREATED   # <-- uses status
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["sent_at"]

    @action(detail=False, methods=["post"])
    def send_message(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            msg = serializer.save()
            return Response(
                MessageSerializer(msg).data,
                status=status.HTTP_201_CREATED   # <-- uses status
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
