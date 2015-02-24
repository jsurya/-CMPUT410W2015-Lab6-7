from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
	# Regex
	# localhost:8000/bookmarks/
	url(r'^$', views.index, name ='index'),
	# localhost:8000/bookmarks/tags/
	url(r'^tags/$', views.tags, name = 'tags'),
	# localhost:8000/bookmarks/tags/<tag_name>/
	url(r'^tags/(?P<tag_name>\w+)/$', views.tag, name = 'tag'),
	url(r'^add_link/$', views.add_link, name = 'add_link'),
)