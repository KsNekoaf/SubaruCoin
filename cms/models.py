from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Django標準のユーザー機能からカスタムフィールドを追加
class CustomUser(AbstractUser):
    pass