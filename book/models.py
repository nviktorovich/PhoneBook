from django.db import models


class SimpleBook(models.Model):
    second_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    fathers_name = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=30)
    phone2 = models.CharField(max_length=30)
    phone3 = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    more = models.CharField(max_length=255)