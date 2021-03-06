# Generated by Django 2.0.4 on 2018-08-12 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import transaction.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_name', models.CharField(max_length=20)),
                ('cost_amount', models.IntegerField(validators=[transaction.validator.positive_int_type])),
                ('credit_type', models.SmallIntegerField(validators=[transaction.validator.type_in_range])),
                ('debit_type', models.SmallIntegerField(validators=[transaction.validator.type_in_range])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, validators=[transaction.validator.positive_int_type])),
            ],
            options={
                'verbose_name': '거래',
                'db_table': 'transaction',
                'ordering': ['-created_at'],
            },
        ),
    ]
