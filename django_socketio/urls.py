from django.conf.urls import url

from django.conf import settings
from django.utils.importlib import import_module

from . import views

# Try and import an ``events`` module in each installed app,
# to ensure all event handlers are connected.
for app in settings.INSTALLED_APPS:
    try:
        import_module("%s.events" % app)
    except ImportError:
        pass


urlpatterns = [
    url("^socket\.io", views.socketio, name="socketio"),
]
