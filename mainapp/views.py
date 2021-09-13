from django.core.paginator import Paginator
from django.shortcuts import render
from.models import*
from django.contrib import messages
import telebot
from bs4 import BeautifulSoup
import requests
from datetime import datetime

me = 696007117
TOKEN = '1934423453:AAH-gOkWjUH0jZn6cd40tU0rfsI2ZGeRuMA'
bot = telebot.TeleBot(TOKEN)

def customHandler404(request, exception=None):
    return render(request, '404.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		Contact.objects.create(
			name=name,
			email=email,
			phone=phone,
			message=message,
			),
		messages.add_message(request, messages.SUCCESS, 'Tabriklaymiz aloqa muofaqiyat amalga oshirildi tez orada sayit adminlari sizbilan bog\'lanishadi')
		bot.send_message(me,f"Aloqa xizmatidan xabar bor\nIsmi:  {name}\nTelfon raqami:  {phone}\nEmail:  {email}\n Xabari:  {message}")
	return render(request,'contact.html')

def index(request):
	times = Namaz_time.objects.all()
	blog = Blog.objects.all().order_by('-id')[:3]
	url = 'https://islom.uz/'
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	time = soup.findAll('div', class_='date_time')
	time_now = datetime.now()
	for i in time:
	    t = i.text
	    time[0] = t
	    time = time[0]
	timer = {
	    'now': time_now.strftime("%H:%M:%S")
}
	context = {
	'times':times,
	'blog':blog,
	'time':time,
	'timer':timer['now']
	}
	return render(request,'index2.html',context)


def blog(request):
	blog = Blog.objects.all().order_by("-id")[:10]
	return render(request,'blog.html',{'blog':blog})

def blog_detail(request,blog_slug):
	blog_page = Blog.objects.get(slug=blog_slug)
	if request.method == "POST":
		name = request.POST['name']
		message = request.POST['message']
		comment = Comment.objects.create(
			name=name,
			message=message,)
		comment.blog_page = blog_page
		comment.save()

		bot.send_message(me,f"Commentaryiadan xabar bor\nIsmi:  {name}  \n Xabari:  {message}")
	return render(request,'blog-detail.html',{'blog_page':blog_page})

def about(request):
	sheikh = Sheikhs.objects.all()
	return render(request,'about.html',{'sheikh':sheikh})


def gallery(request):
	gallery = Gallery.objects.all()
	return render(request,'gallery2.html',{'gallery':gallery})

def audio(request):
	audio = Audio.objects.all().order_by("-id")
	paginator = Paginator(audio, 10) 
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'audio-listening.html',{'audio':audio,'page_obj': page_obj})

def scholar(request,sheikh_slug):
	sheikh = Sheikhs.objects.get(slug=sheikh_slug)
	return render(request,'scholar-detail.html',{'sheikh':sheikh})

def ramadan(request):
	return render(request,'donation-detail.html')