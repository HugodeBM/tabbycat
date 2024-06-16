# Generated by Django 5.0.4 on 2024-05-04 13:21

import utils.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("draw", "0008_alter_debateteam_side_alter_teamsideallocation_side"),
        (
            "participants",
            "0022_rename_team_tournament_institution_short_reference_participant_tournam_160efa_idx_and_more",
        ),
        ("tournaments", "0012_alter_round_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="teamsideallocation",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="teamsideallocation",
            constraint=utils.models.UniqueConstraint(
                fields=("round", "team"), name="draw_teamsideallocation_round__team_uniq"
            ),
        ),
    ]
