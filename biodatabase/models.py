from django.db import models

# Create your models here.
class GeneDbLink(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    subname = models.CharField(max_length=511, blank=True, null=True)
    hgnc = models.CharField(db_column='HGNC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entrez_gene = models.CharField(db_column='Entrez_Gene', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ensembl = models.CharField(db_column='Ensembl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uniprotkb = models.CharField(db_column='UniProtKB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    omim = models.CharField(db_column='OMIM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hgnc_link = models.CharField(db_column='HGNC_link', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entrez_gene_link = models.CharField(db_column='Entrez Gene_link', max_length=255, blank=True, null=True)
    ensembl_link = models.CharField(db_column='Ensembl_link', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uniprotkb_link = models.CharField(db_column='UniProtKB_link', max_length=255, blank=True, null=True)  # Field name made lowercase.
    omim_link = models.CharField(db_column='OMIM_link', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    summary_entrez = models.CharField(max_length=255, blank=True, null=True)
    summary_genecard = models.CharField(max_length=255, blank=True, null=True)
    summary_uniport = models.CharField(max_length=255, blank=True, null=True)
    summary_tocris = models.CharField(db_column='summary_Tocris', max_length=255, blank=True, null=True)  # Field name made lowercase.
    summary_civic = models.CharField(db_column='summary_CIViC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gene_db_link_3'

class GenecardId(models.Model):
    gene = models.CharField(max_length=255, blank=True, null=True)
    subname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genecard_id'




