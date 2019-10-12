# Generated by Django 2.2.4 on 2019-09-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='choices',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='ABC', max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='Started', max_length=120),
        ),
    ]