# Generated by Django 5.1.2 on 2024-11-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_all_up_doc_p_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_up_doc',
            name='p_details',
            field=models.TextField(max_length=55534),
        ),
    ]
