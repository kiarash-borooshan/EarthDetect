# Generated by Django 5.0.3 on 2024-04-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataGather', '0002_datagather_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='datagather',
            name='explain',
            field=models.TextField(blank=True, null=True, verbose_name='هر مطلب مرتبطی که صلاح می\u200cدانید نگارش کنید'),
        ),
        migrations.AddField(
            model_name='datagather',
            name='smoke',
            field=models.TextField(blank=True, null=True, verbose_name='دود حاصل از سوختن چه عراضه یا مارده\u200cای می\u200cباشد و دارای چه عناصری است'),
        ),
        migrations.AlterField(
            model_name='datagather',
            name='feature',
            field=models.CharField(choices=[('انتخاب کنید', 'انتخاب کنید'), ('کشاورزی', 'کشاورزی'), ('باغ', 'باغ'), ('مرتع', 'مرتع'), ('سنگ', 'سنگ'), ('خاک', 'خاک'), ('آب', 'آب'), ('جنگل', 'جنگل'), ('پسماند', 'پسماند'), ('آتش', 'آتش'), ('برف', 'برف'), ('زمین\u200cسوخته', 'زمین\u200cسوخته'), ('دود و گاز', 'دود و گاز'), ('هیچکدام', 'هیچکدام')], default='انتخاب کنید', max_length=20, verbose_name='انتخاب گروه عارضه '),
        ),
        migrations.AlterField(
            model_name='datagather',
            name='geotag_images',
            field=models.ImageField(upload_to='geotag_images', verbose_name='(*) (geo-tag) آپلود تصویر زمین مرجع   '),
        ),
        migrations.AlterField(
            model_name='datagather',
            name='health_state',
            field=models.CharField(blank=True, choices=[('سالم', 'سالم'), ('بیمار', 'بیمار')], max_length=20, null=True, verbose_name='وضعیت سلامت محصول کشاورزی یا باغی '),
        ),
        migrations.AlterField(
            model_name='datagather',
            name='wind_velocity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='سرعت باد(متربرثانیه) '),
        ),
    ]