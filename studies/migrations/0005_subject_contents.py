# Generated by Django 4.1.3 on 2022-11-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0004_alter_study_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='contents',
            field=models.TextField(blank=True, null=True),
        ),
    ]
