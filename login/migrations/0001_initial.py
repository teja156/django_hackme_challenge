# Generated by Django 2.2.10 on 2020-02-08 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrackedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('profile_link', models.URLField()),
                ('solved_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
