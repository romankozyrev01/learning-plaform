# Generated by Django 3.2.5 on 2021-08-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_alter_test_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcase',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
