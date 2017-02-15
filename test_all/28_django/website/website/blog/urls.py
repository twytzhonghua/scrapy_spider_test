from django.conf.urls import include, url, patterns

urlpatterns = patterns('blog.views',
	    url(r'^index/$', 'index'),
		url(r'^time/$', 'time'),
		url(r'^foo/(\d{4})/(\w+)$', 'foo'), # w+ 至少1个字母或数字
		url(r'^bar/(?P<id>\d{4})/(?P<name>\w+)/$', 'bar'),
	)