# Generated by Django 5.0.2 on 2024-03-30 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_application', '0003_remove_application_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationClient',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('client_secret', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='userapplicationauthorization',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_application.applicationclient'),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
