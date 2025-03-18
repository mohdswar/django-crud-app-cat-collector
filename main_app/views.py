from django.shortcuts import render,redirect
# Add the following import
from django.views.generic.edit import CreateView
from .models import Cat
from django.http import HttpResponse
from .forms import FeedingForm


# Define the home view function
def home(request):
   return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


from django.shortcuts import render
from .models import Cat

def cat_index(request):
    cats = Cat.objects.all()  # look familiar?
    return render(request, 'cats/index.html', {'cats': cats})

# views.py

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        # include the cat and feeding_form in the context
        'cat': cat, 'feeding_form': feeding_form
    })

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # Remove success_url so Django uses get_absolute_url from Cat

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)