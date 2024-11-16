# Generated by Django 5.1.3 on 2024-11-13 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30, null=True)),
                ('desg', models.CharField(max_length=30, null=True)),
                ('salary', models.FloatField(null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]