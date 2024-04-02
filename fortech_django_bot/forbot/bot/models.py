from django.db import models


class User(models.Model):
    external_id = models.PositiveIntegerField(
        unique=True,
        verbose_name="ID пользователя в телеграме",
    )
    username = models.CharField(
        null=True,
        blank=False,
        verbose_name="юзернейм пользователя",
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name="Является ли администратором",
    )

    def __str__(self) -> str:
        return f"{self.external_id}: {self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Vacancy(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Requirement(models.Model):
    description = models.TextField(verbose_name="Требование")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Требование"
        verbose_name_plural = "Требования"


class Offer(models.Model):
    description = models.TextField(verbose_name="Предложение")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"


class TemplateText(models.Model):
    name = models.CharField(verbose_name="Название текстового шаблона")
    text = models.TextField(verbose_name="Текст шаблона")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Текстовый шаблон"
        verbose_name_plural = "Текстовые шаблоны"
