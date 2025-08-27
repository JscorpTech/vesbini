from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from core.apps.api.admin import product
from core.apps.api.models import BasketModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel
from core.apps.api.models.product import ProductVariantModel


@receiver(post_save, sender=ProductModel)
def product_created(sender, instance, created, **kwargs):
    if created:
        colors = instance.colors.all()
        sizes = instance.sizes.all()
        for color in colors:
            for size in sizes:
                ProductVariantModel.objects.create(product=instance, color=color, size=size, amount=instance.amount)


@receiver(m2m_changed, sender=ProductModel.colors.through)
@receiver(m2m_changed, sender=ProductModel.sizes.through)
def product_m2m_changed(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        colors = instance.colors.all()
        sizes = instance.sizes.all()

        for color in colors:
            for size in sizes:
                ProductVariantModel.objects.get_or_create(
                    product=instance,
                    color=color,
                    size=size,
                    defaults={"amount": instance.amount},
                )

        ProductVariantModel.objects.filter(product=instance).exclude(
            models.Q(size__in=sizes) & models.Q(color__in=colors)
        ).delete()


@receiver(post_save, sender=TagModel)
def TagSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=CategoryModel)
def CategorySignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=ColorModel)
def ColorSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=SizeModel)
def SizeSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=BasketModel)
def BasketSignal(sender, instance, created, **kwargs): ...
