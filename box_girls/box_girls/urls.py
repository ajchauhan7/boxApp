from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views
from .views import redocs
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

schema_view = get_swagger_view(title='API Docs')

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-docs/', schema_view),

    url(r'^redocs/$', redocs),

    url(r'^api/rest-auth/', include('rest_auth.urls', namespace='rest_auth')),

    # url(r'^api/', include('agents.urls', namespace='agents')),
    url(r'^api/', include('attendance.urls')),
    url(r'^api/', include('category.urls')),
    url(r'^api/', include('notification.urls')),
    url(r'^api/', include('report_system.urls')),
    url(r'^api/', include('schedule_and_calendar.urls')),
    url(r'^api/', include('user_system.urls')),

    #auth urls
    url(r'^', include('login.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
