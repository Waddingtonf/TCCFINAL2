from django.forms import ModelForm
from django import forms
from TCCApp.models import Upload, Mockup

class UploadForm(ModelForm):
    img = forms.ImageField()
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'forms-nome',
        'placeholder': 'Insira o Nome da Imagem',
        'maxlength':'255'
        }))

    class Meta:
        model = Upload
        fields = ['img', 'nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['img'].widget.attrs.update({'class': 'forms-img'})

class MockupForm(ModelForm):
    cor = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'forms-mock',
        'placeholder': 'Insira o Código Cor',
        'maxlength':'255',
        'value': '#00000'
        }))


    class Meta:
        model = Mockup
        fields = ['cor', 'imagem']