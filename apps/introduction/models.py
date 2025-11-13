from django.db import models

#-----------------------------------------------------------------------------------------
class Visitor_Group(models.Model):
    code = models.CharField(max_length=50 , unique=True  ,help_text='کد یکتا برای گروه',verbose_name='کد ')
    TITLE_CHOICES = [
        ('1' , 'عمومی'),
        ('2' , 'گروهی'),
        ('3' , 'دانشجویی'),
        ('4' , 'خارجی'),
    ]
    title = models.CharField(max_length=10,choices=TITLE_CHOICES,default='1',verbose_name='عنوان')

    def __str__(self):
        return  f'{self.code}\t {self.title}'

#------------------------------------------------------------------------------------------
class Place (models.Model):
    code = models.CharField(max_length=50 , unique=True , help_text='کد یکتا برای مکان',verbose_name='کد')
    title = models.CharField(max_length=50 , help_text='نام مکان',verbose_name='عنوان')
    main_image = models.ImageField(upload_to='places/main_image', blank=True ,null=True,verbose_name='تصویر ')
    visiting_hours = models.CharField(max_length=255 , blank=True , null=True , verbose_name='ساعت بازدید')
    OPEN_DAY_CHOISES = [
        ('sat', 'شنبه'),
        ('sun', 'یک‌شنبه'),
        ('mon', 'دوشنبه'),
        ('tue', 'سه‌شنبه'),
        ('wed', 'چهارشنبه'),
        ('thu', 'پنج‌شنبه'),
        ('fri', 'جمعه'),
    ]
    open_days = models.CharField(max_length=100, choices=OPEN_DAY_CHOISES ,blank=True,null=True,verbose_name='روز بازدید')
    regulations = models.TextField(blank=True , null=True ,help_text='فوانین و مقررات' ,verbose_name='قوانین')
    more_info = models.TextField(blank=True,null=True,help_text='اطلاعت بیشتر',verbose_name='اطلاعات بیشتر')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت مکان')
    
    def __str__(self):
        return f'{self.code}\t {self.title}\t {self.visiting_hours}\t'
    
#------------------------------------------------------------------------------------------
class Ticket_Price(models.Model):
    code = models.CharField(max_length=50 , unique=True , help_text='کد یکتا برای بلیط',verbose_name='کد')
    visitor_group = models.ForeignKey(Visitor_Group,on_delete=models.CASCADE , related_name='ticket_price')
    place = models.ForeignKey(Place , on_delete=models.CASCADE,related_name='ticket_price')
    price = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return f"{self.code}\t {self.visitor_group}\t {self.place}\t {self.price}"
    
#-------------------------------------------------------------------------------------------
