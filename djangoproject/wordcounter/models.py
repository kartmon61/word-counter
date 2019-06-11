from django.db import models

# Create your models here.

#objects 명시
objects = models.Manager()

class Blog(models.Model):
    #title에 char 200글자 저장할수 있는 공간 생성
    title = models.CharField(max_length=200) 
    #pub_date에 날짜와 시간을 저장하는 공간 생성
    pub_date = models.DateTimeField('date published') 
    #body에 텍스트 필드 공간 생성
    body = models.TextField()   
    
    #타이틀을 데이터베이스에게 보여준다.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]