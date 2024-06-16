# Generated by Django 2.2.13 on 2020-06-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tournaments", "0006_auto_20191109_1240"),
    ]

    operations = [
        migrations.AlterField(
            model_name="round",
            name="seq",
            field=models.PositiveIntegerField(
                help_text="A number that determines the order of the round, should count consecutively from 1 for the first round",
                verbose_name="sequence number",
            ),
        ),
    ]
