# Generated by Django 3.1.7 on 2021-03-07 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50, null=True)),
                ('gen', models.CharField(max_length=7)),
                ('email', models.EmailField(max_length=100)),
                ('pwd', models.CharField(max_length=10)),
                ('approveldt', models.DateTimeField(null=True)),
                ('utype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.usertype')),
            ],
        ),
    ]
