import glob
import wx, wx.lib.pubsub
 
#from wx.lib.pubsub import Publisher
 
########################################################################
class ViewerFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Image Viewer")
        panel = ViewerPanel(self)
        self.folderPath = ""
        Publisher().subscribe(self.resizeFrame, ("resize"))
 
        self.initToolbar()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
 
        self.Show()
        self.sizer.Fit(self)
        self.Center()
 
    #----------------------------------------------------------------------
    def initToolbar(self):
        """
        Initialize the toolbar
        """
        self.toolbar = self.CreateToolBar()
        self.toolbar.SetToolBitmapSize((16,16))
 
        open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (16,16))
        openTool = self.toolbar.AddSimpleTool(wx.ID_ANY, open_ico, "Open", "Open an Image Directory")
        self.Bind(wx.EVT_MENU, self.onOpenDirectory, openTool)
 
        self.toolbar.Realize()
 
    #----------------------------------------------------------------------
    def onOpenDirectory(self, event):
        """
        Opens a DirDialog to allow the user to open a folder with pictures
        """
        dlg = wx.DirDialog(self, "Choose a directory",
                           style=wx.DD_DEFAULT_STYLE)
 
        if dlg.ShowModal() == wx.ID_OK:
            self.folderPath = dlg.GetPath()
            print self.folderPath
            picPaths = glob.glob(self.folderPath + "\\*.jpg")
            print picPaths
        Publisher().sendMessage("update images", picPaths)
 
    #----------------------------------------------------------------------
    def resizeFrame(self, msg):
        """"""
        self.sizer.Fit(self)