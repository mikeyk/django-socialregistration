"""
Created on 22.09.2009

@author: alen
"""
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from ragendja.dbutils import get_object
from socialregistration.models import (FacebookProfile, TwitterProfile, FriendFeedProfile, OpenIDProfile)

class Auth(object):
	def get_user(self, user_id):
		obj = get_object(User, user_id)
		return obj

class FacebookAuth(Auth):
	def authenticate(self, uid=None):
		obj = get_object(FacebookProfile, "uid =", uid)
		if obj: return obj.user
		else: return None

class TwitterAuth(Auth):
	def authenticate(self, twitter_id=None):
		obj = get_object(TwitterProfile, "twitter_id = ", twitter_id)
		if obj:
			return obj.user
		else:
			return None

class OpenIDAuth(Auth):
	def authenticate(self, identity=None):
		obj = get_object(OpenIDProfile, "identity = ", identity)
		if obj: return obj.user
		else: return None
