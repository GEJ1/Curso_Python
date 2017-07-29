##Laburando con SysArgv

#~ import wx
#~ import sys

#~ class MyApp(wx.App):
    #~ def OnInit(self):
        #~ args = sys.argv[1:]
        #~ frame = wx.Frame(None, -1, "args = %s" % (args,))
        #~ frame.Show(True)
        #~ self.SetTopWindow(frame)
        #~ return True

#~ app = MyApp(0)
#~ app.MainLoop()



## tomar input del usuario

#~ import wx

#~ def ask(parent=None, message='', default_value=''):
    #~ dlg = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    #~ dlg.ShowModal()
    #~ result = dlg.GetValue()
    #~ dlg.Destroy()
    #~ return result

#~ # Initialize wx App
#~ app = wx.App()
#~ app.MainLoop()

#~ # Call Dialog
#~ x = ask(message = 'What is your name?')
#~ print 'Your name was', x


# -*- coding: utf-8 -*-
#!/usr/bin/env python


#!/usr/bin/env python
#!/usr/bin/env python
#~ import os
#~ import wx


#~ class MainWindow(wx.Frame):
    #~ def __init__(self, parent, title):
        #~ wx.Frame.__init__(self, parent, title=title, size=(200,100))
        #~ self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        #~ self.CreateStatusBar() # A StatusBar in the bottom of the window

        #~ # Setting up the menu.
        #~ filemenu= wx.Menu()

        #~ # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        #~ menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        #~ menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        #~ # Creating the menubar.
        #~ menuBar = wx.MenuBar()
        #~ menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        #~ self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        #~ # Set events.
        #~ self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        #~ self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        #~ self.Show(True)

    #~ def OnAbout(self,e):
        #~ # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        #~ dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        #~ dlg.ShowModal() # Show it
        #~ dlg.Destroy() # finally destroy it when finished.

    #~ def OnExit(self,e):
        #~ self.Close(True)  # Close the frame.

#~ app = wx.App(False)
#~ frame = MainWindow(None, "Sample editor")
#~ app.MainLoop()

#!/usr/bin/env python

#!/usr/bin/env python

from functools import partial
import wx

class DemoFrame(wx.Frame):
    """ This window displays a set of buttons """
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        sizer = wx.BoxSizer(wx.VERTICAL)
        for button_name in ["first", "second", "third"]:
            btn = wx.Button(self, label=button_name)
            btn.Bind(wx.EVT_BUTTON, partial( self.OnButton, button_label = button_name ) )
            sizer.Add(btn, 0, wx.ALL, 10)

        self.SetSizerAndFit(sizer)
        
    def OnButton(self, Event, button_label):
        print "In OnButton:", button_label


app = wx.App(False)
frame = DemoFrame(None, title="functools.partial Bind Test")
frame.Show()
app.MainLoop()
