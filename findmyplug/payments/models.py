from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    entity = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    amount_paid = models.IntegerField()
    amount_due = models.IntegerField()
    currency = models.CharField(max_length=20)
    receipt= models.CharField(max_length=25)
    offer_id: models.CharField(max_length=25,null=True,blank=True)
    status=models.CharField(max_length=20)
    attempts= models.IntegerField()
    created_at= models.IntegerField()

class Payment(models.Model):
    razorpay_payment_id = models.CharField(max_length=23)
    razorpay_order_id = models.CharField(max_length=25, primary_key=True)
    razorpay_signature = models.CharField(max_length=70)