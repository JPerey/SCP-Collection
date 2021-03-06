# Generated by Django 3.2.4 on 2021-07-20 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210720_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sighting', models.CharField(choices=[('R', 'Early Morning'), ('M', 'Midday'), ('E', 'Evening')], default='R', max_length=1)),
                ('scp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.scp')),
            ],
        ),
    ]
