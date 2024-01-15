# enrollment/management/commands/seed_program_checkboxoption.py

from django.core.management.base import BaseCommand
from enrollment.models import program_CheckboxOption, aim_CheckboxOption, CheckboxOption, hearAbout_CheckboxOption

class Command(BaseCommand):
    help = 'Seeds the database with program_CheckboxOption records'

    def handle(self, *args, **options):
        program_options = [
            
            'Drone Technology (Hybrid – virtual and in-person) – 3 months',
            'GIS Technology (Virtual Learning) – 2 months',
            '3D Design/Printing (Hybrid – virtual and in-personl) – 1 month',
            # Add more options here
        ]

        for option in program_options:
            program_CheckboxOption.objects.get_or_create(option_text=option)

        aims_options = [
            
            'Skills acquisition',
            'Self-development',
            'Employment',
            # Add more options here
        ]

        for aim in aims_options:
            aim_CheckboxOption.objects.get_or_create(option_text=aim)

        
        packages_options = [
            
            'MS-Word',
            'MS-Excel',
            'MS-PowerPoint',
            'Graphics and Design e.g., AutoCAD, Photoshop',
            'Programming, Statistical and Data Analyses'
            # Add more options here
        ]

        for package in packages_options:
            CheckboxOption.objects.get_or_create(option_text=package)

        hear_options = [
            
            'Twitter',
            'Google',
            'Facebook',
            'LinkedIn',
            'Instagram',
            'WhatsApp',
            'Email Advert',
            'Radio',
            'Newspaper',
            'Tv',
            'Our Website',
            'Others',
            # Add more options here
        ]

        for hear in hear_options:
            hearAbout_CheckboxOption.objects.get_or_create(option_text=hear)

        self.stdout.write(self.style.SUCCESS('Successfully seeded program_CheckboxOption records'))
