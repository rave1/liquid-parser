# Generated by Django 4.0.4 on 2022-05-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liquid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.JSONField(default=list)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
    ]
