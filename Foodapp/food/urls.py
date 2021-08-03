from django.views.generic.edit import CreateView
from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # /food/
    # path("", views.index,name="index"),  #Function-based view's url for index

    # Class-Based View's Url for index
    path("", views.IndexClassView.as_view(), name="index"),

    # /food/1
    # path("<int:item_id>/", views.detail,name="detail"),  for detail
    path("<int:pk>/", views.FoodDetail.as_view(),name="detail"),


    path("item/", views.item,name="item"),    

    # Add Item
    # path("add", views.create_item,name="create_item"),  for create Item
    path("add", views.CreateItem.as_view(), name="create_item"),

    # Updated Item
    path("update/<int:id>/", views.update_item,name="update_item"),
    # Delete Item
    path("delete/<int:id>/", views.delete_item,name="delete_item"),
]
