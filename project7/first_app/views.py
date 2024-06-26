from django.shortcuts import render
from first_app.forms import StudentModel

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentModel(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentModel()
    return render(request, 'home.html', {'form':form})