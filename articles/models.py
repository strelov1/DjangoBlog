from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    create_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('-create_at', )


