# Generated by Django 4.0.5 on 2022-11-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=256)),
                ('link', models.URLField(default='')),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('E', 'ENTERTAINMENT'), ('N', 'NEWS'), ('S', 'SPORTS')], default='E', max_length=3)),
                ('sub_category', models.CharField(choices=[('SOC', 'SOCIAL MEDIA'), ('KNO', 'KNOWLEDGE'), ('FAN', 'FAN APP')], default='SOC', max_length=3)),
            ],
        ),
    ]
