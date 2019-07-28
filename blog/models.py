from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def summary(self):
        return self.body[:200]+'...'

# Create your models here.
#add the blog app to the settings
#create migration
#migrate
#add to admin
