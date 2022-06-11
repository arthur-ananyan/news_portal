from django.db import models
from django.contrib.auth.models import User


class NewsSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_portal_name = models.CharField(max_length=100)
    news_portal_url = models.URLField()
    update_date = models.DateTimeField()

    def __str__(self):
        return self.news_portal_name

