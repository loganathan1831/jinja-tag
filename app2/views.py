from django.shortcuts import render

# Create your views here.
def second(request):
    d={'name' : 'logan'}
    return render(request,'second.html',context=d)