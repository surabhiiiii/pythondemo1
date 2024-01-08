from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    # path('details',views.details)
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')

]