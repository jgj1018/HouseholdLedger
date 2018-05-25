from django.db import models
from django.urls import reverse

# Whenever any transaction happens, The row is added to this table.
class Transaction(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    transaction_id = models.BigAutoField()
    transaction_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    cost_amount = models.IntegerField()
    transaction_type = models.SmallIntegerField()

    class Meta:
        db_table = 'transaction'
        verbose_name = '거래'
        ordering = ['-created_at']

    def __str__(self):
        return self.transaction_name

    def get_absolute_url(self):
        #TODO have to set what page should be next.
        return reverse('', args=[str(self.user_id)])

