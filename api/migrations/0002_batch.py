# Generated by Django 3.2.7 on 2022-02-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20, null=True)),
                ('std', models.CharField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th'), ('9', '9th'), ('10', '10th')], default='1', max_length=20)),
            ],
            options={
                'unique_together': {('year', 'std')},
            },
        ),
    ]
