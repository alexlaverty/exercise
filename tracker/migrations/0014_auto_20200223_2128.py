# Generated by Django 2.2.10 on 2020-02-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_userprofile_weight_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]