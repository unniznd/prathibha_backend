# Generated by Django 4.2 on 2023-05-27 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('fee', '0005_alter_feeinstallment_installment'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeinstallment',
            name='year',
            field=models.CharField(default=2023, max_length=20),
        ),
        migrations.AlterField(
            model_name='feeinstallment',
            name='installment',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='fees',
            name='installment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fee.feeinstallment'),
        ),
        migrations.AlterField(
            model_name='fees',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.students'),
        ),
        migrations.AlterUniqueTogether(
            name='feeinstallment',
            unique_together={('year', 'installment')},
        ),
    ]
