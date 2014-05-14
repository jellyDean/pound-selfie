# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from PygameDisplay import PygameDisplay

###########################################################################
## Class MyFrame1
###########################################################################

class MainFrame ( wx.Frame ):
	
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.display = PygameDisplay(self, -1)
        bSizer1.Add( self.display, 1, wx.ALL|wx.EXPAND, 5 )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.HORIZONTAL )

        self.camera_radioBtn5 = wx.RadioButton( self, wx.ID_ANY, u"Picture", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.camera_radioBtn5, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

        self.video_radioBtn = wx.RadioButton( self, wx.ID_ANY, u"Video", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.video_radioBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


        bSizer1.Add( sbSizer2, 0, wx.ALIGN_BOTTOM, 5 )

        self.btnPhoto = wx.Button( self, wx.ID_ANY, u"Capture", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.btnPhoto, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass
	

