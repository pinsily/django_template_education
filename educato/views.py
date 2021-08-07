from django.shortcuts import render


# Create your views here.
def about(request):
    return render(request, 'educato/about.html')


def index(request):
    return render(request, 'educato/index.html')


def courses(request):
    return render(request, 'educato/courses.html')


def courses_details(request):
    return render(request, 'educato/courses-details.html')


def events_details(request):
    return render(request, 'educato/events-details.html')


def events(request):
    return render(request, 'educato/events.html')


def gallery(request):
    return render(request, 'educato/projects.html')


def gallery_detail(request):
    return render(request, 'educato/projects-detail.html')


def pricing(request):
    return render(request, 'educato/pricing.html')


def team(request):
    return render(request, 'educato/team.html')


def faq(request):
    return render(request, 'educato/faq.html')


def shop(request):
    return render(request, 'educato/shop.html')


def shop_details(request):
    return render(request, 'educato/shop-details.html')


def blog(request):
    return render(request, 'educato/blog.html')


def blog_details(request):
    return render(request, 'educato/blog-details.html')


def contact(request):
    return render(request, 'educato/contact.html')


def services(request):
    return render(request, 'educato/services.html')


def services_detail(request):
    return render(request, 'educato/services-detail.html')


def team_detail(request):
    return render(request, 'educato/team.html')