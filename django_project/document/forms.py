# forms.py
from django import forms

class DocumentForm(forms.Form):
    document_id = forms.IntegerField(label='Document ID')
    document_type = forms.CharField(label='Document Type', max_length=100)
    case_id = forms.CharField(label='Case ID', max_length=100)
    update_date = forms.DateField(label='Update Date')
