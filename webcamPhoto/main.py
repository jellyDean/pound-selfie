import wx
from Controller import MainController


class App(wx.App):
    def OnInit(self):
        self.frame = MainController()
        self.frame.show()

        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()