import customtkinter
import tkinter
from PIL import Image


"""
Icons:
    Home by adrianadam https://www.flaticon.com/authors/adrianadam
    Flame by Aldo Cervantes https://www.flaticon.com/authors/aldo-cervantes
    Settings by Freepik https://www.freepik.com
    To Do by Graphics Plazza https://www.flaticon.com/authors/graphics-plazza
    Goals steps by Andrejs Kirma https://www.flaticon.com/authors/adrianadam
    X icon by Pixel Perfect https://www.flaticon.com/authors/pixel-perfect
    Default wallpaper by Photo by Codioful (formerly Gradienta) https://www.pexels.com/photo/colorful-abstract-background-with-lines-and-lights-6985045/
    Settings wallpaper Photo by Artem Podrez https://www.pexels.com/photo/a-laptop-with-a-white-screen-4884105/
    Tasks wallpaper by Photo by Tirachard Kumtanom https://www.pexels.com/photo/white-blank-notebook-733857/

"""

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("midnight.json")

globalData = []
gbdata = open("globaldata.txt", "r")

for line in gbdata:
    globalData.append(line.strip())

print(globalData)

#Import Logo
#logo = Image.open("TFLogo6.jpg")
#logoImage = customtkinter.CTkImage(light_image=logo, size=(300, 300))

#Import Home wallpaper
wallpaperImage = Image.open("goalsWallpaper.jpg")
wallpaper = customtkinter.CTkImage(light_image=wallpaperImage, size=(920, 250))

goalsBackgroundImage = Image.open("goalsWallpaper.jpg")
goalsBackground = customtkinter.CTkImage(light_image=goalsBackgroundImage, size=(920, 650))

tasksBackgroundImage = Image.open("tasksWallpaper.jpg")
tasksBackground = customtkinter.CTkImage(light_image=tasksBackgroundImage, size=(920, 650))

settingsBackgroundImage = Image.open("settingsWallpaper.jpg")
settingsBackground = customtkinter.CTkImage(light_image=settingsBackgroundImage, size=(920, 650))

WIPImage = Image.open("WIPIcon.png")
WIPIcon = customtkinter.CTkImage(light_image=WIPImage, size=(200, 200))



#Import Home icon
homeImage = Image.open("homeIcon.png")
homeIcon = customtkinter.CTkImage(light_image=homeImage, size=(40, 40))

#Import Flame icon
flameImage = Image.open("flameIcon.png")
flameIcon = customtkinter.CTkImage(light_image=flameImage, size=(40, 40))

#Import To Do Icon
todoImage = Image.open("todoIcon.png")
todoIcon = customtkinter.CTkImage(light_image=todoImage, size=(40, 40))

#Import Goals Icon
goalsImage = Image.open("goalsIcon.png")
goalsIcon = customtkinter.CTkImage(light_image=goalsImage, size=(40, 40))

#Import Close [X] Icon
closeImage = Image.open("xIcon.png")
closeIcon = customtkinter.CTkImage(light_image=closeImage, size=(20, 20))

#Import Settings Icon
settingsImage = Image.open("settingsIcon.png")
settingsIcon = customtkinter.CTkImage(light_image=settingsImage, size=(30, 30))





