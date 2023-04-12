from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db import models


class Basics(models.Model):
    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    summary = RichTextField(blank=True, null=True)
    image = models.CharField(blank=True, null=True,max_length=100)
    phone = models.CharField(blank=True, null=True,max_length=100)
    label = models.CharField(blank=True, null=True,max_length=100)
    url = models.CharField(blank=True, null=True,max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Profiles(models.Model):
    class Meta:
        verbose_name_plural = 'Networks'
        verbose_name = 'Network'

    profiles_id = models.AutoField(primary_key=True)
    url = models.CharField(blank=True, null=True,max_length=100)
    network = models.CharField(max_length=100)
    username = models.CharField(blank=True, null=True,max_length=100)
    basics = models.OneToOneField(Basics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.basics} {self.network}'


class Location(models.Model):
    class Meta:
        verbose_name_plural = 'Locations'
        verbose_name = 'Location'

    location_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    countrycode = models.CharField(max_length=100)
    basics = models.OneToOneField(Basics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.basics} {self.address} {self.countrycode}'


class Education(models.Model):
    class Meta:
        verbose_name_plural = 'Educations'
        verbose_name = 'Education'

    education_id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=100)
    studytype = models.CharField(blank=True, null=True,max_length=100)
    institution = models.CharField(max_length=100)
    score = models.CharField(blank=True, null=True,max_length=100)
    courses = models.CharField(blank=True, null=True,max_length=100)
    enddate = models.DateField(blank=True, null=True,max_length=100)
    startdate = models.DateField(blank=True, null=True,max_length=100)
    basics = models.OneToOneField(Basics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.basics} {self.area} {self.institution}'


class Projects(models.Model):
    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'

    projects_id = models.AutoField(primary_key=True)
    summary = RichTextField(blank=True, null=True)
    name = models.CharField(max_length=100)
    startdate = models.DateField(blank=True, null=True, max_length=100)
    url = models.CharField(blank=True, null=True, max_length=100)
    basics = models.OneToOneField(Basics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.basics} {self.name}'


class Languages(models.Model):
    class Meta:
        verbose_name_plural = 'Languages'
        verbose_name = 'Language'
    languages_id = models.AutoField(primary_key=True)
    fluency = models.CharField(blank=True, null=True, max_length=100)
    language = models.CharField(max_length=100)
    basics = models.OneToOneField(Basics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.basics} {self.language}'


class Work(models.Model):
    class Meta:
        verbose_name_plural = 'Work'
        verbose_name = 'Work'
    work_id = models.AutoField(primary_key=True)
    summary = RichTextField(blank=True, null=True)
    highlights = models.CharField(blank=True, null=True, max_length=100)
    enddate = models.DateField(blank=True, null=True, max_length=100)
    name = models.CharField(blank=True, null=True, max_length=100)
    location = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    startdate = models.DateField(blank=True, null=True, max_length=100)
    url = models.CharField(blank=True, null=True, max_length=100)
    basics = models.OneToOneField(Basics, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.basics} {self.position} {self.location}'


class Skills(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    skills_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    keywords = models.CharField(blank=True, null=True, max_length=100)
    level = models.CharField(blank=True, null=True, max_length=100)
    basics = models.OneToOneField(Basics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.basics} {self.name}'


class Certificates(models.Model):
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'
    certificates_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    startdate = models.DateField(blank=True, null=True, max_length=100)
    issuer = models.CharField(blank=True, null=True, max_length=100)
    url = models.CharField(blank=True, null=True, max_length=100)
    basics = models.OneToOneField(Basics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.basics} {self.name}'

