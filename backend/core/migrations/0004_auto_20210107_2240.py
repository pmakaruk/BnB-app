# Generated by Django 3.1.5 on 2021-01-07 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210105_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='data',
            field=models.TextField(default=dict, null=True),
        ),
    ]
