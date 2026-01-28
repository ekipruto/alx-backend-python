import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from chats.models import Conversation, Message


@pytest.mark.django_db
class TestConversationModel(TestCase):
    """Test cases for Conversation model"""
    
    def setUp(self):
        """Set up test data"""
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@test.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@test.com',
            password='testpass123'
        )
    
    def test_conversation_creation(self):
        """Test creating a conversation"""
        conversation = Conversation.objects.create()
        conversation.participants.add(self.user1, self.user2)
        
        assert conversation is not None
        assert conversation.participants.count() == 2
        assert self.user1 in conversation.participants.all()
    
    def test_conversation_str(self):
        """Test conversation string representation"""
        conversation = Conversation.objects.create()
        assert str(conversation) is not None


@pytest.mark.django_db
class TestMessageModel(TestCase):
    """Test cases for Message model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        self.conversation = Conversation.objects.create()
        self.conversation.participants.add(self.user)
    
    def test_message_creation(self):
        """Test creating a message"""
        message = Message.objects.create(
            sender=self.user,
            conversation=self.conversation,
            message_body='Test message'
        )
        
        assert message is not None
        assert message.sender == self.user
        assert message.message_body == 'Test message'
    
    def test_message_str(self):
        """Test message string representation"""
        message = Message.objects.create(
            sender=self.user,
            conversation=self.conversation,
            message_body='Test message'
        )
        
        assert str(message) is not None
