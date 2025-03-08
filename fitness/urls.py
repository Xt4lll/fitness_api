from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'steps', StepRecordViewSet)
router.register(r'workout_videos', WorkoutVideoViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'goal_progress', GoalProgressViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
