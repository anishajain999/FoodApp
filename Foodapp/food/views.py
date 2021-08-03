from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Class-based
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

# # function-Based Views for index
# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {
#         'item_list':item_list,
#     }
#     return render(request, 'food/index.html', context)



# Class-Based Views for index
class IndexClassView(ListView):
    model=Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'



def item(request):
    return HttpResponse("<h2> This is an item view </h2>")

# # function-Based Views for detail
# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item':item,
#     }
#     return render(request, 'food/detail.html', context)


# Class-Based Views for detail
class FoodDetail(DetailView):
    model = Item
    template_name = "food/detail.html"

# function-Based view for create item
def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    
    return render(request, 'food/item_form.html', {'form':form})

# this is class-based view for create item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_img']
    template_name = 'food/item_form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        
        return super().form_valid(form)


def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, 'food/item_form.html', {'form':form, 'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method=="POST":
        item.delete()
        return redirect("food:index")

    return render(request, 'food/delete_item.html', {'item':item})