from django.conf.urls import include, url, patterns

urlpatterns = patterns('blog.views',
	    url(r'^index/$', 'index'),
		url(r'^time/$', 'time'),
	)