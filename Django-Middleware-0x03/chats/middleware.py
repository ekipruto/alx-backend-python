# chats/middleware.py
import logging
from django.http import HttpResponseForbidden
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logger to write to requests.log
        logging.basicConfig(
            filename="requests.log",
            level=logging.INFO,
            format="%(message)s"
        )

    def __call__(self, request):
        # Get user info (Anonymous if not logged in)
        user = request.user if request.user.is_authenticated else "Anonymous"

        # Log the request details
        logging.info(f"{datetime.now()} - User: {user} - Path: {request.path}")

        # Continue processing the request
        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    """
    Middleware that restricts access to chat endpoints
    outside the allowed time window (6PM - 9PM).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current server time (24-hour format)
        current_hour = datetime.now().hour

        # Allowed window: 18 (6PM) <= hour < 21 (9PM)
        if not (18 <= current_hour < 21):
            return HttpResponseForbidden(
                "Access to chat is restricted outside 6PM - 9PM."
            )

        # Continue normal request flow
        response = self.get_response(request)
        return response
