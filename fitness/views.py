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
