from django.db import models


class Ticket(models.Model):
    number = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.number
