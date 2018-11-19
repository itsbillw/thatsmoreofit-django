# Generated by Django 2.1.1 on 2018-11-19 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('blood_sugar', models.IntegerField(blank=True, null=True)),
                ('carbs', models.IntegerField(blank=True, null=True)),
                ('insulin', models.IntegerField(blank=True, null=True)),
                ('insulin_type', models.CharField(choices=[('Tresiba', 'Basal'), ('Fiasp', 'Bolus')], default='Fiasp', max_length=10)),
                ('event_type', models.CharField(choices=[('Manual', 'Manual'), ('Dexcom', 'Auto')], default='Manual', max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Topic'),
        ),
    ]
