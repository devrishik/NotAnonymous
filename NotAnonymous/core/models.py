# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True


class SensorType(TimeStampedModel):
	kt_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=255)


class Sensor(TimeStampedModel):
	kt_id = models.IntegerField(unique=True)


class Feed(TimeStampedModel):
	kt_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=255, null=True, blank=True)
	sensor_type = models.ForeignKey(SensorType)
	sensor = models.ForeignKey(Sensor)
	active = models.BooleanField(default=True)
	last_sample_time = models.DateTimeField()
	localtion_x = models.CharField(max_length=255, null=True, blank=True)
	localtion_y = models.CharField(max_length=255, null=True, blank=True)
	localtion_z = models.CharField(max_length=255, null=True, blank=True)


class Sample(TimeStampedModel):
	kt_id = models.IntegerField(unique=True)
	time = models.DateTimeField()
	value = models.CharField(max_length=255)
