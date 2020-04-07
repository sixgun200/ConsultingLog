# Generated by Django 2.2 on 2020-01-31 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='pjt', max_length=50)),
                ('fname', models.CharField(default='Phillip', max_length=128)),
                ('lname', models.CharField(default='Trujillo', max_length=128)),
                ('email', models.CharField(default='pjt@outlook.com', max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
                ('start', models.TimeField()),
                ('stop', models.TimeField()),
                ('duration', models.TimeField()),
                ('created_by', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='log_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=128)),
                ('contactfname', models.CharField(max_length=128)),
                ('contactlname', models.CharField(max_length=128)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=255)),
                ('rate', models.FloatField()),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='clients', to='log_app.User')),
            ],
        ),
    ]
