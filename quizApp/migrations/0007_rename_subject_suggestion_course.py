# Generated by Django 4.0.3 on 2022-12-17 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0006_rename_suggestions_suggestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='subject',
            new_name='course',
        ),
    ]
