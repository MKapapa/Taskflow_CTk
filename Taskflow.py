import customtkinter
from PIL import Image


"""
Icons:
    Home by adrianadam https://www.flaticon.com/authors/adrianadam
    Flame by Aldo Cervantes https://www.flaticon.com/authors/aldo-cervantes
    Settings by Freepik https://www.freepik.com
    To Do by Graphics Plazza https://www.flaticon.com/authors/graphics-plazza
    Goals steps by Andrejs Kirma https://www.flaticon.com/authors/adrianadam

"""

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("midnight.json")


taskList = ["Rake leaves", "Eat hot dog", "Take out Dog", "Work on app", "Make this"]


#Import Logo
logo = Image.open("TFLogo6.jpg")
logoImage = customtkinter.CTkImage(light_image=logo, size=(300, 300))

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

#Import Trends Icon
trendsImage = Image.open("trendsIcon.png")
trendsIcon = customtkinter.CTkImage(light_image=trendsImage, size=(40, 40))

#Import Settings Icon
settingsImage = Image.open("settingsIcon.png")
settingsIcon = customtkinter.CTkImage(light_image=settingsImage, size=(40, 40))


class home(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        txt = "home!"
        title = customtkinter.CTkLabel(self, 
                                       text=txt, 
                                       anchor="center")
        title.grid(row=0, column=0)

class taskFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller, tasklist):
        super().__init__(parent)
        self.controller = controller

        self.tasks = tasklist
        
        self.configure(fg_color="#DCE4EE")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self, fg_color="#BCC6D0")
        self.checkbox_slider_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")


        title = customtkinter.CTkLabel(text="Tasks", master=self.checkbox_slider_frame)
        title.grid(row=0, column=0, pady=(20,0), padx=10, sticky="n")
        
        for task in range(len(self.tasks)):
            
            self.checkbox = customtkinter.CTkCheckBox(text=self.tasks[task],
                                                      master=self.checkbox_slider_frame
                                                      )
            self.checkbox.grid(row=task+1, column=0, pady=(10, 10), padx=(30,30), sticky="nsew")

    def destroy_checkbox(thing):
        thing.destroy()


class tasks(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

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

        #Make a CTK Tabview to hold the To-Do lists for each goal,
        #Have goal completion trackers on second row

        self.taskframe = taskFrame(self, controller=self, tasklist=taskList)
        self.taskframe.grid(row=0, column=0, columnspan=2, sticky="nwes")
        
        

class goals(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(self, 
                                       text="goals!", 
                                       anchor="center")
        title.grid(row=0, column=0)

class trends(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(self, 
                                       text="trends!", 
                                       anchor="center")
        title.grid(row=0, column=0)

class settings(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(self, 
                                       text="settings!", 
                                       anchor="center")
        title.grid(row=0, column=0)

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
        tasksBtn.grid(row=3, column=0, padx=(0, 0), pady=(50,0), sticky="ew")


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
        goalsBtn.grid(row=4, column=0, padx=(0, 0), pady=(50,0), sticky="ew")

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
        trendsBtn.grid(row=5, column=0, padx=(0, 0), pady=(50,0), sticky="ew")


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
        settingsBtn.grid(row=6, column=0, padx=(0, 0), pady=(20,20), sticky="esw")

        


    def homeScreen(self):
        self.controller.home.tkraise()

    def tasksScreen(self):
        self.controller.tasks.tkraise()

    def goalsScreen(self):
        self.controller.goals.tkraise()

    def trendsScreen(self):
        self.controller.trends.tkraise()

    def settingsScreen(self):
        self.controller.settings.tkraise()
       
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Taskflow GTM")

        self.after(0, lambda:self.state('zoomed'))

        self.grid_columnconfigure(0, weight=0, pad=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation = NavigationFrame(self, controller=self)
        self.navigation.grid(row=0, column=0, sticky="nesw")


        self.tasks = tasks(self, controller=self)
        self.goals = goals(self, controller=self)
        self.trends = trends(self, controller=self)
        self.settings = settings(self, controller=self)

        self.home = home(self, controller=self)

        self.home.grid(row=0, column=1, sticky="nsew")
        self.tasks.grid(row=0, column=1, sticky="nsew")
        self.goals.grid(row=0, column=1, sticky="nsew")
        self.trends.grid(row=0, column=1, sticky="nsew")
        self.settings.grid(row=0, column=1, sticky="nsew")

        
app = App()
app.mainloop()

