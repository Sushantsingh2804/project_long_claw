# Generated by Django 3.0.6 on 2020-06-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_patientrequests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrequests',
            name='attached_msg',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='patientrequests',
            name='contact_info',
            field=models.TextField(),
        ),
    ]