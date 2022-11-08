from django import forms
from . models import MlModel
from django.forms import ModelForm



'''
class MlForm(forms.Form):
    likes = forms.IntegerField(label='like amount')
    comments = forms.IntegerField(label='comment amount')
    category = forms.ChoiceField(label='please select a category',
                                widget=forms.RadioSelect, 
                                choices=CATEGORIES)
'''

class MlForm(ModelForm):
    class Meta:
        model = MlModel
        fields = '__all__'