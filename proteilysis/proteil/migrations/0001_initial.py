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
            ('pdbId', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4)),
            ('uniprotkbId', self.gf('django.db.models.fields.CharField')(unique=True, max_length=6)),
            ('pdb_classification', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('pdb_title', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'proteil', ['Protein'])

        # Adding model 'Helix'
        db.create_table(u'proteil_helix', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protein_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proteil.Protein'])),
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
        ))
        db.send_create_signal(u'proteil', ['Sheet'])

        # Adding model 'Sequence'
        db.create_table(u'proteil_sequence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'proteil', ['Sequence'])


    def backwards(self, orm):
        # Deleting model 'Protein'
        db.delete_table(u'proteil_protein')

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['proteil']