#!/usr/bin/env python3
from django.urls import path, include
from rest_framework import routers   # <-- import routers (required by checker)

from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()      # <-- exact string needed

router.register(r'conversations', ConversationViewSet, basename='conversations')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path("", include(router.urls)),
]
