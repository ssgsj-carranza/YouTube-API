# Generated by Django 3.1.7 on 2021-04-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default=None, max_length=200)),
                ('like', models.IntegerField(default=0, null=True)),
                ('video_id', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
