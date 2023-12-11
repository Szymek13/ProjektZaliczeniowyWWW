from rest_framework import serializers
from .models import Producent, Gatunek, Wytwornia, Album, Festiwal, RODZAJ
from datetime import date
from django.contrib.auth.models import User

class ProducentSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    pseudonim = serializers.CharField(required=True)
    gatunek = serializers.PrimaryKeyRelatedField(queryset=Gatunek.objects.all())
    pochodzenie = serializers.CharField(required=True)
    #wytwornia = serializers.PrimaryKeyRelatedField(queryset=Wytwornia.objects.all())

    def create(self, validated_data):
        return Producent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.pseudonim = validated_data.get('pseudonim', instance.pseudonim)
        instance.gatunek = validated_data.get('gatunek', instance.gatunek)
        instance.pochodzenie = validated_data.get('pochodznie', instance.pochodzenie)
        instance.wytwornia = validated_data.get('wytwornia', instance.wytwornia)
        instance.save()
        return instance

    class Meta:
        ordering = ["pseudonim"]
        model = Producent
        fields = '__all__'

class GatunekSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    gatunek = serializers.CharField(required=True)

    def create(self, validated_data):
        return Gatunek.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.gatunek = validated_data.get('gatunek', instance.gatunek)
        instance.save()
        return instance

    class Meta:
        model = Gatunek
        fields = '__all__'

class WytworniaSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    gatunek = serializers.PrimaryKeyRelatedField(queryset=Gatunek.objects.all())
    zalozyciel = serializers.CharField(required=True)
    siedziba = serializers.CharField(required=True)

    def create(self, validated_data):
        return Wytwornia.objects.all(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.gatunek = validated_data.get('gatunek', instance.gatunek)
        instance.zalozyciel = validated_data.get('zalozyciel', instance.zalozyciel)
        instance.siedziba = validated_data.get('siedziba', instance.siedziba)
        instance.save()
        return instance

    class Meta:
        ordering = ["nazwa"]
        model = Wytwornia
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):

    def validate_ilosc_utworow(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Album nie może zawierać ujemnej ilości utworów!"
            )

    id = serializers.IntegerField(read_only=True)
    autor = serializers.PrimaryKeyRelatedField(queryset=Producent.objects.all())
    rodzaj = serializers.ChoiceField(choices=RODZAJ, default=RODZAJ[0][0])
    nazwa = serializers.CharField(required=True)
    gatunek = serializers.PrimaryKeyRelatedField(queryset=Gatunek.objects.all())
    data_premiery = serializers.DateField(required=True)
    ilosc_utworow = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Album.objects.all(**validated_data)

    def update(self, instance, validated_data):
        instance.autor = validated_data.get('autor', instance.autor)
        instance.rodzaj = validated_data.get('rodzaj', instance.rodzaj)
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.gatunek = validated_data.get('gatunek', instance.gatunek)
        instance.data_premiery = validated_data.get('data_premiery', instance.data_premiery)
        instance.ilosc_utworow = validated_data.get('ilosc_utworow', instance.ilosc_utworow)
        instance.save()
        return instance

    class Meta:
        ordering = ["nazwa"]
        model = Album
        fields = '__all__'

class FestiwalSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    gospodarz = serializers.PrimaryKeyRelatedField(queryset=Producent.objects.all())
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Festiwal.objects.all(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.gospodarz = validated_data.get('gospodarz', instance.gospodarz)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance

    class Meta:
        ordering = ["nazwa"]
        model = Festiwal
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
