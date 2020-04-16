# Generated by Django 3.0.3 on 2020-03-07 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20200307_0843'),
        ('transact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loan',
            options={'ordering': ['mode_cycles']},
        ),
        migrations.AlterModelOptions(
            name='pay',
            options={'ordering': ['loan_id']},
        ),
        migrations.RenameField(
            model_name='pay',
            old_name='cycles',
            new_name='cycle',
        ),
        migrations.AlterField(
            model_name='loan',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.Client'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='loan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transact.Loan'),
        ),
    ]
