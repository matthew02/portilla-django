from django.shortcuts import render
from django.http import HttpResponse


from first_app.models import AccessRecord, Topic, Webpage
#from . import forms
from .forms import FormName


def index(request):
    webpages = AccessRecord.objects.order_by('date')
    dates = {'access_records': webpages}
    return render(request, 'first_app/index.html', context=dates)

def form_view(request):
    form = {'form': FormName()}
    return render(request, 'first_app/form.html', context=form)
