# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from forms import ExchangeForm

def index(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            return HttpResponse('thanks')
    else:
        form = ExchangeForm()
        return render(request, 'base_index.html' , {'form': form})