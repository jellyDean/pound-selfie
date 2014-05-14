import wx
from View import MainFrame
import pygame
import datetime, time
import pexif
import Dropbox.DropBoxFuncts as dbo
import os
#import Utils.FileUtils as fu

pygame.init()
class MainController:
    def __init__(self):
        self.mainWindow = MainFrame(None)
        self.save_path = os.getcwd()#(os.environ['HOME'], 'WebcamPhotos')
        #import pdb; pdb.set_trace()
        #fu.checkWriteOnDirectory(self.save_path)

        self.mainWindow.btnPhoto.Bind(wx.EVT_BUTTON, self.onClick)
        self.mainWindow.Bind(wx.EVT_CLOSE, self.Close, self.mainWindow)
        #self.base_path = 'C:\\workdir\\Media Space Manager\\MediaSpaceManager\\Dropbox'
        #key,secret = dbo.config()
        #self.client = dbo.connect(key,secret)
        #dbo.connect()


    def show(self):
        self.mainWindow.Show()


    def Close(self, event):
        exit()

    def onClick(self, event):
        img = pygame.image.frombuffer(self.mainWindow.display.picture, self.mainWindow.display.size, 'RGB')
        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        pygame.image.save(img, '%s.jpeg' % date)
        time.sleep(1)

        filename = date + '.jpeg'

        with open(filename, 'rb'):
            jpeg = pexif.JpegFile.fromFile(filename)
            exif = jpeg.get_exif(create=True)
            exif.primary.ExtendedEXIF.DateTimeOriginal = date
            #print os.getcwd() + '\\' + filename
            #dbo.upload_file(self.client,filename,'Camera Uploads')

