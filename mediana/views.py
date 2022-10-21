from django.shortcuts import render, redirect
from django.http import HttpRequest

from .admin import StudentAdmin



def admin_dashboard(request: HttpRequest):
	if request.user.is_superuser:
		template_name = 'admin_dashboard.html'
		return render(request=request, template_name=template_name)
	
	elif request.user.is_staff:
		template_name = 'stuff_dashboard.html'
		context = {
			'all_users': 666, 
			'active_users': 599, 
			'blocked_users': 67, 
			'today_users': 112
		}
		return render(request=request, template_name=template_name, context=context)

	else:
		return redirect('/admin/login')


def send_sms_view(request: HttpRequest):
	if request.method == 'GET':
		template_name = 'send_sms_form.html'
		return render(request, template_name)

	elif request.method == 'POST':
		template_name = 'done_sms.html'
		return render(request, template_name)
