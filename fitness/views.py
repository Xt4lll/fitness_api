import firebase_admin
from firebase_admin import auth, credentials
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from rest_framework import viewsets
from .models import User, UserProfile, StepRecord, WorkoutVideo, Goal, GoalProgress
from .serializers import UserSerializer, UserProfileSerializer, StepRecordSerializer, WorkoutVideoSerializer, GoalSerializer, GoalProgressSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class StepRecordViewSet(viewsets.ModelViewSet):
    queryset = StepRecord.objects.all()
    serializer_class = StepRecordSerializer

class WorkoutVideoViewSet(viewsets.ModelViewSet):
    queryset = WorkoutVideo.objects.all()
    serializer_class = WorkoutVideoSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class GoalProgressViewSet(viewsets.ModelViewSet):
    queryset = GoalProgress.objects.all()
    serializer_class = GoalProgressSerializer

# Подключаем Firebase Admin SDK
cred = credentials.Certificate("C:/Users/xtal/PycharmProjects/fitness_api/fitnessdb-7b60a-firebase-adminsdk-fbsvc-9a53d78a8f.json")
firebase_admin.initialize_app(cred)

def firebase_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        firebase_token = data.get("firebase_token")

        try:
            decoded_token = auth.verify_id_token(firebase_token)
            uid = decoded_token["uid"]
            email = decoded_token.get("email")

            user, created = User.objects.get_or_create(username=uid, defaults={"email": email})

            return JsonResponse({"message": "Success", "user_id": user.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)