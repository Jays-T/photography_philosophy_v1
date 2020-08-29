from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import AdminProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    all_category = Category.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name=query) | Q(category__friendly_name__contains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'all_category': all_category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    all_category = Category.objects.all()

    context = {
        'product': product,
        'all_category': all_category,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def products_admin_hub(request):
    """Display Admin Product Hub"""

    products = Product.objects.all()
    all_categories = Category.objects.all()
    categories = None
    form = AdminProductForm()

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners allowed here.')
        return redirect(reverse('home'))

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    template = 'products/products_hub.html'
    context = {
        'products': products,
        'all_categories': all_categories,
        'current_categories': categories,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """
    View for Admin to handle product CRUD functions
    Add a product to the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Oops, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AdminProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                                     Please check the form.')
    else:
        form = AdminProductForm()

    template = 'products/products_hub.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(request, 'Tsk tsk, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AdminProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                                     Please check the form.')
    else:
        form = AdminProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/products_hub.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
