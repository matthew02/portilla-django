from django.shortcuts import render

from first_app.models import AccessRecord
from first_app.forms import FormName


def index(request):
    webpages = AccessRecord.objects.order_by('date')
    context = {'access_records': webpages}
    return render(request, 'first_app/index.html', context=context)

def form_view(request):
    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print('Validation success.')
            print(f'NAME: {form.cleaned_data["name"]}')
            print(f'EMAIL: {form.cleaned_data["email"]}')
            print(f'TEXT: {form.cleaned_data["text"]}')
    else:
        form = FormName()

    context = {'form': form}
    return render(request, 'first_app/form.html', context=context)
