# Generated by Django 2.1 on 2019-09-03 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190829_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductImage')),
            ],
        ),
    ]
