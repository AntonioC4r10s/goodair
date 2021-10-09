import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file("gui/interface.glade")
builder.connect_signals(Handler())


window = builder.get_object("windowroot")
window.show_all()

Gtk.main()
