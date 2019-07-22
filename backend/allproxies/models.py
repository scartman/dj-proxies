from django.db import models

# Create your models here.
class Proxy(models.Model):
    ip = models.CharField(max_length = 16)
    port = models.IntegerField()
    connection_type = models.CharField(max_length=16)
    anonymity = models.BooleanField(default=False)
    city = models.ForeignKey('City', on_delete=False)
    origin_ip = models.CharField(max_length=16, null=True, blank=True)
    passed = models.FloatField(null=True, blank=True)
    no_captcha = models.FloatField(null=True, blank=True)
    proxy_list = models.ForeignKey('ProxyList', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip

    @property
    def formeted(self):
        return '{}://{}:{}'.format(self.connection_type, self.ip, self.port)


class ProxyList(models.Model):
    proxy_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Region(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    region = models.ForeignKey('Region', on_delete=False, null=True, blank=True)

    def __str__(self):
        return self.name
