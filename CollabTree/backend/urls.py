from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = "index"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('profile/<int:id>', views.profile, name = 'profile'),
    path('assign_user/<int:id>/<int:proj_id>', views.assign_user, name = 'assign_user'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('otp_verification/', views.otp_verification, name="otp_verification"),
    path('blogs/', views.blog, name="blogs"),
    path('my_blogs/', views.my_blogs, name="my_blogs"),
    path('new_blog',views.new_blog, name="new_blog"),
    path('my_projects',views.my_projects, name='my_projects'),
    path('project_form',views.project_form, name='project_form'),
    path('view_user/<int:id>/<int:proj_id>',views.view_user,name='view_user'),
    path('mark_complete/<int:user_id>/<int:project_id>', views.mark_complete, name='mark_complete'),
    path('view_project/<int:proj_id>',views.view_project, name='view_project'),
    path('view_blog/<int:blog_id>', views.view_blog, name='view_blog'),
    path('like_blog/<int:blog_id>', views.like_blog, name="like_blog"),
    path('dislike_blog/<int:blog_id>', views.dislike_blog, name="dislike_blog"),
    path('delete_blog/<int:blog_id>', views.delete_blog, name = "delete_blog"),
    path('edit_blog/<int:blog_id>', views.edit_blog, name="edit_blog"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)