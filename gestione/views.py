from django.http import Http404
from django.shortcuts import render, redirect

# authentification
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm, AddMemberForm, AddDepartmentForm, AddCityForm, AddDistrictForm

# Models import
from .models import Member, Department, City, District

# Create your views here.

def dashboard(request):
    return render(request, 'gestione/index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authentification
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login con successo !')
            return redirect('gestione:dashboard')
        else:
            messages.error(request, 'Username o password errati !')
            return redirect('gestione:login')
    else:
        return render(request, 'gestione/pages/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logout con successo !')
    return redirect('gestione:login')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authentification et conexion
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registrazione con successo !')
            return redirect('gestione:login')
    else:
        form = SignUpForm()
        return render(request, 'gestione/pages/register.html', {'form': form})

    return render(request, 'gestione/pages/register.html', {'form': form})

# Gestion des membres
def list_members(request):
    members = Member.objects.all()
    return render(request, 'gestione/pages/members.html', {'members': members})


def add_member(request):
    form = AddMemberForm(request.POST or None)
    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')
    if request.method == 'POST':
        if form.is_valid():
            member = form.save(commit=False)  # Crée le membre sans sauvegarder
            member.save()  # Sauvegarde le membre
            messages.success(request, 'Member Added!')
            return redirect('gestione:members')
    return render(request, 'gestione/pages/add_member.html', {'form': form})


def member_record(request, pk):
    if request.user.is_authenticated:
        member = Member.objects.get(pk=pk)
        return render(request, 'gestione/pages/member_details.html', {'member': member})
    else:
        messages.success(request, "You are not logged in")
        return redirect('gestione:login')


def delete_member(request, pk):
    if request.user.is_authenticated:
        delete_it = Member.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Membre cancallato con successo !')
        return redirect('gestione:members')
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')


def update_member(request, pk):
    if request.user.is_authenticated:
        current_member = Member.objects.get(id=pk)
        form = AddMemberForm(request.POST or None, instance=current_member)
        if form.is_valid():
            form.save()
            messages.error(request, "Member has been updated !")
            return redirect('gestione:members')
        return render(request, 'gestione/pages/update_member.html', {'form': form, 'current_member': current_member})
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')


# Gestion des departement
def list_departments(request):
    departments = Department.objects.all()
    return render(request, 'gestione/pages/departements.html', {'departments': departments})


def department_record(request, pk):
    if request.user.is_authenticated:
        try:
            department = Department.objects.get(id=pk)
        except Department.DoesNotExist:
            raise Http404("Department does not exist")

        cities = department.cities.all()
        return render(request, 'gestione/pages/department_details.html', {'department': department, 'cities': cities})
    else:
        messages.success(request, "You are not logged in")
        return redirect('gestione:login')


def add_department(request):
    form = AddDepartmentForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                department = form.save(commit=False)  # Crée le membre sans sauvegarder
                department.save()  # Sauvegarde le membre
                messages.success(request, 'Department Added!')
                return redirect('gestione:departments')
        return render(request, 'gestione/pages/add_department.html', {'form': form})
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')



def update_department(request, pk):
    if request.user.is_authenticated:
        current_department = Department.objects.get(id=pk)
        form = AddDepartmentForm(request.POST or None, instance=current_department)
        if form.is_valid():
            form.save()
            messages.error(request, "Department has been updated !")
            return redirect('gestione:departments')
        return render(request, 'gestione/pages/update_department.html', {'form': form, 'current_department': current_department})
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')



def delete_department(request, pk):
    if request.user.is_authenticated:
        delete_it = Department.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Department cancallato con successo !')
        return redirect('gestione:departments')
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')



# Gestion des villes
def list_cities(request):
    cities = City.objects.prefetch_related('districts').all()
    return render(request, 'gestione/pages/cities.html', {'cities': cities})


def city_record(request, pk):
    if request.user.is_authenticated:
        try:
            city = City.objects.get(id=pk)
        except City.DoesNotExist:
            raise Http404("City does not exist")

        districts = city.districts.all()
        return render(request, 'gestione/pages/city_details.html', {'city': city, 'districts': districts})
    else:
        messages.success(request, "You are not logged in")
        return redirect('gestione:login')



def add_city(request):
    form = AddCityForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                city = form.save(commit=False)  # Crée le membre sans sauvegarder
                city.save()  # Sauvegarde le membre
                messages.success(request, 'City Added!')
                return redirect('gestione:cities')
        return render(request, 'gestione/pages/add_city.html', {'form': form})
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')


def update_city(request, pk):
    if request.user.is_authenticated:
        current_city = City.objects.get(id=pk)
        form = AddCityForm(request.POST or None, instance=current_city)
        if form.is_valid():
            form.save()
            messages.error(request, "City has been updated !")
            return redirect('gestione:cities')
        return render(request, 'gestione/pages/update_city.html', {'form': form, 'current_city': current_city})
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')



def delete_city(request, pk):
    if request.user.is_authenticated:
        delete_it = City.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'City cancallato con successo !')
        return redirect('gestione:cities')
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')


# Gestion des quartier
def list_districts(request):
    districts = District.objects.all()
    return render(request, 'gestione/pages/districts.html', {'districts': districts})


def district_record(request, pk):
    if request.user.is_authenticated:
        try:
            district = District.objects.get(id=pk)
        except District.DoesNotExist:
            raise Http404("District does not exist")

        members = district.members.all()
        return render(request, 'gestione/pages/district_details.html', {'district': district, 'members': members})
    else:
        messages.success(request, "You are not logged in")
        return redirect('gestione:login')


def add_district(request):
    form = AddDistrictForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                district = form.save(commit=False)  # Crée le membre sans sauvegarder
                district.save()  # Sauvegarde le membre
                messages.success(request, 'District Added!')
                return redirect('gestione:districts')
        return render(request, 'gestione/pages/add_district.html', {'form': form})
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')



def update_district(request, pk):
    if request.user.is_authenticated:
        current_district = District.objects.get(id=pk)
        form = AddDistrictForm(request.POST or None, instance=current_district)
        if form.is_valid():
            form.save()
            messages.error(request, "District has been updated !")
            return redirect('gestione:cities')
        return render(request, 'gestione/pages/update_district.html', {'form': form, 'current_district': current_district})
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')



def delete_district(request, pk):
    if request.user.is_authenticated:
        delete_it = District.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'District cancallato con successo !')
        return redirect('gestione:districts')
    else:
        messages.error(request, "You are not logged in")
        return redirect('gestione:login')

def member_record_by_district(request, pk):
    if request.user.is_authenticated:
        member = Member.objects.get(pk=pk)
        district_id = member.district_id
        return render(request, 'gestione/pages/member_details_by_district.html', {'member': member, 'district_id': district_id})
    else:
        messages.success(request, "You are not logged in")
        return redirect('gestione:login')

def settings(request):
    return render(request, 'gestione/pages/settings.html')


def handler404(request, exception):
    return render(request, 'gestione/errors/404.html', {'error': exception},  status=404)

def handler500(request, exception):
    return render(request, 'gestione/errors/500.html', {'error': exception},  status=500)