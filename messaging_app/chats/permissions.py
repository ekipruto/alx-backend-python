from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Allows access only to participants of a conversation.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Messages
        if hasattr(obj, "conversation"):
            return (
                obj.conversation.user1 == user or
                obj.conversation.user2 == user
            )

        # Conversation itself
        if hasattr(obj, "user1") and hasattr(obj, "user2"):
            return obj.user1 == user or obj.user2 == user

        return False
