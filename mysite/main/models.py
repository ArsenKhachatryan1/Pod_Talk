from django.db import models

# Create your models here.


class HomeLogo(models.Model):

    logo = models.ImageField('Home logo', upload_to='images')


class HomeInfo(models.Model):

    name1 = models.CharField('Home info name1', max_length=50)
    name2 = models.CharField('Home info name2', max_length=50)
    button_name = models.CharField('Home button', max_length=50)

    def __str__(self):
        return self.name1


class Hero(models.Model):
    name = models.CharField('Name', max_length=50)
    img = models.ImageField('Image', upload_to='images', null=True)
    badge_1 = models.CharField('badge_1', max_length=20, blank=True)
    badge_2 = models.CharField('badge_2', max_length=20, blank=True)
    kayq_1 = models.CharField('kayq_', max_length=20, blank=True)
    kayq_1_link = models.URLField('kayq_1_link', max_length=50, blank=True)
    kayq_2 = models.CharField('kayq_2', max_length=20, blank=True)
    kayq_2_link = models.URLField('kayq_2_link', max_length=50, blank=True)
    kayq_3 = models.CharField('kayq_3', max_length=20, blank=True)
    kayq_3_link = models.URLField('kayq_3_link', max_length=50, blank=True)
    verification = models.BooleanField('Yes/No', null=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Heroes'


class Topic(models.Model):
    name = models.CharField('Name', max_length=50)
    img = models.ImageField('Image', upload_to='images', null=True)
    info = models.CharField('Info', max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'


class Download(models.Model):
    name = models.CharField('Name', max_length=50)
    img = models.ImageField('Image', upload_to='images', null=True)
    link = models.CharField('link', max_length=60,)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'


class Social(models.Model):
    name = models.CharField('Name', max_length=50)
    link = models.CharField('link', max_length=60,)

    def __str__(self) -> str:
        return self.name





class ContactUs(models.Model):

    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    company = models.CharField('User name', max_length=50)
    message = models.TextField('User message')

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    def __str__(self) -> str:
        return self.name
    


class LastEpisode(models.Model):

    author = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='last_episode')
    name = models.CharField('Last_episode name', max_length=60)
    img = models.ImageField('Last_episode image', upload_to='images', null=True)
    text = models.TextField('Description')
    minute = models.CharField('Minutes', max_length=50)
    episode = models.IntegerField('Episodes')
    listen = models.CharField('Listen', max_length=10)
    like = models.CharField('Like', max_length=10)
    comment = models.CharField('Comment', max_length=10)
    download =models.CharField('Download', max_length=10)

    def __str__(self) -> str:
        return self.author.name
    


class TrendEpisode(models.Model):

    author = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='trend_episode_author')
    info = models.ForeignKey(LastEpisode, on_delete=models.CASCADE, related_name='trend_episode_info', null=True)

    def __str__(self) -> str:
        return self.author.name
    


class BgImage(models.Model):
    header = models.ImageField('Header Image', upload_to='images', blank=True)
    banner = models.ImageField('Banner Image', upload_to='images', blank=True)
    footer = models.ImageField('Footer Image', upload_to='images', blank=True)



class Ourstory(models.Model):

    author = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='story_hero')
    

    class Meta:
        verbose_name = 'Ourstory'
        verbose_name_plural = 'Ourstories'

    def __str__(self) -> str:
        return self.author.name


class AboutPod(models.Model):
    img = models.ImageField('About Pod image', upload_to='images')
    text = models.TextField('Text')

    