from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Member, City, District, Department

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Prénom', 'class': 'form-control'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nom', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur.'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requis. 150 caractères maximum. Lettres, chiffres et les symboles @/./+/-/_ uniquement.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe.'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text texte-muted small"><li>Votre mot de passe ne peut pas être trop similaire à vos autres informations personnelles.</li><li>Votre mot de passe doit contenir au moins 8 caractères.</li><li>Votre mot de passe ne peut pas être un mot de passe couramment utilisé.</li><li>Votre mot de passe ne peut pas être entièrement numérique.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe.'
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmer le mot de passe', 'class': 'form-control'})
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Entrez le même mot de passe qu\'auparavant, pour vérification.</small></span>'


# Creation du formulaire d'ajout d'un membre
# noinspection PyTypeChecker
class AddMemberForm(forms.ModelForm):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label=''
    )
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,  # Quartier est facultatif
        label=''
    )

    class Meta:
        model = Member
        exclude = ('user',)
        fields = ['name', 'firstName', 'email', 'phone', 'city', 'district']


    def __init__(self, *args, **kwargs):
        super(AddMemberForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = ''
        self.fields['name'].label = 'Nom:'


        self.fields['firstName'].widget.attrs['class'] = 'form-control'
        self.fields['firstName'].widget.attrs['placeholder'] = ''
        self.fields['firstName'].label = 'Prénom:'


        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['email'].label = 'Email:'

        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = ''
        self.fields['phone'].label = 'Numéro de téléphone:'

        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['placeholder'] = ''
        self.fields['city'].label = 'Ville'

        self.fields['district'].widget.attrs['class'] = 'form-control'
        self.fields['district'].widget.attrs['placeholder'] = ''
        self.fields['district'].label = 'Quartier'



# noinspection PyTypeChecker
class AddDepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        exclude = ('user',)
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(AddDepartmentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Nom du département.'
        self.fields['name'].label = ''


# noinspection PyTypeChecker
class AddCityForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label=''
    )

    class Meta:
        model = City
        exclude = ('user',)
        fields = ['name', 'department']

    def __init__(self, *args, **kwargs):
        super(AddCityForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Nom de la ville.'
        self.fields['name'].label = ''


# noinspection PyTypeChecker
class AddDistrictForm(forms.ModelForm):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label=''
    )

    class Meta:
        model = District
        exclude = ('user',)
        fields = ['name', 'city']

    def __init__(self, *args, **kwargs):
        super(AddDistrictForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Nom du quartier.'
        self.fields['name'].label = ''
