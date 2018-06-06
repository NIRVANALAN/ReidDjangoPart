# Generated by Django 2.0.5 on 2018-06-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('participants', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
