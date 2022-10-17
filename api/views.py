from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import requests, json, uuid

def delete_user(request, user_id):
    """
    1. User delete with user_id and user_id is required!
    """
    try:
        headers = {
            "Api-Token": "cffd15a4ae931a48b4efc4e14b35cf2fae08a104",
            "Content-Type": "application/json"
        }
        api_endpoint = f"https://api-4B2B87F9-D8CA-4A58-8026-05EAEE5D9FEC.sendbird.com/v3/users/{user_id}"
        response = requests.delete(api_endpoint, headers=headers)
        output = response.json()
        output["message"] = "Deleted!"
        return JsonResponse(output, status=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        return JsonResponse({"message": error}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_user(request, user_id):
    """
    1. Required: user_id
    2. Single user update function with user_id
    """
    try:
        output = {}
        data = json.dumps(json.loads(request.body))
        headers = {
            "Api-Token": "cffd15a4ae931a48b4efc4e14b35cf2fae08a104",
            "Content-Type": "application/json"
        }
        api_endpoint = f"https://api-4B2B87F9-D8CA-4A58-8026-05EAEE5D9FEC.sendbird.com/v3/users/{user_id}"
        response = requests.put(api_endpoint, data=data, headers=headers)
        output = response.json()
        return JsonResponse(output, status=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        return JsonResponse({"message": error}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def create_user(request):
    """
    {
        "user_id": "test1",
        "nickname": "test1",
        "profile_url": "https://sendbird.com/main/img/profiles/profile_05_512px.png",
        "issue_access_token": True,
        "session_token_expires_at": 1542945056625,
        "metadata": {"location": "mohali","marriage": "N","hasSomeone": "Y"}
    }
    """
    try:
        if request.method == "POST":
            output = {}
            user_id = uuid.uuid4
            data = json.dumps(json.loads(request.body))
            headers = {
                "Api-Token": "cffd15a4ae931a48b4efc4e14b35cf2fae08a104",
                "Content-Type": "application/json"
            }
            api_endpoint = "https://api-4B2B87F9-D8CA-4A58-8026-05EAEE5D9FEC.sendbird.com/v3/users"
            response = requests.post(api_endpoint, data=data, headers=headers)
            output = response.json()
            return JsonResponse(output, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"message": "user not created!"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception as error:
        print(error)
        return JsonResponse({"message": error}, status=status.HTTP_406_NOT_ACCEPTABLE)


def list_all_users(request):
    """
    1. Fetch data with get request without pass any params.
    2. URL: http://127.0.0.1:8000/api/all_users/
    """
    try:
        headers = {
            "Api-Token": "cffd15a4ae931a48b4efc4e14b35cf2fae08a104",
            "Content-Type": "application/json"
        }
        api_endpoint = "https://api-4B2B87F9-D8CA-4A58-8026-05EAEE5D9FEC.sendbird.com/v3/users"
        request_data = requests.get(api_endpoint, headers=headers)
        # print(request_data.json())
        return JsonResponse(request_data.json(), status=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        return JsonResponse({"message": error}, status=status.HTTP_404_NOT_FOUND)


def get_single_user(request):
    """
    1. Send the user_id in url, if user exist on the sendbird then get the data with user_id
    2. for example: http://127.0.0.1:8000/api/get_single_user/?user_id=user1
    """
    try:
        user_id = request.GET["user_id"]
        if user_id != "":
            headers = {
                "Api-Token": "cffd15a4ae931a48b4efc4e14b35cf2fae08a104",
                "Content-Type": "application/json"
            }
            api_endpoint = f"https://api-4B2B87F9-D8CA-4A58-8026-05EAEE5D9FEC.sendbird.com/v3/users/{user_id}"
            request_data = requests.get(api_endpoint, headers=headers)
            print(request_data.json())
            return JsonResponse(request_data.json(), status=status.HTTP_200_OK)
        return JsonResponse({"message": "user_is not found!"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        print(error)
        return JsonResponse({"message": error}, status=status.HTTP_404_NOT_FOUND)