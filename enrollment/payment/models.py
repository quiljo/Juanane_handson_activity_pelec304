from django.db import models

class Payment(models.Model):
    payment_id = models.CharField(max_length=10, primary_key=True)
    student_id = models.CharField(max_length=10)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_length=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
