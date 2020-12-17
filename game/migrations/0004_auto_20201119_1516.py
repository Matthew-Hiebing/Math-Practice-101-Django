# Generated by Django 3.1.2 on 2020-11-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20201119_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='number_of_correct_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='score',
            name='number_of_incorrect_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='score',
            name='total_questions_answered',
            field=models.IntegerField(default=0),
        ),
    ]