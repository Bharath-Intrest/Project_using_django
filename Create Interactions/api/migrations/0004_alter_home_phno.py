# Generated by Django 5.1.2 on 2024-10-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_home_phno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='phno',
            field=models.CharField(max_length=20),
        ),
    ]
