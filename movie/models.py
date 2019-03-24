from django.db import models
from datetime import datetime
import re
import os


# to set the path to save the images
def movie_directory_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'movie/'+re.sub('[-:. ]','',str(datetime.today()))+file_extension

class Movie(models.Model):
    movie_image = models.ImageField(upload_to=movie_directory_path ,null=True, blank=True)
    movie_title = models.CharField(max_length = 50, null = False, blank = False)
    user_city = models.CharField(max_length = 50, null = False, blank = False)
    user_country = models.CharField(max_length = 50, null = False, blank = False)
    user_producer = models.CharField(max_length = 50, null = False, blank = False)
    username = models.CharField(max_length = 50, null = False, blank = False)