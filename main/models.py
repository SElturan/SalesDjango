from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class User(models.Model):
    nickname = models.CharField(max_length=50,verbose_name='Никнейм')
    user_id = models.BigIntegerField(unique=True, verbose_name='ID пользователя')
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    last_name = models.CharField(max_length=50,verbose_name='Фамилия')
    phone_number = models.CharField(max_length=100, unique=True, verbose_name='Номер телефона')
    phone_number2 = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='Номер телефона2')
    age = models.IntegerField(verbose_name='Возраст')
    date = models.CharField(max_length=50,verbose_name='Дата')
    points = models.IntegerField(null=True, blank=True, verbose_name='Баллы')
    is_admin = models.BooleanField(default=False, verbose_name='Админ')
    age_check = models.BooleanField(default=False, verbose_name='Возраст подтвержден')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    


    def __str__(self):
        if self.nickname:
            return f'{self.nickname}\n{self.phone_number}'
        else:
            return f'{self.user_id}'


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class CodeGenerate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_code', verbose_name='Пользователь')
    code = models.BigIntegerField(unique=True, verbose_name='Сгенерированный код')
    summ = models.IntegerField(null=True, blank=True, verbose_name='Сумма товара')
    discount = models.IntegerField(default=2,verbose_name='Процент скидки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата генерации кода')
    confirmed_presence = models.BooleanField(default=False, verbose_name='Подтверждено личное присутствие')

    def __str__(self) -> str:
        return self.user.phone_number
    
    def save(self, *args, **kwargs):
        if self.user and self.summ is not None and self.confirmed_presence:
            discount_value = (self.summ * self.discount) / 100
            user_points = discount_value
            if self.user.points is None:
                self.user.points = user_points
            else:
                self.user.points += user_points
            self.user.save()
        super().save(*args, **kwargs)





    
    class Meta:
        verbose_name = 'Код пользователей'
        verbose_name_plural = 'Коды пользователей'




class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name='Филиал')
    location = models.CharField(max_length=100, verbose_name='Локация')
    opening_time = models.TimeField(verbose_name='Время открытия', default='08:00')
    closing_time = models.TimeField(verbose_name='Время закрытия', default='21:00')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'



class RegularUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    summ = models.IntegerField(null=True, default=0,blank=True, verbose_name='Сумма товара')
    visits = models.IntegerField(null=True,default=0, blank=True,verbose_name='Посещение')
    discount = models.IntegerField(null=True, blank=True,default=2,verbose_name='Процент скидки')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')


    def __str__(self):
        return self.user.phone_number
    

    class Meta:
        verbose_name = 'Постоянный клиент'
        verbose_name_plural = 'Постоянные клиенты'
        unique_together = ('user',)
        

@receiver(pre_save, sender=RegularUser)
def update_summ(sender, instance, **kwargs):
    if instance.pk:  # Проверяем, что объект уже сохранен (не новый)
        try:
            old_instance = RegularUser.objects.get(pk=instance.pk)  # Получаем старый экземпляр из базы данных
            if instance.summ is not None:  # Проверяем, что новая сумма не None
                instance.summ += old_instance.summ  # Прибавляем новую сумму к старой сумме
        except RegularUser.DoesNotExist:
            pass
