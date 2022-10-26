from django.db import models


class Vitamins(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vitamins'
