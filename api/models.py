from django.db import models


class Category(models.Model):
    title = models.CharField(
        verbose_name="Название категории", max_length=150, unique=True
    )
    photo = models.ImageField(
        verbose_name="Фото категории", upload_to="photos/categories/"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.CharField(
        verbose_name="Название продукта", max_length=255, unique=True
    )
    price = models.IntegerField(verbose_name="Стоимость продукта")
    body = models.TextField(verbose_name="Описание продукта", default="")
    brand = models.CharField(verbose_name="Бренд", max_length=150, default="")
    vendor_code = models.CharField(verbose_name="Артикул", default='', max_length=150)
    gender = models.CharField(verbose_name="Пол", max_length=150, default="")
    preview = models.ImageField(verbose_name="Заставка", upload_to="preview", blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductImage(models.Model):
    def make_folder_path(self, filename):
        return f"photos/products/{filename}"

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="Продукт")
    photo = models.ImageField(verbose_name="Фото продукта", upload_to=make_folder_path)


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="options",
                                verbose_name="Название продукта")
    option_main = models.CharField(verbose_name="Основная характеристика", max_length=155)

    def __str__(self):
        return f"{self.product}: {self.option_main}"

    class Meta:
        verbose_name = "Основная характеристика"
        verbose_name_plural = "Основные характеристики"


class ProductOptionItem(models.Model):
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE, related_name="option")
    name = models.CharField(verbose_name="Дополнительная характеристика", max_length=155)

    class Meta:
        verbose_name = "Дополнительная характеристика"
        verbose_name_plural = "Дополнительные характеристики"
