# EarthDetect.ir
satellite image process by collective wisdom

سامانه اشتراک‌گذاری داده‌های مکانی به کمک خردجمعی

بدین صورت که خردجمعی با موبایل خود تصاویر ژئوتگ از هر عارضه روی زمین تهیه می کند

این عوارض شامل: تمامی محصولات کشاورزی، باغ، فنولوژی(دوره رشد گیاه)، آفت‌ها، تنش‌ها، خاک، سنگ، منابع معدنی/کانی،
      جنگل‌ها، منابع طبیعی، آتش-زمین‌سوخته-دود، گازهای آلاینده، پسماند و کلا هر آنچه روی سطح زمین می‌باشد

از این داده‌ها برای پردازش تصاویر ماهواره استفاده خواهد شد

ویدئو زیر چرايی نیاز به خرد جمعی در پردازش تصاویر ماهواره‌/پهپاد را به زبان ساده و خلاصه توضیح داده است. خواهشمنداست ملاحظه فرمایید

(https://www.aparat.com/v/MnPS6)

در ویدئو زیر راهنمای کار با سایت توضیح داده شده است 

(https://www.aparat.com/v/teY40)


## TODO list
-[ ] css failed when DEBUG = False
- [ ] عناوین بصورت برعکس (ار آخر به اول) نمایش داده می‌شود

- [ ] اکنون پروژه روی دیتابیس دیفالت می‌باشد وو باید به پستگرس تغییر کند ولی مشکل زیر را دارد
- اضافه کردن مپ به مدل: این کار انجام شده ولی کارشناس ارائه دهنده هاست می‌گوید که سی‌پنل نسخه جدید پستگرس را آپدیت نمی‌کند


برای پروژم نیاز دارم از فیلد زیررا به مدلم اضافه کنم. که یک نقشه‌ای شبیه گوگل ارث را در اختیار قرار میدهد تا با دابل کلیک مختصات یک نقطه ثبت شود.
model.py

from django.contrib.gis.db import models

location = models.PointField(blank=True, null=True,
                                 srid=4326)
                                 
 DATABASES = {
     'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         ...
         }
 }
 
 terminal
 pip install psycopg2-binary
 pip freeze > requirements.txt
 
 این پروژه در لوکال هاست بخوبی کار میکنه ولی در ترمینال سی پنل دستور pip install -r requirements.txt با خطای زیر را میدهد
 
 django.core.exceptions.ImproperlyConfigured: Could not find the GDAL library (tried "gdal", "GDAL", "gdal3.7.0", "gdal3.6.0", "gdal3.5.0", "gdal3.4.0", "gdal3.3.0", "gdal3.2.0", "gdal3.1.0", "gdal3.0.0", "gdal2.4.0"). Is GDAL installed? If it is, try setting GDAL_LIBRARY_PATH in your settings.
((EDet:3.11)) [earthdet@server174 EDet]$

pip install gdal هم اررور میدهد

پشتیبانی هاست میگه نسخه پستکرس سرور قدیمی می باشد
سی پنل برای این دیتابیس آپدیت نمی دهد متاسفانه

تمامی موارد بالا را در کد غیر فعال (کامنت) کردم و دیتابیس را هم تغییر دادم 
'ENGINE': 'django.contrib.gis.db.backends.postgis'

ولی بازهم این اررور را میدهد
File "/home/earthdet/virtualenv/Edtc/3.10/lib/python3.10/site-packages/django/db/backends/postgresql/base.py", line 25, in <module>
    import psycopg as Database
ModuleNotFoundError: No module named 'psycopg'

During handling of the above exception, another exceptionoccurred:

Traceback (most recent call last):
  File "/home/earthdet/virtualenv/Edtc/3.10/lib/python3.10/site-packages/django/db/backends/postgresql/base.py", line 27, in <module>
    import psycopg2 as Database
ModuleNotFoundError: No module named 'psycopg2'

----------------------------------------


![Screenshot from 2024-04-23 15-33-11cen](https://github.com/kiarash-borooshan/EarthDetect/assets/71966936/7a75b5be-7305-477e-b524-1f178ab3cc3a)

![Screenshot from 2024-04-24 06-14-09_cen](https://github.com/kiarash-borooshan/EarthDetect/assets/71966936/cc1105b9-f74e-4dc4-a887-5ce298201f61)

![Screenshot from 2024-04-22 08-25-02cen](https://github.com/kiarash-borooshan/EarthDetect/assets/71966936/d9b48582-0581-48ae-875e-2f7a929e7097)