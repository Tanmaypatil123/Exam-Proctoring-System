# Generated by Django 4.2.7 on 2023-11-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermodel_tc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(blank=True, max_length=50, null=True)),
                ('feedback', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]