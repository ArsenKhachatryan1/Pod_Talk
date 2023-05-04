from django.shortcuts import render, redirect
from . models import Hero, Topic, Download, Social, ContactUs, HomeLogo, HomeInfo, LastEpisode, BgImage, AboutPod
from .forms import ContactForm
from django.db.models import Q
# Create your views here.


def index(request):
    homelogo = HomeLogo.objects.all()[0]
    hominfo = HomeInfo.objects.all()[0]
    hero_list = Hero.objects.all()
    topic_list = Topic.objects.all()
    download = Download.objects.all()
    social = Social.objects.all()
    last_episode = Hero.objects.all()[:2]
    trend_episode_author = Hero.objects.all()
    trend_episode_info = LastEpisode.objects.all()
    footerimage = BgImage.objects.all()[0]
    bannerimage = BgImage.objects.all()[0]
    search_post = request.GET.get('search')
    if search_post:    
        posts = Hero.objects.filter(Q(name__icontains=search_post))
    else:
        posts = Hero.objects.all()
    return render(request, 'main/index.html', context={
        'act':'index',
        'hero_list':hero_list,
        'topic_list':topic_list,
        'download':download,
        'social':social,
        'posts':posts,
        'homelogo':homelogo,
        'hominfo':hominfo,
        'last_episode':last_episode,
        'trend_episode_author':trend_episode_author,
        'trend_episode_info':trend_episode_info,
        'footerimage':footerimage,
        'bannerimage':bannerimage,
        
        })




def about(request):
    homelogo = HomeLogo.objects.all()[0]
    download = Download.objects.all()
    social = Social.objects.all()
    footerimage = BgImage.objects.all()[0]
    headerimage = BgImage.objects.all()[0]
    story_hero = Hero.objects.all()
    aboutpod = AboutPod.objects.all()[0]
    return render(request, 'main/about.html', context={
        'act':'about',
        'download':download,
        'social':social,
        'homelogo':homelogo,
        'footerimage':footerimage,
        'headerimage':headerimage,
        'story_hero':story_hero,
        'aboutpod':aboutpod
        })


def listing_page(request):
    homelogo = HomeLogo.objects.all()[0]
    download = Download.objects.all()
    social = Social.objects.all()
    last_episode = Hero.objects.all()[:2]
    trend_episode_author = Hero.objects.all()
    trend_episode_info = LastEpisode.objects.all()
    footerimage = BgImage.objects.all()[0]
    headerimage = BgImage.objects.all()[0]

    return render(request, 'main/listing-page.html', context={
        'act':'listing_page',
        'download':download,
        'social':social,
        'homelogo':homelogo,
        'last_episode':last_episode,
        'trend_episode_author':trend_episode_author,
        'trend_episode_info':trend_episode_info,
        'footerimage':footerimage,
        'headerimage':headerimage
        })


def detail_page(request):
    homelogo = HomeLogo.objects.all()[0]
    download = Download.objects.all()
    social = Social.objects.all()
    trend_episode_author = Hero.objects.all()
    trend_episode_info = LastEpisode.objects.all()
    footerimage = BgImage.objects.all()[0]
    headerimage = BgImage.objects.all()[0]

    return render(request, 'main/detail-page.html', context={
        'act':'detail_page',
        'download':download,
        'social':social,
        'homelogo':homelogo,
        'trend_episode_author':trend_episode_author,
        'trend_episode_info':trend_episode_info,
        'footerimage':footerimage,
        'headerimage':headerimage
        })



def contact(request):
    homelogo = HomeLogo.objects.all()[0]
    download = Download.objects.all()
    social = Social.objects.all()
    contact_us = ContactUs.objects.all()
    footerimage = BgImage.objects.all()[0]
    headerimage = BgImage.objects.all()[0]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactUs.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', context={
        'act':'contact',
        'download':download,
        'social':social,
        'contact_us':contact_us,
        'form': form,
        'homelogo':homelogo,
        'footerimage':footerimage,
        'headerimage':headerimage
        })