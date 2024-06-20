from django import forms
from django.core import validators

class Form(forms.Form):
    name = forms.CharField(label='User Name', initial="User", help_text="Name Must be within 50 Characters", required=False, widget=forms.Textarea(attrs={'id':'name', 'placeholder':"Enter Your Name"}))
    #file = forms.ImageField()
    # email = forms.EmailField(label='User Email')
    # age = forms.IntegerField(label='Age')
    # weight = forms.IntegerField(label='Weight')
    # balance = forms.IntegerField(label='Balance')
    check = forms.BooleanField(label='Are You Human?')
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateField(widget=forms.DateInput(attrs={'type':'datetime-local'}))

    CHOICES = [("S","Small"),("M","Medium"),("L","Large")]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    CHOICES = [("C","Chilli"),("M","Mashroom"),("B","Beef")]
    size = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)

class StudentForm(forms.Form):
    name = forms.CharField(label='Student Name: ', validators=[validators.MinLengthValidator(6, message="Write a name a least 6 characters")])
    email = forms.EmailField(label='Email: ', validators=[validators.EmailValidator(message="Write a valid email")])
    age = forms.IntegerField(validators=[validators.MinValueValidator(6, "We are not Student")])

    file = forms.FileField(validators=[validators.FileExtensionValidator('png', message="Your file must be png")])

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) > 19:
    #         raise forms.ValidationError("Write a name less then 18 character")
    #     else:
    #         return valname
       
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '@' not in valemail or '.com' not in valemail:
    #         raise forms.ValidationError("Write proper Email")
    
    #     else:
    #         return valemail


class PasswordValidationProject(forms.Form):
    name = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()

        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_confirm_pass = self.cleaned_data['confirm_password']

        if val_pass != val_confirm_pass:
            raise forms.ValidationError("Password is incorrect")
        
        if len(val_name) < 10:
            raise forms.ValidationError("Name must be 10 characters")