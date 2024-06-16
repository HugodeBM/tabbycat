# Generated by Django 2.0.5 on 2018-07-22 00:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tournaments", "0002_remove_tournament_welcome_msg"),
        ("participants", "0005_auto_20180717_0820"),
        ("notifications", "0003_home_page_email"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MessageSentRecord",
            new_name="SentMessageRecord",
        ),
        migrations.AlterModelOptions(
            name="sentmessagerecord",
            options={
                "ordering": ["timestamp"],
                "verbose_name": "sent message",
                "verbose_name_plural": "sent messages",
            },
        ),
        migrations.AddField(
            model_name="sentmessagerecord",
            name="context",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, null=True, verbose_name="context"
            ),
        ),
        migrations.AddField(
            model_name="sentmessagerecord",
            name="message",
            field=models.TextField(null=True, verbose_name="message"),
        ),
        migrations.AddField(
            model_name="sentmessagerecord",
            name="email",
            field=models.EmailField(null=True, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="sentmessagerecord",
            name="event",
            field=models.CharField(
                blank=True,
                choices=[
                    ("p", "team points"),
                    ("c", "ballot confirmed"),
                    ("f", "feedback URL"),
                    ("b", "ballot URL"),
                    ("u", "landing page URL"),
                    ("d", "draw released"),
                ],
                max_length=1,
                verbose_name="event",
            ),
        ),
        migrations.AlterField(
            model_name="sentmessagerecord",
            name="method",
            field=models.CharField(
                choices=[("e", "email"), ("s", "SMS")], max_length=1, verbose_name="method"
            ),
        ),
        migrations.AlterField(
            model_name="sentmessagerecord",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="participants.Person",
                verbose_name="recipient",
            ),
        ),
    ]
