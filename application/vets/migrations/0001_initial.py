# Generated by Django 4.0.1 on 2022-01-31 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date_time', models.DateTimeField()),
                ('surgery', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('primary_contact', models.IntegerField()),
                ('secondary_contact', models.IntegerField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('human_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vets.human')),
            ],
            bases=('vets.human',),
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('human_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vets.human')),
                ('salary', models.IntegerField()),
            ],
            bases=('vets.human',),
        ),
    ]