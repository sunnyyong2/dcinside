from django.shortcuts import render
from .forms import MovieForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        pass
    else:
        form = MovieForm()
        context ={
            'form':form
        }
        return render(request, 'form.html',context)
    
