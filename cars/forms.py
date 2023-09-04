from typing import Any, Dict
from django import forms
from cars.models import Car

class CarsModelFrom(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'Valor mínimo do carro deve ser maior que R$10.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1950:
            self.add_error('factory_year', 'Ano do veiculo precisa ser maior que 1950')
        return factory_year