# Generated by Django 2.2.6 on 2021-01-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20210117_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcat',
            name='id',
        ),
        migrations.AlterField(
            model_name='addcat',
            name='Cat_Title',
            field=models.CharField(max_length=60, primary_key=True, serialize=False),
        ),
    ]