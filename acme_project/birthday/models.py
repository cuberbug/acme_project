from django.db import models
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse

# Импортируется функция-валидатор.
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20,
    )
    birthday = models.DateField(
        'Дата рождения', validators=(real_age,)
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='birthdays_images',
        blank=True,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})
