from django.urls import path
from .views import AllSmartphones,DetailPhone,Personroot,Getall,URLshorten
from rest_framework import routers
#from .views import SmartphonePage, SmartphoneCreate,SmartPhoneRUD

router= routers.SimpleRouter()
router.register('detail',Getall, basename='getall')

urlpatterns= router.urls
urlpatterns += [
    # path('detail', AllSmartphones, name = 'allsmarts' ),
    # path('detail/<int:pk>', DetailPhone, name = 'detail' ),
    path('person/', Personroot, name='personroot'),
    path('service/', URLshorten, name='urlshort'),
#     path('',SmartphonePage.as_view(), name='smatphonepage'),
#     path('create/',SmartphoneCreate.as_view(), name='smatphonecreate'),
#     path('rud/<int:pk>', SmartPhoneRUD.as_view(), name='smatphoneRUD'),
]