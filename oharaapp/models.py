from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Tokuten_post(models.Model):
    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.CASCADE)
    subject=models.CharField(verbose_name='科目',max_length=100)
    num=models.IntegerField(verbose_name='点数',validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])
    posted_at=models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)
    def __str__(self):
        return self.subject
