from django.conf.urls import url

from stabilo.views import keywords_for_category, all_keywords

urlpatterns = [
    url(r'^category/(?P<slug>\w+)/keywords/$',
        view=keywords_for_category,
        name='stabilo-keywords-for-category'),
    url(r'^keywords/$',
        view=all_keywords,
        name='stabilo-all-keywords')
]
