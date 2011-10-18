"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.template import Template, Context
from django.http import HttpRequest
from chart import PieChart

class SimpleTest(TestCase):
    def setUp(self):
        self.TEMPLATE = "{% load django_rgraph %}{% rgraph data %}"
        self.DATA = [10, 20, 35, 50]
        self.CHART_OPTIONS = {'chart.gutter.left': 30}

        self.PIE_JSCRIPT = "\n\n\n\n\n<script>\nwindow.onload = function() {\n\tvar pie1 = new RGraph.Pie('pie1', [10,20,35,50]);\n\t\n\tpie1.Set('chart.gutter.left', 30);\n\t\n\t\n\t\n\tpie1.Draw();\t\n\t\n}\n</script>\n"

    def testPieChart(self):
        """Tests that a template containing a pie chat tag renders the correct javascript."""
        t = Template(self.TEMPLATE)
        
        chart = PieChart(name="pie1", values=self.DATA, options=self.CHART_OPTIONS)
        
        html = t.render(Context({'chart': chart, 'request': HttpRequest()}))

        self.assertEqual(html, self.PIE_JSCRIPT)