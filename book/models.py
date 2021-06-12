from django.db import models


class SimpleBook(models.Model):
    second_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    fathers_name = models.CharField(max_length=45)
    phone1 = models.CharField(max_length=11)
    phone2 = models.CharField(max_length=11)
    phone3 = models.CharField(max_length=11)
    email = models.CharField(max_length=45)
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    more = models.CharField(max_length=2000)