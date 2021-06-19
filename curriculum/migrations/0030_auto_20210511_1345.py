# Generated by Django 2.2.10 on 2021-05-11 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0029_auto_20210511_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslots',
            name='standard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='standard_time_slots', to='curriculum.Standard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workingdays',
            name='standard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='standard_days', to='curriculum.Standard'),
            preserve_default=False,
        ),
    ]
