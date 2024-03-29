from django.db import models
from datetime import datetime

# Create your models here.

class Protein(models.Model):
    uniprotkb_id = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True, default=datetime.now())

    def __unicode__(self):
        return "{}".format(self.uniprotkb_id)


class Structure(models.Model):
    protein = models.ForeignKey('Protein', null=True)
    pdb_id = models.CharField(max_length=4, unique=True)
    classification = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True, default=datetime.now())

    def __unicode__(self):
        return "{} - {}".format(self.pdb_id, self.title)


class Helix(models.Model):

    HELIX_CLASSIFICATIONS = (
        (0, 'Right-handed alpha (default)'),
        (1, 'Right-handed omega'),
        (2, 'Right-handed pi'),
        (3, 'Right-handed gamma'),
        (4, 'Right-handed 3 - 10'),
        (5, 'Left-handed alpha'),
        (6, 'Left-handed omega'),
        (7, 'Left-handed gamma'),
        (8, '2 - 7 ribbon/helix'),
        (9, 'Polyproline'),
    )

    structure = models.ForeignKey('Structure')
    comment = models.CharField(max_length=256)
    helix_class = models.PositiveSmallIntegerField()
    end_i_code = models.CharField(max_length=1)
    helix_id = models.CharField(max_length=3)
    end_seq_num = models.PositiveSmallIntegerField()
    init_seq_num = models.PositiveSmallIntegerField()
    init_res_name = models.CharField(max_length=3)
    ser_num = models.PositiveSmallIntegerField()
    init_chain_id = models.CharField(max_length=1)
    init_i_code = models.CharField(max_length=1)
    length = models.PositiveSmallIntegerField()
    end_chain_id = models.CharField(max_length=1)
    end_res_name = models.CharField(max_length=3)
    classification = models.PositiveSmallIntegerField(choices=HELIX_CLASSIFICATIONS)

    def __unicode__(self):
        return "{} - {}".format(self.helix_id, self.classification)


class Sheet(models.Model):
    structure = models.ForeignKey('Structure')
    strand = models.PositiveSmallIntegerField()
    sheet_id = models.CharField(max_length=3)
    numStrands = models.PositiveSmallIntegerField()
    init_res_name = models.CharField(max_length=3)
    init_chain_id = models.CharField(max_length=1)
    init_seq_num = models.PositiveSmallIntegerField()
    init_i_code = models.CharField(max_length=1)
    end_res_name = models.CharField(max_length=3)
    end_chain_id = models.CharField(max_length=1)
    end_seq_num = models.PositiveSmallIntegerField()
    end_i_code = models.CharField(max_length=1)
    sense = models.SmallIntegerField()
    cur_atom = models.CharField(max_length=4, null=True)
    cur_res_name = models.CharField(max_length=3, null=True)
    cur_chain_id = models.CharField(max_length=1, null=True)
    cur_res_seq = models.PositiveSmallIntegerField(null=True)
    cur_i_code = models.CharField(max_length=1, null=True)
    prev_atom = models.CharField(max_length=4, null=True)
    prev_res_name = models.CharField(max_length=3, null=True)
    prev_chain_id = models.CharField(max_length=1, null=True)
    prev_res_seq = models.PositiveSmallIntegerField(null=True)
    prev_i_code = models.CharField(max_length=1, null=True)

    def __unicode__(self):
        return "{} - {}".format(self.sheet_id, self.protein_id)

class Sequence(models.Model):
    structure = models.ForeignKey('Structure')
    chain_id = models.CharField(max_length=1)
    num_res = models.PositiveSmallIntegerField()
    residues = models.TextField()

    def __unicode__(self):
        return "{}".format(self.residues)