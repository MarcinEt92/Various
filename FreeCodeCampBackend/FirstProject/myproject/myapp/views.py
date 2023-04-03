from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# from django.http import HttpResponse
from .models import Feature, FeatureModel


# Create your views here.
def index(request):
    # name = "John"
    context = {
        "name": "John",
        "age": 23,
        "nationality": "British",
    }
    # return HttpResponse("<h1>Sample Response</h1>")
    # return render(request, "index.html", {"name": name})
    return render(request, "myapp/index.html", context)


def counter(request):
    return render(request, "myapp/counter.html")


def count_words(request):
    # retrieving arguments provided after ? GET alternatively
    text = request.POST["text"]
    amount_of_words = len(text.split())
    context = {"amount_of_words": amount_of_words}
    return render(request, "myapp/counter.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        # checking if user is really in database, after authentication
        # redirect to homepage
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials not valid")
            return redirect("login")
    else:
        return render(request, "myapp/login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def model_sample(request):
    feature_1 = Feature()
    feature_1.id = 0
    feature_1.name = "Feature One"
    feature_1.details = "Our service is very quick"
    feature_1.is_true = True

    feature_2 = Feature()
    feature_2.id = 1
    feature_2.name = "Feature Two"
    feature_2.details = "Our service is very slow"
    feature_2.is_true = False

    # features = [feature_1, feature_2]
    features = FeatureModel.objects.all()

    context = {"features": features}
    return render(request, "myapp/model_sample.html", context)


def posts(request):
    posts = [1, 2, 3]
    context = {"posts": posts}
    return render(request, "myapp/post.html", context)


def post(request, pk):
    # dynamic urls
    context = {"pk": pk}
    return render(request, "myapp/post.html", context)


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                # return to the register page and preventing
                # form resubmitting
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "User name already used")
                return redirect("register")
            else:
                # create user if criteria are met
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Passwords not match")
            return redirect("register")
    else:
        return render(request, "myapp/register.html")
