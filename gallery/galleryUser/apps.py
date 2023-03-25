from django.apps import AppConfig


class GalleryuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'galleryUser'

    def ready(self):
        import galleryUser.signals
