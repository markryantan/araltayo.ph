from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from worksheets.models import Material

def get_index(request):
	
	worksheets = Material.objects.filter(type=Material.WORKSHEET).order_by('-updated', '-created')
	
	return render_to_response('index.html', {
		'worksheets': worksheets,
	})
