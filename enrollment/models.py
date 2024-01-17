from django.db import models

class CheckboxOption(models.Model):
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text

class program_CheckboxOption(models.Model):
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text
    
class hearAbout_CheckboxOption(models.Model):
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text


class aim_CheckboxOption(models.Model):
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text
# Create your models here.
class Applicant(models.Model):
    GENDER_CHOICES = [
       
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]

    qualification_choices = [
        ('Secondary School', 'Secondary School'),
        ('Undergraduate', 'Undergraduate'),
        ('Graduate','Graduate'),
    ]

    

    program_choices = [
        ("GIS Technology", "GIS Technology (Virtual Learning) – 2 months"),
        ("Drone Technology", "Drone Technology (Hybrid – partly virtual and partly physical) – 1 month"),
        ("3D Design/Printing", "3D Design/Printing (Hybrid – partly virtual and partly physical) – 1 month"),
       # ("Final Project & Exhibition", "Final Project & Exhibition – 1 week (Requires physical presence) – 1 week"),
    ]

    computerLiteracy_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced User','Advanced User'),
    ]

    aim_choices = [
        ('Skills acquisition', 'Skills acquisition'),
        ('Self-development', 'Self-development'),
        ('Employment','Employment'),
    ]
    
    packages_choices = [
        ('MS-Word','MS-Word'),
        ('MS-Excel','MS-Excel'),
        ('MS-PowerPoint','MS-PowerPoint'),
        ('Graphics and Design e.g AutoCAD, Photoshop','Graphics and Design e.g AutoCAD, Photoshop'),
        ('Programming, Statistical and Data Analyses','Programming, Statistical and Data Analyses'),
    ]

    hearAbout_choices = [
        ('Twitter','Twitter'),
        ('Email Advert','Email Advert'),
        ('Facebook','Facebook'),
         ('Radio','Radio'),
        ('Newspaper','Newspaper'),
        ('Our Website','Our Website'),
        ('Google','Google'),
        ('LinkedIn','LinkedIn'),
        ('Instagram','Instagram'),
         ('TV','TV'),
        ('WhatsApp','WhatsApp'),
        ('Others','Others'),
    ]

    # options=CheckboxOption.objects.all()

    name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    qualification = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    lga = models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=50, blank=True, null=True)
    govtID = models.CharField(max_length=50, blank=True, null=True)
    employment = models.BooleanField( blank=True, null=True)
    occupation = models.CharField(max_length=20, blank=True, null=True)
    bankAccount = models.BooleanField( blank=True, null=True)
    noBankReason = models.CharField(max_length=255, blank=True, null=True)
    disability = models.BooleanField(blank=True, null=True)
    disabilityType = models.CharField(max_length=255, blank=True, null=True)
    computerLiteracy = models.CharField(max_length=50, blank=True, null=True)
    packages = models.ManyToManyField(CheckboxOption)
    familiar = models.BooleanField( blank=True, null=True)
    hasComputer = models.BooleanField(blank=True, null=True)
    availability = models.BooleanField( blank=True, null=True)
    majorProgram = models.CharField(max_length=50, blank=True, null=True)
    majorProgramInterest = models.CharField(max_length=50, blank=True, null=True)
    optionalProgram= models.CharField(max_length=50, blank=True, null=True)
    optionalProgramInterest = models.CharField(max_length=50, blank=True, null=True)
    social_media_handle_facebook = models.CharField(max_length=255, blank=True, null=True)
    social_media_handle_linkedIn = models.CharField(max_length=255, blank=True, null=True)
    social_media_handle_X = models.CharField(max_length=255, blank=True, null=True)
    hearAbout = models.ManyToManyField(hearAbout_CheckboxOption)
    aim = models.ManyToManyField(aim_CheckboxOption)
    hearAboutother = models.CharField(max_length=50, blank=True, null=True)
    form_opened_at = models.DateTimeField(null=True, blank=True)
    form_submitted_at = models.DateTimeField(null=True, blank=True)
    # ####approval = models.BooleanField()

    @property
    def total_minutes(self):
        if self.form_opened_at and self.form_submitted_at:
            time_difference = self.form_submitted_at - self.form_opened_at
            return time_difference.total_seconds() / 60
        return None

