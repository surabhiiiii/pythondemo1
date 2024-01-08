from django.shortcuts import render
from django.http import HttpResponse
from . models import taski
from django.shortcuts import redirect
from . forms import todoform
# Create your views here.
    
def index(request):
    tas=taski.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=taski(name=name,priority=priority,date=date)
        task.save()
        # (mandel koduthkna objectsall um ee variable same koduknda athan munb tas object not ietrable ann vana)
    return render(request,'index.html',{'result':tas})
# def details(request):
    # return render(request,'details.html',{'result':tas})
def delete(request,taskid):
    task=taski.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{})
def update(request,id):
    task=taski.objects.get(id=id)
    f=todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})