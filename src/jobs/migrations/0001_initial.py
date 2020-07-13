# Generated by Django 2.2.12 on 2020-05-01 05:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('external_url', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=255, null=True)),
                ('employment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('pay_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('published', models.BooleanField(blank=True, default=False)),
                ('is_featured', models.BooleanField(blank=True, default=False)),
                ('is_expired', models.BooleanField(blank=True, default=False)),
                ('apply_here', models.BooleanField(blank=True, default=False)),
                ('apply_instructions', models.TextField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('positions_to_fill', models.PositiveIntegerField(blank=True)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='accounts.Employer')),
            ],
            options={
                'verbose_name': 'job',
                'verbose_name_plural': 'jobs',
            },
        ),
    ]