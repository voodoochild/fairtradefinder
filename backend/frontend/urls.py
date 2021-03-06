from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url('locations/', 'frontend.views.locationList'),
	url('location/(?P<location_id>\d+)', 'frontend.views.locationView'),
	url('products/', 'frontend.views.productList'),
	url('product/(?P<product_id>\d+)', 'frontend.views.productView'),
	url('', 'frontend.views.homePage'),
)
