from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util



def index(request):
    if request.method == 'POST':
        search = request.POST
        return render(request, 'encyclopedia/search')

    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def entries(request, title):
        return render(request, "encyclopedia/entries.html", {
        "content": util.get_entry(title)
    }) 

def search(request):
    q = request.GET.get('q').strip()
    return render(request, "encyclopedia/entries/q") 
    
      