from django import forms


class ConversionForm(forms.Form):
    amount = forms.DecimalField(label='Value', widget=forms.NumberInput(attrs={'id': 'amount'}))
    from_currency = forms.ChoiceField(choices=[
        ('BRL', 'Real Brasileiro (BRL)'),
        ('USD', 'Dólar Americano (USD)'),
        ('EUR', 'Euro (EUR)'),
        ('GBP', 'Libra Esterlina (GBP)'),
    ], label='From:', widget=forms.Select(attrs={'class': 'from_currency'}))
    to_currency = forms.ChoiceField(choices=[
        ('BRL', 'Real Brasileiro (BRL)'),
        ('USD', 'Dólar Americano (USD)'),
        ('EUR', 'Euro (EUR)'),
        ('GBP', 'Libra Esterlina (GBP)'),
    ], label='To:', widget=forms.Select(attrs={'class': 'to_value'}))
