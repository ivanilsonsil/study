# Generated by Django 4.1.3 on 2022-11-16 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0002_study'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='subject',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='studies.subject'),
        ),
    ]