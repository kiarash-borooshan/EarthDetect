from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import DataGather

from .forms import AddPostForm
from account.models import Account


def index(request):
    return render(request,
                  "dataGather/index.html")


# @login_required
# def add_post(request):
#
#     if not request.user.is_authenticated:
#         return redirect("account:login")
#
#     if request.POST:
#         form = AddPostForm(data=request.POST,
#                            files=request.FILES,
#                            instance=request.user
#                            )
#         if form.is_valid():
#             # author = Account.objects.get(user=request.user)
#             # new_post = form.save(commit=False)
#             # new_post.user = author
#             # new_post.save()
#             # form.save_m2m()
#
#             # form.instance.user = get_object_or_404(Account,
#             #                                        user=request.user)
#             form.save()
#             return redirect("dataGather:success")
#     else:
#         form = AddPostForm()
#     return render(request,
#                   "dataGather/add_post.html",
#                   {"form": form})
#
# def success(request):
#     return HttpResponse("داده‌ها با موفقیت ثبت شدند. ")


class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    # TODO: user and slug must exclude and EditPost
    # TODO: UserPassesTestMixin failed for rest
    model = DataGather
    template_name = "dataGather/add_post.html"
    fields = ("geotag_images", "location", "title1", "title2", "temperature", "humidity",
              "wind_velocity", "wind_direction", "feature", "health_state",
              "disease", "disease_explain", "height", "date_of_irrigation",
              "date_of_Fertilization", "rock_choice", "color", "Mohs_hardness",
              "reaction_acid", "smoke", "explain")
    success_url = reverse_lazy("dataGather:add_post")
    success_message = 'اطلاعات با موفقیت ثبت شد'
    error_meesage = "خطا در پر کزدن فیلدها"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.user == self.request.user