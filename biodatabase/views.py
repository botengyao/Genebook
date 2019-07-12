from django.shortcuts import render
from .models import GeneDbLink
from .models import GenecardId
from django.http import JsonResponse
from django.http import HttpResponse
#from django.views import View
from django.db.models import Q
from django.db.models.expressions import RawSQL
import json
import csv
# Create your views here.
class searchID:
    def __init__(self, id, cre, info):
        self.id = id
        self.cre = cre
        self.info = info

def genebook(request):
    infor = GeneDbLink.objects.filter(omim='611000')
    #info2 = GenecardDescriptionSummary.objects.get(gene__name="KLK13")
    #summary = info.genecarddescriptionsummary_set.all().values('gene__name','type','description','summary_entrez','summary_genecard')
    # filter(子表外键字段__母表字段='过滤条件')
    #summary2 = GenecardDescriptionSummary.objects.filter(gene__name = 'KLK13').values('gene__name','type','description','summary_entrez','summary_genecard')
    #summary_info2 = list(summary2)
    #summary_info = list(info)
    return render(request, 'biodatabase/templates/genebooks.html',\
                  {'info_filter':infor})
def search(request):
    infor =[]
    global info_filter
    info_filter = GeneDbLink.objects.filter(name="KLK13")
    try:
        gene_pool = request.GET['genepool']
        search_id = request.GET['gene_id']
        print(search_id)
        cred = 'No results'
        if search_id:
            if gene_pool == "Fuzzy Search":
                info_filter = GeneDbLink.objects.filter(Q(name__iexact=search_id)|Q(hgnc__iexact=search_id)|Q(entrez_gene__iexact=search_id)|Q(ensembl__iexact=search_id)\
                                                        |Q(uniprotkb__iexact=search_id)|Q(omim__iexact=search_id))
                if info_filter:
                    cred = "Trust, find exact name or id"
                #print(len(info_filter))
                else:
                    #print(0)
                    #regex = '(?i)'+'^'+ search_id + '\d'
                    #regex = '^'+ search_id + '\d'
                    #regex = search_id
                    #info_filter = GeneDbLink.objects.filter(name__iregex = regex)
                    info_filter = GeneDbLink.objects.raw('SELECT id FROM gene_db_link_3 WHERE name REGEXP ' +'"' + '^'+ search_id + '[0-9]' + '"'  + ';')
                    #info_filter = GeneDbLink.objects.extra(where=['name= %s'],
                                                        #    params = ['REGEXP ' + '^' + search_id + '[0-9]'],)

                        #select = 'SELECT id FROM gene_db_link_3 WHERE name = %s', ('REGEXP' + '^' + search_id + '[0-9]',)))
                    count = 0
                    for ele in info_filter:
                        count += 1
                        if count >= 2:
                            break

                    #print(info_filter)
                    if count >= 1:
                        cred = "Trust (group)"
                    elif not count:
                        info_filter = GeneDbLink.objects.filter(Q(subname__icontains = "," + search_id + ",")|Q(subname__iregex = '^' + search_id + ","))
                        #print(info_filter)
                        if info_filter:
                            cred = "Trust, find exact alias"
                        else:
                            info_filter = GeneDbLink.objects.filter(subname__icontains = search_id)
                            cred = "Possible, don't find exact alias"
                            if len(info_sfilter) >= 30:
                                info_filter = info_filter[:31]
                                cred = "Possible, don't find exact alias"

                    """
                    if not info_filter:
                        gene_name = GenecardId.objects.filter(subname__icontains = search_id).distinct()
                        for name in gene_name:
                            filter = GeneDbLink.objects.filter(name = name.gene)
                            if GeneDbLink.objects.filter(
                            info_filter.append(GeneDbLink.objects.filter(name = name.gene))
                        if len(info_filter) >= 50:
                            info_filter = info_filter[:51]
                    """
            elif gene_pool == "HGNC":
                info_filter = GeneDbLink.objects.filter(hgnc__iexact=search_id)
                if info_filter:
                    cred = "Trust, find exact name or id"

            elif gene_pool == "ENTREZ":
                info_filter = GeneDbLink.objects.filter(entrez_gene__iexact=search_id)
                if info_filter:
                    cred = "Trust, find exact name or id"
            elif gene_pool == "ENSEMBL":
                info_filter = GeneDbLink.objects.filter(ensembl__iexact=search_id)
                if info_filter:
                    cred = "Trust, find exact name or id"
            elif gene_pool == "UNIPROTKB":
                info_filter = GeneDbLink.objects.filter(uniprotkb__iexact=search_id)
                if info_filter:
                    cred = "Trust, find exact name or id"
            elif gene_pool == "OMIM":
                info_filter = GeneDbLink.objects.filter(omim__iexact=search_id)
                if info_filter:
                    cred = "Trust, find exact name or id"
        else:
            info_filter = GeneDbLink.objects.filter(name="")

    except:
        return render(request, 'biodatabase/templates/genebooks.html',{'info_filter':info_filter})

    # info2 = GenecardDescriptionSummary.objects.get(gene__name="KLK13")
    # filter(子表外键字段__母表字段='过滤条件')
    # summary2 = GenecardDescriptionSummary.objects.filter(gene__name = 'KLK13').values('gene__name','type','description','summary_entrez','summary_genecard')
    # summary_info2 = list(summary2)
    #summary_info = list(summary)
    return render(request, 'biodatabase/templates/genebooks.html',\
                  {'trust':cred,'info_filter':info_filter, "search_id":json.dumps(search_id),"pool":json.dumps(gene_pool)})
                 # {'info_filter':info_filter, "search_id":json.dumps(search_id),"pool":json.dumps(gene_pool),"gene_name":gene_name})


