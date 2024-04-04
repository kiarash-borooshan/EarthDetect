
from django.db import models


class DataGather(models.Model):
    geotag_images = models.ImageField(upload_to="geotag_images",
                                      verbose_name="تصاویر ژئوتگ ")
    temperature = models.FloatField(max_length=4,
                                    verbose_name="دمای محیط به درجه سانتی‌گراد")
    humidity = models.FloatField(max_length=4,
                                 verbose_name="رظوبت هوا به درصد ")
    Feature_Choices = (
        ("انتخاب کنید", "انتخاب کنید"),
        ("کشاورزی", "کشاورزی"),
        ("باغ", "باغ"),
        ("مرتع", "مرتع"),
        ("سنگ", "سنگ"),
        ("خاک", "خاک"),
        ("آب", "آب"),
        ("جنگل", "جنگل"),
        ("پسماند", "پسماند"),
        ("آتش", "آتش"),
        ("هیچکدام", "هیچکدام")
    )
    Health_Choices = (
        ("سالم", "بیمار"),
        ("بیمار", "بیمار")
    )
    feature = models.CharField(max_length=20,
                               choices=Feature_Choices,
                               default="انتخاب کنید",
                               verbose_name="انتخاب گروه عارضه ")
    title1 = models.CharField(max_length=50,
                              verbose_name="نام عارضه به فارسی ")
    title2 = models.CharField(max_length=100,
                              verbose_name="نام عارضه به انگلیسی ")

    """ اگر عارضه انتخاب شده کشاورزی یا باغ باشد """
    health_state = models.CharField(max_length=20,
                                    choices=Health_Choices,
                                    verbose_name="وضعیت سلامت محصول کشاورزی یا باغی ")
    """ اگر گیاه بیمار باشد """
    disease = models.CharField(max_length=200,
                               verbose_name=" اگر گیاه یا درخت دارای بیماری باشد نام بیماری یا تنش وارد شده به عارضه را بیان کنید")
    disease_explain = models.TextField(verbose_name=" توضیحات یا راه‌حل مشکل را بیان کنید ")

    """ خصوصیات محصول کشاورزی یا درخت """
    height = models.FloatField(max_length=4,
                               verbose_name="ارتفاع گیاه یا درخت به سانتی‌متر")
    date_of_irrigation = models.CharField(max_length=100,
                                          verbose_name="تاریخ و ساعت آخرین آبیاری")
    date_of_Fertilization = models.CharField(max_length=100,
                                             verbose_name="نوع، تاریخ و ساعت آخرین کوددهی")

    """ اگر عارضه زمین‌شناسی مربوط به سنگ/کانی باشد """
    Rock_Choices = (
        ("انتخاب کنید", "انتخاب کنید"),
        ("آذرین", "آذرین"),
        ("رسوبی", "رسوبی"),
        ("دگرگونی", "دگرگونی"),
    )
    rock_choice = models.CharField(max_length=20,
                                   choices=Rock_Choices,
                                   default="انتخاب کنید",
                                   verbose_name="نوع عازضه سنگ/کانی را انتخاب کنید ")
    """ https://www.tabiat.ir/page/4691/%d8%b1%d9%86%da%af-%d8%ae%d8%a7%da%a9%d9%87 """

    color = models.CharField(max_length=100,
                             verbose_name="رنگ سنگ/کانی و رنگ خاکه آن ")
    Mohs_hardness = models.IntegerField(verbose_name=" سختی سنگ در مفیاس موس از ۱ تا ۹ ")
    """ https://www.google.com/search?q=%D8%A7%D8%B4%D9%84+%D9%85%D9%88%D8%B3&client=ubuntu-sn&hs=GlL&sca_esv=
    6246709ce63302d6&sca_upv=1&channel=fs&ei=h7AKZtGVNqaLxc8PrqOn-AM&ved=0ahUKEwiR9ZXhiaGFAxWmRfEDHa7RCT8Q4dUDCBA&uact=
    5&oq=%D8%A7%D8%B4%D9%84+%D9%85%D9%88%D8%B3&gs_lp=Egxnd3Mtd2l6LXNlcnAiDdin2LTZhCDZhdmI2LMyBhAAGBYYHkidM1CqDljdLnADeAC
    QAQCYAfgCoAHVEqoBBTItOC4xuAEDyAEA-AEBmAILoAKBFMICBRAAGIAEwgIFEC4YgATCAhQQLhiABBiXBRjcBBjeBBjgBNgBAcICCxAuGIAEGMcBGK8
    BwgIIEC4YFhgeGArCAggQABgWGB4YCpgDAIgGAboGBggBEAEYFJIHCTIuMC43LjEuMaAHyVM&sclient=gws-wiz-serp """

    reaction_acid_Choices = (
        ("می‌جوشد", "می‌جوشد"),
        ("نمی‌جوشد", "نمی‌جوشد")
    )
    reaction_acid = models.CharField(max_length=25,
                                     choices=reaction_acid_Choices,
                                     verbose_name="واکنش سنگ/کانی به اسید")

    """ اگر عارضه خاک باشد """
    """ جنس، اندازه دانه، دبی گذر آب، """

    """ اگر عارضه جنگل باشد """
    """ ارتفاع درخت سلامت گیاه، تاج پوشش  و ... """

    objects = models.Manager()

    def __str__(self):
        return self.title1


