from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticated, IsAdminUser, AllowAny
import requests
from ..data_service import SendBirdService

class SendBirdService:
    
    def get_profile_by_id(user_id):
        headers = {
            "Api-Token": "cffd15a4ae931a48b4efc4e14b35cf2fae08a104",
            "Content-Type": "application/json"
        }
        api_endpoint = f"https://api-4B2B87F9-D8CA-4A58-8026-05EAEE5D9FEC.sendbird.com/v3/users/{user_id}"
        request_data = requests.get(api_endpoint, headers=headers)
        data = request_data.json()
        return data