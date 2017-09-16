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
      panel.SetBackgroundColour(wx.BLACK)
      font = wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.SLANT, wx.NORMAL)
      panel.SetFont(font)

      def fieldMaker():
         for item in prompts:
             n = str(prompts.index(item)+1)
             l = 'l'+n
             t = 't'+n
             hbox = 'hbox' + n
             hbox = wx.BoxSizer(wx.HORIZONTAL)
             l = wx.StaticText(panel, -1, item)
             l.SetForegroundColour((wx.WHITE))
             hbox.Add(l, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
             self.t = wx.TextCtrl(panel)
             hbox.Add(self.t,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
             #self.t.Bind(wx.EVT_TEXT,self.OnKeyTyped)
             vbox.Add(hbox, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)
             return

      vbox = wx.BoxSizer(wx.VERTICAL)

      fieldMaker()

      hbox10 = wx.BoxSizer(wx.HORIZONTAL)

      hbox10.AddSpacer(5)

      def saveDocument (self):
        with open(os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
                 lines = notes.readlines()
                 with open (os.path.expanduser("~/Documents/notes/ticketNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "a") as finalNotes:
                     finalNotes.writelines(lines)
                     notes.close()
                     finalNotes.close()
                 return


      def takeNote (self, event=None):
         prompts = ({self.t1 : "Customer Name: ", self.t2 : "TID:  ",
             self.t3 : "Call Driver: ", self.t5 : "Caller's Name: ",
             self.t6 : "Phone Number: ", self.t4 : "Serial Number: ",
             self.t7 : "Street Address: ", self.t8 : "ZIP or Postal Code: ",
             self.t9 : "Notes: "})
         with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "w") as notes:
             def border():
                 notes.write("\n*********************************************************\n")
                 return
             border()
             for item in prompts:
                 notes.write(prompts[item] + item.GetValue() + "\n")
             border()
         self.saveDocument()
         return

      def clear(self, event=None):
          prompts = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7, self.t8 , self.t9]
          for item in prompts:
              item.SetValue("")

      btn2 = wx.Button(panel, -1, "Clear")
      hbox10.Add(btn2, 1, wx.ALIGN_LEFT)
      btn2.Bind(wx.EVT_BUTTON, clear)

      hbox10.AddSpacer(80)

      btn = wx.Button(panel, -1, "Add This to Notes")
      hbox10.Add(btn, 1, wx.ALIGN_RIGHT)
      btn.Bind(wx.EVT_BUTTON, takeNote)

      hbox10.AddSpacer(5)

      vbox.Add(hbox10, wx.ALL)



      self.Centre()
      self.Show()
      self.Fit()


app = wx.App()
Mywin(None,  'Here I am!')
app.MainLoop()
