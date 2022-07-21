from django.db import models

class SurveyTable(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    from_date = models.CharField(max_length=100, default='')
    to_date = models.CharField(max_length=100, default='')

