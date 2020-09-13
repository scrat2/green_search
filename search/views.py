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
        form = SearchForm(request.POST, request.FILES)

        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            speciality = form.cleaned_data['speciality']
            address = form.cleaned_data['address']
            postalcode = form.cleaned_data['postalCode']
            city = form.cleaned_data['city']
            picture = form.cleaned_data['picture']
            Student.objects.create(
                lastname=lastname,
                firstname=firstname,
                speciality=speciality,
                address=address,
                postal_code=postalcode,
                city=city,
                photo=picture,
            )
    return render(request, 'add.html', context)


def search(request):
    form = SearchForm
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)

        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            speciality = form.cleaned_data['speciality']
            address = form.cleaned_data['address']
            postalcode = form.cleaned_data['postalCode']
            city = form.cleaned_data['city']

            results = None

            if firstname != "":
                results = Student.objects.filter(firstname=firstname)

            if lastname != "":
                if results is not None:
                    results = results.filter(lastname=lastname)
                else:
                    results = Student.objects.filter(lastname=lastname)

            if speciality != "":
                if results is not None:
                    results = results.filter(speciality=speciality)
                else:
                    results = Student.objects.filter(speciality=speciality)

            if address != "":
                if results is not None:
                    results = results.filter(address=address)
                else:
                    results = Student.objects.filter(address=address)

            if postalcode != "":
                if results is not None:
                    results = results.filter(postal_code=postalcode)
                else:
                    results = Student.objects.filter(postal_code=postalcode)

            if city != "":
                if results is not None:
                    results = results.filter(city=city)
                else:
                    results = Student.objects.filter(city=city)

            context['student_list'] = results
            for student in results:
                print(student.firstname + " " + student.lastname)
            print(results)

    return render(request, 'TP3.html', context)


def details(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student
    }
    return render(request, 'details.html', context)
