from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Namaz_time(models.Model):
	name = models.CharField('Namoz nomi', max_length=100)
	time = models.CharField('Namoz vaqti', max_length=100)

	class Meta:
		verbose_name = 'Namoz vaqti'
		verbose_name_plural = 'Namoz vaqtlari'

	def __str__(self):
		return f"{self.name}"

class Blog(models.Model):
	title = models.CharField('Maqola nomi',max_length=300)
	body = RichTextField()
	slug = models.SlugField('*',max_length=100, unique=True, db_index=True)
	author = models.CharField('Muallif', default='Admin',max_length=200,blank=True)
	date = models.DateField("Qo'shilgan vaqti", auto_now_add=True)
	image = models.ImageField('Maqola rasmi', upload_to='Maqolalar_rasmi/')

	class Meta:
		verbose_name = 'Maqola'
		verbose_name_plural = 'Maqolalar'

	def get_absalute_url(self):   
		return reverse('mainapp:blogDetailPage',kwargs={'blog_slug':self.slug})

	def __str__(self):
		return f'{self.title}'

class Comment(models.Model):
	blog_page = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
	name = models.CharField('Ismi', max_length=50)
	message = models.TextField('Xabar',)

	class  Meta:
		verbose_name = 'Muhokama'
		verbose_name_plural = 'Muhokamalar'

	def __str__(self):
		return f"{self.name}"

class Sheikhs(models.Model):
	slug = models.SlugField('*',max_length=200, unique=True, db_index=True)
	name = models.CharField('Ismi', max_length=200)
	direction = models.CharField("Yo'nalishi", max_length=200)
	fullname = models.CharField('Toliq ismi',max_length=300)
	surname = models.CharField("familiyasi",max_length=300)
	address = models.CharField('Yashash manzili',max_length=500)
	phone = models.CharField('Telfon raqami',max_length=100)
	about = models.TextField("To'liq malumoti")
	image = models.ImageField('Rasmi',upload_to='Sheikhs/')

	class Meta:
		verbose_name = 'Qori va Imom'
		verbose_name_plural = 'Qorilar va Imomlar'

	def get_absalute_url(self):
		return reverse('mainapp:scholarDetailPage',kwargs={'sheikh_slug':self.slug})
	def __str__(self):
		return f'{self.name}'

class Gallery(models.Model):
	title = models.CharField('Rasm matni',max_length=200,default='Imomi Azazm Rahmutullohi alayh jome masjid')
	date = models.DateField('Joylangan vaqti',auto_now_add=True)
	images = models.ImageField('Rasmi',upload_to='Gallerys/')

	class Meta:
		verbose_name = 'Rasim'
		verbose_name_plural = 'Rasmlar'

	def __str__(self):
		return f"{self.title}"

class Audio(models.Model):
	audio_name = models.CharField('Sura nomi',max_length=250)
	audio_img = models.ImageField(upload_to='Audio_files/')
	audio_files = models.FileField('Audioni yuklash')

	class Meta:
		verbose_name = "Audio"
		verbose_name_plural = "Audiolar"
	def __str__(self):
		return f"{self.audio_name}"

class Contact(models.Model):
	name = models.CharField("F,I,SH",max_length=250)
	email = models.EmailField('Elektron pochta',max_length=100)
	phone = models.CharField("Telfon raqami",max_length=20)
	message = models.TextField("Xabari")

	class Meta:
		verbose_name = "Aloqa"
		verbose_name_plural = "Aloqalar"
	def __str__ (self):
		return f'{self.name}'