from django.db import models

# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.IntegerField()
    budget_type = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # only one auto option can be set
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'budget'
        verbose_name = '자산'
        ordering = ['-created_at']
