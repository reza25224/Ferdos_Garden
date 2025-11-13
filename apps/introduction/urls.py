from django.urls import path
from .views import VisitorGroup , PlaceCreate,Placelist ,PlaceDetail,PlaceUpdate,PlaceDelete


urlpatterns = [
   path('step1/',VisitorGroup.as_view(),name='VisitorGroup'),
   path('add/',PlaceCreate.as_view(),name='PlaceCreate'),
   path('list/',Placelist.as_view(),name='Placelist'),
   path('detail/<int:pk>',PlaceDetail.as_view(),name='PlaceDetail'),
   path('update/<int:pk>',PlaceUpdate.as_view(),name='PlaceUpdate'),
   path('delete/<int:pk>',PlaceDelete.as_view(),name='PlaceDelete')
   

]