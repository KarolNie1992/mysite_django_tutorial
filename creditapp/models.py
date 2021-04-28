from django.db import models

# Create your models here.

class Credit (models.Model):

    #nazwa kalkulacji, nazwa własna 
    credit_name_text = models.CharField(max_length=200 )
    #oprocentowanie
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    #liczba rat
    installmentsVal = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    #wartosc kredytu
    creditValue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #miesięczny przychód
    monthlyIncome = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #miesięczne wydatki
    monthlyExpenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.credit_name_text

class CreditResult(models.Model):

    credit = models.ForeignKey(Credit,on_delete=models.CASCADE)
    #Możliwą kwotę pożyczki
    #TO DO #wartosc kredytu #creditValue na razie
    #kwotę całkowitą do spłaty
    totalAmountRepaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #czas na jaki został rozłożony okres spłaty
    #TO DO
    #miesięczną ratę
    monthlyInstallment = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.totalAmountRepaid

