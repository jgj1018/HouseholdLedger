from django.db import models
from django.urls import reverse
from .validator import *

# Whenever any transaction happens, The row is added to this table.


class Transaction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, validators=[positive_int_type])
    # Primary Key necessary, Or auto generate Id column
    # Only Primary Key can be autoField
    transaction_id = models.BigAutoField(primary_key=True)
    transaction_name = models.CharField(max_length=20)
    cost_amount = models.IntegerField(validators=[positive_int_type])
    credit_type = models.SmallIntegerField(validators=[type_in_range])
    debit_type = models.SmallIntegerField(validators=[type_in_range])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # only one auto option can be set
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'
        verbose_name = '거래'
        ordering = ['-created_at']

    def __str__(self):
        return self.transaction_name

    def get_absolute_url(self):
        # TODO have to set what page should be next.
        return reverse('', args=[str(self.user_id)])
