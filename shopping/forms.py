from django import forms
from .models import buying_model
class buying_form(forms.Form):
    name = forms.CharField(min_length=3,max_length=100,error_messages={'required': 'This field required!'})
    email = forms.EmailField(max_length=255,error_messages={'required': 'This field required!'})
    # mobile=forms.IntegerField()
    #mobile = forms.RegexField(min_length=10,regex=r'^\+?1?\d{10}$',   error_messages = {'required':"Please enter valid mobile number."})
    deliver_address=forms.CharField(max_length=255,error_messages={'required': 'This field required!'})
    password1=forms.CharField(max_length=255,error_messages={'required': 'This field required!'})
    password2=forms.CharField(max_length=255,error_messages={'required': 'This field required!'})
    def clean_username(self):
        username = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        if username and buying_model.objects.filter(name=username).exclude(email=email).count():
            raise forms.ValidationError("user already registerd")
            return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('name')
        if email and buying_model.objects.filter(email=email).exclude(name=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
            return email

    def clean(self):
        password1 =self.cleaned_data.get('password1')
        password2 =self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self._errors['password2'] = self.error_class(['passwords did not match.'])
            del self.cleaned_data['password2']
        return password1
class sellers_form(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    sellers_contact_address = forms.CharField(max_length=255)
    sellers_contact_number = forms.IntegerField()
class products_form(forms.Form):    
    product_name = forms.CharField(max_length=255)
    product_images = forms.ImageField()
    product_details = forms.CharField(max_length=255)
class contacts_form(forms.Form):
    email = forms.CharField(max_length=255)
    query = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    #product_details=forms.CharField(max_length=255)