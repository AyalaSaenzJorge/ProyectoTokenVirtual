# Generated by Django 3.2.11 on 2022-01-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('token_value', models.IntegerField(blank=True, null=True)),
                ('created_since', models.BigIntegerField(blank=True, null=True)),
                ('times_used', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tokens',
                'managed': False,
            },
        ),
    ]
