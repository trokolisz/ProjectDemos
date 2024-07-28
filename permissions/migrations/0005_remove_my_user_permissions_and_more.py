# Generated by Django 5.0.7 on 2024-07-28 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0004_alter_my_user_tsz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_user',
            name='Permissions',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='last_updated',
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('got_permission_at', models.DateTimeField(auto_now_add=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.my_user')),
            ],
        ),
    ]