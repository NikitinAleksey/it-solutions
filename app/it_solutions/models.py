from django.db import models


class Request(models.Model):
    path = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
