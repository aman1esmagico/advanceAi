# Generated by Django 5.0.4 on 2024-04-09 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('OPENING', 'Opening'), ('QUESTIONING', 'Questioning'), ('PRESENTING', 'Presenting'), ('CLOSING_OUTCOME', 'Closing & Outcome')], max_length=20)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('statement', models.TextField()),
                ('transcription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.transcription')),
            ],
        ),
    ]
