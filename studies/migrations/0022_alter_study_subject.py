# Generated by Django 4.1.3 on 2022-12-09 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0021_alter_study_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studies', to='studies.subject'),
        ),
    ]