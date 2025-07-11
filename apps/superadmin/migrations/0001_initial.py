# Generated by Django 5.1.6 on 2025-02-11 21:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supersyndic', '0001_initial'),
        ('syndic', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('fonctionnalites', models.JSONField(verbose_name='Features')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('date_fin', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('fonctionnalites_personnalisees', models.JSONField(blank=True, null=True, verbose_name='Custom Features')),
                ('est_personnalise', models.BooleanField(default=True, verbose_name='Is Custom')),
                ('supersyndic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supersyndic_licenses', to='supersyndic.supersyndic', verbose_name='Super Syndic')),
                ('syndic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='syndic_licenses', to='syndic.syndic', verbose_name='Syndic')),
                ('license_base', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licenses', to='superadmin.licensebase', verbose_name='Base License')),
            ],
        ),
        migrations.CreateModel(
            name='Superadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supersyndics', models.ManyToManyField(blank=True, related_name='managed_by_superadmins', to='supersyndic.supersyndic', verbose_name='SuperSyndics')),
                ('syndics', models.ManyToManyField(blank=True, related_name='managed_by_superadmins', to='syndic.syndic', verbose_name='Syndics')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='superadmin_profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
