from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mywebserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
	url(r'^smdeals', 'myapp.views.index', name='index'),
    
    url(r'^superuser', 'myapp.views.superuser', name='superuser'),
    url(r'^addContest', 'myapp.views.addContest', name='addContest'),
    url(r'^deleteContest', 'myapp.views.deleteContest', name='deleteContest'),
    url(r'^checkContestName', 'myapp.views.checkContestName', name='checkContestName'),

    #------------Home---------------#
    
    url(r'^$', 'myapp.views.home', name='home'),
    url(r'^registration', 'myapp.views.registration', name='registration'),
    url(r'^checkUserName', 'myapp.views.checkUserName', name='checkUserName'),
    url(r'^regisuccess', 'myapp.views.regisuccess', name='regisuccess'),

    #---------Login----------#
    
    url(r'^loginform', 'myapp.views.loginform', name='loginform'),
    url(r'^loginvalidate', 'myapp.views.loginvalidate', name='loginvalidate'),
    #------------Contestant Home------------#

    url(r'^contestanthome', 'myapp.views.contestanthome', name='contestanthome'),
    #url(r'^submissions', 'myapp.views.submissions', name='submissions'),

    #------------TestAdmin Home------------#
   
    url(r'^testadminhome', 'myapp.views.testadminhome', name='testadminhome'),
    url(r'^puppetrun', 'myapp.views.puppetrun', name='puppetrun'),
    url(r'^puppetstop', 'myapp.views.puppetstop', name='puppetstop'),
    url(r'^deactivateuser', 'myapp.views.deactivateuser', name='deactivateuser'),
    
    #------------TestCreator Home------------#

    url(r'^testcreatorhome$', 'myapp.views.testcreatorhome', name='testcreatorhome'),
    url(r'^createquestionpaper', 'myapp.views.createquestionpaper', name='createquestionpaper'),

    #------------ParticipantApprover Home------------#

    url(r'^participantapproverhome', 'myapp.views.participantapproverhome', name='participantapproverhome'),
    url(r'^approve', 'myapp.views.approve', name='approve'),
)
