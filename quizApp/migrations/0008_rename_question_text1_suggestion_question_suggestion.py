# Generated by Django 4.0.3 on 2022-12-17 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0007_rename_subject_suggestion_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='question_text1',
            new_name='question_suggestion',
        ),
    ]
