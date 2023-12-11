from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

@api_view(['GET'])
def producent_list(request):
    if request.method == 'GET':
        producenci = Producent.objects.all()
        serializer = ProducentSerializer(producenci, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def producent_detail(request, pk):
    try:
        producent = Producent.objects.get(pk=pk)
    except Producent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        producent = Producent.objects.get(pk=pk)
        serializer = ProducentSerializer(producent)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProducentSerializer(producent, dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def gatunek_list(request):
    if request.method == 'GET':
        gatunki = Gatunek.objects.all()
        serializer = GatunekSerializer(gatunki, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def gatunek_detail(request, pk):
    try:
        gatunek = Gatunek.objects.get(pk=pk)
    except Gatunek.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        gatunek = Gatunek.objects.get(pk=pk)
        serializer = GatunekSerializer(gatunek)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GatunekSerializer(gatunek, dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        gatunek.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def wytwornia_list(request):
    if request.method == 'GET':
        wytwornie = Wytwornia.objects.all()
        serializer = WytworniaSerializer(wytwornie, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def wytwornia_detail(request, pk):
    try:
        wytwornia = Wytwornia.objects.get(pk=pk)
    except Wytwornia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        wytwornia = Wytwornia.objects.get(pk=pk)
        serializer = WytworniaSerializer(wytwornia)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WytworniaSerializer(wytwornia, dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        wytwornia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def album_list(request):
    if request.method == 'GET':
        albumy = Album.objects.all()
        serializer = AlbumSerializer(albumy, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, pk):
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        album = Album.objects.get(pk=pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlbumSerializer(album, dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def festiwal_list(request):
    if request.method == 'GET':
        festiwale = Festiwal.objects.all()
        serializer = FestiwalSerializer(festiwale, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def festiwal_detail(request, pk):
    try:
        festiwal = Festiwal.objects.get(pk=pk)
    except Festiwal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        festiwal = Festiwal.objects.get(pk=pk)
        serializer = FestiwalSerializer(festiwal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlbumSerializer(festiwal, dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        festiwal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def producent_update_delete(request, pk):
    try:
        producent = Producent.objects.get(pk=pk)
    except Producent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProducentSerializer(producent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def gatunek_update_delete(request, pk):
    try:
        gatunek = Gatunek.objects.get(pk=pk)
    except Gatunek.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = GatunekSerializer(gatunek, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gatunek.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def wytwornia_update_delete(request, pk):
    try:
        wytwornia = Wytwornia.objects.get(pk=pk)
    except Wytwornia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = WytworniaSerializer(wytwornia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wytwornia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def album_update_delete(request, pk):
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def festiwal_update_delete(request, pk):
    try:
        festiwal = Festiwal.objects.get(pk=pk)
    except Festiwal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = FestiwalSerializer(festiwal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        festiwal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#widok, który wyświetla wszystkie albumy danego producenta
@api_view(['GET'])
def albumy_po_autorze(request, author_id):
    if request.method == 'GET':
        author = get_object_or_404(Producent, pk=author_id)
        albumy = Album.objects.filter(autor=author)
        serializer = AlbumSerializer(albumy, many=True)
        return Response(serializer.data)

#widok, który wyświetla wszystkie albumy danego gatunku
@api_view(['GET'])
def albumy_po_gatunku(request, genre_id):
    if request.method == 'GET':
        genre = get_object_or_404(Gatunek, pk=genre_id)
        albumy = Album.objects.filter(gatunek=genre)
        serializer = AlbumSerializer(albumy, many=True)
        return Response(serializer.data)

class UserRegistrationView(generics.GenericAPIView, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        request.data["password"] = make_password(request.data["password"])
        return self.create(request, *args, **kwargs)

