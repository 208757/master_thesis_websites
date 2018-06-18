# Generated by Django 2.0.6 on 2018-06-16 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaskedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit', models.CharField(max_length=256)),
                ('challenge', models.CharField(max_length=256)),
                ('token', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('service_id', models.IntegerField()),
                ('verification_key', models.CharField(max_length=256)),
                ('signing_key', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='safe2fa.User'),
        ),
        migrations.AddField(
            model_name='maskeduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unmasked_user', to='safe2fa.User'),
        ),
    ]