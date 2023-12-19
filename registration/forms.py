from django import forms

# class GenderForm(forms.Form):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )

#     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)


class StudentRegistration(forms.Form):
    firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'first-name','pattern':'[A-Za-z]+','title':'Enter the First name'}))
    lastname=forms.CharField(required=True,widget=forms.TextInput(attrs={'pattern':'[A-Za-z]+','title':'Enter the First name'}))
    date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email=forms.EmailField(min_length=5,max_length=30)
    mobile=forms.IntegerField(min_value=10)
    CHOICES=[('M','Male'),('F','Female')]
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # gender=forms.CharField(label='Gender',widget=forms.RadioSelect(choice=CHOICE))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    address=forms.CharField(min_length=5,max_length=50,widget=forms.Textarea(attrs={'rows':3,'cols':50}))
    city=forms.CharField(min_length=4,max_length=20)
    pincode=forms.IntegerField()
    state=forms.CharField(min_length=5,max_length=20)
    country=forms.CharField(min_length=5,max_length=30)

    
    
    
    