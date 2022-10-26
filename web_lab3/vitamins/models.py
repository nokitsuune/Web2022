from django.db import models


class Orders(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    vitamin = models.ForeignKey('Vitamins', models.DO_NOTHING)
    date_order = models.DateField()
    date_delivery = models.DateField()

    class Meta:
        managed = False
        db_table = 'orders'


class Users(models.Model):
    user_name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'users'


class Vitamins(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vitamins'
