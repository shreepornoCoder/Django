from django import forms
from first_app.models import StudentModel

class StudentModel(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"

        labels = {
            'name':"Student Name",
            'roll':"Student Roll"
        }

        help_texts = {
            'name' : 'Write Your Full Name'
        }

        error_messages = {
            'name' : {'required':'Your name is Required'}
        }