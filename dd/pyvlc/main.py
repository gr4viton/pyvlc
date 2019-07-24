from player.tk import Tk_get_root, Player, _quit
import os
from threading import Thread


class ApplicationThread(Thread):
    """
    """

    def __init__(self, callback):
        Thread.__init__(self)
        self.callback = callback

    def run(self):
        self.callback()
        while True:
            pass


class Nano(object):

    def __init__(self, dirs=):
        self.init_app()

    def run(self):

        gui = Thread(target=self.start_app)
        gui.start()
        process = Thread(target=self.loop)
        process.start()
        gui.join()
        process.join()

    def loop(self):
        # self.start_app()
        self.traverse()

        while True:
            pass

    def traverse(self):


        video_roots = os.getenv('PYVLC_DIRS')
        # path = os.path.join(dirname, filename)

        # traverse root directory, and list directories as dirs and files as files
        for root, dirs, files in os.walk("."):
            path = root.split(os.sep)
            print((len(path) - 1) * '---', os.path.basename(root))
            for file in files:
                print(len(path) * '---', file)

    def init_app(self):
        # Create a Tk.App(), which handles the windowing system event loop
        root = Tk_get_root()
        root.protocol("WM_DELETE_WINDOW", _quit)

        self.player = Player(root, title="tkinter vlc")
        self.root = root

    def start_app(self):
        # show the player window centred and run the application
        self.root.mainloop()
        self.app = ApplicationThread(self.root.mainloop)


if __name__ == "__main__":
    nano = Nano()
    nano.run()
