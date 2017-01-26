from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from restaurantes.models import Rest
from django import forms
from restaurantes import forms
import os
from .forms import *
from pymongo import MongoClient

client = MongoClient()
if client:
    print "Conectado a la base de datos"

db = client.test
if db:
    print "conexion establecida"

collection = db.restaurants

# Create your views here.
def index(request):
    return render(request,'index.html', {})

@login_required
def test(request):
    return render(request,'test.html', {})

@login_required
def add_rest(request):
    if request.method == 'POST':
        rest_form=RestForm(request.POST)
        nombre = request.POST['nombre']
        cuisine = request.POST['cuisine']
        borough = request.POST['borough']
        street = request.POST['street']
        building = request.POST['building']
        zipcode = request.POST['zipcode']
        
        db.restaurants.insert({"name":nombre,"cuisine":cuisine,"borough":borough, "street":street, "building":building, "zipcode":zipcode})
        
        return render(request,'index.html', {})
        
    return render(request,'insertaRest.html',{'restform':RestForm()})



