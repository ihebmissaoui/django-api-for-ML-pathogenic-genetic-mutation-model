from django.db import models

# Create your models here.
class pathogenics(models.Model):
    """
    A model for defining a pathogenic model
    """
    #for categorial feature
    IMPACT_CHOICES = (
        ('LOW','LOW'),
        ('MODERATE','MODERATE'),
        ('HIGH','HIGH'),
        ('MODIFIER','MODIFIER')

    )
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    chrom  = models.CharField(max_length=20)
    pos = models.IntegerField()
    ref =  models.CharField(max_length=20)
    alt =  models.CharField(max_length=20)
    afEsp = models.IntegerField()
    afExac = models.IntegerField()
    afTgp = models.IntegerField()
    clDn = models.CharField(max_length=20)
    clnVc = models.CharField(max_length=20)
    origin =  models.IntegerField()
    allele = models.CharField(max_length=20)
    consequence = models.CharField(max_length=20)
    impact = models.CharField(max_length=20,choices=IMPACT_CHOICES)
    cdnaPosition = models.CharField(max_length=20)
    cdsPosition = models.CharField(max_length=20)
    proteinPosition = models.CharField(max_length=20)
    aminoAcids = models.CharField(max_length=20)
    codons = models.CharField(max_length=20)
    strand =  models.IntegerField()
    sift = models.CharField(max_length=20)
    polyPhen = models.CharField(max_length=20) 
    loFTool = models.IntegerField()
    caddPhred = models.IntegerField()
    bloSum62 = models.IntegerField()

    def __str__(self):
        return self.firstName


