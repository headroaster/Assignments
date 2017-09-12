import wx

class Mywin(wx.Frame):
   def __init__(self, parent, title):
      super(Mywin, self).__init__(parent, title = title,size = (345,475), style= wx.CAPTION | wx.CLOSE_BOX)

      panel = wx.Panel(self)
      self.SetBackgroundColour(wx.BLACK)



      vbox = wx.BoxSizer(wx.VERTICAL)

      hbox1 = wx.BoxSizer(wx.HORIZONTAL)
      l1 = wx.StaticText(panel, -1, "What line did this\n come in on?")
      l1.SetForegroundColour((wx.WHITE))
      hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t1 = wx.TextCtrl(panel)
      hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox1)

      hbox2 = wx.BoxSizer(wx.HORIZONTAL)
      l2 = wx.StaticText(panel, -1, "Is the TID available?")
      l2.SetForegroundColour((wx.WHITE))
      hbox2.Add(l2, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t2 = wx.TextCtrl(panel)
      hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t2.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox2)

      hbox3 = wx.BoxSizer(wx.HORIZONTAL)
      l3 = wx.StaticText(panel, -1, "Why is this person\n calling you?")
      l3.SetForegroundColour((wx.WHITE))
      hbox3.Add(l3, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t3 = wx.TextCtrl(panel)
      hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t3.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox3)

      hbox4 = wx.BoxSizer(wx.HORIZONTAL)
      l4 = wx.StaticText(panel, -1, "Is the safe serial\n available?")
      l4.SetForegroundColour((wx.WHITE))
      hbox4.Add(l4, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t4 = wx.TextCtrl(panel)
      hbox4.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t4.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox4)

      hbox5 = wx.BoxSizer(wx.HORIZONTAL)
      l5 = wx.StaticText(panel, -1, "Callers name?")
      l5.SetForegroundColour((wx.WHITE))
      hbox5.Add(l5, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t5 = wx.TextCtrl(panel)
      hbox5.Add(self.t5,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t5.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox5)

      hbox6 = wx.BoxSizer(wx.HORIZONTAL)
      l6 = wx.StaticText(panel, -1, "Callback Number?")
      l6.SetForegroundColour((wx.WHITE))
      hbox6.Add(l6, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t6 = wx.TextCtrl(panel)
      hbox6.Add(self.t6,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t6.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox6)

      hbox7 = wx.BoxSizer(wx.HORIZONTAL)
      l7 = wx.StaticText(panel, -1, "Street Address?")
      l7.SetForegroundColour((wx.WHITE))
      hbox7.Add(l7, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t7 = wx.TextCtrl(panel)
      hbox7.Add(self.t7,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t7.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox7)

      hbox8 = wx.BoxSizer(wx.HORIZONTAL)
      l8 = wx.StaticText(panel, -1, "Zip Code?")
      l8.SetForegroundColour((wx.WHITE))
      hbox8.Add(l8, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t8 = wx.TextCtrl(panel)
      hbox8.Add(self.t8,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t8.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox8)

      hbox9 = wx.BoxSizer(wx.HORIZONTAL)
      l9 = wx.StaticText(panel, -1, "What did you do,\n or what needs\n to be done?")
      l9.SetForegroundColour((wx.WHITE))
      hbox9.Add(l9,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t9 = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE)
      hbox9.Add(self.t9,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      vbox.Add(hbox9)
      self.t9.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)

      self.btn = wx.Button(panel, -1, "Add This to Notes")
      vbox.Add(self.btn,0,wx.ALIGN_CENTER)



      panel.SetSizer(vbox)

      self.Centre()
      self.Show()
      self.Fit()

   def OnKeyTyped(self, event):
      print (event.GetString())

   def OnEnterPressed(self,event):
      print ("Enter pressed")


app = wx.App()
Mywin(None,  'Note Taker')
app.MainLoop()