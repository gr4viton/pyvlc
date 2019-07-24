import platform


class PlayerMixin(object):

    def set_window(self):
        if platform.system() == 'Windows':
            self.player.set_hwnd(self.GetHandle())
        else:
            self.player.set_xwindow(self.GetHandle())  # this line messes up windows

    def open(self, path):
        self.Media = self.Instance.media_new(path)
        self.player.set_media(self.Media)
        self.set_window()
