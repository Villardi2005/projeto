from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastroaluno'),
    path('saldoacumulado', views.saldoacumulado, name='saldoacumulado'),
    path('chat', views.chat, name='chat'),
    path('recompensas', views.recompensas, name='recompensas'),
    #path('cadastroaluno', views.cadastro, name='cadastroaluno'),
    #path('cadastroprofessor', views.cadastroprofessor, name='cadastroprofessor'),
    #path('cadastroresponsavel', views.cadastroresponsavel, name='cadastroresponsavel'),
    path('login', views.login, name='login'),
    # path('redireciona/', views.redireciona_usuario, name='redireciona_usuario'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    #path('painel-responsavel/', views.painel_responsavel, name='painel_responsavel'),
    path('painel-professor/', views.painel_professor, name='painel_professor'),
    path('metas', views.metas, name='metas'),
    path('professor_turmas',views.professor_turmas, name='professor_turmas'),
    path('professor_relatorios',views.professor_relatorios, name='professor_relatorios'),
    path('professor_mensagens',views.professor_mensagens, name='professor_mensagens'),
    # path('admin/', admin.site.urls),
    # #path("__reload__/", include("django_browser_reload.urls")),
]

