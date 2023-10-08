from django.shortcuts import render,redirect
from .models import Datas
# Create your views here.  
def home(request):
    return render(request,'index.html')   
def addData(request):
    if request.method == 'POST':
        name= request.POST ['name']
        age= request.POST ['age']
        dob= request.POST ['dob']
        email= request.POST ['email']
        phone_no= request.POST ['phone_no']
        print(name,age,email)
        obj=Datas()
        obj.name=name
        obj.age = age
        obj.dob = dob
        obj.email= email
        obj.phone_no = phone_no
        obj.save()
        
        mydata= Datas.objects.all()
        return redirect('/addData')
    return render(request,'home.html')
def detials(request):
        mydata= Datas.objects.all()
        return render (request,'detials.html',{'datas':mydata})

def update (request,id):
    mydata = Datas.objects.get(id=id)
    if request.method=="POST":
        up_name=request.POST['up_name']
        up_age=request.POST['up_age']
        up_dob=request.POST['up_dob']
        up_email=request.POST['up_email']
        up_phone_no=request.POST['up_phone_no']
    
        mydata.name = up_name
        mydata.age = up_age
        mydata.dob = up_dob
        mydata.email = up_email
        mydata.phone_no = up_phone_no
        mydata.save()
        return redirect('/detials')
    return render(request,"update.html",{'data':mydata})
def delete(request,id):
    mydata= Datas.objects.get(id=id)
    mydata.delete()
    return redirect('/detials')
    return render(request,'detials.html')