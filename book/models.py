from django.db import models


class SimpleBook(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=255)
    more = models.CharField(max_length=255)