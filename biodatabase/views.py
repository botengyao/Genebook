from django.shortcuts import render
from .models import GeneDbLink
from .models import GenecardDescriptionSummary
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def genebook(request):
    gene_db = GeneDbLink.objects
    info = GeneDbLink.objects.get(name="TBC1D29")
    summary = GenecardDescriptionSummary.get()
    return render(request, 'biodatabase/templates/genebooks.html',{'gene_dbs':gene_db,'info':info})


def ajax_list(request):
    a = [1,2,3,4,5,6,7,8,9,10]
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))