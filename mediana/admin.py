import csv
import shortuuid

from redis import Redis

from django.contrib import admin
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Student, Course
from .utils import write_users_to_csv


r = Redis(
	host='redis-16500.c73.us-east-1-2.ec2.cloud.redislabs.com', 
	port=16500, 
	password='wz61H13hTzFDT6bBtAVY6AGowyOcUorS'
)

class StudentAdmin(admin.ModelAdmin):
	users_list = []
	list_per_page = 200
	list_display = ['full_name', 'username', 'phone', 'referral', 'offline_study', 'registered', 'blocked']
	search_fields = ['phone', 'username', 'full_name']
	list_filter = ['offline_study', 'subscribed', 'referral', 'created_at']

	actions = ["broadcast_func", "send_sms", "export_as_csv"]

	def export_as_csv(self, request, queryset):

		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])

		return response
	export_as_csv.short_description = "Foydalanuvchilar jadvalini yuklab olish"

	def broadcast_func(self, request, queryset):
		write_users_to_csv(queryset)
		password = shortuuid.ShortUUID().random(length=8)
		r.set('password', password)
		return redirect(f'https://t.me/mediana_center_bot?start=broadcast_{password}')
	broadcast_func.short_description = "Xabar Yuborish"

	def send_sms(self, request, queryset):
		StudentAdmin.users_list = queryset
		return redirect('send_sms')
	send_sms.short_description = "SMS Yuborish"


class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)

admin.site.site_header = "MEDIANA ADMIN"
admin.site.index_title = "Mediana Adminga xush kelibsiz!"
admin.site.unregister(Group)
