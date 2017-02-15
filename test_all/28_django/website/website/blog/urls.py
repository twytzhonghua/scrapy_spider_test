from django.conf.urls import include, url, patterns

urlpatterns = patterns('blog.views',
	    url(r'^index/$', 'index'),
		url(r'^time/$', 'time'),
		url(r'^foo/(\d{4})/(\w+)$', 'foo'), # w+ ����1����ĸ������
		url(r'^bar/(?P<id>\d{4})/(?P<name>\w+)/$', 'bar'),
	)