from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'articles'
    verbose_name = '博客管理'

    def ready(self):
        import articles.signals
