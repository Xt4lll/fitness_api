from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="fitness_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="fitness_users",
        blank=True
    )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goal_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    daily_step_goal = models.IntegerField(default=10000)

class StepRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step_count = models.IntegerField()
    recorded_at = models.DateField(auto_now_add=True)

class WorkoutVideo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.TextField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50, choices=[("steps", "Шаги"), ("workout", "Тренировка"), ("custom", "Другое")])
    target_value = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, choices=[("steps", "Шаги"), ("reps", "Повторы"), ("minutes", "Минуты")])
    status = models.CharField(max_length=20, choices=[("active", "Активна"), ("completed", "Выполнена")], default="active")
    created_at = models.DateTimeField(auto_now_add=True)

class GoalProgress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    progress_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)
