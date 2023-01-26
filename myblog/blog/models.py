from django.db import models

class PostOn(models.Model):
    """данные о посте"""
    title = models.CharField("Заголовок записи", max_length=100)
    description = models.TextField("Текст записи")
    author = models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата публикации")
    image = models.ImageField("Изображение", upload_to='image/%Y')
    slug = models.SlugField(max_length=100, unique=True, null=True)
    class Meta:
        """Для имени модели в админке"""
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
    def __str__(self):
        return f"{self.title}, {self.author}"

class Comments(models.Model):
    """Комментарий"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=50)
    text_comments = models.TextField("Текст комментария", max_length=2000)
    post = models.ForeignKey(PostOn, verbose_name="Публикация", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.name}, {self.post}"


class Example_Models(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    posts = models.ForeignKey(PostOn, on_delete=models.CASCADE, verbose_name="Посты", null=True)
    # def get_absolute_url(self):
    #     return reverse()






