import wx, sys, os, pygame
import pygame.camera

pygame.init()
pygame.camera.init()

class PygameDisplay(wx.Window):
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.parent = parent
        self.hwnd = self.GetHandle()

        self.size = 640,480
        self.size_dirty = True

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.Update, self.timer)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            print '\nFATAL ERROR: NO CAMERA ATTACHED TO SYSTEM\n'
            exit()

        self.screen = pygame.Surface(self.size, 0, 32)
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()
        self.snapshot = pygame.Surface(self.size, 0, self.screen)

        self.fps = 30.0
        self.timespacing = 1000.0 / self.fps
        self.timer.Start(self.timespacing, False)

    def Update(self, event):
        self.Redraw()

    def Redraw(self):
        if self.size_dirty:
            self.screen = pygame.Surface(self.size, 0, 32)
            self.size_dirty = False
            self.snapshot = pygame.Surface(self.size, 0, self.screen)

        self.snapshot = self.cam.get_image(self.snapshot)
        self.snapshot = pygame.transform.flip(self.snapshot, True, False)

        self.picture = pygame.image.tostring(self.snapshot, 'RGB', False)
        self.screen.blit(self.snapshot, (0, 0))

        s = pygame.image.tostring(self.screen, 'RGB')
        img = wx.ImageFromData(self.size[0], self.size[1], s)
        bmp = wx.BitmapFromImage(img)
        dc = wx.ClientDC(self)
        dc.DrawBitmap(bmp, 0, 0, False)
        del dc

        #pygame.display.flip()

    def OnPaint(self, event):
        self.Redraw()
        event.Skip()

    def OnSize(self, event):
        self.size = self.GetSizeTuple()
        self.size_dirty = True

    def Kill(self, event):
        self.Unbind(event = wx.EVT_PAINT, handler = self.OnPaint)
        self.Unbind(event = wx.EVT_TIMER, handler = self.Update, source = self.timer)