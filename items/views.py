from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Item
from .models import Category
from .forms import ItemForm

def items_page(request):
    items = Item.objects.all()
    return render(request, 'items/items.html', {'items': items})


def item_detail(request, item_id):
    selected_item = get_object_or_404(Item, pk=item_id)
    
    if request.method == 'POST':
        # Verarbeiten Sie das Löschen des Items hier, wenn ein POST-Antrag vorliegt
        selected_item.delete()
        return redirect('items_page')
    
    return render(request, 'items/item_detail.html', {'item': selected_item})



def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items_page')
    else:
        form = ItemForm()
    
    return render(request, 'items/item_create.html', {'form': form})

def items_category(request):
    categories = Category.objects.all()
    return render(request, 'items/category.html', {'categories': categories})


def category_contains(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items_in_category = Item.objects.filter(category=category)
    return render(request, 'items/contains.html', {'category': category, 'items_in_category': items_in_category})


def test(request):
    items = Item.objects.all()
    return render(request, 'items/test.html', {'items': items})