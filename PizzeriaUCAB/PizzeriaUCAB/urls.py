from django.contrib import admin
from django.urls import path, include

from .views import (
	Ingredient,
	Pizza,
	Order
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredient/', Ingredient.as_view(), name='ingredient'),
    path('pizza/', Pizza.as_view(), name='pizza'),
    path('order/', Order.as_view(), name='order'),

    path('', include('store.urls')),
    path('reports/', Ingredient.as_view(), name='ingredient'),
    path('agregar/', include('store.urls'))
]
