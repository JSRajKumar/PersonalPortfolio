# Generated by Django 3.0.6 on 2020-06-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=500)),
                ('BlogDate', models.DateField()),
            ],
        ),
    ]
