# Generated by Django 2.1.1 on 2018-09-10 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouTiaoNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(max_length=500, null=True)),
                ('source', models.CharField(max_length=200, null=True)),
                ('time', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
