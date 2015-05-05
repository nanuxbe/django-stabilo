import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from stabilo.models import Category, Keyword

def keywords_for_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    keywords = category.keywords.values_list('keyword', flat=True)
    return HttpResponse(json.dumps(list(keywords)), content_type='application/json')

def all_keywords(request):
    return HttpResponse(
        json.dumps(list(Keyword.objects.all().values_list('keyword', flat=True))),
        content_type='application/json'
    )
