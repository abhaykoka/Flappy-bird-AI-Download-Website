from django import forms


class DownloadForm(forms.Form):
    name=forms.CharField(max_length=20,required=True)
    emailaddress = forms.CharField(max_length=100, required=True)
    num2 = forms.IntegerField(required=True)
