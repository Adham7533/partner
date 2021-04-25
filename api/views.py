from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from .form import EditEmployee, AddEmployee
from taxi.models import Taxis
from .serializers import TaxisSerializers


class TaxisAPIView(generics.ListAPIView):
    queryset = Taxis.objects.all()
    serializer_class = TaxisSerializers

    filter_backends = [SearchFilter]
    search_fields = ['id', 'first_name', 'last_name', 'family_name', 'phone']


def edit_employee(request, staff_name, employee_name):
    if not request.User.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        employee = get_object_or_404(Taxis, Name=employee_name)
        context = {'first_name': employee.first_name, 'last_name': employee.last_name,
                   'family_name': employee.family_name,
                   'phone': employee.phone, 'address': employee.address, 'profile_pic': employee.profile_pic,
                   'status': employee.status,
                   'auto_model': employee.auto_model, 'auto_marka': employee.auto_marka,
                   'autogrovnum': employee.autogrovnum,
                   'time': employee.time, 'auto_license': employee.auto_license, 'fule': employee.fule,
                   'color': employee.color,
                   'year': employee.year, 'driver_lic': employee.driver_lic, 'passport': employee.passport,
                   'oven': employee.oven
                   }
        form = EditEmployee(request.POST or None, request.FILES or None, initial=context)
        if form.is_valid():
            employee.first_name = form.cleaned_data.get('first_name')
            employee.last_name = form.cleaned_data.get('last_name')
            employee.family_name = form.cleaned_data.get('family_name')
            employee.phone = form.cleaned_data.get('phone')
            employee.address = form.cleaned_data.get('address')
            employee.status = form.cleaned_data.get('status')
            employee.auto_model = form.cleaned_data.get('auto_madel')
            employee.auto_marka = form.cleaned_data.get('auto_marka')
            employee.autogrovnum = form.cleaned_data.get('autogrovnum')
            employee.time = form.cleaned_data.get('time')
            employee.fule = form.cleaned_data.get('fule')
            employee.color = form.cleaned_data.get('color')
            employee.year = form.cleaned_data.get('year')
            employee.oven = form.cleaned_data.get('oven')
            # employee.created_ad=form.cleaned_data.get('created_ad')
            # employee.update_ad=form.cleaned_data.get('update_ad')
            if request.FILES:
                employee.profile_pic = request.FILES['image']
                employee.auto_license = request.FILES['image']
                employee.driver_lic = request.FILES['image']
                employee.passport = request.FILES['image']
            employee.save()
            return redirect('Staff_list', staff_name)
    return render(request, 'Staff/edit_employee.html', {'form': form, 'employee': employee})


def delete_employee(request, staff_name, employee_name):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        employee = get_object_or_404(Taxis, Name=employee_name)
        if request.method == 'POST':
            if 'delete' in request.POST:
                employee.delete()
                return redirect('Staff_list', staff_name)
            elif 'cancel' in request.POST:
                return redirect('Staff_list', staff_name)
    return render(request, 'Staff/delete_staff.html', {'employee_name': employee_name})


def add_employee(request, staff_name):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        form = AddEmployee(request.POST or None, request.FILES or None)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.Staff_name = get_object_or_404(Staff, Name=staff_name)
            if request.FILES:
                employee.profile_pic = request.FILES['profile_pic']
            employee.save()
            return redirect('Staff_list', staff_name)
        return render(request, 'Staff/add_employee.html', {'form': form})
