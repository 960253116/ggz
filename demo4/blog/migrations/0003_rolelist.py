# Generated by Django 2.2.2 on 2019-06-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_introduce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rolelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]