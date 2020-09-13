from django.shortcuts import render
from .forms import SearchForm
from .models import Student
# Create your views here.


def add(request):
    form = SearchForm
    context = {
        'form': form
    }
    if request.method == 'POST':
        print("post requete")
        form = SearchForm(request.POST, request.FILES)

        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            speciality = form.cleaned_data['speciality']
            address = form.cleaned_data['address']
            postalcode = form.cleaned_data['postalCode']
            city = form.cleaned_data['city']
            picture = form.cleaned_data['picture']
            print("les resultats du formulaire " + firstname + " "
                  + lastname + " " + speciality + " " + address + " " + postalcode + " " + city)
            Student.objects.create(
                lastname=lastname,
                firstname=firstname,
                speciality=speciality,
                address=address,
                postal_code=postalcode,
                city=city,
                photo=picture,
            )
        """if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            speciality = form.cleaned_data['speciality']
            address = form.cleaned_data['address']
            postalcode = form.cleaned_data['postalCode']
            city = form.cleaned_data['city']
            picture = form.cleaned_data['picture']
            print("les resultats du formulaire "+firstname+" "+lastname+" "+speciality+" "+address+" "+postalcode+" "+city)
            student = Student.objects.create(
                lastname=lastname,
                firstname=firstname,
                speciality=speciality,
                address=address,
                postal_code=postalcode,
                city=city,
                photo=picture,
            )
            student.save()"""

    return render(request, 'add.html', context)


def search(request):
    return render(request, 'TP3.html')
