from django.contrib import admin
from .models import User, UserProfile, StepRecord, WorkoutVideo, Goal, GoalProgress

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    search_fields = ("username", "email")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "height", "weight", "goal_weight", "daily_step_goal")
    search_fields = ("user__username", "user__email")

@admin.register(StepRecord)
class StepRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "step_count", "recorded_at")
    search_fields = ("user__username",)
    list_filter = ("recorded_at",)

@admin.register(WorkoutVideo)
class WorkoutVideoAdmin(admin.ModelAdmin):
    list_display = ("user", "video_url", "created_at")
    search_fields = ("user__username",)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("user", "goal_type", "target_value", "unit", "status", "created_at")
    search_fields = ("user__username",)
    list_filter = ("status", "goal_type")

@admin.register(GoalProgress)
class GoalProgressAdmin(admin.ModelAdmin):
    list_display = ("goal", "user", "progress_value", "updated_at")
    search_fields = ("user__username",)
