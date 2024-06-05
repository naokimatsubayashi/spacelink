from django.db import models

class Advertiser(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    logo = models.ImageField(upload_to='images/', null=True, blank=True)  # ロゴフィールドの追加

class AdSpaceProvider(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.EmailField()

class Ad(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    advertiser = models.ForeignKey('Advertiser', on_delete=models.CASCADE)
    ad_space_provider = models.ForeignKey('AdSpaceProvider', on_delete=models.CASCADE)
    url = models.URLField()
    qr_code = models.ImageField(upload_to='qrcodes/')

    def __str__(self):
        return f"Ad {self.id} for {self.advertiser}"

class Consumer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    ad = models.ForeignKey(Ad, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name