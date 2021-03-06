from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize
from imagekit.processors import ResizeToFill
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User


class Place(models.Model):
    """
    Clase Place que modela un lugar en la aplicacion. Hereda de
    django.db.models.Model y es para casi uso exclusivo de django.
    """
    placeName = models.CharField(max_length=50,
                                 blank=False,
                                 primary_key=True)

    def __unicode__(self):
        """Retorna el nombre de un lugar al imprimir un objeto Place"""
        return str(self.placeName)


class Photo(models.Model):
    """
    Clase Photo que modela una foto en la aplicacion. Hereda de
    django.db.models.Model y es para casi uso exclusivo de django.
    """
    picture = ProcessedImageField(upload_to='pictures',
                                  null=True,
                                  processors=[SmartResize(640, 480)],
                                  format='JPEG',
                                  options={'quality': 90})
    picture_crop = ImageSpecField(source='picture',
                                  processors=[ResizeToFill(300, 300)],
                                  format='JPEG',
                                  options={'quality': 60})
    date = models.DateField(null=True,
                            help_text="<em>yyyy-mm-dd</em>.")
    time = models.TimeField(null=True,
                            help_text="<em>hh:mm</em>.")
    place = models.ForeignKey(Place, null=True)

    def image_tag(self):
        """Retorna url absoluta para uso html de una foto"""
        return u'<img src="%s" alt= "404"/>' % self.picture_crop.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Notification(models.Model):
    """
    Clase Notification que dimensiona las notifiaciones que recibe un usuario.
    Hereda de django.db.models.Model y es para casi uso exclusivo de django.
    """
    text = models.CharField(max_length=200, blank=False, null=True)
    sender = models.ForeignKey(User,
                               null=True,
                               related_name='sender')

    receiver = models.ForeignKey(User,
                                 null=True,
                                 related_name='receiver')

    dateTime = models.DateTimeField(auto_now_add=True,
                                    null=True)

    seen = models.BooleanField(default=False)

    tagged_photo = models.ForeignKey(Photo, null=True,
                                     related_name='tagged_photo')

    NOTIF_TYPE = (
        ('tag', 'tag'),
        ('friend_request', 'friend_request'),
        ('custom', 'custom')  # muestra el texto en "text"
    )

    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPE,
                                  null=False)

    def __unicode__(self):
        """Retorna el nombre de un lugar al imprimir un objeto Place"""
        return str(self.text)


class Tag(models.Model):

    photo = models.ForeignKey(Photo, null=True)

    user = models.ForeignKey(User, null=True)

    x_pos = models.IntegerField(default=0)

    y_pos = models.IntegerField(default=0)

    def __unicode__(self):
        """Retorna el nombre de un lugar al imprimir un objeto Place"""
        return str(self.user)+" "+str(self.photo)
