# Generated by Django 3.2.20 on 2023-08-13 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0002_feat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
                ('subrace_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_v2.race')),
            ],
            options={
                'verbose_name_plural': 'races',
            },
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.race')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
