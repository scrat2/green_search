"""Here you create forms like you create models in models.py you give all specifications for each field."""
from django import forms


class SearchForm(forms.Form):
    firstname = forms.CharField(
        label='Firstname',
        widget=forms.TextInput(attrs={'placeholder': 'Prenom'}),
        max_length=20,
        required=True
    )

    lastname = forms.CharField(
        label='Lastname',
        widget=forms.TextInput(attrs={'placeholder': 'Nom'}),
        max_length=30,
        required=True
    )

    speciality = forms.CharField(
        label='Speciality',
        widget=forms.TextInput(attrs={'placeholder': 'Filiere'}),
        max_length=3,
        required=True
    )

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Adresse'}),
        max_length=50,
        required=True
    )

    postalCode = forms.CharField(
        label='PostalCode',
        widget=forms.TextInput(attrs={'placeholder': 'Code postal'}),
        max_length=5,
        required=True
    )

    city = forms.CharField(
        label='City',
        widget=forms.TextInput(attrs={'placeholder': 'Ville'}),
        max_length=20,
        required=True
    )

    picture = forms.ImageField(
        label='Picture',
    )
