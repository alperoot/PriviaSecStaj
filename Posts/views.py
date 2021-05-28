from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserForm, ToggleForm, PostUpdateForm
import datetime


# Create your views here.

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'basliklar/detail.html', {'post': post})
    # ana sayfada gönderi listesinde bir linke basıldığında sayfaya doğru postu döndüren bir fonksiyon

def current_user(request):
    return request.user

def toggle_thread(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.original_poster = request.post.username
            instance.date_posted = request.post.date_posted
            instance.post_icerik = request.post.post_icerik
            instance.comments_number = request.post.comments_number
            instance.post_title = request.request.post.post_title
            if instance.comment_status == 1:
                instance.comment_status = 0
            else:
                instance.comment_status = 1
            # gönderiyle alakalı her şeyi aynı tutup, status fieldını 1 ise 0, 0 ise 1'e çeviren bir fonksiyon
            instance.save()
            return redirect("/basliklar/gonderi/" + request.post.id)

    else:
        form = PostForm()
    return render(request, 'basliklar/gonderi.html', {"commentform": form})


def publish_post(request):
    # model publish_post form fonksiyonu
    # post isteğiyle alakalı birçok özelliği burda yazıp buradan kopyaladım
    if request.method == 'POST':
        # eğer POST isteğiyse isteğe göre formu oluşturup kaydet
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.original_poster = request.user.username
            instance.date_posted = datetime.datetime.now()
            instance.save()
            return redirect("/basliklar")
            # gönderi gönderildikten sonra /basliklar'a redirectle

    else:
        # eğer GET isteğiyse boş form renderla
        form = PostForm()
    return render(request, 'basliklar/gonderi.html', {"form" : form})
    # urls.py de gonderi.html dosyasının nerede olduğunu buradan alıyor, sonra da renderlıyor

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    flush_comments(post_id)
    # flush_comments, bir gönderi silindiğinde yorumları temizleyen fonksiyon
    post.delete()
    return redirect("/basliklar")

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    post = Post.objects.get(id=comment.post.id)
    post.comments_number = post.comments_number - 1
    post.save()
    # gönderinin yorum sayacını 1 indirip kaydet
    comment.delete()
    # yorumu sil
    return redirect("/basliklar/" + str(comment.post.id))

def flush_comments(post_id):
    post = Post.objects.get(id=post_id)
    for comment in post.comment_set.all():
        if comment.post == post:
            comment.delete()

def publish_comment(request, post_id):
    # bu fonksiyonun ismi biraz kafa karıştırıcı, çünkü aslında hem yorum yazma hem de yorumları açma/kapatma işlevi görüyor
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST' and 'publishcomment' in request.POST:
        # eğer fonksiyonu çağıran butonun ismi "publishcomment" (yorumu gönder) ise bu kısım çalışır
        form = CommentForm(request.POST)
        form2 = ToggleForm()
        if form.is_valid():
            if post.comments_status == 0:
                # status 0 yorumlar kapalı demek
                # bu aslında bir tür fallback mechanism, çünkü status 0 olduğunda yorum gönderme kısmı direk renderlanmıyor
                print("thread locked")
            else:
                instance = form.save(commit=False)
                instance.original_commenter = request.user.username
                instance.post = post
                instance.date_commented = datetime.datetime.now()
                post.comment_added()
                # comment_added'in tek işlevi post modelindeki yorum sayacını artırmak
                post.save()
                instance.save()
                return redirect("/basliklar/" + str(post_id))
    elif request.method == 'POST' and 'togglethread' in request.POST:
        # eğer buton ismi "togglethread" ise bu kısım çalışır
        form2 = ToggleForm(request.POST)
        form = CommentForm()
        if form2.is_valid():
            post = Post.objects.get(id=post_id)
            post.toggle_comments()
            # modeldeki toggle_comments'in tek işlevi status'u 0 ise 1, 1 ise 0 yapmak
            post.save()
            return redirect("/basliklar/" + str(post_id))
    else:
        form = CommentForm()
        form2 = ToggleForm()
    return render(request, "basliklar/detail.html", {"toggleform" : form2, "post" : post, "form" : form})
    # sayfada birden fazla form olduğu için birçok form gönderilmesi gerek

def update_status(request):
    latest_post_list = Post.objects.order_by('-date_posted')
    # update status sayfası aynı zamanda kullanıcı postlarının gösterildiği sayfa olduğu için
    # o sayfaya da latest_post_list (gönderi listesi) sağlanması lazım
    # parsing template seviyesinde hallediliyor zaten
    if request.method == "POST":
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("/basliklar/")
    else:
        form = UserForm()
    return render(request, "basliklar/about.html", {"form": form, 'latest_post_list': latest_post_list})

def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, initial={'post_icerik' : post.post_icerik}, instance=post)
        # normal gönderi gibi, ama kullanılan formdaki tek field içerik fieldı, ve form renderlandığında
        # gönderi içeriği çoktan form text kutusuna yazılmış oluyor (initial tagiyle)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.save()
            return redirect("/basliklar/" + str(post_id))
    else:
        form = PostUpdateForm(initial={'post_icerik' : post.post_icerik})
    return render(request, "basliklar/guncelle.html", {"form" : form})

def show_profile(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    ad = comment.original_commenter
    user = User.objects.get(username=ad)
    latest_post_list = Post.objects.order_by('-date_posted')
    status = user.last_name
    # status last_name fieldını kullanıyor, çünkü bu Django uygulaması varsayılan Django kullanıcı modelini kullanıyor
    # ve bu kullanıcı modelinde bir durum mesajı fieldı yok
    # neyse ki bu forum uygulamasında kullanıcı soyadı sorulmuyor, fakat eğer buna ihtiyaç duyulursa
    # Django abstract kullanıcı modeli extendlenerek durum fieldı olan yeni bir kullanıcı modeli oluşturulabilir
    return render(request, "basliklar/kullanici.html", {'kullanici' : user, 'latest_post_list' : latest_post_list, 'status' : status})

def index(request):
    latest_post_list = Post.objects.order_by('-date_posted')
    template = loader.get_template('basliklar/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    # ana sayfa için gönderi listesini alıp, gönderi tarihine göre sıralayan ve geri döndüren bir fonksiyon
    return HttpResponse(template.render(context, request))