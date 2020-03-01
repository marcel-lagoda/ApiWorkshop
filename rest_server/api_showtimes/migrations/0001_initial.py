# Generated by Django 3.0.3 on 2020-03-01 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_adaptations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_showtimes.Cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_adaptations.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='movies',
            field=models.ManyToManyField(through='api_showtimes.Screening', to='api_adaptations.Movie'),
        ),
    ]