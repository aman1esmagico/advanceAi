# Generated by Django 5.0.4 on 2024-04-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0007_transcription_segments'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='segment_number',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
    ]