def search_multi(request):
    gene_db = GeneDbLink.objects
    global results
    infor = GeneDbLink.objects.filter(name="")
    results = []
    search_input = []
    gene_output = 'All'
    search_id = []

    try:
        search_input = request.GET['gene_id']
        gene_output = request.GET['geneoutput']
        search_id = search_input.split("\r\n")
    except:
        render(request, 'biodatabase/templates/genebooksmulti.html', \
               {'gene_dbs': gene_db, 'infor': results, "search_input":search_input, 'gene_output':json.dumps(gene_output),'gene_out':gene_output})

    for id in search_id:
        infor = GeneDbLink.objects.filter(name__iexact=id)
        if infor:
            inputID = searchID(id, "Trust, find exact name or id", infor[0])
        else:
            #regex =  '^' + id + '\d'
            #regex = '(?i)' + '^' + id + '\d'
            #infor = GeneDbLink.objects.filter(name__iregex=regex)
            infor = GeneDbLink.objects.raw('SELECT id FROM gene_db_link_3 WHERE name REGEXP ' + '"' + '^' + id + '[0-9]' + '"' + ';')
            #print(infor)
            count = 0

            for ele in infor:
                temp = ele
                count += 1
                if count >= 1:
                    break

            if count >= 1:
                inputID = searchID(id, "Trust (Group)", temp)
            else:
                infor = GeneDbLink.objects.filter(Q(subname__icontains = "," + id + ",")|Q(subname__icontains = id + ","))

                if 1 < len(infor):
                    #infor = GeneDbLink.objects.filter(
                    #    Q(name__iexact=id) | Q(hgnc__iexact=id) | Q(entrez_gene__iexact=id) | Q(ensembl__iexact=id) \
                      #  | Q(uniprotkb__iexact=id) | Q(omim__iexact=id))
                    inputID = searchID(id, "Trust (many), find exact alias, try to use single 'Gene ID convert' to find all", infor[1])
                elif len(infor) == 1:
                    inputID = searchID(id, "Trust (only), find exact alias", infor[0])
                else:
                    infor = None
                    infor = GeneDbLink.objects.filter(subname__icontains= id )
                    if 1 < len(infor) < 50:
                        inputID = searchID(id, "Probably, fuzzy match, results < 50, try to use single 'Gene ID convert' to find all", infor[0])
                    elif len(infor) >= 50:
                        inputID = searchID(id, "Probably, fuzzy match, too many results (>50), try to be more specific", infor[0])
                    else:
                        infor = None
                        inputID = searchID(id, "No match", infor)

        results.append(inputID)
        #print(results[0].id,results[0].cre,results[0].info)
    '''
    if gene_pool == "Gene Name":    pass
    elif gene_pool == "HGNC":pass
    elif gene_pool == "ENTREZ":pass
    elif gene_pool == "ENSEMBL":pass
    elif gene_pool == "UNIPROTKB":pass
    elif gene_pool == "OMIM":pass
    '''
    #except:
      #  return render(request, 'biodatabase/templates/genebooksmulti.html')
    # info2 = GenecardDescriptionSummary.objects.get(gene__name="KLK13")
    # filter(子表外键字段__母表字段='过滤条件')
    # summary2 = GenecardDescriptionSummary.objects.filter(gene__name = 'KLK13').values('gene__name','type','description','summary_entrez','summary_genecard')
    # summary_info2 = list(summary2)
    #summary_info = list(summary)
    return render(request, 'biodatabase/templates/genebooksmulti.html',\
                  {'gene_dbs':gene_db, 'infor':results, "search_input":search_input, 'gene_output':json.dumps(gene_output),'gene_out':gene_output})

def downloads(request):
    response = HttpResponse(content_type='text/csv')
    # attachment 代表这个csv文件作为一个附件的形式下载
    # filename='abc.csv' 指定下载的文件名字
    response['Content-Disposition'] = "attachment; filename= muti_convert_summary.csv "
    writer = csv.writer(response)
    writer.writerow(['Input','credibility','name', 'HGNC','Entrez_Gene', 'Ensembl', 'UniProtKB', 'OMIM', 'type', 'description', \
                     'summary_entrez', 'summary_genecard', 'summary_uniport', 'summary_Tocris', 'summary_CIViC'])
    for info in results:
        if info.info:
            writer.writerow([info.id, info.cre, info.info.name, info.info.hgnc, info.info.entrez_gene, info.info.ensembl, info.info.uniprotkb, info.info.omim, \
                             info.info.type, info.info.description, info.info.summary_entrez, info.info.summary_genecard,\
                             info.info.summary_uniport, info.info.summary_tocris, info.info.summary_civic])
        else:
            writer.writerow([info.id, info.cre,'None','None','None','None','None','None','None'\
                                ,'None','None','None','None','None','None'])
    return response
def download(request):
    response = HttpResponse(content_type='text/csv')
    # attachment 代表这个csv文件作为一个附件的形式下载
    # filename='abc.csv' 指定下载的文件名字
    response['Content-Disposition'] = "attachment; filename= single_convert_summary.csv "
    writer = csv.writer(response)
    writer.writerow(['name', 'subname','HGNC','Entrez_Gene', 'Ensembl', 'UniProtKB', 'OMIM', 'type', 'description', \
                     'summary_entrez', 'summary_genecard', 'summary_uniport', 'summary_Tocris', 'summary_CIViC'])
    for info in info_filter:
        writer.writerow([info.name, info.subname, info.hgnc, info.entrez_gene, info.ensembl, info.uniprotkb, info.omim, \
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