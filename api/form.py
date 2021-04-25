from django import forms

from taxi.models import Taxis


class EditEmployee(forms.ModelForm):
    class Meta:
        model = Taxis
        fields = ['first_name',
            'last_name',
            'family_name',
            'phone',
            'address',
            'profile_pic',
            'status',
            'auto_model',
            'auto_marka',
            'autogrovnum',
            'time',
            'auto_license',
            'fule',
            'color',
            'year',
            'driver_lic',
            'passport',
            'oven',
            # 'created_ad',
            # 'update_ad',
                   ]


class AddEmployee(forms.ModelForm):
    class Meta:
        model = Taxis
        fields = ['first_name',
            'last_name',
            'family_name',
            'phone',
            'address',
            'profile_pic',
            'status',
            'auto_model',
            'auto_marka',
            'autogrovnum',
            'time',
            'auto_license',
            'fule',
            'color',
            'year',
            'driver_lic',
            'passport',
            'oven',
            # 'created_ad',
            # 'update_ad',
                  ]