from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Django標準のユーザー機能からカスタムフィールドを追加
class CustomUser(User):
    Balance = models.IntegerField('残高',default=1000)