from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect  # 'redirect' fonksiyonunu içe aktarın
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required


def login_signup_view(request):
    login_form = AuthenticationForm(request, request.POST or None)
    signup_form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if 'login_submit' in request.POST and login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Giriş yapıldıktan sonra yönlendirme

        elif 'signup_submit' in request.POST and signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('dashboard')  # Kayıt olduktan sonra yönlendirme

    return render(request, 'login.html', {'login_form': login_form, 'signup_form': signup_form})

    


# Ana sayfa görünümü
def index(request):
    return render(request, 'index.html')

# Checkout sayfa görünümü
def checkout_view(request):
    return render(request, 'checkout.html')

# Cart sayfa görünümü
def cart_view(request):
    return render(request, 'cart.html')

# Login sayfa görünümü
def login_view(request):
    return render(request, 'login.html')


def account_view(request):
    # Kullanıcı bilgilerini alın
    user = request.user

    # Kullanıcının ilişkili siparişleri veya diğer verileri de alabilirsiniz.
    # Örnek olarak kullanıcının son siparişlerini alalım (varsayılan olarak bu kod çalışmayacaktır, ek sipariş modeline ihtiyacınız olacak).
    # recent_orders = user.orders.all()  # Eğer siparişleriniz için bir model kullanıyorsanız.

    context = {
        'user': user,
        # 'recent_orders': recent_orders,  # Kullanıcının son siparişleri.
        # Diğer kullanıcı bilgilerini veya verilerini ekleyebilirsiniz.
    }

    return render(request, 'account.html', context)

def shop_view(request):
    # Görünüm işlemleri burada yapılır
    return render(request, 'shop.html')

def product_details_view(request):
    # Görünüm işlemleri burada yapılır
    return render(request, 'product-details.html')

def blog_list_view(request):
    # Görünüm işlemleri burada yapılır
    return render(request, 'blog-list.html')

def blog_single_view(request):
    # Görünüm işlemleri burada yapılır
    return render(request, 'blog-single.html')

def contact_us_view(request):
    return render(request, 'contact-us.html')

# Özel 404 sayfa görünümü
def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def wishlist_view(request):
    # Wishlist verileri burada alınır veya hesaplanır
    wishlist = [...]  # Wishlist verilerini burada listeleyin
    return render(request, 'wishlist.html', {'wishlist': wishlist})
