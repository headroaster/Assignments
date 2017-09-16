import os
import wx
import datetime

prompts = ["What line did this\n come in on?", "Is the TID available?",
      "Why is this person\n calling you?", "Callers name?",
      "Callback Number?", "Is the safe serial\n available?",
      "Street Address?", "Zip Code?",
      "What did you do,\n or what needs\n to be done?"]

class Mywin(wx.Frame):
   def __init__(self, parent, title):
      super(Mywin, self).__init__(parent, title = title,size = (320,470), style= wx.CAPTION | wx.CLOSE_BOX)


      panel = wx.Panel(self)
      SetBackgroundColour(wx.BLACK)
      font = wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.SLANT, wx.NORMAL)
      SetFont(font)

      vbox = wx.BoxSizer(wx.VERTICAL)




   def fieldMaker():
      for item in prompts:
          n = str(prompts.index(item)+1)
          l = 'l'+n
          t = 't'+n
          l = wx.StaticText(panel, -1, item)
          l.SetForegroundColour((wx.WHITE))
          hbox+n.Add(l, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
          t = wx.TextCtrl(panel)
          hbox+n.Add(t,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
          t.Bind(wx.EVT_TEXT,OnKeyTyped)
          vbox.Add(hbox+n, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)
          return

       
      fieldMaker()

       
      hbox10 = wx.BoxSizer(wx.HORIZONTAL)

      hbox10.AddSpacer(5)

      btn2 = wx.Button(panel, -1, "Clear")
      hbox10.Add(btn2, 1, wx.ALIGN_LEFT)
      btn2.Bind(wx.EVT_BUTTON, clear)

      hbox10.AddSpacer(80)

      btn = wx.Button(panel, -1, "Add This to Notes")
      hbox10.Add(btn, 1, wx.ALIGN_RIGHT)
      btn.Bind(wx.EVT_BUTTON, takeNote)

      hbox10.AddSpacer(5)

      vbox.Add(hbox10, wx.ALL)
   



   MyWin.Centre()
   MyWin.Show()
   MyWin.Fit()




app = wx.App()
Mywin(None,  'Note Maker')
app.MainLoop()
