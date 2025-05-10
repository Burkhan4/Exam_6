from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'


class EmailVerifycationCodes(models.Model):
    email = models.EmailField
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'email_verifycation_codes'
