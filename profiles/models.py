from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	MANAGER = 'Manager'
	MEMBER = 'Member'
	ROLE_CHOICES = (
		(MANAGER, 'Manager'),
		(MEMBER, 'Member'),
	)
	roles = models.CharField(choices=ROLE_CHOICES, default=MEMBER, max_length=7)


class App(models.Model):
	app_full_name = models.TextField(blank=True, null=True)
	app_name = models.TextField(blank=True, null=True)
	app_id = models.TextField(blank=True, null=True)
	app_img = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.app_id


class InstallDetails(models.Model):
	date = models.DateField(blank=True, null=True)
	package_name = models.TextField(blank=True, null=True)
	carrier = models.TextField(blank=True, null=True)
	daily_device_installs = models.IntegerField(blank=True, null=True)
	active_device_installs = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return "{}--{}--{}--{}".format(str(self.date), self.package_name, self.carrier, self.daily_device_installs)

