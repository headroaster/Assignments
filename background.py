def gatherNotes ():
    prompts = ({self.t1 : "Customer Name: ", self.t2 : "TID:  ",
        self.t3 : "Call Driver: ", self.t5 : "Caller's Name: ",
        self.t6 : "Phone Number: ", self.t4 : "Serial Number: ",
        self.t7 : "Street Address: ", self.t8 : "ZIP or Postal Code: ",
        self.t9 : "Notes: "})
    gathered = ({})
    for item in prompts:
        gathered[prompts[item]] = item.GetValue()
        print(gathered)
    return gathered


def ticket():
    base_url = "http://app00.pendum.com/ServiceCenter/ServiceCallDetail.aspx?type=serviceC"
#This gathers your username, and password.
    userUName = "dcretan"
    userPWord = "BURR2015"
#This gathers the necessary information to fill out the ticket.
    inputNotes = gatherNotes()
#This opens and signs in to the website for work
    login(base_url, userUName, userPWord)
#This opens a phone support ticket making sure we're opening a ticket for a valid customer.
    getTarget()
    makeTicket()
#Creates .txt documents capturing call number created and  notes gathered for and submitted to this call
    documentThis()
    documentThat()
#Closes the browser
    driver.close()
    return
    
