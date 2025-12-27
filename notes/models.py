from django.db import models


class Note(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    body = models.TextField(verbose_name="Conteúdo", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
