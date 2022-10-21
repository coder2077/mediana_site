from django.shortcuts import render, redirect
from django.http import HttpRequest

from datetime import datetime

from .models import Student



def admin_dashboard(request: HttpRequest):
	if request.user.is_superuser:
		template_name = 'admin_dashboard.html'
		return render(request=request, template_name=template_name)

	elif request.user.is_staff:
		template_name = 'stuff_dashboard.html'
		today = datetime.now().date()
		all_users = Student.objects.all().count()
		for user in Student.objects.all():	
			print(f"{user.full_name}: {user.created_at}")
		active_users = Student.objects.filter(blocked=False).count()
		blocked_users = Student.objects.filter(blocked=True).count()
		today_users = Student.objects.filter(created_at__date=today).count()
		context = {
			'all_users': all_users, 
			'active_users': active_users, 
			'blocked_users': blocked_users, 
			'today_users': today_users
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


def home(request: HttpRequest):
	return redirect('/admin/')
