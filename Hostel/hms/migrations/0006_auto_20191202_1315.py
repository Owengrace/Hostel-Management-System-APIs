# Generated by Django 2.2.3 on 2019-12-02 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0005_warden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='warden',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='hms.Warden'),
        ),
    ]
