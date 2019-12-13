from django.shortcuts import render, HttpResponse
from . import mappingscript

# Create your views here.
def frontpage(request):
    return render(request, 'frontpage/frontpage.html')
    
def mapper(request):
    mapped = mappingscript.map_maker()
    return render(request, 'maps/the_map.html')
