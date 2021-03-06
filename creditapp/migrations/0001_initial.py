# Generated by Django 3.2 on 2021-04-29 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_name_text', models.CharField(max_length=200)),
                ('interest_rate', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('installmentsVal', models.DecimalField(decimal_places=0, default=0, max_digits=4)),
                ('creditValue', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('monthlyIncome', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('monthlyExpenses', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CreditResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalAmountRepaid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('monthlyInstallment', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('creditResultDate', models.DateTimeField(verbose_name='calculation date')),
                ('credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditapp.credit')),
            ],
        ),
    ]
