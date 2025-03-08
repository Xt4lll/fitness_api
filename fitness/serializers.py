from rest_framework import serializers
from .models import User, UserProfile, StepRecord, WorkoutVideo, Goal, GoalProgress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class StepRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepRecord
        fields = "__all__"

class WorkoutVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutVideo
        fields = "__all__"

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"

class GoalProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalProgress
        fields = "__all__"
