from django.db import models



class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")
	updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Yangilangan sana")

	class Meta:
		abstract = True


class Student(BaseModel):
	user_id = models.BigIntegerField(primary_key=True, null=False, verbose_name="Telegram ID raqami")
	referral = models.CharField(max_length=50, null=True, default=None, verbose_name="Referral", blank=True)
	full_name = models.CharField(max_length=255, null=False, verbose_name="F.I.SH")
	phone = models.CharField(max_length=50, default=None, null=True, verbose_name="Telefon", blank=True)
	username = models.CharField(max_length=150, null=True, default=None, verbose_name="TG username", blank=True)
	subscribed = models.ManyToManyField('Course', verbose_name="Botdan olgan kurslari", blank=True)
	offline_study = models.BooleanField(default=False, verbose_name="Offline o'qiydi")
	registered = models.BooleanField(default=False, verbose_name="Botda ro'yxatdan o'tgan")
	mediana = models.IntegerField(default=0, verbose_name="Mediana coin")
	blocked = models.BooleanField(default=False, verbose_name="Botni bloklagan")

	class Meta:
		db_table = 'students'
		verbose_name = 'Foydalanuvchi'
		verbose_name_plural = "Foydalanuvchilar"

	def __str__(self) -> str:
		return self.full_name


class Course(BaseModel):
	name = models.CharField(max_length=250, null=False, verbose_name="Kurs nomi")

	class Meta:
		db_table = 'courses'
		verbose_name = "Kurs"
		verbose_name_plural = "Kurslar"

	def __str__(self) -> str:
		return self.name
