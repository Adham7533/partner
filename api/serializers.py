from rest_framework import serializers
from taxi.models import Taxis


class TaxisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Taxis

        fields = [
            'id',
            'first_name',
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
            'created_ad',
            'update_ad',
        ]

