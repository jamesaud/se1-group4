# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/index.html'), name='home'),
    url(r'^login/$', TemplateView.as_view(template_name='pages/index1.html'), name='login'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    url(r'^postJob/$', TemplateView.as_view(template_name='job/postJob.html'), name='postJob'),
    url(r'^test/$', TemplateView.as_view(template_name='test.html'), name='test'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('jmatcher.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^job/', include('jmatcher.job.urls', namespace='job')),
    url(r'^students/', include('jmatcher.students.urls', namespace='students')),
    url(r'^employers/', include('jmatcher.employers.urls', namespace='employers')),

    url(r'^messages/', include('django_messages.urls')),
    # Your stuff: custom urls includes go here
    url(r'^posts/', include('jmatcher.posts.urls', namespace='posts')),
    url(r'^search/', include('jmatcher.search.urls', namespace='search'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
            ]


