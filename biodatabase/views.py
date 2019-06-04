from django.shortcuts import render
from .models import GeneDbLink
from django.http import JsonResponse
from django.http import HttpResponse
import json
# Create your views here.
def genebook(request):
    gene_db = GeneDbLink.objects
    info = GeneDbLink.objects.get(omim='611000')
    #info2 = GenecardDescriptionSummary.objects.get(gene__name="KLK13")
    #summary = info.genecarddescriptionsummary_set.all().values('gene__name','type','description','summary_entrez','summary_genecard')
    # filter(子表外键字段__母表字段='过滤条件')
    #summary2 = GenecardDescriptionSummary.objects.filter(gene__name = 'KLK13').values('gene__name','type','description','summary_entrez','summary_genecard')
    #summary_info2 = list(summary2)
    #summary_info = list(info)
    return render(request, 'biodatabase/templates/genebooks.html',\
                  {'gene_dbs':gene_db,'info':info})
def search(request):
    gene_db = GeneDbLink.objects
    try:
        gene_pool = request.GET['genepool']
        search_id = request.GET['gene_id']
        if gene_pool == "Gene Name":
            info = GeneDbLink.objects.get(name=search_id)
        elif gene_pool == "HGNC":
            info = GeneDbLink.objects.get(hgnc=search_id)
        elif gene_pool == "ENTREZ":
            info = GeneDbLink.objects.get(entrez_gene=search_id)
        elif gene_pool == "ENSEMBL":
            info = GeneDbLink.objects.get(ensembl=search_id)
        elif gene_pool == "UNIPROTKB":
            info = GeneDbLink.objects.get(uniprotkb=search_id)
        elif gene_pool == "OMIM":
            info = GeneDbLink.objects.get(omim=search_id)
    except:
        return render(request, 'biodatabase/templates/genebooks.html')

    # info2 = GenecardDescriptionSummary.objects.get(gene__name="KLK13")
    # filter(子表外键字段__母表字段='过滤条件')
    # summary2 = GenecardDescriptionSummary.objects.filter(gene__name = 'KLK13').values('gene__name','type','description','summary_entrez','summary_genecard')
    # summary_info2 = list(summary2)
    #summary_info = list(summary)
    return render(request, 'biodatabase/templates/genebooks.html',\
                  {'gene_dbs':gene_db,'info':info})
def ajax_list(request):
    a = [1,2,3,4,5,6,7,8,9,10]
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)
'''
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))
'''