from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
