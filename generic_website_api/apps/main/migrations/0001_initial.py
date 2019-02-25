# Generated by Django 2.0.2 on 2018-11-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Articles', max_length=15)),
                ('header', models.CharField(default='Articles', max_length=30)),
                ('title', models.CharField(default='Articles', max_length=35)),
                ('sub_title', models.TextField(default='Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. pellentesque eget nunc.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ContactSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Contact', max_length=15)),
                ('header', models.CharField(default='Contact', max_length=30)),
                ('title', models.CharField(default='Où nous trouver', max_length=35)),
                ('sub_title', models.TextField(default="N'hésitez pas à nous contacter...", max_length=200)),
                ('sub_title2', models.TextField(default='... en nous laissant un message...', max_length=200)),
                ('sub_title3', models.TextField(default='... ou en passant directement nous voir:', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Events', max_length=15)),
                ('header', models.CharField(default='Galerie', max_length=30)),
                ('title', models.CharField(default='Derniers événements', max_length=35)),
                ('sub_title', models.TextField(default='Nulla tellus. morbi non quam nec dui luctus rutrum. etiam pretium iaculis justo.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Hero', max_length=15)),
                ('icon1', models.CharField(default='fab fa-cloudversify', max_length=20)),
                ('icon2', models.CharField(default='far fa-paint-brush', max_length=20)),
                ('icon3', models.CharField(default='far fa-compass', max_length=20)),
                ('title1', models.CharField(default='Magna non', max_length=20)),
                ('title2', models.CharField(default='Nisi nulla', max_length=20)),
                ('title3', models.CharField(default='Nibh dapibus', max_length=20)),
                ('text1', models.CharField(default='Vivamus vestibulum sagittis sapien. maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.', max_length=200)),
                ('text2', models.CharField(default='In hac habitasse platea dictumst. etiam vel augue.', max_length=200)),
                ('text3', models.CharField(default='Duis at velit eu est congue elementum. duis ac nibh.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('message', models.TextField(max_length=3000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_new', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='PresentationSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Presentation', max_length=15)),
                ('title', models.CharField(default='Proin interdum mauris non ligula pellentesque ultrices.', max_length=35)),
                ('sub_title', models.TextField(default='Suspendisse potenti. duis ac nibh.', max_length=200)),
                ('text1', models.TextField(default='Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; nulla dapibus dolor vel est. etiam faucibus cursus urna. quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. proin at turpis a pede posuere nonummy. in hac habitasse platea dictumst. nunc nisl. nulla suscipit ligula in lacus. integer ac neque.', max_length=800)),
                ('text2', models.TextField(default='Maecenas pulvinar lobortis est. integer a nibh. sed vel enim sit amet nunc viverra dapibus. cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. curabitur at ipsum ac tellus semper interdum. suspendisse ornare consequat lectus. suspendisse accumsan tortor quis turpis. cras in purus eu magna vulputate luctus. in blandit ultrices enim.', max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='PromoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Promo', max_length=15)),
                ('title', models.CharField(default='In congue.', max_length=35)),
                ('text', models.CharField(default='Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. donec semper sapien a libero. aenean auctor gravida sem. nam nulla.', max_length=800)),
                ('label', models.CharField(default='Action spéciale !', max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='SiteContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('tripadvisor', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('google', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('twitter', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('instagram', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('linkedin', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('snapchat', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInformations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25)),
                ('name_add', models.CharField(default='', max_length=15)),
                ('oppening', models.CharField(default='', max_length=4)),
                ('adress', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('post_code', models.CharField(default='', max_length=8)),
                ('phone', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('mail', models.EmailField(blank=True, default='', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_auto_scroll', models.BooleanField(default=False)),
                ('carousel_auto_scroll_speed', models.IntegerField(default=5000)),
                ('show_articles_price', models.BooleanField(default=True)),
            ],
        ),
    ]