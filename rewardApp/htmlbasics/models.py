from django.db import models

# Create your models here.
class AdminModel(models.Model):

    APP_CATEGORY_ENTERTAINMENT='E'
    APP_CATEGORY_NEWS='N'
    APP_CATEGORY_SPORTS='S'

    SUB_CATEGORY_SOCIAL='SOC'
    SUB_CATEGORY_KNOWLEDGE='KNO'
    SUB_CATEGORY_FAN ='FAN'
    
    APP_CATEGORY_CHOICES=[
        (APP_CATEGORY_ENTERTAINMENT,'ENTERTAINMENT'),
        (APP_CATEGORY_NEWS,'NEWS'),
        (APP_CATEGORY_SPORTS,'SPORTS')
    ]

    SUB_CATEGORY_CHOICES=[
        (SUB_CATEGORY_SOCIAL,'SOCIAL MEDIA'),
        (SUB_CATEGORY_KNOWLEDGE,'KNOWLEDGE'),
        (SUB_CATEGORY_FAN,'FAN APP')
    ]

    app_name=models.CharField(max_length=256,default='')
    link=models.URLField(default='')
    points=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=3,choices=APP_CATEGORY_CHOICES,default=APP_CATEGORY_ENTERTAINMENT)
    sub_category=models.CharField(max_length=3,choices=SUB_CATEGORY_CHOICES,default=SUB_CATEGORY_SOCIAL)