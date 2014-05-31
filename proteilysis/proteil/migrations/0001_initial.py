# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Protein'
        db.create_table(u'proteil_protein', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uniprotkb_id', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 31, 0, 0), auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'proteil', ['Protein'])

        # Adding model 'Structure'
        db.create_table(u'proteil_structure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proteil.Protein'], null=True)),
            ('pdb_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4)),
            ('classification', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 31, 0, 0), auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'proteil', ['Structure'])

        # Adding model 'Helix'
        db.create_table(u'proteil_helix', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proteil.Structure'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('helix_class', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('end_i_code', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('helix_id', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('end_seq_num', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('init_seq_num', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('init_res_name', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('ser_num', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('init_chain_id', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('init_i_code', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('length', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('end_chain_id', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('end_res_name', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('classification', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'proteil', ['Helix'])

        # Adding model 'Sheet'
        db.create_table(u'proteil_sheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proteil.Structure'])),
            ('strand', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('sheet_id', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('numStrands', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('init_res_name', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('init_chain_id', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('init_seq_num', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('init_i_code', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('end_res_name', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('end_chain_id', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('end_seq_num', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('end_i_code', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('sense', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cur_atom', self.gf('django.db.models.fields.CharField')(max_length=4, null=True)),
            ('cur_res_name', self.gf('django.db.models.fields.CharField')(max_length=3, null=True)),
            ('cur_chain_id', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('cur_res_seq', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('cur_i_code', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('prev_atom', self.gf('django.db.models.fields.CharField')(max_length=4, null=True)),
            ('prev_res_name', self.gf('django.db.models.fields.CharField')(max_length=3, null=True)),
            ('prev_chain_id', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('prev_res_seq', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('prev_i_code', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
        ))
        db.send_create_signal(u'proteil', ['Sheet'])

        # Adding model 'Sequence'
        db.create_table(u'proteil_sequence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proteil.Structure'])),
            ('chain_id', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('num_res', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('residues', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'proteil', ['Sequence'])


    def backwards(self, orm):
        # Deleting model 'Protein'
        db.delete_table(u'proteil_protein')

        # Deleting model 'Structure'
        db.delete_table(u'proteil_structure')

        # Deleting model 'Helix'
        db.delete_table(u'proteil_helix')

        # Deleting model 'Sheet'
        db.delete_table(u'proteil_sheet')

        # Deleting model 'Sequence'
        db.delete_table(u'proteil_sequence')


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
            'ser_num': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proteil.Structure']"})
        },
        u'proteil.protein': {
            'Meta': {'object_name': 'Protein'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 31, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uniprotkb_id': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'proteil.sequence': {
            'Meta': {'object_name': 'Sequence'},
            'chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_res': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'residues': ('django.db.models.fields.TextField', [], {}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proteil.Structure']"})
        },
        u'proteil.sheet': {
            'Meta': {'object_name': 'Sheet'},
            'cur_atom': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'}),
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
            'prev_atom': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'}),
            'prev_chain_id': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'prev_i_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'prev_res_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'prev_res_seq': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'sense': ('django.db.models.fields.SmallIntegerField', [], {}),
            'sheet_id': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'strand': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proteil.Structure']"})
        },
        u'proteil.structure': {
            'Meta': {'object_name': 'Structure'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 31, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdb_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proteil.Protein']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['proteil']