from django import forms
from .models import Resume

GENDER_CHOICES = (
    ('Male','Male'),
    ('Female','Female'),
)

JOB_CITY = [
    ('Delhi','Delhi'),
    ('Noida','Noida'),
    ('lucknow','Lucknow'),
    ('Mumbai','Mumbai'),
    ('gurugram','Gurugram'),
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label ='Prefered job city',choices=JOB_CITY,widget = forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {'name':'Full name','dob':'Date Of Birth','pin':'Pin Code','mobile':'Mobile No.','profile_image':
                  'Profile Image','my_file':'Document','email':'Email Id'}
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'pin':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }