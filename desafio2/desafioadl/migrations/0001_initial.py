# Generated by Django 4.2.11 on 2024-05-02 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('eliminada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('eliminada', models.BooleanField(default=False)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtareas', to='desafioadl.tarea')),
            ],
        ),
    ]
