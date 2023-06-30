from django.db import models

import random
import string


class Url(models.Model):
    class Meta:
        unique_together = ("original_url", "short_path")

    original_url = models.URLField()
    short_path = models.CharField(max_length=8, db_index=True, default='')
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_path:
            while True:
                self.short_path = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                if not Url.objects.filter(short_path=self.short_path).exists():
                    break
        super().save(*args, **kwargs)
