# enrollment/forms.py
from django import forms
from .models import Applicant, CheckboxOption  # Add CheckboxOption to your imports

class ApplicantForm(forms.ModelForm):
    
    packages_choices = [
        ('MS-Word','MS-Word'),
        ('MS-Excel','MS-Excel'),
        ('MS-PowerPoint','MS-PowerPoint'),
        ('Graphics and Design e.g AutoCAD, Photoshop','Graphics and Design e.g AutoCAD, Photoshop'),
        ('Programming, Statistical and Data Analyses','Programming, Statistical and Data Analyses'),
    ]

    govtID_choices =[
        ('None', 'None'),
        ("Driver's License", "Driver's License"),
        ('National ID Card', 'National ID Card'),
        ("Voter's Card", "Voter's Card"),
    ]
    # gender = forms.ChoiceField(
    #    choices=GENDER_CHOICES,
    #    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    # )
    class Meta:
        model = Applicant
        # Or list the fields you want to include in your form
        fields = '__all__'
       
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name and surname', 'required':'required'}),
            
            'dob': forms.DateInput(attrs={'class':'form-control', 'placeholder':'dob', 'type': 'date', 'required':'required'}),
            'gender':forms.Select(attrs={'class':'form-control', 'required': 'required'}, choices=[('Female','Female'), ('Male', 'Male')]),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a Valid Email', 'required':'required'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your phone number', 'required':'required', 'type': 'tel'}),
            'qualification':forms.Select(attrs={'class':'form-control', 'required': 'required'}),
            'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State', 'required':'required'}),
            'LGA':forms.TextInput(attrs={'class':'form-control', 'placeholder':'LGA', 'required':'required'}),
            'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'locality'}),
            'govtID':forms.Select(attrs={'class':'form-control', 'required':'required'}),
            'employment':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'occupation':forms.TextInput(attrs={'class':'form-control', 'placeholder':'occupation', 'required':'required'}),
            'bankAccount':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'noBankReason':forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'disability' :forms.RadioSelect(choices=[(False, 'No'),(True, 'Yes')]),
            'disabilityType':forms.Select(attrs={'class':'form-control', 'placeholder':'disabilityType'}, choices=[('', 'Select'),('Hearing', 'Hearing'), ('Visual', 'Visual'), ('Mobility', 'Mobility')]),
            'computerLiteracy':forms.Select(attrs={'class':'form-control', 'required':'required'}),
            'packages' : forms.CheckboxSelectMultiple(),
            'hasComputer':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'familiar':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'availability':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
           
            'majorProgram':forms.HiddenInput(),
            'majorProgramInterest':forms.RadioSelect(),
            'optionalProgram':forms.RadioSelect(choices=[("GIS", "GIS"),("3D Design/Printing", "3D Design/Printing")]),
            'optionalProgramInterest':forms.RadioSelect(),
            'social_media_handle_facebook':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Facebook ID'}),
            'social_media_handle_linkedIn':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your LinkedIn ID'}),
            'social_media_handle_X':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your X ID'}),
            'hearAbout':forms.CheckboxSelectMultiple(),
            'form_opened_at' : forms.DateTimeInput(attrs={'class':'d-none'}),
            'aim':forms.CheckboxSelectMultiple(),
            #'hearAboutother':forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),

        } 
