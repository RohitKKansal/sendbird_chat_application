from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticated, IsAdminUser, AllowAny
import requests
# from ..data_service import SendBirdService

# class UserFetchByID(APIView):
#     permission_classes = (AllowAny,)
#     def get(self, request):
#         try:
#             user_id = request.GET["user_id"]
#             if user_id != "":
#                 data = SendBirdService.get_profile_by_id()
#                 return JsonResponse(request_data.json(), status=status.HTTP_200_OK)
#             return JsonResponse({"message": "user_is not found!"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as error:
#             print(error)
#             return JsonResponse({"message": error}, status=status.HTTP_404_NOT_FOUND)