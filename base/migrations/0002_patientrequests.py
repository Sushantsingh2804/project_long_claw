# Generated by Django 3.0.6 on 2020-06-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-')], default='O+', max_length=3)),
                ('contact_info', models.CharField(max_length=100)),
                ('attached_msg', models.CharField(max_length=50)),
            ],
        ),
    ]