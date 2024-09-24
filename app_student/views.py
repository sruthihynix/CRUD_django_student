from django.shortcuts import render,redirect

from .models import Student
# Create your views here.
def index(request):
    data = Student.objects.all()  # getting all the  datas from db to 'data'
    context = {"data": data}  # passing all the data into context in the form of dictionary
    # print(context)
    return render(request,'index.html',context)

def insertData(request):
    data = Student.objects.all()  # getting all the  datas from db to 'data'
    context = {"data": data}  # passing all the data into context in the form of dictionary
    # print(context)
# inserting data to db- Student
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        # print(name)
        query=Student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/") # redirect to homepage, ie indexpage
    return render(request, 'index.html', context)

def updateData(request,id):
# inserting data to db Student
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        return redirect("/")

# display the data from the database base don seleated id
    data= Student.objects.get(id=id)  # getting all the  datas from db to 'd'
    # print(d)
    context = {"d": data}  # passing all the data into context in the form of dictionary
    # print(context)
    return render(request,'edit.html',context)

def deleteData(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return  redirect("/")


