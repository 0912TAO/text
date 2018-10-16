from django.db import models




class Article(models.Model):
    id =models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,verbose_name='用户名称')
    password=models.CharField(max_length=255,verbose_name="用户密码")
    age=models.IntegerField(default=18,verbose_name='用户年龄')
    nickname=models.CharField(max_length=255,null=True,blank=True,verbose_name='用户昵称')
    email=models.EmailField(max_length=255,verbose_name='用户邮箱')
    #默认是0表示男生，1表示女生
    gender=models.BooleanField(default=0)

    class Meta:
        ordering = ["id"]


    def __str__(self):
        return self.username
