from django.db import models

class Est_wei(models.Model):
    length = models.FloatField()
    width = models.FloatField()
    thick = models.FloatField()
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"무게 : {self.weight}"