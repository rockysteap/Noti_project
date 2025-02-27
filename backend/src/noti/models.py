from django.db import models


class NotiOwner(models.Model):
    telegram_id = models.CharField(max_length=12)


class Contact(models.Model):
    title = models.CharField(max_length=40)
    phone = models.CharField(max_length=20, default=None)
    telegram_id = models.CharField(max_length=12, default=None)
    telegram_username = models.CharField(max_length=20, default=None)


class NotiType(models.Model):
    title = models.CharField(max_length=20)


class Notification(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(NotiOwner, on_delete=models.CASCADE)
    noti_type = models.ForeignKey(NotiType, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    weekday = models.IntegerField(null=True)
    periodic = models.BooleanField(default=False)
