# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sheet.protein_id'
        db.add_column(u'proteil_sheet', 'protein_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['proteil.Protein']),
                      keep_default=False)

        # Adding field 'Sheet.strand'
        db.add_column(u'proteil_sheet', 'strand',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Sheet.sheet_id'
        db.add_column(u'proteil_sheet', 'sheet_id',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=3),
                      keep_default=False)

        # Adding field 'Sheet.numStrands'
        db.add_column(u'proteil_sheet', 'numStrands',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Sheet.init_res_name'
        db.add_column(u'proteil_sheet', 'init_res_name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=3),
                      keep_default=False)

        # Adding field 'Sheet.init_chain_id'
        db.add_column(u'proteil_sheet', 'init_chain_id',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1),
                      keep_default=False)

        # Adding field 'Sheet.init_seq_num'
        db.add_column(u'proteil_sheet', 'init_seq_num',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Sheet.init_i_code'
        db.add_column(u'proteil_sheet', 'init_i_code',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1),
                      keep_default=False)

        # Adding field 'Sheet.end_res_name'
        db.add_column(u'proteil_sheet', 'end_res_name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=3),
                      keep_default=False)

        # Adding field 'Sheet.end_chain_id'
        db.add_column(u'proteil_sheet', 'end_chain_id',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1),
                      keep_default=False)

        # Adding field 'Sheet.end_seq_num'
        db.add_column(u'proteil_sheet', 'end_seq_num',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Sheet.end_i_code'
        db.add_column(u'proteil_sheet', 'end_i_code',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1),
                      keep_default=False)

        # Adding field 'Sheet.sense'
        db.add_column(u'proteil_sheet', 'sense',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Sheet.cur_atom'
        db.add_column(u'proteil_sheet', 'cur_atom',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True),
                      keep_default=False)

        # Adding field 'Sheet.cur_res_name'
        db.add_column(u'proteil_sheet', 'cur_res_name',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True),
                      keep_default=False)

        # Adding field 'Sheet.cur_chain_id'
        db.add_column(u'proteil_sheet', 'cur_chain_id',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True),
                      keep_default=False)

        # Adding field 'Sheet.cur_res_seq'
        db.add_column(u'proteil_sheet', 'cur_res_seq',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sheet.cur_i_code'
        db.add_column(u'proteil_sheet', 'cur_i_code',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True),
                      keep_default=False)

        # Adding field 'Sheet.prev_atom'
        db.add_column(u'proteil_sheet', 'prev_atom',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True),
                      keep_default=False)

        # Adding field 'Sheet.prev_res_name'
        db.add_column(u'proteil_sheet', 'prev_res_name',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True),
                      keep_default=False)

        # Adding field 'Sheet.prev_chain_id'
        db.add_column(u'proteil_sheet', 'prev_chain_id',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True),
                      keep_default=False)

        # Adding field 'Sheet.prev_res_seq'
        db.add_column(u'proteil_sheet', 'prev_res_seq',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sheet.prev_i_code'
        db.add_column(u'proteil_sheet', 'prev_i_code',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sheet.protein_id'
        db.delete_column(u'proteil_sheet', 'protein_id_id')

        # Deleting field 'Sheet.strand'
        db.delete_column(u'proteil_sheet', 'strand')

        # Deleting field 'Sheet.sheet_id'
        db.delete_column(u'proteil_sheet', 'sheet_id')

        # Deleting field 'Sheet.numStrands'
        db.delete_column(u'proteil_sheet', 'numStrands')

        # Deleting field 'Sheet.init_res_name'
        db.delete_column(u'proteil_sheet', 'init_res_name')

        # Deleting field 'Sheet.init_chain_id'
        db.delete_column(u'proteil_sheet', 'init_chain_id')

        # Deleting field 'Sheet.init_seq_num'
        db.delete_column(u'proteil_sheet', 'init_seq_num')

        # Deleting field 'Sheet.init_i_code'
        db.delete_column(u'proteil_sheet', 'init_i_code')

        # Deleting field 'Sheet.end_res_name'
        db.delete_column(u'proteil_sheet', 'end_res_name')

        # Deleting field 'Sheet.end_chain_id'
        db.delete_column(u'proteil_sheet', 'end_chain_id')

        # Deleting field 'Sheet.end_seq_num'
        db.delete_column(u'proteil_sheet', 'end_seq_num')

        # Deleting field 'Sheet.end_i_code'
        db.delete_column(u'proteil_sheet', 'end_i_code')

        # Deleting field 'Sheet.sense'
        db.delete_column(u'proteil_sheet', 'sense')

        # Deleting field 'Sheet.cur_atom'
        db.delete_column(u'proteil_sheet', 'cur_atom')

        # Deleting field 'Sheet.cur_res_name'
        db.delete_column(u'proteil_sheet', 'cur_res_name')

        # Deleting field 'Sheet.cur_chain_id'
        db.delete_column(u'proteil_sheet', 'cur_chain_id')

        # Deleting field 'Sheet.cur_res_seq'
        db.delete_column(u'proteil_sheet', 'cur_res_seq')

        # Deleting field 'Sheet.cur_i_code'
        db.delete_column(u'proteil_sheet', 'cur_i_code')

        # Deleting field 'Sheet.prev_atom'
        db.delete_column(u'proteil_sheet', 'prev_atom')

        # Deleting field 'Sheet.prev_res_name'
        db.delete_column(u'proteil_sheet', 'prev_res_name')

        # Deleting field 'Sheet.prev_chain_id'
        db.delete_column(u'proteil_sheet', 'prev_chain_id')

        # Deleting field 'Sheet.prev_res_seq'
        db.delete_column(u'proteil_sheet', 'prev_res_seq')

        # Deleting field 'Sheet.prev_i_code'
        db.delete_column(u'proteil_sheet', 'prev_i_code')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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