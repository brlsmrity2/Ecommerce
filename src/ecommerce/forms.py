from django import forms

from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Your Full Name'}),
        max_length=100,
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Your Email'}),
        max_length=100,
        required=True
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Your Message'}),
        required=True
    )


#custom validation

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email Has to be Gmail")        
        return email
    
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)    