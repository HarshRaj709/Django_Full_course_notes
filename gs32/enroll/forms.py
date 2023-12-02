from django import forms

class userforms(forms.Form):
    name = forms.CharField(max_length=10,min_length=5,error_messages={'required':'Enter your name Please.//custom error message','max_length':'chota dalo na','min_length':'bhai bda dalo'},strip=True,empty_value='harshsahu',initial='harshrathore')
    agree = forms.BooleanField(label = 'I Agree',label_suffix='',error_messages={'required':'why you not agree?'})
    rolls = forms.IntegerField(max_value=10,min_value=2,error_messages={'max_value':'chota likho dada 10 se','min_value':'2 se bda only'})
    price = forms.DecimalField(min_value=2,max_value=10,max_digits=5,error_messages={'max_value':'10 se chota janab','min_value':'2 se bda','max_digits':'5 se km rhega max numbers'})
    rate = forms.FloatField(min_value=2,max_value=10,)
    comment = forms.SlugField()
    email = forms.EmailField(max_length=25,min_length=10)
    website = forms.URLField(min_length=10,max_length=25)
    pasword = forms.CharField(max_length=50,min_length=20,widget=forms.PasswordInput)
    description = forms.CharField(widget=forms.Textarea,initial='this is done by using "widget=forms.Textarea"')
    feedback = forms.CharField(min_length=5,max_length=50,widget=forms.TextInput(attrs={'class':'somecss1 somecss2','id':'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':10,'col':50})) #ye rows aur column ke through apni height aur width le rha h
    