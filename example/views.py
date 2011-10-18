# Create your views here.
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from rgraph.chart import PieChart

def testCharts(request):
    """Test drawing various types of graph."""
    data = [10, 24, 15, 82]
    options = {'chart.gutter.left': 30}
    
    pie = PieChart("pie1", data, options)
    
    return render_to_response('pie_example.html', {'chart': pie}, context_instance=RequestContext(request))