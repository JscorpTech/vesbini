# type: ignore
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

User = get_user_model()


class ProductModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("name"), max_length=255)
    desc = models.TextField(_("desc"))
    status = models.BooleanField(_("status"), default=True)
    image = models.ImageField(_("image"), upload_to="product/")
    colors = models.ManyToManyField("ColorModel")
    sizes = models.ManyToManyField("SizeModel")
    amount = models.BigIntegerField(_("amount"), default=0)
    tags = models.ManyToManyField("TagModel", related_name="products", blank=True)
    categories = models.ManyToManyField("CategoryModel", related_name="products", blank=True)

    @property
    def quantity(self):
        return self.variants.aggregate(models.Sum("quantity"))  # type: ignore

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(cls):
        return cls.objects.get_or_create(
            title="mock",
            desc="sasa",
            image="/test/product.jpg",
            amount=0,
        )[0]

    class Meta:
        db_table = "product"
        verbose_name = _("ProductModel")
        verbose_name_plural = _("ProductModels")


class ProductVariantModel(AbstractBaseModel):
    product = models.ForeignKey("ProductModel", on_delete=models.CASCADE, related_name="variants")
    color = models.ForeignKey("ColorModel", on_delete=models.SET_NULL, null=True, blank=False)
    size = models.ForeignKey("SizeModel", on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.BigIntegerField(_("quantity"), default=0)
    amount = models.BigIntegerField(_("amount"), default=0)
    sku = models.CharField(_("sku"), max_length=255, unique=True, blank=True, null=True)
    is_bundle = models.BooleanField(_("is bundle"), default=True)
    href = models.CharField(_("href"), max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return f"color: {self.color} - size: {self.size} - quantity: {self.quantity}"

    @classmethod
    def _create_fake(cls, quantity=100):
        return cls.objects.get_or_create(
            product=ProductModel._create_fake(),
            color=ColorModel._create_fake(),
            size=SizeModel._create_fake(),
            quantity=quantity,
        )[0]


class TagModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "tag"
        verbose_name = _("TagModel")
        verbose_name_plural = _("TagModels")


class CategoryModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "category"
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModels")


class ColorModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "color"
        verbose_name = _("ColorModel")
        verbose_name_plural = _("ColorModels")


class SizeModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "size"
        verbose_name = _("SizeModel")
        verbose_name_plural = _("SizeModels")


class BasketModel(AbstractBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("ProductModel", on_delete=models.CASCADE)
    count = models.BigIntegerField(_("quantiry"), default=1)
    variant = models.ForeignKey("ProductVariantModel", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.phone)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            user=User._create_fake(),
            product=ProductModel._create_fake(),
            variant=ProductVariantModel._create_fake(),
        )

    class Meta:
        db_table = "basket"
        verbose_name = _("BasketModel")
        verbose_name_plural = _("BasketModels")


class ProductImageModel(AbstractBaseModel):
    product = models.ForeignKey("ProductModel", on_delete=models.CASCADE, related_name="images")
    image = models.FileField(_("image"), upload_to="product/")
    color = models.ForeignKey("ColorModel", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.image.name)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            image="default.jpg",
        )

    class Meta:
        db_table = "productimage"
        verbose_name = _("ProductimageModel")
        verbose_name_plural = _("ProductimageModels")
