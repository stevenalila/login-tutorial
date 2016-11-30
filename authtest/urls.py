from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from log.forms import LoginForm
urlpatterns = [
    # Examples:
    # url(r'^$', 'authtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
]
