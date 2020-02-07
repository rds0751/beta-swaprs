from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from registr.views import activate
from registr.views import register, login1, change_password_done, reset_done,update,change_password_complete


urlpatterns = [
	re_path(r'^page/$',
		update,
		),
		
	re_path(r'^activate/(?P<activation_key>\w+)/$',
		activate,
		name='registration_activate'),

	re_path(r'^oauth/', include('social_django.urls', namespace='social')),
		
	re_path(r'^login/$',
		login1,
		name='auth_login'),
		
	re_path(r'^logout/$',
		auth_views.LogoutView,
		{'next_page':'/'},
		name='auth_logout'),
			
	re_path(r'^password/change/$', 
		auth_views.PasswordChangeView,
		{'post_change_redirect' : '/accounts/password_change/done/','template_name': 'registration/password_change.html','from_email':'trade@ywaga.com'},
		name='auth_password_change'),

	re_path(r'^password_change/done',                           
		change_password_done 
		),

	re_path(r'^password/reset/$',
		auth_views.PasswordResetView,
		{'post_reset_redirect' : '/accounts/password/reset/done/','template_name': 'registration/reset.html'},
		name='auth_password_reset'),

	re_path(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
		auth_views.PasswordResetConfirmView, {'template_name': 'registration/registration_form.html'},                                                      
		name='auth_password_reset_confirm'),

	re_path(r'^password/reset/complete/$',
		change_password_complete,		
		name='auth_password_reset_complete'),

	re_path(r'^password/reset/done/$',
		reset_done,
	),

	re_path(r'^register/$',
		register,
		name='registration_register'),
		
	re_path(r'^register/complete/$',
		TemplateView.as_view(template_name='registration/registration_complete.html'),
		name='registration_complete'),
	]