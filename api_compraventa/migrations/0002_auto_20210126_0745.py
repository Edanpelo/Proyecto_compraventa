# Generated by Django 3.1.5 on 2021-01-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_compraventa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prendas',
            name='capital_debt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prendas',
            name='debt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prendas',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prendas',
            name='interest_rate',
            field=models.FloatField(default=0.1),
        ),
        migrations.AlterField(
            model_name='prendas',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]