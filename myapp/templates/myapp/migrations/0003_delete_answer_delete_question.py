# Generated by Django 5.0.6 on 2024-06-15 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]