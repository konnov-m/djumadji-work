# Generated by Django 3.2.4 on 2021-07-11 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_auto_20210711_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='specialty',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='specialty',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.specialty'),
            preserve_default=False,
        ),
    ]