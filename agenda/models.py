from django.db import models

class AgendaItem(models.Model):
    title = models.CharField(max_length=255)
    start_day = models.DateField(null=True)
    end_day = models.DateField(null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    interval = models.DurationField()
    color = models.CharField(max_length=7)

