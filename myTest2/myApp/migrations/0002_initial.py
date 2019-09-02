# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('myApp_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('myApp', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name('myApp_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm['myApp.user'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name('myApp_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm['myApp.user'], null=False)),
            ('permission', models.ForeignKey(orm['auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding model 'Ad'
        db.create_table('myApp_ad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image_url', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_publish', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('myApp', ['Ad'])

        # Adding model 'Category'
        db.create_table('myApp_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('typ', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('west_east', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('myApp', ['Category'])

        # Adding model 'Brand'
        db.create_table('myApp_brand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('myApp', ['Brand'])

        # Adding model 'Size'
        db.create_table('myApp_size', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('myApp', ['Size'])

        # Adding model 'Tag'
        db.create_table('myApp_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('myApp', ['Tag'])

        # Adding model 'Furniture'
        db.create_table('myApp_furniture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myApp.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myApp.Brand'])),
            ('old_price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('new_price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('discount', self.gf('django.db.models.fields.FloatField')(default=1)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sales', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('num', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image_url_i', self.gf('django.db.models.fields.files.ImageField')(default='furniture/default.jpg', max_length=100)),
            ('image_url_l', self.gf('django.db.models.fields.files.ImageField')(default='furniture/default.jpg', max_length=100)),
            ('image_url_m', self.gf('django.db.models.fields.files.ImageField')(default='furniture/default.jpg', max_length=100)),
            ('image_url_r', self.gf('django.db.models.fields.files.ImageField')(default='furniture/default.jpg', max_length=100)),
            ('image_url_c', self.gf('django.db.models.fields.files.ImageField')(default='furniture/ce.jpg', max_length=100)),
        ))
        db.send_create_signal('myApp', ['Furniture'])

        # Adding M2M table for field size on 'Furniture'
        m2m_table_name = db.shorten_name('myApp_furniture_size')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('furniture', models.ForeignKey(orm['myApp.furniture'], null=False)),
            ('size', models.ForeignKey(orm['myApp.size'], null=False))
        ))
        db.create_unique(m2m_table_name, ['furniture_id', 'size_id'])

        # Adding M2M table for field tag on 'Furniture'
        m2m_table_name = db.shorten_name('myApp_furniture_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('furniture', models.ForeignKey(orm['myApp.furniture'], null=False)),
            ('tag', models.ForeignKey(orm['myApp.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['furniture_id', 'tag_id'])

        # Adding model 'Caritem'
        db.create_table('myApp_caritem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('furniture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myApp.Furniture'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sum_price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('myApp', ['Caritem'])

        # Adding model 'Order'
        db.create_table('myApp_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myApp.User'])),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('order_state', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('staff', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('myApp', ['Order'])

        # Adding model 'Order_list'
        db.create_table('myApp_order_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('furniture', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myApp.Order'])),
        ))
        db.send_create_signal('myApp', ['Order_list'])

        # Adding model 'Comment'
        db.create_table('myApp_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comm', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fur_id', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('myApp', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('myApp_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name('myApp_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name('myApp_user_user_permissions'))

        # Deleting model 'Ad'
        db.delete_table('myApp_ad')

        # Deleting model 'Category'
        db.delete_table('myApp_category')

        # Deleting model 'Brand'
        db.delete_table('myApp_brand')

        # Deleting model 'Size'
        db.delete_table('myApp_size')

        # Deleting model 'Tag'
        db.delete_table('myApp_tag')

        # Deleting model 'Furniture'
        db.delete_table('myApp_furniture')

        # Removing M2M table for field size on 'Furniture'
        db.delete_table(db.shorten_name('myApp_furniture_size'))

        # Removing M2M table for field tag on 'Furniture'
        db.delete_table(db.shorten_name('myApp_furniture_tag'))

        # Deleting model 'Caritem'
        db.delete_table('myApp_caritem')

        # Deleting model 'Order'
        db.delete_table('myApp_order')

        # Deleting model 'Order_list'
        db.delete_table('myApp_order_list')

        # Deleting model 'Comment'
        db.delete_table('myApp_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myApp.ad': {
            'Meta': {'object_name': 'Ad', 'ordering': "['index', 'id']"},
            'date_publish': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'myApp.brand': {
            'Meta': {'object_name': 'Brand', 'ordering': "['index']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'myApp.caritem': {
            'Meta': {'object_name': 'Caritem'},
            'furniture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myApp.Furniture']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sum_price': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        'myApp.category': {
            'Meta': {'object_name': 'Category', 'ordering': "['index', 'id']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'west_east': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'myApp.comment': {
            'Meta': {'object_name': 'Comment'},
            'comm': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fur_id': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'myApp.furniture': {
            'Meta': {'object_name': 'Furniture', 'ordering': "['id']"},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myApp.Brand']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myApp.Category']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url_c': ('django.db.models.fields.files.ImageField', [], {'default': "'furniture/ce.jpg'", 'max_length': '100'}),
            'image_url_i': ('django.db.models.fields.files.ImageField', [], {'default': "'furniture/default.jpg'", 'max_length': '100'}),
            'image_url_l': ('django.db.models.fields.files.ImageField', [], {'default': "'furniture/default.jpg'", 'max_length': '100'}),
            'image_url_m': ('django.db.models.fields.files.ImageField', [], {'default': "'furniture/default.jpg'", 'max_length': '100'}),
            'image_url_r': ('django.db.models.fields.files.ImageField', [], {'default': "'furniture/default.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'new_price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'old_price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'sales': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'size': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['myApp.Size']"}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['myApp.Tag']"})
        },
        'myApp.order': {
            'Meta': {'object_name': 'Order'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_state': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'staff': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myApp.User']"})
        },
        'myApp.order_list': {
            'Meta': {'object_name': 'Order_list'},
            'furniture': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myApp.Order']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'myApp.size': {
            'Meta': {'object_name': 'Size', 'ordering': "['index']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'myApp.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'myApp.user': {
            'Meta': {'object_name': 'User', 'ordering': "['-id']"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        }
    }

    complete_apps = ['myApp']