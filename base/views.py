from django.shortcuts import render

# Create your views here.

taskData = [
    {'id':1,'title':'qwertyuiopp','description':'ertyuiopfghjkltryui'},
    {'id':2,'title':'sdfghjkl','description':'asdfghjksdfghjkll'},
    {'id':3,'title':'zxcvbnm,','description':'zxcvbnm,.wertyuio345678'},
]



def index(request):
    return render(request, 'index.html')

def tasks(request):
    context = {
        'tasks':taskData,
    }
    return render(request,'tasks.html',context=context)