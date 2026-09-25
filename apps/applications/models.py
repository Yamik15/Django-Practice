from django.db import models
from apps.users.models import User

class Application(models.Model):
    STATUS_CHOICES = [ # Выборка статуса (1 значение - в базе, 2 значение - для фронта)
        ('new', 'New'),
        ('in_progress', 'Progress'),
        ('completed', 'Completed')
    ]
    
    PAYMENT_CHOICES = [ # Выборка способа платежа (1 значение - в базе, 2 значение - для фронта)
        ('cash', 'Cash'),
        ('transfer', 'Transfer')
    ]
    
    # Поля
    user = models.ForeignKey(User, on_delete=models.CASCADE) # пользователь, подавший заявку (1. on_delete - при удалении пользователя удаляются и все его заявки. 2. ForeignKey - связь "много к одному", один пользователь может иметь много заявок, каждая заявка принадлежит ровно одному пользователю)
    course = models.CharField(max_length=100) # название курса
    start_date = models.CharField(max_length=10) # дата начала
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES) # метод оплаты
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new') # статус заявки
    review = models.TextField(blank=True, null=True) # отзыв (1. blank=True - допускает пустое поле в формах. 2. null=True - допускает пустое поле в базе)
    created_at = models.DateTimeField(auto_now_add=True) # автоматическая простановка даты в момент создания записи (потом помогает в удобной сортировке через order_by("created_at"))
    
    class Meta:
        db_table = 'applications_application' # конкретное имя таблицы в бд
    
    def __str__(self):
        return f"{self.course} - {self.user.username}"