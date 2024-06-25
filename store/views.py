from django.shortcuts import render,redirect

# Create your views here.
def about(request):
    return render(request,'about.html')
def account(request):
    return render(request,'account.html')
def bamboo_craft(request):
    return render(request,'bamboo-craft.html')
def blank(request):
    return render(request,'blank.html')
def block_printed_bag(request):
    return render(request,'block-printed-bag.html')
def blog(request):
    return render(request,'blog.html')
def blog_detail(request):
    return render(request,'blog-detail.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def compare(request):
    return render(request,'compare.html')
def contact(request):
    return render(request,'contact.html')
def forgot_password(request):
    return render(request,'forgot-password.html')
def forum(request):
    return render(request,'forum.html')
def forum_detail(request):
    return render(request,'forum-detail.html')
def index(request):
    return render(request,'index.html')
def jute_crafts(request):
    return render(request,'jute-crafts.html')
def my_account(request):
    return render(request,'my-account.html')
def my_account_order(request):
    return render(request,'my-account-order.html')
def policy(request):
    return render(request,'policy.html')
def product_detail(request):
    return render(request,'product-detail.html')
def stone_carving(request):
    return render(request,'stone-carving.html')
def terracotta(request):
    return render(request,'terracotta.html')
def wishlist(request):
    return render(request,'wishlist.html')
def wooden_craft(request):
    return render(request,'wooden-craft.html')
def zari_zardozi(request):
    return render(request,'zari-zardozi.html')
def home(request):
    return redirect('index')





