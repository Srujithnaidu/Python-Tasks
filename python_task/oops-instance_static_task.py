class SmartPhone:
    brand="IQOO"
    def assign_data(self,model,cost):
        self.model=model
        self.cost=cost
    def display_details(self):
        print("Brand: ",SmartPhone.brand)
        print("Model name: ",self.model)
        print("Cost: ",self.cost)
        

s1=SmartPhone()
s1.assign_data("Z7 Pro", 27000)
s1.display_details()

s2=SmartPhone()
s2.assign_data("15", 77000)
s2.display_details()


# ====================================================================

class MovieTheatre:
    location="Hyderabad"
    def assign_data(self,t_name,t_screen):
        self.t_name=t_name
        self.t_screen=t_screen
    def display_details(self):
        print("Theatre name: ",self.t_name)
        print("Theatre screen: ",self.t_screen)

s1=MovieTheatre()
s1.assign_data("Sandhya", "70 MM")
s1.display_details()

s2=MovieTheatre()
s2.assign_data("Sudharshan", "35 MM")
s2.display_details()
