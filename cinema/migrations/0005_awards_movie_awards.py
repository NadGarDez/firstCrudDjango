# Generated by Django 4.2.3 on 2023-09-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_director_actor_image_director_actor_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='awards',
            field=models.ManyToManyField(blank=True, null=True, to='cinema.awards'),
        ),
    ]