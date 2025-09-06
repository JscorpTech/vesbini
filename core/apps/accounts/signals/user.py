from io import BytesIO

import qrcode
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.apps.accounts.models.user import Profile


@receiver(post_save, sender=get_user_model())
def user_signal(sender, created, instance, **kwargs):
    if created and instance.username is None:
        instance.username = "U%(id)s" % {"id": 1000 + instance.id}
        instance.save()
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def profile_signal(sender, created, instance, **kwargs):
    if not created:
        return
    data = "{}:{}".format(instance.user.username, instance.id)
    filename = "qrcode/{}.png".format(instance.user.id)
    qr = qrcode.QRCode(
        version=1,  # avtomatik o‘lcham uchun 1 yoki None
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    # Default storage orqali saqlash
    file = ContentFile(buffer.read())
    saved_path = default_storage.save(filename, file)
    instance.qrcode = saved_path
    instance.save()
