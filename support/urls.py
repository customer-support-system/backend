
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
       title="customer_support_system",
       default_version='v1',
       description="it shows  endpoints for different models",
       terms_of_service="",
       contact=openapi.Contact(email=""),
       license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # url="http://localhost:8000/swagger.json"

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portal/',include("portal.urls")),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #  path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #   path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json-with-slash'), 

]
