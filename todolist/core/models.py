from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
