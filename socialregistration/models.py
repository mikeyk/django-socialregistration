"""
Created on 22.09.2009

@author: alen
"""

from django.db import models
from google.appengine.ext import db
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
# Create your models here.


class FacebookProfile(db.Model):
    user = db.ReferenceProperty(User, verbose_name=_('user'), collection_name=None)
    uid = db.StringProperty(verbose_name=_('uid'), required=True)
    
    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.uid)
    
    def authenticate(self):
        return authenticate(uid=self.uid)
    
class TwitterProfile(db.Model):
    user = db.ReferenceProperty(reference_class=User, verbose_name=_('user'), collection_name=None)
    twitter_id = db.IntegerProperty(verbose_name=_('twitter id'))
    
    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.twitter_id)
    
    def authenticate(self):
        return authenticate(twitter_id=self.twitter_id)

class FriendFeedProfile(db.Model):
    user = db.ReferenceProperty(User, verbose_name=_('user'), collection_name=None)

class OpenIDProfile(db.Model):
    user = db.ReferenceProperty(User, verbose_name=_('user'), collection_name=None)
    identity = db.TextProperty(verbose_name=_('identity'), required=False)
    
    def authenticate(self):
        return authenticate(identity=self.identity)

class OpenIDStore(db.Model):
    server_url = db.LinkProperty()
    handle = db.StringProperty()
    secret = db.TextProperty()
    issued = db.IntegerProperty()
    lifetime = db.IntegerProperty()
    assoc_type = db.TextProperty()

class OpenIDNonce(db.Model):
    server_url = db.StringProperty(verbose_name=_('server url'), required=True)
    timestamp = db.IntegerProperty(verbose_name=_('timestamp'), required=True)
    salt = db.StringProperty(verbose_name=_('salt'), required=True)
    date_created = db.DateTimeProperty(verbose_name=_('date created'), auto_now_add=True)
