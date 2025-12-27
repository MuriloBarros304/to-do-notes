from django.db import models
from django.contrib.auth.models import User


class NoteQuerySet(models.QuerySet):
    def for_user(self, user: User):
        return self.filter(user=user)


class Note(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    body = models.TextField(verbose_name="Conteúdo", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    objects = NoteQuerySet.as_manager()

    def __str__(self) -> str:
        return self.title
