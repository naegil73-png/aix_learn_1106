from django.db import models

class Est_wei(models.Model):
        length = models.FloatField()
        width = models.FloatField()
        thick = models.FloatField()
        weight = models.FloatField(null=True)
        creat_at = models.DateTimeField(auto_now_add=True)