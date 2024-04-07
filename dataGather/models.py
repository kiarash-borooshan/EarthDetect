from django.contrib.auth.models import User
from django.db import models
from account.models import Account


class DataGather(models.Model):

    Wind_Dir_Choices = (
        ("شمال به جنوب", "شمال به جنوب"),
        ("جنوب به شمال", "جنوب به شمال"),
        ("شرق به غرب", "شرق به غرب"),
        ("غرب به شرق", "غرب به شرق"),
        ("شمال‌غربی به جنوب‌شرقی", "شمال‌غربی به جنوب‌شرقی"),
        ("جنوب‌شرقی به شمال‌غربی", "جنوب‌شرقی به شمال‌غربی"),
        ("شمال‌شرقی به جنوب‌غربی", "شمال‌شرقی به جنوب‌غربی"),
        ("جنوب‌غربی به شمال‌شرقی", "جنوب‌غربی به شمال‌شرقی"),

    )

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
        ("برف", "برف"),
        ("زمین‌سوخته", "زمین‌سوخته"),
        ("دود و گاز", "دود و گاز"),
        ("هیچکدام", "هیچکدام")
    )

    Health_Choices = (
        ("سالم", "سالم"),
        ("بیمار", "بیمار")
    )

    Rock_Choices = (
        ("انتخاب کنید", "انتخاب کنید"),
        ("آذرین", "آذرین"),
        ("رسوبی", "رسوبی"),
        ("دگرگونی", "دگرگونی"),
    )

    reaction_acid_Choices = (
        ("می‌جوشد", "می‌جوشد"),
        ("نمی‌جوشد", "نمی‌جوشد")
    )

    author = models.ForeignKey(Account,
                               on_delete=models.SET_NULL,
                               related_name="author", 
                               null=True, blank=True)
    geotag_images = models.ImageField(upload_to="geotag_images",
                                      verbose_name="(*) (geo-tag) آپلود تصویر زمین مرجع   ")
    temperature = models.FloatField(max_length=4,
                                    verbose_name="دمای محیط به درجه سانتی‌گراد",
                                    blank=True, null=True)
    humidity = models.FloatField(max_length=4,
                                 verbose_name="رظوبت هوا به درصد ",
                                 blank=True, null=True)
    wind_velocity = models.PositiveIntegerField(verbose_name="سرعت باد(متربرثانیه) ",
                                                blank=True, null=True)
    feature = models.CharField(max_length=20,
                               choices=Feature_Choices,
                               default="انتخاب کنید",
                               verbose_name="انتخاب گروه عارضه ")

    wind_direction = models.CharField(max_length=50,
                                      choices=Wind_Dir_Choices,
                                      verbose_name="جهت وزش باد",
                                      blank=True, null=True)

    title1 = models.CharField(max_length=50,
                              verbose_name="نام عارضه به فارسی ",
                              blank=True, null=True)
    title2 = models.CharField(max_length=100,
                              verbose_name="نام عارضه به انگلیسی ",
                              blank=True, null=True)
    """ اگر عارضه انتخاب شده کشاورزی یا باغ باشد """
    health_state = models.CharField(max_length=20,
                                    choices=Health_Choices,
                                    verbose_name="وضعیت سلامت محصول کشاورزی یا باغی ",
                                    blank=True, null=True)
    """ اگر گیاه بیمار باشد """
    disease = models.CharField(max_length=200,
                               verbose_name=" اگر گیاه یا درخت دارای بیماری باشد"
                                            " نام بیماری یا تنش وارد شده به عارضه را بیان کنید",
                               blank=True, null=True)
    disease_explain = models.TextField(verbose_name=" توضیحات یا راه‌حل مشکل را بیان کنید ",
                                       blank=True, null=True)

    """ خصوصیات محصول کشاورزی یا درخت """
    height = models.FloatField(max_length=4,
                               verbose_name="ارتفاع گیاه یا درخت به سانتی‌متر",
                               blank=True, null=True)
    date_of_irrigation = models.CharField(max_length=100,
                                          verbose_name="تاریخ و ساعت آخرین آبیاری",
                                          blank=True, null=True)
    date_of_Fertilization = models.CharField(max_length=100,
                                             verbose_name="نوع، تاریخ و ساعت آخرین کوددهی",
                                             blank=True, null=True)

    """ اگر عارضه زمین‌شناسی مربوط به سنگ/کانی باشد """
    rock_choice = models.CharField(max_length=20,
                                   choices=Rock_Choices,
                                   default="انتخاب کنید",
                                   verbose_name="نوع عازضه سنگ/کانی را انتخاب کنید ",
                                   blank=True, null=True)
    """ https://www.tabiat.ir/page/4691/%d8%b1%d9%86%da%af-%d8%ae%d8%a7%da%a9%d9%87 """

    color = models.CharField(max_length=100,
                             verbose_name="رنگ سنگ/کانی و رنگ خاکه آن ",
                             blank=True, null=True)
    Mohs_hardness = models.PositiveIntegerField(verbose_name=" سختی سنگ در مفیاس موس از ۱ تا ۹ ",
                                                blank=True, null=True)
    """ https://www.google.com/search?q=%D8%A7%D8%B4%D9%84+%D9%85%D9%88%D8%B3&client=ubuntu-sn&hs=GlL&sca_esv=
    6246709ce63302d6&sca_upv=1&channel=fs&ei=h7AKZtGVNqaLxc8PrqOn-AM&ved=0ahUKEwiR9ZXhiaGFAxWmRfEDHa7RCT8Q4dUDCBA&uact=
    5&oq=%D8%A7%D8%B4%D9%84+%D9%85%D9%88%D8%B3&gs_lp=Egxnd3Mtd2l6LXNlcnAiDdin2LTZhCDZhdmI2LMyBhAAGBYYHkidM1CqDljdLnADeAC
    QAQCYAfgCoAHVEqoBBTItOC4xuAEDyAEA-AEBmAILoAKBFMICBRAAGIAEwgIFEC4YgATCAhQQLhiABBiXBRjcBBjeBBjgBNgBAcICCxAuGIAEGMcBGK8
    BwgIIEC4YFhgeGArCAggQABgWGB4YCpgDAIgGAboGBggBEAEYFJIHCTIuMC43LjEuMaAHyVM&sclient=gws-wiz-serp """

    reaction_acid = models.CharField(max_length=25,
                                     choices=reaction_acid_Choices,
                                     verbose_name="واکنش سنگ/کانی به اسید",
                                     blank=True, null=True)

    """ اگر عارضه دود یا گاز باشد """
    smoke = models.TextField(verbose_name="دود حاصل از سوختن چه عراضه یا مارده‌ای می‌باشد و دارای چه عناصری است",
                             blank=True, null=True)

    """ اگر عارضه خاک باشد """
    """ جنس، اندازه دانه، دبی گذر آب، """

    """ اگر عارضه جنگل باشد """
    """ ارتفاع درخت سلامت گیاه، تاج پوشش  و ... """

    explain = models.TextField(verbose_name="هر مطلب مرتبطی که صلاح می‌دانید نگارش کنید", 
                               null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50,
                            null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title1


