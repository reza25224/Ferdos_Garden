from django.db import models

#-----------------------------------------------------------------------------------------
class Visitor_group(models.Model):
    code = models.PositiveIntegerField(max_length=10 ,help_text='کد یکتا برای گروه',verbose_name='کد ')
    TITLE_CHOICES = [
        ('1' , 'عمومی'),
        ('2' , 'گروهی'),
        ('3' , 'دانشجویی'),
        ('4' , 'خارجی'),
    ]
    title = models.CharField(max_length=10,choices=TITLE_CHOICES,default='1',verbose_name='عنوان')

    def __str__(self):
        return self.code + ' ' + self.title

#------------------------------------------------------------------------------------------
class Place (models.Model):
    code = models.CharField(max_length=50 , unique=True , help_text='کد یکتا برای مکان',verbose_name='کد')
    title = models.CharField(max_length=50 , help_text='نام مکان',verbose_name='عنوان')