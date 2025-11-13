from django.urls import path
from .views import VisitorGroup , Place


urlpatterns = [
   path('step1/',VisitorGroup.as_view(),name='VisitorGroup'),
   path('step2/',Place.as_view(),name='Place')

]