from django.db import models

# Create your models here.

class Credit (models.Model):

    #nazwa kalkulacji, nazwa własna 
    credit_name_text = models.CharField(max_length=200, unique=True, )
    #oprocentowanie
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    #liczba rat
    installmentsVal = models.DecimalField(max_digits=4, decimal_places=0, null=False)
    #wartosc kredytu
    creditValue = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    #miesięczny przychód
    monthlyIncome = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    #miesięczne wydatki
    monthlyExpenses = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    #Możliwą kwotę pożyczki
    #TO DO #wartosc kredytu #creditValue na razie
    #kwotę całkowitą do spłaty
    totalAmountRepaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #czas na jaki został rozłożony okres spłaty
    #TO DO
    #miesięczną ratę
    monthlyInstallment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #data wykonania kalkulacji
    creditResultDate = models.DateTimeField('calculation date', null=True)

    def __str__(self):
        return self.credit_name_text

