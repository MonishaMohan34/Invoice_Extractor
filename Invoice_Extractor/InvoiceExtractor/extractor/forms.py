from django import forms

class InvoiceUploadForm(forms.Form):
    pdf_file = forms.FileField()
