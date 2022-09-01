# Generated by Django 3.0.4 on 2022-09-01 08:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0004_auto_20200325_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='game',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game'),
        ),
        migrations.AlterField(
            model_name='move',
            name='x',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='move',
            name='y',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
