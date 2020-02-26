from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    vmail = forms.EmailField(label='Enter your email again.')
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        vmail = cleaned_data['vmail']

        if email != vmail:
            raise forms.ValidationError('The email addresses do not match.')
    