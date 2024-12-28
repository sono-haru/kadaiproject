from django.shortcuts import render, redirect
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Tokuten_post
from .forms import TokutenForm
from .models import Tokuten_post
from django.views.generic import ListView

class IndexView(TemplateView):
    template_name='index.html'

class Post_success(TemplateView):
    template_name='post_success.html'

class MypageView(TemplateView):
    template_name = 'mypage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Tokuten_post.objects.all()
        context['object_list'] = object_list
        return context

class TokutenView(CreateView):
    form_class = TokutenForm
    template_name = "tokuten.html"
    success_url = reverse_lazy('oharaapp:post_success')
    
    def form_valid(self, form):
        # フォームデータを保存せずに取得
        post = form.save(commit=False)
        post.user = self.request.user  # 現在ログインしているユーザーを設定
        post.save()  # 保存
        return super().form_valid(form)  # その後、成功の処理を実行

class Tokuten_post_List(ListView):
    template_name='detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            Tokuten_post_list = Tokuten_post.objects.filter(
                subject__icontains=query
            )
        else:
            Tokuten_post_list = Tokuten_post.objects.all().order_by('posted_at')
        return Tokuten_post_list
    