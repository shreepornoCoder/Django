from django.shortcuts import render

# Create your views here.
def index(request):


    return render(request, 'home.html')

def about(request, id):
    return render(request, 'home.html', {'id': id})

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")

        return render(request, 'form.html', {'name': name, 'email':email})
    
    else:
        return render(request, 'form.html')