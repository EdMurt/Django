from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin # Para interfaz admin
admin.autodiscover() #Para interfaz admin
from blog.views import PostList, PostDetail,PostCreate, PostUpdate, PostDelete# , AddCommentView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amazing_blog.views.home', name='home'),
    # url(r'^amazing_blog/', include('amazing_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), # Para interfaz admin

    url(r'^login/$','django.contrib.auth.views.login',{'template_name': 'blog/post_login.html'}, name="post_login"),
   	
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page': 'http://localhost:8000'}, name="post_logout"),

    url(r'^post/create/$', login_required(PostCreate.as_view()), name="post_create"),
    url(r'^post/(?P<pk>\d+)/edit$', login_required(PostUpdate.as_view()), name="post_update"),
    url(r'^post/(?P<pk>\d+)/delete$', login_required(PostDelete.as_view()), name="post_delete"),

    url(r'^post/(?P<pk>\d+)$', PostDetail.as_view(), name="post_detail"),
#    url(r'^post/(?P<pk>\d+)/addcomment$', AddCommentView.as_view(), name="post_comment"),
    url(r'^$',PostList.as_view(), name="post_list"), #Para interfaz vista IMPORTANTE


)

# urlpatterns = patterns ('blog.views',
#	url(r'^$',"post_list", )              Estas 3 lineas es para si tienes varias vista en el mismo archivo para no repetir blog.views

#)
