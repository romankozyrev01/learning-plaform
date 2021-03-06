# Generated by Django 3.2.5 on 2021-08-26 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0005_stepuser_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('text', models.TextField()),
                ('step', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reading_material', to='lessons.step')),
            ],
        ),
    ]
