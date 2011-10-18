#!/usr/bin/env python
# encoding: utf-8
"""
django-rgraph.py

Creates the necasary javascript to draw various graphs.

Created by Stuart Grimshaw on 2011-10-13.
Copyright (c) 2011 Stuart M. Grimshaw. All rights reserved.
"""

import sys
import os
import unittest

from django.conf import settings

from django.template import TemplateSyntaxError, Context, Variable, Node, Template, Library
from django.template.loader import get_template

register = Library()

class RenderRGraph(Node):
    def __init__(self, data):
        self.data = data
        
    def render(self, context):
        t = get_template(context['chart'].template)
        return t.render(context)

@register.tag	
def rgraph(parser, token):
	"""
	
	Example:: 
	{% rgraph chart %}
	
	"""
	
	bits = token.contents.split()
	
	return RenderRGraph(bits)