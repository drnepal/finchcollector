from django.urls import path
from . import views

# urlpatterns = [
#     # using an empty string here makes this our root route
#     # views.home refers to a view that renders a file
#     # the name='home' kwarg gives the route a name
#     # naming routes is optional, but best practices
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     # paths for finchs
#     path('finchs/', views.finchs_index, name='index'),
#     path('finchs/<int:finch_id>/', views.finchs_detail, name='detail'),
# ]
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finchs/', views.finchs_index, name='index'),
  path('finchs/<int:finch_id>/', views.finchs_detail, name='detail'),
  # new route used to show a form and create a finch
  path('finchs/create/', views.FinchCreate.as_view(), name='finchs_create'),
]
