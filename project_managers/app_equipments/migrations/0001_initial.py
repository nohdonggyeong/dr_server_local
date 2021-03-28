# Generated by Django 3.1.7 on 2021-03-28 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateField(default=datetime.date.today)),
                ('category', models.CharField(choices=[('', '장비타입 선택'), ('노트북', '노트북'), ('데스크톱', '데스크톱'), ('모니터', '모니터'), ('키보드', '키보드'), ('마우스', '마우스'), ('외장저장장치', '외장저장장치'), ('네트워크장비', '네트워크장비'), ('음향장비', '음향장비'), ('액세서리', '액세서리'), ('기타', '기타')], default='', max_length=20)),
                ('brand', models.CharField(choices=[('', '브랜드 선택'), ('노트북', (('apple', 'apple'), ('asus', 'asus'), ('corsair', 'corsair'), ('dell', 'dell'), ('gram', 'gram'), ('hansung', 'hansung'), ('hp', 'hp'), ('intel', 'intel'), ('lenovo', 'lenovo'), ('msi', 'msi'), ('samsung', 'samsung'), ('ultra', 'ultra'))), ('데스크톱', (('조립식', '조립식'), ('apple', 'apple'), ('asus', 'asus'), ('corsair', 'corsair'), ('dell', 'dell'), ('hansung', 'hansung'), ('hp', 'hp'), ('intel', 'intel'), ('lenovo', 'lenovo'), ('lg', 'lg'), ('msi', 'msi'), ('samsung', 'samsung'))), ('모니터', (('lg', 'lg'), ('samsung', 'samsung'), ('viewsonic', 'viewsonic'), ('viewsync', 'viewsync'))), ('키보드/마우스', (('abko', 'abko'), ('gram노트북용', 'gram노트북용'), ('logitech', 'logitech'), ('micronics', 'micronics'), ('samsung노트북용', 'samsung노트북용'), ('ultra노트북용', 'ultra노트북용'))), ('외장저장장치', (('seagate', 'seagate'), ('ultra_star', 'ultra_star'), ('micron', 'micron'))), ('액세서리', (('gram노트북가방', 'gram노트북가방'), ('samsung노트북가방', 'samsung노트북가방'))), ('기타', (('hdmi', 'hdmi'), ('hdmi허브', 'hdmi허브'), ('도킹스테이션', '도킹스테이션'), ('키오스크', '키오스크'), ('스피커', '스피커'), ('지향성마이크', '지향성마이크'))), ('사무실가전', (('복합기', '복합기'), ('냉장고', '냉장고'), ('공기청정기', '공기청정기'), ('세절기', '세절기')))], default='', max_length=20)),
                ('amount', models.IntegerField(default=1)),
                ('spec', models.TextField(blank=True, default='')),
                ('is_assets', models.CharField(blank=True, choices=[('', '자산구분 선택'), ('자산', '자산'), ('자산 외', '자산 외'), ('렌탈', '렌탈')], default='', max_length=20)),
                ('etc', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ('category', 'brand', 'purchase_date'),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('rank', models.CharField(choices=[('', '직급 선택'), ('주임', '주임'), ('대리', '대리'), ('책임', '책임'), ('법인장님', '법인장님'), ('보관장소', '보관장소')], default='', max_length=20)),
                ('seat', models.IntegerField(default=1, unique=True)),
            ],
            options={
                'ordering': ('seat', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('usage_id', models.AutoField(primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_id', models.ForeignKey(db_column='device_id', on_delete=django.db.models.deletion.CASCADE, related_name='us_device', to='app_equipments.device')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app_equipments.user')),
            ],
            options={
                'ordering': ('user_id', 'device_id'),
            },
        ),
    ]
