# Generated by Django 3.2.5 on 2021-07-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('preview', models.CharField(max_length=250, verbose_name='Превью')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('date', models.DateTimeField(verbose_name='Дата создания')),
            ],
        ),
    ]
