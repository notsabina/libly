from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from books.models import Library
from feed.models import Post
from users.forms import UserUpdateForm, UserRegisterForm
from users.models import FriendRequest


def users_list(request):
    pass


def friend_list(request):
    pass


@login_required
def send_friend_request(request):
    pass


@login_required
def cancel_friend_request(request):
    pass


@login_required
def accept_friend_request(request):
    pass


@login_required
def delete_friend_request(request):
    pass


@login_required
def search_users(request):
    query = request.GET.get('q')  # TODO
    object_list = User.objects.filter(username__incontais=query)
    context = {
        'users': object_list
    }
    return render(request, "users/search_users.html", context)


def my_profile(request):
    p = request.user.profile
    who = p.user
    sent_friend_requests = FriendRequest.objects.filter(from_user=who)
    received_friend_requests = FriendRequest.objects.filter(to_user=who)
    user_posts = Post.objects.filter(user_name=who)
    friends = p.friends.all()
    library = Library.objects.filter(user=who)

    # TODO add requests display

    context = {
        'u': who,
        # TODO add button
        'friends_list': friends,
        'sent_friend_requests': sent_friend_requests,
        'received_friend_requests': received_friend_requests,
        # TODO add posts processing
    }

    return render(request, "users/profile.html", context)


@login_required
def edit_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
    # TODO


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={'form': form})
