# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LocationCategory'
        db.create_table('core_locationcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('numchild', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['LocationCategory'])

        # Adding field 'Location.category'
        db.add_column('core_location', 'category', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='locations', to=orm['core.LocationCategory']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'LocationCategory'
        db.delete_table('core_locationcategory')

        # Deleting field 'Location.category'
        db.delete_column('core_location', 'category_id')


    models = {
        'core.businessentity': {
            'Meta': {'object_name': 'BusinessEntity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.locale': {
            'Meta': {'object_name': 'Locale'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'business_entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': "orm['core.BusinessEntity']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': "orm['core.LocationCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'locale': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': "orm['core.Locale']"}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Product']", 'through': "orm['core.Offering']", 'symmetrical': 'False'})
        },
        'core.locationcategory': {
            'Meta': {'object_name': 'LocationCategory'},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'core.offering': {
            'Meta': {'object_name': 'Offering'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offerings'", 'to': "orm['core.Location']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offerings'", 'to': "orm['core.Product']"})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': "orm['core.ProductCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fairtrade_org_uk_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Location']", 'through': "orm['core.Offering']", 'symmetrical': 'False'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'products'", 'null': 'True', 'to': "orm['core.BusinessEntity']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
