# Generated by Django 2.2.4 on 2019-08-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190824_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='products/images'),
        ),
    ]