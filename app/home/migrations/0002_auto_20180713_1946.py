# Generated by Django 2.0.4 on 2018-07-13 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]