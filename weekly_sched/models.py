from django.db import models

class TimeSlot(models.Model):
    day = models.CharField(max_length=9)
    start = models.TimeField()
    stop = models.TimeField()
    ids = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.day} {self.start}-{self.stop} ({self.ids})'
