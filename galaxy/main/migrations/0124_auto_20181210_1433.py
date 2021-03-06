from django.db import migrations, models

SET_COMMUNITY_SURVEY_COUNT = """
UPDATE main_repository
set community_survey_count =
    (SELECT COUNT (*) FROM main_communitysurvey
     WHERE main_communitysurvey.repository_id = main_repository.id)
"""


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0123_fix_importtaskmessage_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='community_survey_count',
            field=models.IntegerField(default=0),
        ),
        migrations.RunSQL(SET_COMMUNITY_SURVEY_COUNT),
    ]
