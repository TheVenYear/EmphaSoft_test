from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(default='user/default.jpg', verbose_name='изображение профиля')
    about = models.TextField(blank=True, verbose_name='обо мне')