class home(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
    
        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        self.configure(fg_color="#EEEEEE")

        self.titleFont = customtkinter.CTkFont(family="Roboto", size=40, weight="bold")



        #0 is first time, 1 is return
        if int(globalData[3]) == 0:

            globalData[0] = self.getName()
            globalData[3] = "1"
            
            self.wallpaper = customtkinter.CTkLabel(self,
                                                    text="Welcome to Taskflow, " + globalData[0] + "!",
                                                    text_color="black",
                                                    font=self.titleFont,
                                                    fg_color="white",
                                                    image=wallpaper,
                                                    corner_radius=0,
                                                    )
        else:
            self.wallpaper = customtkinter.CTkLabel(self,
                                                    text="Welcome back, " + globalData[0] + "!",
                                                    text_color="black",
                                                    font=self.titleFont,
                                                    fg_color="white",
                                                    image=wallpaper,
                                                    corner_radius=0,
                                                    )                       

        self.wallpaper.grid(row=0, column=0, columnspan=2, sticky="nw")


        WIPlabel = customtkinter.CTkLabel(self, text="Home widgets in progress!", font=("", 20), fg_color="#EEEEEE", text_color="gray20")
        WIPlabel.grid(row=1, column=0, columnspan=2, sticky="new", pady=40)

    
           
    def getName(self):
        dialog = customtkinter.CTkInputDialog(text="It's your first time here. What's your name?", title="")
        return dialog.get_input()
        

class taskFrame(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        #The list of tasks and their 1/0 states. Printed into file at file close.
        self.taskList = []
        self.taskState = []
        
        self.configure(fg_color='transparent')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.wallpaper = customtkinter.CTkLabel(self,
                                                text="",
                                                image=tasksBackground,
                                                corner_radius=0,
                                                )

        self.wallpaper.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")

        with open("tasks.txt", "r") as tasksFile:
            for line in tasksFile:    
                self.taskList.append(line[:-2])
                self.taskState.append(customtkinter.IntVar(value=line[-2:-1]))
                
        """
        with open("tasks.txt", "a") as tasksFile:
            tasksFile.write("hey.\nhey.\n")
        """

        """

        self.chooseGoal = customtkinter.CTkComboBox(self,
                                                    corner_radius=10,
                                                    fg_color="white",
                                                    border_color="white",
                                                    values=self.controller.goals,
                                                    font=("", 30),
                                                    dropdown_font=("", 25),
                                                    height=60,
                                                    width=350,
                                                    state="readonly",
                                                    )
        self.chooseGoal.grid(row=1, column=0, columnspan=2, padx=20, pady=(10, 10), sticky="nw")
        
        """

        # create checkbox and switch frame
        #self.checkbox_slider_frame = customtkinter.CTkFrame(self, fg_color="#BCC6D0")
        self.checkbox_slider_frame = customtkinter.CTkScrollableFrame(self,
                                                                      height=350,
                                                                      #label_text="Tasks",
                                                                      #label_fg_color="white",
                                                                      #label_font=("", 40),
                                                                      #label_anchor="sw",
                                                                      fg_color="white",
                                                                      border_width=2,
                                                                      border_color="gray60",
                                                                      corner_radius=0
                                                                      )
        self.checkbox_slider_frame.grid(row=2, column=0, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        """
        title = customtkinter.CTkLabel(text="  Tasks",
                                       master=self.checkbox_slider_frame,
                                       font=("",40)
                                       )
        #title.grid(row=0, column=0, pady=(30,0), padx=10, sticky="nsw")
        """

        
        self.checkboxes = []

        #create checkboxes from file
        for task in range(len(self.taskList)):
            checkbox = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame,
                                                      text=self.taskList[task],
                                                      corner_radius=15,
                                                      font=("", 20),
                                                      checkbox_width=30,
                                                      checkbox_height=30,
                                                      border_width=2,
                                                      border_color="black",
                                                      hover_color="gray70",
                                                      fg_color="black",
                                                      hover=True,
                                                      variable=self.taskState[task],
                                                      #lambda so the function will accept the index
                                                      command=lambda: self.switchState(task),
                                                      #command=self.destroy_checkbox,
                                                      )
            self.checkboxes.append(checkbox)

        self.createTasks()

        #New task entry box
        self.newTaskEntry = customtkinter.CTkEntry(self,
                                                   placeholder_text="New task",
                                                   height=50,
                                                   fg_color="white",
                                                   corner_radius=0,
                                                   font=("", 20))
        self.newTaskEntry.grid(row=3, column=0, padx=(20,0), pady=(0, 20), sticky="nsew")

        #Add new task button
        self.addTaskBtn = customtkinter.CTkButton(self,
                                                  text="+",
                                                  font=("", 40),
                                                  corner_radius=0,
                                                  width=45,
                                                  height=50,
                                                  command=self.addTask)
        self.addTaskBtn.grid(row=3, column=1, padx=(5, 20), pady=(0, 20), sticky="nsew")


    def switchState(self, index):
        if self.taskState[index] == 1:
            self.taskState[index] = customtkinter.IntVar(value=0)
        else:
            self.taskState[index] = customtkinter.IntVar(value=1)

    def addTask(self):

        if self.newTaskEntry.get() != "":        
            self.taskList.append(self.newTaskEntry.get())
            self.taskState.append(customtkinter.IntVar(value=0))

            #Clear entry box
            self.newTaskEntry.delete(0, customtkinter.END)

            self.checkboxes.append(customtkinter.CTkCheckBox(master=self.checkbox_slider_frame,
                                                 text=self.taskList[len(self.taskList)-1],
                                                 corner_radius=15,
                                                 font=("", 20),
                                                 checkbox_width=30,
                                                 checkbox_height=30,
                                                 border_width=2,
                                                 border_color="black",
                                                 hover_color="gray70",
                                                 fg_color="black",
                                                 hover=True,
                                                 variable=self.taskState[len(self.taskList)-1],
                                                 #lambda so the function will accept the index
                                                 command=lambda: self.switchState(len(self.taskList)-1),
                                                 #command=self.destroy_checkbox,
                                                 ))

        
            self.createTasks()


    def createTasks(self):
        """
        for widget in self.checkboxes:
            widget.destroy()
        self.checkboxes.clear()
        """
        for task in range(len(self.taskList)):
            self.checkboxes[task].grid(row=task+1, column=0, pady=(20, 0), padx=(30,30), sticky="nw")
            
            
    """
    def destroy_checkbox(self):
        for checkbox in range(len(self.checkboxes)):
            if self.checkboxes[checkbox].get():
                self.checkboxes[checkbox].destroy()
                self.checkboxes.remove(self.checkboxes[checkbox])
    """
        

class tasks(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color="#DCE4EE")
        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        

        """title = customtkinter.CTkLabel(self,
                                       image=logoImage,
                                       text="", 
                                       anchor="w"
                                       )
                                       
        title.grid(row=0, column=0, padx=(0, 0), pady=(20, 20))
        """

        #Make a CTK Combobox to select the To-Do lists for each goal,
        #Make seperate files for each goal,
        #Goal progress bar above task list

        self.taskframe = taskFrame(self,
                                   controller=self.controller)
        self.taskframe.grid(row=0, column=0, columnspan=2, sticky="nwes")
        
        

class goals(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        
        title2 = customtkinter.CTkLabel(self,
                                       image=WIPIcon,
                                       text="")
        title2.grid(row=0, column=0)

class trends(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        
        title2 = customtkinter.CTkLabel(self,
                                       image=WIPIcon,
                                       text="")
        title2.grid(row=0, column=0)
        

class settings(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(self,
                                       text="",
                                       image=settingsBackground)
        title.grid(row=0, column=0, sticky="nw")


        WIPlabel = customtkinter.CTkLabel(self, fg_color="#FAFAFA", height=50, text="Preferences page in progress!", font=("", 30), text_color="gray20")
        WIPlabel.grid(row=0, column=0, sticky="new", padx=180, pady=(240, 0))

    

class NavigationFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.configure(fg_color="white")

        self.grid_columnconfigure(0, weight=0, minsize=0, pad=0)
        self.grid_rowconfigure(6, weight=1)
        
        #self.grid_rowconfigure(1, weight=1)
        """
        title = customtkinter.CTkLabel(self,
                                       image=ctk_image,
                                       text="", 
                                       anchor="center", 
                                       font=("Helvetica Light", 20))
        title.grid(row=0, column=0, padx=(0, 0), pady=(20, 20))
        """
        homeBtn = customtkinter.CTkButton(self,
                                          image=homeIcon,
                                          text="Home",
                                          compound="top",
                                          border_spacing=4,
                                          font=customtkinter.CTkFont(family="Arial", size=15, weight="bold"),
                                          anchor="center",
                                          fg_color="transparent", 
                                          text_color="black",
                                          hover_color="#F0F0F0",
                                          corner_radius=5,
                                          command=self.homeScreen)
        homeBtn.grid(row=2, column=0, padx=(0, 0), pady=(30, 0), sticky="ew")


        tasksBtn = customtkinter.CTkButton(self, 
                                           image=todoIcon,
                                           text="Tasks",
                                           compound="top",
                                           border_spacing=4,
                                           font=customtkinter.CTkFont(family="Arial", size=15, weight="bold"),
                                           anchor="center",
                                           fg_color="transparent", 
                                           text_color="black",
                                           hover_color="#F0F0F0",
                                           corner_radius=5,
                                           command=self.tasksScreen)
        tasksBtn.grid(row=3, column=0, padx=(0, 0), pady=(30,0), sticky="ew")


        goalsBtn = customtkinter.CTkButton(self, 
                                           image=goalsIcon,
                                           text="Goals",
                                           compound="top",
                                           border_spacing=4,
                                           font=customtkinter.CTkFont(family="Arial", size=15, weight="bold"),
                                           anchor="center",
                                           fg_color="transparent", 
                                           text_color="black",
                                           hover_color="#F0F0F0",
                                           corner_radius=5,
                                           command=self.goalsScreen)
        goalsBtn.grid(row=4, column=0, padx=(0, 0), pady=(30,0), sticky="ew")

        trendsBtn = customtkinter.CTkButton(self, 
                                            image=flameIcon,
                                            text="Trends",
                                            compound="top",
                                            border_spacing=4,
                                            font=customtkinter.CTkFont(family="Arial", size=15, weight="bold"),
                                            anchor="center",
                                            fg_color="transparent", 
                                            text_color="black",
                                            hover_color="#F0F0F0",
                                            corner_radius=5,
                                            command=self.trendsScreen)
        trendsBtn.grid(row=5, column=0, padx=(0, 0), pady=(30,0), sticky="ew")


        settingsBtn = customtkinter.CTkButton(self, 
                                             image=settingsIcon,
                                             text="",
                                             compound="top",
                                             border_spacing=4,
                                             font=("Helvetica", 10),
                                             anchor="center",
                                             fg_color="transparent", 
                                             text_color="black",
                                             hover_color="#F0F0F0",
                                             corner_radius=5,
                                             command=self.settingsScreen)
        settingsBtn.grid(row=6, column=0, padx=(0, 0), pady=(30,0), sticky="esw")

        settingsBtn = customtkinter.CTkButton(self, 
                                             image=closeIcon,
                                             text="",
                                             compound="top",
                                             border_spacing=4,
                                             font=("Helvetica", 10),
                                             anchor="center",
                                             fg_color="transparent", 
                                             text_color="black",
                                             hover_color="#F0F0F0",
                                             corner_radius=5,
                                             command=self.closeApp)
        settingsBtn.grid(row=7, column=0, padx=(0, 0), pady=20, sticky="esw")
    

    def homeScreen(self):
        self.controller.scene = 0
        self.controller.switchScreen()

    def tasksScreen(self):
        self.controller.scene = 1
        self.controller.switchScreen()

    def goalsScreen(self):
        self.controller.scene = 2
        self.controller.switchScreen()

    def trendsScreen(self):
        self.controller.scene = 3
        self.controller.switchScreen()

    def settingsScreen(self):
        self.controller.scene = 4
        self.controller.switchScreen()
       
    def closeApp(self):
        self.controller.scene = 5
        self.controller.switchScreen()
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Taskflow")
        self.geometry("1000x650")

        self.grid_columnconfigure(0, weight=0, pad=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        self.home = home(self, controller=self)
        self.tasks = tasks(self, controller=self)
        self.goals = goals(self, controller=self)
        self.trends = trends(self, controller=self)
        self.settings = settings(self, controller=self)

        self.scene = 0

        self.switchScreen()

    
        self.navigation = NavigationFrame(self, controller=self)
        self.navigation.grid(row=0, column=0, sticky="ns")






       
    def switchScreen(self):
        if self.scene != 5:
            for widget in self.winfo_children():
                if type(widget) != NavigationFrame:
                    widget.grid_forget()


        #Equivalent of switch case statement in JavaScript (optimization)

        
        match self.scene:
            case 0:
                self.home.grid(row=0, column=1, sticky="nsew")
                
            case 1:

                self.tasks.grid(row=0, column=1, sticky="nsew")

            case 2:
                self.goals.grid(row=0, column=1, sticky="nsew")
        
            case 3:
                self.trends.grid(row=0, column=1, sticky="nsew")
        
            case 4:
                self.settings.grid(row=0, column=1, sticky="nsew")

            case 5:
                textFile = open("tasks.txt", "w")
                
                for i in range(len(self.tasks.taskframe.taskList)):
                    #For debugging
                    #print(self.taskList[i] + str(self.taskState[i].get()))     
                    textFile.write(self.tasks.taskframe.taskList[i] + str(self.tasks.taskframe.taskState[i].get()) + '\n')   
                textFile.close()

                gbdata = open("globalData.txt", "w")
                
                for i in range(len(globalData)):
                    gbdata.write(globalData[i] + '\n')   
                gbdata.close()
                
                self.destroy()
                

#Save changes when the app is closed
def on_closing():
    app.scene = 5
    app.switchScreen()

app = App()
app.resizable(0, 0)
app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()


