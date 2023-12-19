from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
# Create your views here.
def show_data(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():          
            fn=fm.cleaned_data['firstname']
            ln=fm.cleaned_data['lastname']
            dt=fm.cleaned_data['date']
            em=fm.cleaned_data['email']
            mb=fm.cleaned_data['mobile']
            gn=fm.cleaned_data['gender']
            add=fm.cleaned_data['address']
            ct=fm.cleaned_data['city']
            pin=fm.cleaned_data['pincode']
            st=fm.cleaned_data['state']
            con=fm.cleaned_data['country']
            reg=Student(firstname=fn,lastname=ln,date=dt,email=em,mobile=mb,gender=gn,address=add,city=ct,pincode=pin,state=st,country=con)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
        
    return render(request, 'student/student.html', {'form':fm})
