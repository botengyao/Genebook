from django.shortcuts import render
from .models import GeneDbLink
from django.http import JsonResponse
from django.http import HttpResponse
#from django.views import View
import json
import csv
# Create your views here.
infor = []

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
    infor =[]
    global info
    info = GeneDbLink.objects.get(omim='611000')
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
        return render(request, 'biodatabase/templates/genebooks.html',{'info':info})

    # info2 = GenecardDescriptionSummary.objects.get(gene__name="KLK13")
    # filter(子表外键字段__母表字段='过滤条件')
    # summary2 = GenecardDescriptionSummary.objects.filter(gene__name = 'KLK13').values('gene__name','type','description','summary_entrez','summary_genecard')
    # summary_info2 = list(summary2)
    #summary_info = list(summary)
    return render(request, 'biodatabase/templates/genebooks.html',\
                  {'gene_dbs':gene_db,'info':info,'infor':infor})
def search_multi(request):
    gene_db = GeneDbLink.objects
    global infor
    infor = []

    gene_pool = request.GET['genepool']
    try:
        search_id = request.GET['gene_id'].split()
    except:
        render(request, 'biodatabase/templates/genebooksmulti.html', \
               {'gene_dbs': gene_db, 'infor': infor})
    if gene_pool == "Gene Name":
        for id in search_id:
            try:
                infor.append(GeneDbLink.objects.get(name=id))
            except:
                continue
    elif gene_pool == "HGNC":
        for id in search_id:
            try:
                infor.append(GeneDbLink.objects.get(hgnc=id))
            except:
                continue
    elif gene_pool == "ENTREZ":
        for id in search_id:
            try:
                infor.append(GeneDbLink.objects.get(entrez_gene=id))
            except:
                continue
    elif gene_pool == "ENSEMBL":
        for id in search_id:
            try:
                infor.append(GeneDbLink.objects.get(ensembl=id))
            except:
                continue
    elif gene_pool == "UNIPROTKB":
        for id in search_id:
            try:
                infor.append(GeneDbLink.objects.get(uniprotkb=id))
            except:
                continue
    elif gene_pool == "OMIM":
        for id in search_id:
            try:
                infor.append(GeneDbLink.objects.get(omim=id))
            except:
                continue
    #except:
      #  return render(request, 'biodatabase/templates/genebooksmulti.html')
    # info2 = GenecardDescriptionSummary.objects.get(gene__name="KLK13")
    # filter(子表外键字段__母表字段='过滤条件')
    # summary2 = GenecardDescriptionSummary.objects.filter(gene__name = 'KLK13').values('gene__name','type','description','summary_entrez','summary_genecard')
    # summary_info2 = list(summary2)
    #summary_info = list(summary)
    return render(request, 'biodatabase/templates/genebooksmulti.html',\
                  {'gene_dbs':gene_db, 'infor':infor})

def downloads(request):
    response = HttpResponse(content_type='text/csv')
    # attachment 代表这个csv文件作为一个附件的形式下载
    # filename='abc.csv' 指定下载的文件名字
    response['Content-Disposition'] = "attachment; filename= muti_convert_summary.csv "
    writer = csv.writer(response)
    writer.writerow(['name', 'HGNC','Entrez_Gene', 'Ensembl', 'UniProtKB', 'OMIM', 'type', 'description', \
                     'summary_entrez', 'summary_genecard', 'summary_uniport', 'summary_Tocris', 'summary_CIViC'])
    for info in infor:
        writer.writerow([info.name, info.hgnc, info.entrez_gene, info.ensembl, info.uniprotkb, info.omim, \
                         info.type, info.description, info.summary_entrez, info.summary_genecard,\
                         info.summary_uniport, info.summary_tocris, info.summary_civic])
    return response
def download(request):
    response = HttpResponse(content_type='text/csv')
    # attachment 代表这个csv文件作为一个附件的形式下载
    # filename='abc.csv' 指定下载的文件名字
    response['Content-Disposition'] = "attachment; filename= single_convert_summary.csv "
    writer = csv.writer(response)
    writer.writerow(['name', 'HGNC','Entrez_Gene', 'Ensembl', 'UniProtKB', 'OMIM', 'type', 'description', \
                     'summary_entrez', 'summary_genecard', 'summary_uniport', 'summary_Tocris', 'summary_CIViC'])
    writer.writerow([info.name, info.hgnc, info.entrez_gene, info.ensembl, info.uniprotkb, info.omim, \
                         info.type, info.description, info.summary_entrez, info.summary_genecard,\
                         info.summary_uniport, info.summary_tocris, info.summary_civic])
    return response
'''
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))
'''
'''

def ajax_list(request):
    a = [1,2,3,4,5,6,7,8,9,10]
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)
'''