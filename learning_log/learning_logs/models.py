from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    '''Something Specific learned about a topic'''
    topic = models.ForeignKey(to=Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'     #verbose_name_plural: This attribute specifies the plural name for the object in the Django admin interface. By default, Django will create a plural name by appending an 's' to the model's name. However, in this case, you've explicitly set it to 'entries'. So, when you view the model in the Django admin interface, it will be displayed as 'entries' instead of the default 'Entrys'

    def __str__(self):
        return self.text[:50]+'....'