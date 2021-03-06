# Generated by Django 3.2.7 on 2021-12-02 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordText', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Anagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anagramText', models.CharField(max_length=200)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anagram.word')),
            ],
        ),
    ]
