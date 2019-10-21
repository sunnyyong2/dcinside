from IPython import embed
from django.shortcuts import render, redirect
from .models import Feed

# Create your views here.
def index(request):
    feeds = Feed.objects.all()
    context = {
        'feeds' : feeds
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        image = request.FILES.get('image')

        feed = Feed.objects.create(content=content, image=image)
        # embed()

        return redirect('feeds:index')
    else:
        return render(request, 'form.html')