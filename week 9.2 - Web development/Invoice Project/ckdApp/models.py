from django.db import models

# Create your models here.
class ckdModel(models.Model):

    unit_price=models.FloatField()
    quantity=models.FloatField()
    vat=models.FloatField()
    cogs=models.FloatField()
    gross_income=models.FloatField()
