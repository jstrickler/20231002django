# Generated by Django 4.1 on 2023-10-05 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email_address', models.EmailField(max_length=64)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('position', models.CharField(max_length=32)),
                ('start_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.city')),
            ],
        ),
    ]
