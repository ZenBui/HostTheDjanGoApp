from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import blogRegForm
from .models import blogForm
from django.views.generic import TemplateView
from .views import blogRegForm
# Create your views here.

def home(request):
    return render(request, 'Website/home.html')

def tintuc(request):
    return render(request, 'Website/tin-tuc.html')

class HomeView(TemplateView):
    template_name = 'Website/home.html'

    def post(self, request):
        form = blogRegForm(request.POST)

        if form.is_valid():
            form.save()
            text = form.cleaned_data['email']
            form = blogRegForm()
            return redirect('Website:home')

        args = {'form': form, 'text' : text}
        return render(request, self.template_name, args)