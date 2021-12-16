# import tkinter as tk
# from tkinter.constants import BOTH, CENTER, RIGHT, S, SOLID, TOP 
# GOODNEWSCOLOR = "#0D4851"
# GOODNEWSCOLOR2= "#E9C694"
# appfont = ("Helvetica", 24)

# def CheckPassword(_username, _password):

	


# root = tk.Tk()
# root.title("BarManager")
# root.geometry("1920x1080")
# mainFrame= tk.Frame(root, bg= GOODNEWSCOLOR, height=root.winfo_height(), width=root.winfo_width())
# mainFrame.pack(fill=BOTH, expand=True)
# nameLabel = tk.Label(mainFrame, text= "GOOD NEWS BAR", font= appfont, fg = GOODNEWSCOLOR2, bg = GOODNEWSCOLOR)
# nameLabel.pack(side=TOP, pady=30)


# connectFrame = tk.Frame(mainFrame, width= 800, height= 500, highlightcolor=GOODNEWSCOLOR2, highlightthickness=5, bg=GOODNEWSCOLOR)
   
# usernameLabel = tk.Label(connectFrame, text = "Nom d'utilisateur : ",font= appfont, bg = GOODNEWSCOLOR, fg = GOODNEWSCOLOR2).grid(row=1, column=0)
# un = tk.StringVar()
# usernameInput = tk.Entry (connectFrame, textvariable=un,  font= appfont).grid(row=1, column=1, pady=30)
# passwordLabel = tk.Label(connectFrame, text ="Mot de passe : ", font= appfont,bg = GOODNEWSCOLOR, fg = GOODNEWSCOLOR2).grid(row=2, column=0)
# up = tk.StringVar()
# passwordInput = tk.Entry(connectFrame,textvariable=up,show="*",font= appfont).grid(row=2, column=1, pady=30)
# connectFrame.pack(expand=True, ipadx= 30,anchor=CENTER,)
# ConnectionButton = tk.Button(connectFrame, text= "Se connecter", font = appfont).grid(row=3,column=0, columnspan=4,sticky=S, pady= 30)    

# root.mainloop()


