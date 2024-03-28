# Generated by Django 5.0.2 on 2024-02-28 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_matchtable_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('name', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('publicProfile', models.ImageField(null=True, upload_to='')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='TeamInDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.division')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.team')),
            ],
            options={
                'unique_together': {('division', 'team')},
            },
        ),
        migrations.DeleteModel(
            name='Divisons',
        ),
    ]