# Generated by Django 3.0.6 on 2020-06-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_id', models.CharField(max_length=16)),
                ('value', models.BooleanField()),
            ],
        ),
    ]
