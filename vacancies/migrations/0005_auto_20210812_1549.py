# Generated by Django 3.2.4 on 2021-08-12 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0004_auto_20210711_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='image',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=128)),
                ('written_phone', models.CharField(max_length=16)),
                ('written_cover_letter', models.CharField(max_length=512)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='vacancies.vacancy')),
            ],
        ),
    ]
