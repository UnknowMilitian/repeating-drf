# Generated by Django 5.1.1 on 2024-10-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
                ('days', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
