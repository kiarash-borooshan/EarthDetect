# Generated by Django 5.0.3 on 2024-04-07 06:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataGather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geotag_images', models.ImageField(upload_to='geotag_images', verbose_name='تصاویر ژئوتگ ')),
                ('temperature', models.FloatField(blank=True, max_length=4, null=True, verbose_name='دمای محیط به درجه سانتی\u200cگراد')),
                ('humidity', models.FloatField(blank=True, max_length=4, null=True, verbose_name='رظوبت هوا به درصد ')),
                ('wind_velocity', models.PositiveIntegerField(blank=True, null=True, verbose_name='سرعت باد ')),
                ('feature', models.CharField(choices=[('انتخاب کنید', 'انتخاب کنید'), ('کشاورزی', 'کشاورزی'), ('باغ', 'باغ'), ('مرتع', 'مرتع'), ('سنگ', 'سنگ'), ('خاک', 'خاک'), ('آب', 'آب'), ('جنگل', 'جنگل'), ('پسماند', 'پسماند'), ('آتش', 'آتش'), ('هیچکدام', 'هیچکدام')], default='انتخاب کنید', max_length=20, verbose_name='انتخاب گروه عارضه ')),
                ('wind_direction', models.CharField(blank=True, choices=[('شمال به جنوب', 'شمال به جنوب'), ('جنوب به شمال', 'جنوب به شمال'), ('شرق به غرب', 'شرق به غرب'), ('غرب به شرق', 'غرب به شرق'), ('شمال\u200cغربی به جنوب\u200cشرقی', 'شمال\u200cغربی به جنوب\u200cشرقی'), ('جنوب\u200cشرقی به شمال\u200cغربی', 'جنوب\u200cشرقی به شمال\u200cغربی'), ('شمال\u200cشرقی به جنوب\u200cغربی', 'شمال\u200cشرقی به جنوب\u200cغربی'), ('جنوب\u200cغربی به شمال\u200cشرقی', 'جنوب\u200cغربی به شمال\u200cشرقی')], max_length=50, null=True, verbose_name='جهت وزش باد')),
                ('title1', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام عارضه به فارسی ')),
                ('title2', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام عارضه به انگلیسی ')),
                ('health_state', models.CharField(blank=True, choices=[('سالم', 'بیمار'), ('بیمار', 'بیمار')], max_length=20, null=True, verbose_name='وضعیت سلامت محصول کشاورزی یا باغی ')),
                ('disease', models.CharField(blank=True, max_length=200, null=True, verbose_name=' اگر گیاه یا درخت دارای بیماری باشد نام بیماری یا تنش وارد شده به عارضه را بیان کنید')),
                ('disease_explain', models.TextField(blank=True, null=True, verbose_name=' توضیحات یا راه\u200cحل مشکل را بیان کنید ')),
                ('height', models.FloatField(blank=True, max_length=4, null=True, verbose_name='ارتفاع گیاه یا درخت به سانتی\u200cمتر')),
                ('date_of_irrigation', models.CharField(blank=True, max_length=100, null=True, verbose_name='تاریخ و ساعت آخرین آبیاری')),
                ('date_of_Fertilization', models.CharField(blank=True, max_length=100, null=True, verbose_name='نوع، تاریخ و ساعت آخرین کوددهی')),
                ('rock_choice', models.CharField(blank=True, choices=[('انتخاب کنید', 'انتخاب کنید'), ('آذرین', 'آذرین'), ('رسوبی', 'رسوبی'), ('دگرگونی', 'دگرگونی')], default='انتخاب کنید', max_length=20, null=True, verbose_name='نوع عازضه سنگ/کانی را انتخاب کنید ')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='رنگ سنگ/کانی و رنگ خاکه آن ')),
                ('Mohs_hardness', models.PositiveIntegerField(blank=True, null=True, verbose_name=' سختی سنگ در مفیاس موس از ۱ تا ۹ ')),
                ('reaction_acid', models.CharField(blank=True, choices=[('می\u200cجوشد', 'می\u200cجوشد'), ('نمی\u200cجوشد', 'نمی\u200cجوشد')], max_length=25, null=True, verbose_name='واکنش سنگ/کانی به اسید')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]