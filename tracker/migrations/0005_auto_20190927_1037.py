# Generated by Django 2.1.7 on 2019-09-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_entries_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='Tracking',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
