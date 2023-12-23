from django.shortcuts import redirect, render
from .forms import AddPostForm
from .models import Country


def japan(request):
    return render(request, 'main/japan.html')

def china(request):
    return render(request, 'main/china.html')

def south_korea(request):
    return render(request, 'main/south_korea.html')

def main(request):
    return render(request, 'main/main.html')

def models(request):
    countries = Country.objects.all()
    return render(request, 'main/models.html', {'countries': countries})

def add(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                Country.objects.create(**form.cleaned_data)
                return redirect('main.html')
            except Exception as e:
                form.add_error(None, f'Помилка додавання країни: {e}')

    else:
        form = AddPostForm()

    return render(request, 'main/add_country.html', {'form' : form})

