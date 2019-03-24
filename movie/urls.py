from django.conf.urls import url
                       
from .views import *                   
                    
urlpatterns = [

    url(r'^all/$'                     ,MovieListAPIView.as_view()       ,name="movie_list"),
    url(r'^add-movie/$'                     ,add_movie       ,name="add_movie"),
    url(r'^home/$'                     ,home       ,name="home"),
    url(r'^detail/(?P<pk>\d+)/$'            ,movie_detail             ,name="movie_detail"),

    
]
