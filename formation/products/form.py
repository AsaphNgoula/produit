from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    email =forms.EmailField()
    name=forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'placeholder':'entrer votre nom ici'
    }))
    description=forms.CharField(label='', widget=forms.Textarea(attrs= {
            'PlaceHolder':'enter your product description',
            'rows':5,
            'cols':10
            }))
    price=forms.DecimalField(label='')
    # image=forms.ImageField()
    slug=forms.SlugField(label='',widget=forms.TextInput(attrs={
        'placeholder':'entrer votre slug ici'
    }))
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'image', 'slug')

    def clean_name(self,*args, **kwargs):
            name= self.cleaned_data.get('name')
            if not 'uba' in name:
                raise forms.ValidationError("votre nom doit contenir le mot uba")
            
            elif not 'man' in name:
                 raise forms.ValidationError('man doit apparaitre')
            else:
                return name

    def clean_email(self,*args, **kwargs):
         email =self.cleaned_data.get('email')
         if not email.endswith('com'):
              raise forms.ValidationError("l'email doit se terminer avec .com")











class RowProductForm(forms.Form):
    name=forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'placeholder':'voici votre nom ici'
    }))
    description=forms.CharField(label='', widget=forms.Textarea(attrs= {
            'PlaceHolder':'enter your product description',
            'rows':5,
            'cols':10
            }))
    price=forms.DecimalField(label='')
    # image=forms.ImageField()
    slug=forms.CharField(label='')


    
