# Generated by Django 3.1.7 on 2021-03-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.IntegerField(default=1)),
                ('name', models.CharField(default='No Name', max_length=10)),
                ('rank', models.CharField(choices=[('', '직급을 선택해주세요.'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('Freelancer', 'Freelancer'), ('Intern', 'Intern'), ('Contract', 'Contract')], default='Not Ranked', max_length=20)),
                ('mainbody', models.CharField(blank=True, choices=[('', '노트북/데스크탑 선택'), ('노트북', (('그램', '그램'), ('울트라', '울트라'), ('삼성', '삼성'), ('아수스', '아수스'), ('한성', '한성'))), ('데스크톱', (('서버PC', '서버PC'), ('학습PC', '학습PC'), ('운영PC', '운영PC')))], max_length=20)),
                ('monitor', models.CharField(blank=True, choices=[('', '모니터 선택'), ('ViewSync', 'ViewSync'), ('LG', 'LG'), ('Samsung', 'Samsung')], max_length=20)),
                ('keyboard', models.CharField(blank=True, choices=[('', '키보드 선택'), ('Logitech(신형)', 'Logitech(신형)'), ('Logitech(구형)', 'Logitech(구형)'), ('기계식 키보드', '기계식 키보드')], max_length=20)),
                ('mouse', models.CharField(blank=True, choices=[('', '마우스 선택'), ('Logitech(신형)', 'Logitech(신형)'), ('Logitech(구형)', 'Logitech(구형)'), ('LG gram 마우스', 'LG gram 마우스'), ('삼성 노트북 마우스', '삼성 노트북 마우스'), ('Micronics', 'Micronics')], max_length=20)),
                ('smalldevice', models.CharField(blank=True, choices=[('', '소형 장비 선택'), ('외장HDD', '외장HDD'), ('외장SSD', '외장SSD'), ('NAS', 'NAS'), ('도킹스테이션', '도킹스테이션'), ('VPN 공유기', 'VPN 공유기'), ('허브', '허브')], max_length=20)),
                ('bigdevice', models.CharField(blank=True, choices=[('', '대형 장비 선택'), ('키오스크', '키오스크')], max_length=20)),
                ('accessory', models.CharField(blank=True, choices=[('', '액세서리 선택'), ('삼성 노트북 가방', '삼성 노트북 가방'), ('그램 노트북 가방', '그램 노트북 가방'), ('울트라 노트북 가방', '울트라 노트북 가방')], max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
