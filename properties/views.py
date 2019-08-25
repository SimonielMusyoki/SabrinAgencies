from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Properties
from properties.forms import PropertiesForm
from django.shortcuts import render

#  CRUD of Properties

class PropertiesListView(ListView):
    model = Properties
    template_name='properties/properties.html'
    context_object_name = 'posts'
    paginate_by = 15

class PropertiesDetailView(DetailView):
    model=Properties
    template_name='properties/property_detail.html'
    context_object_name = "posts"
    

class PropertiesCreateView(CreateView):
    model=Properties
    template_name='properties/property_create.html'
    fields = '__all__'
    def form_valid(self, form):
        return super().form_valid(form)

class PropertiesUpdateView(UpdateView):
    model = Properties
    template_name='properties/property_create.html'
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class PropertiesDeleteView(DeleteView):
    model = Properties
    success_url ='/'
    template_name='properties/property_delete.html'

def propertiesCreateView(request):
    form = PropertiesForm(request.POST)
    if form.is_valid():
        message = "message send successfully. Please wait for response on your email"
        form.save()
        return redirect('home')

    return render(request,'properties/property_create.html', {'form':form,'title': 'Contact'})