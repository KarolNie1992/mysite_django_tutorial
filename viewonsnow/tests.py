from django.test import TestCase
from django.test import Client
from .models import Snow
from .functions import viewOnSnow


#Create your tests here.
class SnowModelTests(TestCase):
    def test_return_value_from_function_viewOnSnow(self):
        """
        Weryfikacja czy wartość zwracana przez funkcję jest zgodna z danymi wejściowymi.
        """
        inputList=[2,1,3,1,2,5,1,3,1,1,2,1,1]
        outputList = viewOnSnow(inputList)
        self.assertEqual(outputList,[2,2,3,3,3,5,3,3,2,2,2,1,1])
    
    def test_return_value_from_function_viewOnSnow_notOK(self):
        """
        Weryfikacja czy wartość zwracana przez funkcję nie jest zgodna z danymi wejściowymi.
        """
        inputList=[2,1,3,1,2,5,1,3,1,1,2,1,1]
        outputList = viewOnSnow(inputList)
        self.assertNotEqual(outputList,[2,2,3,3,3,5,3,3,2,2,2,1,3])

