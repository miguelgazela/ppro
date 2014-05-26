# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sequence.protein_id'
        db.add_column(u'proteil_sequence', 'protein_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['proteil.Protein']),
                      keep_default=False)

        # Adding field 'Sequence.ser_num'
        db.add_column(u'proteil_sequence', 'ser_num',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Sequence.chain_id'
        db.add_column(u'proteil_sequence', 'chain_id',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1),
                      keep_default=False)

        # Adding field 'Sequence.num_res'
        db.add_column(u'proteil_sequence', 'num_res',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Sequence.residues'
        db.add_column(u'proteil_sequence', 'residues',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=51),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sequence.protein_id'
        db.delete_column(u'proteil_sequence', 'protein_id_id')

        # Deleting field 'Sequence.ser_num'
        db.delete_column(u'proteil_sequence', 'ser_num')

        # Deleting field 'Sequence.chain_id'
        db.delete_column(u'proteil_sequence', 'chain_id')

        # Deleting field 'Sequence.num_res'
        db.delete_column(u'proteil_sequence', 'num_res')

        # Deleting field 'Sequence.residues'
        db.delete_column(u'proteil_sequence', 'residues')


    models = {
        u'proteil.helix': {
            'Meta': {'object_name': 'Helix'},
            'classification': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'end_chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'end_i_code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'end_res_name': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'end_seq_num': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'helix_class': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'helix_id': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'init_i_code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'init_res_name': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'init_seq_num': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'length': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'protein_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proteil.Protein']"}),
            'ser_num': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'proteil.protein': {
            'Meta': {'object_name': 'Protein'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdbId': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'pdb_classification': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pdb_title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'uniprotkbId': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6'})
        },
        u'proteil.sequence': {
            'Meta': {'object_name': 'Sequence'},
            'chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_res': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'protein_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proteil.Protein']"}),
            'residues': ('django.db.models.fields.CharField', [], {'max_length': '51'}),
            'ser_num': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'proteil.sheet': {
            'Meta': {'object_name': 'Sheet'},
            'cur_atom': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'cur_chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'cur_i_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'cur_res_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'cur_res_seq': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'end_chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'end_i_code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'end_res_name': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'end_seq_num': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'init_i_code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'init_res_name': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'init_seq_num': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'numStrands': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'prev_atom': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'prev_chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'prev_i_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'prev_res_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'prev_res_seq': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'protein_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proteil.Protein']"}),
            'sense': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sheet_id': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'strand': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['proteil']