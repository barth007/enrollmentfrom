# enrollment/forms.py
from django import forms
from .models import Applicant, CheckboxOption  # Add CheckboxOption to your imports

class ApplicantForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
    ]

    packages_choices = [
        ('MS-Word','MS-Word'),
        ('MS-Excel','MS-Excel'),
        ('MS-PowerPoint','MS-PowerPoint'),
        ('Graphics and Design e.g AutoCAD, Photoshop','Graphics and Design e.g AutoCAD, Photoshop'),
        ('Programming, Statistical and Data Analyses','Programming, Statistical and Data Analyses'),
    ]


   # gender = forms.ChoiceField(
    #    choices=GENDER_CHOICES,
     #   widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    #)
    class Meta:
        model = Applicant
        # Or list the fields you want to include in your form
        fields = '__all__'
       
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name', 'required':'required'}),
            
            'dob': forms.TextInput(attrs={'class':'form-control', 'placeholder':'dob', 'type': 'date'}),

            'gender':forms.RadioSelect(),

            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a Valid Email', 'required':'required'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your phone number', 'required':'required', 'type': 'tel'}),
            'qualification':forms.Select(attrs={'class':'form-control', 'required': 'required'}),
            'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'LGA':forms.TextInput(attrs={'class':'form-control', 'placeholder':'LGA'}),
            'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'locality'}),
            'govtID':forms.Select(attrs={'class':'form-control', 'placeholder':'govtID'}),
            'employment':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'occupation':forms.TextInput(attrs={'class':'form-control', 'placeholder':'occupation'}),
            'bankAccount':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'noBankReason':forms.TextInput(attrs={'class':'form-control', 'placeholder':'noBankReason'}),
            'disability' :forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'disabilityType':forms.TextInput(attrs={'class':'form-control', 'placeholder':'disabilityType'}),
            'computerLiteracy':forms.Select(attrs={'class':'form-control', 'placeholder':'computerLiteracy'}),
            'packages' : forms.CheckboxSelectMultiple(),
            'hasComputer':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'familiar':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'availability':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'interestLevel':forms.Select(attrs={'class':'form-control', 'placeholder':'Interest Level'}),
            'program':forms.CheckboxSelectMultiple(),
            'social_media_handle_facebook':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Facebook ID'}),
            'social_media_handle_linkedIn':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your LinkedIn ID'}),
            'social_media_handle_X':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your X ID'}),
            'hearAbout':forms.CheckboxSelectMultiple(),
            'form_opened_at' : forms.DateTimeField(),
            'aim':forms.CheckboxSelectMultiple(),

        } 
