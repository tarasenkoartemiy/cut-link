from cut_link.celery_app import app
from django.core.cache import cache
from .models import Url


@app.task
def update_db_and_clean_cache():
    queryset = Url.objects.all()
    for obj in queryset:
        new_clicks = cache.get(obj.short_path, None)
        if new_clicks:
            obj.clicks += new_clicks
    Url.objects.bulk_update(queryset, ["clicks"])
    cache.clear()


@app.task
def remove_unused_links():
    Url.objects.filter(clicks__lt=10).delete()
