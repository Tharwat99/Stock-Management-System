from django.contrib import admin
from django.urls import path, include
from StockManager import views
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
#admin.site.enable_nav_sidebar = False

admin.site.index_title = _('My Index Title')
admin.site.site_header = _('My Site Administration')
admin.site.site_title  = _('My Site Management')
urlpatterns = i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += i18n_patterns(
    path('',views.stocks,name='list'),   
    path('history/',views.stock_history,name='history'),
    path('add_item/',views.add_item,name='add_item'),
    path('detail/<str:pk>/',views.detail_item,name='detail'),
    path('update/<str:pk>/',views.update_item,name='update'),
    path('delete/<str:pk>/',views.delete_item,name='delete'),
    path('issue/<str:pk>/',views.issue_item,name='issue'),
    path('receive/<str:pk>/',views.receive_item,name='receive'),
    path('categories/',views.categories,name='categories'),
    path('add_cat/',views.add_cat,name='add_cat'),
    path('accounts/',include('allauth.urls')),
    path('admin/', admin.site.urls),
    prefix_default_language=False
)
#path('accounts/', include('registration.backends.one_step.urls')),
