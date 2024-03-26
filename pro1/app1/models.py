from django.db import models


class Create(models.Model):
    choice = (('YES', 'yes'), ('NO', 'no'))
    f_name = models.CharField(max_length=20)
    s_name = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    rooms = models.IntegerField()
    ac = models.CharField(max_length=10, choices=choice)
