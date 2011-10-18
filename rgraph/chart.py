class Chart(object):
    """Basic modelt o hold information about a chart."""

    def __init__(self, name, values, options):
        """An instance of a chart, holds all the data for the chart & it's config items"""
        self.name = name
        self.values = values
        self.options = options
        
        self.js = ["RGraph.common.core.js", "RGraph.common.tooltips.js", "RGraph.common.effects.js"]

class PieChart(Chart):
    """Create a Pie Chart"""
    def __init__(self, name, values, options):
        super(PieChart, self).__init__(name, values, options)

        self.template = "django_rgraph/pie.html"
        
        self.js.append("RGraph.pie.js")
        
class BarChart(Chart):
    """Create a bar chat"""
    def __init__(self, name, values, options):
        super(BarChart, self).__init__(name, values, options)
        self.template = "django_rgraph/bar.html"
        