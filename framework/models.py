from django.db import models


class FrameworkModel(models.Model):
    name = models.CharField(max_length=25, verbose_name="Имя фреймворка")
    language = models.CharField(max_length=50, verbose_name="Язык фреймворка")

    class Meta:
        verbose_name = "Фреймворк"
        verbose_name_plural = "Фреймворки"
        indexes = [
            models.Index(fields=['language'])
        ]

    def __str__(self):
        return self.name
