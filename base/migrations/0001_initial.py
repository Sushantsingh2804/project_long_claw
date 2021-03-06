# Generated by Django 3.0.6 on 2020-06-28 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-')], default='O+', max_length=3)),
                ('resident_state', models.CharField(max_length=2)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('registered_as', models.CharField(choices=[('Donor', 'Donor'), ('Patient', 'Patient')], default='Donar', max_length=7)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
