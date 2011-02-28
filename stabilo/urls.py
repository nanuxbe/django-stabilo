from django.conf.urls.defaults import *

urlpatterns = patterns('stabilo.views',
    url(r'^category/(?P<slug>\w+)/keywords/$',
        view='keywords_for_category',
        name='stabilo-keywords-for-category'),
    url(r'^keywords/$',
        view='all_keywords',
        name='stabilo-all-keywords')
)
