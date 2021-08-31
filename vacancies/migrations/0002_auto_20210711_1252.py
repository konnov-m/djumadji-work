# Generated by Django 3.2.4 on 2021-07-11 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='specialty',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='specialti',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.specialty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.CharField(max_length=32),
        ),
    ]