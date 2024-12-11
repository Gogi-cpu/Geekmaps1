
from django.urls import path, include
from . import views
from pagina.views import Objeto
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    #rutas pagina
    path('index', views.index, name='index'),
    path('contacto',views.contacto ,name='contacto'),
    path('nosotros',views.nosotros ,name='nosotros'),
    path('preguntas',views.preguntas ,name='preguntas'),
    path('servicios',views.servicios ,name='servicios'),
    path('servicios',views.servicios ,name='servicios'),
    path('inicio', views.inicio, name='inicio'),
    path('error', views.error, name='error'),
    path('login', views.login, name='login'),
    path('validar', views.validar, name='validar'),
    path('salir_error', views.salir_error, name='salir_error'),
    path('nosesion', views.nosesion, name='nosesion'),
    path('evento1',views.evento1,name='evento1'),
    path('evento2',views.evento2,name='evento2'),
    path('evento3',views.evento3,name='evento3'),
    path('evento4',views.evento4,name='evento4'),
    path('evento5',views.evento5,name='evento5'),
    path('evento6',views.evento6,name='evento6'),

    #rutas inventario
    path('inventarioadmin', views.inventarioadmin, name='inventarioadmin'),
    path('inventarioworker', views.inventarioworker, name='inventarioworker'),
    path('agregar',views.agregar,name='agregar'),
    path('volver_tabla',views.volver_tabla,name='volver_tabla'),
    path('cerrar',views.cerrar,name='cerrar'),
    path('editar',views.editar,name='editar'),

    path('producto_add',views.producto_add,name='producto_add'),
    path('producto_editar',views.producto_editar,name='producto_editar'),
    path('producto_edit/<str:key>',views.producto_edit,name='producto_edit'),
    path('producto_del/<str:producto_id>',views.producto_del,name='producto_del'),
    
    #rutas usuarios
    path('usuarioadmin',views.usuarioAdmi,name='usuarioadmin'),
    path('usuario_agregar',views.usuario_agregar,name='usuario_agregar'),
    path('usuario_add',views.usuario_add,name='usuario_add'),
    path('usuario_editar',views.usuario_editar,name='usuario_aditar'),
    path('usuario_edit/<str:key>',views.usuario_edit,name='usuario_edit'),
    path('usuario_del/<str:key>',views.usuario_del,name='usuario_del'),


    path('tabla/', views.tabla, name="tabla"), 
    
]   