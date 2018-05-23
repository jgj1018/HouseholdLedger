from django.db import models

class Transaction(models.Model):
  user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  transaction_id = models.BigAutoField()
  transaction_name = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

class DebitSide(models.Model):
  transaction_id = models.ForeignKey('Transaction', on_delete=models.CASCADE)
  cost_amount = models.IntegerField()
  transaction_type = models.SmallIntegerField()

class CreditSide(models.Model):
  transaction_id = models.ForeignKey('Transaction', on_delete=models.CASCADE)
  cost_amount = models.IntegerField()
  transaction_type = models.SmallIntegerField()
