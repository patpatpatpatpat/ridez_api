# Generated by Django 5.1.5 on 2025-01-23 14:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('EN_ROUTE', 'En Route'), ('PICK_UP', 'Pick Up'), ('DROP_OFF', 'Drop Off')], max_length=15)),
                ('pickup_latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True)),
                ('pickup_longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=13, null=True)),
                ('dropoff_latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True)),
                ('dropoff_longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=13, null=True)),
                ('pickup_time', models.DateTimeField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driven_rides', to=settings.AUTH_USER_MODEL)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ridden_rides', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RideEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ride')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
