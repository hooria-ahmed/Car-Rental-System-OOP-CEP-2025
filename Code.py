# All the imports are done here
import os
import csv
from tkinter import Tk, Label,Frame, Button, Entry, Radiobutton, StringVar, PhotoImage, IntVar, Checkbutton, Toplevel,messagebox,simpledialog, ttk,BOTH,END
from PIL import Image, ImageTk
from datetime import datetime
from abc import ABC, abstractmethod

class BaseUserInterface(ABC):
    """Abstract base class for user interfaces (login, signup, etc.)."""

    def _init_(self):
        self.root = None

    @abstractmethod
    def view_profile(self):
        """Display user profile."""
        pass

    @abstractmethod
    def view_car_inventory(self):
        """Display car inventory."""
        pass


#Userdefined Exception Class
class UserError(Exception):
    """Custom exception class for user-related errors."""

    def __init__(self):
        """Initialize the UserError exception."""
        super().__init__()

    def incorrect_pass(self):
        """Return a message for incorrect password."""
        return '⚠️ Login Unsuccessful\n\n Please Enter Correct Password'
    
    def empty_input(self):
        """Return a message for empty input fields."""
        return '⚠️ Please Enter Values for all Fields'
    
    def invalid_cred(self):
        """Return a message for invalid credentials."""
        return '⚠️ Error\nInvalid Credentials'
    
    def pass_check(self):
        """Return a message for password check."""
        return '⚠️ Your Password should contain atleast 6 characters'
    
    def match_input(self):
        """Return a message for input match check."""
        return '⚠️ Match not found'
    
    def user_not_found(self):
        """Return a message for user not found."""
        return '⚠️ User not found\nPlease create an account first'
    
    def invalid_bankid(self):
        """Return a message for invalid Bank ID."""
        return '⚠️ Invalid Bank ID\nPlease enter Bank ID (6-12 characters) long'

    
    def invalid_transaction(self):
        """Return a message for invalid transaction."""
        return '⚠️ Invalid Transaction\nPlease enter Transaction Code (8-16 characters) long'



#Custom message window class
class message_window:
    """Custom message window class."""

    def __init__(self, title, message):
        """Creates a custom-styled message window."""

        # Message window configuration
        self.title = title
        self.message = message
        self.msg_window = Tk()
        self.msg_window.title(self.title)
        self.msg_window.geometry("450x150")  # Increased size
        self.msg_window.configure(bg="white")

        # Label and button for message window
        self.label = Label(self.msg_window, text=self.message, font=("Arial", 12), fg="black", bg="white")
        self.label.pack(expand=True, fill="both", padx=20, pady=20)
        self.button_ok = Button(self.msg_window, text="OK", command=self.msg_window.destroy)
        self.button_ok.pack(pady=20)


#Class for user account
class user_account:
    '''Creates user account window'''

    def __init__(self):
        """Initialize the user account window."""

        # User account window configuration
        self.root=Tk()
        self.root.config(bg='#121212')
        self.root.geometry('1920x1080')
        self.root.title('HFH Rentals Web')

        # Background image
        image = Image.open('pictures/RedMainCar.png')
        image = image.resize((1920, 1080))
        self.photo1 = ImageTk.PhotoImage(image)
        L1 = Label(self.root, image=self.photo1)
        L1.place(x=0, y=0, relwidth=1, relheight=1)

        # Label and button for user account window
        L2 = Label(self.root, text='HFH Rentals', font=('Algerian', 100, 'bold'), fg='#FFFFFF', bg='#121212')
        L2.place(relx=0.5, rely=0.1, anchor='center')
        b0 = Button(self.root, text='Admin Login', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.admin)
        b0.place(relx=0.5, rely=0.57, anchor='center')
        L3 = Label(self.root, text='OR\nCreate Account?', font=('Times New Roman', 40, 'bold'), fg='#FFFFFF', bg='#121212')
        L3.place(relx=0.5, rely=0.68, anchor='center')
        b1 = Button(self.root, text='Sign Up', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.signup)
        b1.place(relx=0.5, rely=0.8, anchor='center')
        b2 = Button(self.root, text='Log In', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.login)
        b2.place(relx=0.5, rely=0.89, anchor='center')

    def admin(self):
        """Open the admin login window."""
        self.admin = admin()
        self.admin.root.mainloop()

    def signup(self):
        """Open the sign-up window."""
        self.signup = Sign_up()
        self.signup.root.mainloop()

    def login(self):
        """Open the login window."""
        self.login = Log_in()
        self.login.root.mainloop()


#Log in class
class Log_in(BaseUserInterface):
    '''Creates log in window'''
    def __init__(self):
         '''Initialize the log in window.'''

         # Log in window configuration
         self.root = Tk()
         self.root.config(bg='#121212')
         self.root.geometry('1000x1000')
         self.root.title('LOG IN')

         # Labels, buttons  and entry for login window
         L1 = Label(self.root, text='Log In To Your Existing Account', font=('Times New Roman', 32, 'bold'), fg='#FFFFFF', bg='#121212')
         L1.place(relx=0.5, rely=0.1, anchor='n')
         L2 = Label(self.root, text='Enter Your Name:', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF', borderwidth=6)
         L2.place(relx=0.5, rely=0.2, anchor='n')
         self.username = Entry(self.root, width=20, font=('Times New Roman', 20))
         self.username.place(relx=0.5, rely=0.27, anchor='n')
         L4 = Label(self.root, text='Enter Your Password (Min-6 characters):', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF', borderwidth=6)
         L4.place(relx=0.5, rely=0.35, anchor='n')
         self.password = Entry(self.root, width=20, font=('Times New Roman', 20))
         self.password.place(relx=0.5, rely=0.42, anchor='n')
         b4 = Button(self.root, text='Submit', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.verify_login)
         b4.place(relx=0.5, rely=0.5, anchor='n')


    def verify_login(self):
        """Verify user credentials from users.csv."""
        try: 
            if self.username.get() == '' or self.password.get() == '':
                raise UserError()
        except UserError as e:
            self.message1 = e.empty_input()
            self.message_window = message_window('Error', self.message1)
            return
        
        # Check if the password is at least 6 characters long
        if len(self.password.get()) < 6:
            self.message1 = "⚠️ Password must be at least 6 characters long."
            self.message_window = message_window('Error', self.message1)
            return

        found = False
        # Check if the user exists and the password is correct
        with open("csv_files/users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3 and row[0] == self.username.get().strip() and row[2] == self.password.get().strip():
                    found = True
                    break
            try:
                if found:
                    result_text = "Login Successful!"
                    a = 'green'
                    self.result_label = Label(self.root, text=result_text, font=('Times New Roman', 15), fg=a, bg='#121212')
                    self.result_label.place(relx=0.5, rely=0.6, anchor='n')

                    b5 = Button(self.root, text='View Profile', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.view_profile)
                    b5.place(relx=0.5, rely=0.65, anchor='n')
                    b6 = Button(self.root, text='View Car Inventory', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.view_car_inventory)
                    b6.place(relx=0.5, rely=0.75, anchor='n')
                else:
                    raise UserError()
            except UserError as e:
                self.message2 = e.user_not_found()
                self.message_window = message_window('Error', self.message2)
                return

    def view_profile(self):
            """Open the user profile window."""

            # Profile window configuration
            self.root = Toplevel()
            self.root.config(bg='#610a0a')
            self.root.geometry('700x750')
            self.root.title('Profile')
            self.username_value = ""  # Store raw username without "Name: " prefix
            rented_car_found = False
            with open("csv_files/users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 5 and row[0].strip().lower() == self.username.get().strip().lower():
                        self.username_value = row[0]
                        self.Name = f"Name: {row[0]}"
                        self.Address = f"Address: {row[1]}"
                        self.gender_value = row[4].strip()
                        self.balance = f'Balance: {row[3]}'
                        Gender = f"Gender: {self.gender_value}"
                        break

            # Profile window labels and images
            self.result_Label04 = Label(self.root, text="Profile Information", font=('Arial', 30,'bold'), fg='white', bg='black')
            self.result_Label04.place(relx=0.5, rely=0.4, anchor='center')

            # Profile photo according to gender
            if  self.gender_value == "Female":
                image2=Image.open('pictures/female.jpg')
                image2= image2.resize((200,200))
            else:
                image2=Image.open('pictures/male.jpg')
                image2= image2.resize((200,200))
            self.profile_photo= ImageTk.PhotoImage(image2)

            # Label for user information
            self.L5 = Label(self.root, image=self.profile_photo)
            self.L5.place(relx=0.5, rely=0.15, anchor='center')
            self.result_Label01 = Label(self.root, text=self.Name, font=('Times New Roman', 15), fg='white', bg='black')
            self.result_Label01.place(relx=0.5, rely=0.5, anchor='center')
            self.result_Label02 = Label(self.root, text=self.Address, font=('Times New Roman', 15), fg='white', bg='black')
            self.result_Label02.place(relx=0.5, rely=0.55, anchor='center')
            self.result_Label03 = Label(self.root, text=Gender, font=('Times New Roman', 15), fg='white', bg='black')
            self.result_Label03.place(relx=0.5, rely=0.6, anchor='center')
            self.result_Label04 = Label(self.root, text=f'{self.balance}.00 PKR', font=('Times New Roman', 15), fg='white', bg='black')
            self.result_Label04.place(relx=0.5, rely=0.65, anchor='center')

            # Check if the user has rented a car
            try:
                with open('csv_files/RentedCars.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row and row[0].strip().lower() == self.username_value.strip().lower():
                            self.result_Label04 = Label(self.root, text=f'Current Rented Car: {row[2]}', font=('Times New Roman', 15), fg='white', bg='black')
                            self.result_Label04.place(relx=0.5, rely=0.7, anchor='center')
                            self.result_Label04 = Label(self.root, text=f'Car to be returned in {row[3]} day(s)', font=('Times New Roman', 15), fg='white', bg='black')
                            self.result_Label04.place(relx=0.5, rely=0.75, anchor='center')
                            self.result_Label04 = Label(self.root, text=f'Note: Make sure to return the rented car before renting another one', font=('Times New Roman', 15), fg='#ff6b6b',bg='black')
                            self.result_Label04.place(relx=0.5, rely=0.85, anchor='center')
                            return_button = Button(self.root, text="Return Car", font=("Arial", 15), bg="black", fg="white", command=self.return_car)
                            return_button.place(relx=0.15, rely=0.93, anchor='center')        
                            rented_car_found = True
                            break
                if not rented_car_found:
                    Label(self.root, text='No currently rented cars', font=('Times New Roman', 15), fg='white', bg='black').place(relx=0.5, rely=0.8, anchor='center')
            except FileNotFoundError:
                Label(self.root, text='No rental history found', font=('Times New Roman', 15), fg='white', bg='black').place(relx=0.5, rely=0.7, anchor='center')
            
            # Back button
            ok_button = Button(self.root, text="OK", font=("Arial", 15), bg="black", fg="white", command=self.root.destroy)
            ok_button.place(relx=0.9, rely=0.93, anchor='center')
    
    def return_car(self):
        """Remove the user's rental entry from RentedCars.csv and refresh the profile."""
        try:
            username = self.username_value.strip().lower()
            
            # Read all data from RentedCars.csv
            with open('csv_files/RentedCars.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)
            
            if len(rows) < 1:
                raise IndexError("Empty file")
            
            header = rows[0]
            data = rows[1:]
            
            # Filter out the user's entry
            new_data = [row for row in data if row[0].strip().lower() != username]
            
            # Write updated data back to the file
            with open('csv_files/RentedCars.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(new_data)
            
            messagebox.showinfo("Success", "Car returned successfully!")
            self.root.destroy()  # Close current profile window
            self.view_profile()  # Reopen profile to show updated status
            
        except FileNotFoundError:
            messagebox.showerror("Error", "Rental records not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to return car: {str(e)}")

        

    def view_car_inventory(self):
        """Open the car inventory window."""

        # Car inventory window configuration
        self.root=Toplevel()
        self.root.config(bg='#610a0a')
        self.root.geometry('1920x1080')
        self.root.title('Car Inventory')

        # Label and button for car inventory window
        self.result_Label = Label(self.root, text='Car Inventory', font=('Algerian', 40, 'bold'), fg='white', bg='black')
        self.result_Label.place(relx=0.5, rely=0.1, anchor='center')
        with open("csv_files/Cars.csv", "r") as file:
                reader=csv.DictReader(file)
                fieldnames= reader.fieldnames
                record=list(reader)
                x= 0.15
                y= 0.3
                self.images=[]

                # Displays the first 6 car images and names
                for idx, r in enumerate(record):
                    img_path = r.get('Picture', '').strip()
                    image = Image.open(img_path)
                    image = image.resize((180, 176))
                    self.image1 = ImageTk.PhotoImage(image)
                    self.images.append(self.image1)
                    L7 = Label(self.root, image=self.image1)
                    L7.place(relx=x, rely=y, anchor='e')
                    self.name_car = r.get('Name', '').strip()
                    b7 = Button(self.root, text=self.name_car, font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=lambda r=r: self.view_car_1(r))
                    b7.place(relx=x, rely=y+0.15, anchor='e')
                    x += 0.16
                    if len(self.images) == 6:
                        break
                x = 0.15
                y = 0.7

                # Displays the next 6 car images and names
                for idx in range(6, len(record)):
                    img_path = record[idx].get('Picture', '').strip()
                    image = Image.open(img_path)
                    image = image.resize((180, 176))
                    self.image2 = ImageTk.PhotoImage(image)
                    self.images.append(self.image2)
                    L7 = Label(self.root, image=self.image2)
                    L7.place(relx=x, rely=y, anchor='e')
                    self.name_car2 = record[idx].get('Name', '').strip()
                    car_data = record[idx]
                    b8 = Button(self.root, text=self.name_car2, font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=lambda r=record[idx]: self.view_car_2(r))
                    b8.place(relx=x, rely=y+0.15, anchor='e')
                    x += 0.16
                    if len(self.images) >= 12:
                        break

    def view_car_1(self, r):
        """Open the car details window for the first 6 cars."""

        # Car details window configuration
        self.root = Toplevel()
        self.root.config(bg='#222222')
        self.root.geometry('800x850')
        with open('csv_files/Cars.csv') as file:
            reader2 = csv.DictReader(file)
            fieldnames_2 = reader2.fieldnames
            record2 = list(reader2)
            self.name_car = r['Name'].strip()
            self.root.title(f'{self.name_car.strip()}')
            L5 = Label(self.root, text=f'{self.name_car.strip()}', font=('Algerian', 40, 'bold'), fg='white', bg='black')
            L5.place(relx=0.5, rely=0.05, anchor='center')

            #Exterior Image of Car
            img_path = r.get('Picture', '').strip()
            image = Image.open(img_path)
            image = image.resize((320, 280))
            self.image1 = ImageTk.PhotoImage(image)
            self.images.append(self.image1)
            L8 = Label(self.root, image=self.image1)
            L8.place(relx=0.98, rely=0.3, anchor='e')

            #Interior Image of Car
            img_path = r.get('Interior', '').strip()
            image = Image.open(img_path)
            image = image.resize((320, 280))
            self.image1 = ImageTk.PhotoImage(image)
            #self.images.append(self.image1)
            L8 = Label(self.root, image=self.image1)
            L8.place(relx=0.98, rely=0.7, anchor='e')
            
            #Car Specifications
            y = 0.1
            for iteration, i in enumerate(fieldnames_2):
                if iteration == 1 or iteration == 2:
                    continue
                y += 0.05
                if i == "Rental Price":  # Ensure it only modifies the price field
                    val = f"Rs. {r.get(i, '').strip()} per day"
                else:
                    val = r.get(i, '').strip()
                l = Label(self.root, text=f'{i}: {val}', font=('Times New Roman', 11), fg='black', bg='white')
                l.place(relx=0.02, rely=y, anchor='w')
    
            # Rent This Car Button
            
            rent_button = Button(self.root, text="Rent This Car", font=("Arial", 14), bg="blue", fg="white", command=lambda car=r['Name'].strip(): self.initiate_rental(car))
            rent_button.place(relx=0.2, rely=0.85, anchor='center')
    
            # Back Button
            back_button = Button(self.root, text="Back", font=("Arial", 14), bg="red", fg="white", command=self.root.destroy)
            back_button.place(relx=0.4, rely=0.85, anchor='center')


    def view_car_2(self,r):
        """Open the car details window for the next 6 cars."""

        # Car details window configuration
        self.root = Toplevel()
        self.root.config(bg='#222222')
        self.root.geometry('800x850')
        with open('csv_files/Cars.csv') as file:
            reader3 = csv.DictReader(file)
            fieldnames_3 = reader3.fieldnames
            record3 = list(reader3)
            self.name_car2 = r['Name'].strip()
            self.root.title(f'{self.name_car2.strip()}')
            L6 = Label(self.root, text=f'{self.name_car2.strip()}', font=('Algerian', 40, 'bold'), fg='white', bg='black')
            L6.place(relx=0.5, rely=0.05, anchor='center')
            
            #Exterior Image of Car
            img_path = r.get('Picture', '').strip()
            image = Image.open(img_path)
            image = image.resize((320, 280))
            self.image1 = ImageTk.PhotoImage(image)
            self.images.append(self.image1)
            L8 = Label(self.root, image=self.image1)
            L8.place(relx=0.98, rely=0.3, anchor='e')

            #Interior Image of Car
            img_path = r.get('Interior', '').strip()
            image = Image.open(img_path)
            image = image.resize((320, 280))
            self.image1 = ImageTk.PhotoImage(image)
            self.images.append(self.image1)
            L8 = Label(self.root, image=self.image1)
            L8.place(relx=0.98, rely=0.7, anchor='e')
           
            #Car Specifications
            y = 0.1
            for iteration, i in enumerate(fieldnames_3):
                if iteration == 1 or iteration == 2:
                    continue
                y += 0.05
                if i == "Rental Price":
                    val = f"Rs. {r.get(i, '').strip()} per day"
                else:
                    val = r.get(i, '').strip()
                l = Label(self.root, text=f'{i}: {val}', font=('Times New Roman', 11), fg='black', bg='white')
                l.place(relx=0.02, rely=y, anchor='w')
              
            # Rent This Car Button
            rent_button = Button(self.root, text="Rent This Car", font=("Arial", 14), bg="blue", fg="white", command=lambda car=r['Name'].strip(): self.initiate_rental(car))
            rent_button.place(relx=0.2, rely=0.85, anchor='center')


            # Back Button
            back_button = Button(self.root, text="Back", font=("Arial", 14), bg="red", fg="white", command=self.root.destroy)
            back_button.place(relx=0.4, rely=0.85, anchor='center')

    # def CarRental(self):
    #     """Open the car rental window."""
    #     self.CarRental = CarRental(self.name_car)
    #     self.CarRental.root.mainloop()

    def initiate_rental(self, selected_car):
        """Initiate the car rental process."""
        rental_app = CarRental(selected_car)
        rental_app.root.mainloop()


# Sign up class
class Sign_up(Log_in):
    '''Creates sign up window'''
    def __init__(self):
        """Initialize the sign-up window."""

        # Sign-up window configuration
        self.root = Tk()
        self.root.config(bg='#121212')
        self.root.geometry('1000x1000')
        self.root.title('SIGN UP')

        # Labels, buttons and entry for sign up window
        L1 = Label(self.root, text='Create A New Account', font=('Algerian', 32, 'bold'), fg='#FFFFFF', bg='#121212')
        L1.place(relx=0.5, rely=0.03, anchor='n')
        L2 = Label(self.root, text='Enter Your Name:', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF', borderwidth=6)
        L2.place(relx=0.5, rely=0.13, anchor='n')
        self.username = Entry(self.root, width=20, font=('Times New Roman', 20))
        self.username.place(relx=0.5, rely=0.20, anchor='n')
        L3 = Label(self.root, text='Enter Your Address:', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF', borderwidth=6)
        L3.place(relx=0.5, rely=0.26, anchor='n')
        self.address = Entry(self.root, border=None, width=30, font=('Times New Roman', 20))
        self.address.place(relx=0.5, rely=0.32, anchor='n')
        L4 = Label(self.root, text='Enter Your Bank Balance:', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF', borderwidth=6)
        L4.place(relx=0.5, rely=0.38, anchor='n')
        self.balance = Entry(self.root, width=20, font=('Times New Roman', 20))
        self.balance.place(relx=0.5, rely=0.44, anchor='n')
        L5 = Label(self.root, text='Enter Your Password (Min-6 characters):', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF', borderwidth=6)
        L5.place(relx=0.5, rely=0.5, anchor='n')
        self.password = Entry(self.root, width=20, font=('Times New Roman', 20))
        self.password.place(relx=0.5, rely=0.56, anchor='n')
        self.gender_value = StringVar(self.root, ' ')
        L6 = Label(self.root, text='Enter Your Gender', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF', borderwidth=6)
        L6.place(relx=0.5, rely=0.62, anchor='n')
        male_cb = Radiobutton(self.root, text="Male", variable=self.gender_value, value='Male', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF')
        female_cb = Radiobutton(self.root, text="Female", variable=self.gender_value, value='Female', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF')
        male_cb.place(relx=0.4, rely=0.68, anchor='n')
        female_cb.place(relx=0.58, rely=0.68, anchor='n')
        b3 = Button(self.root, text='Submit', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.save_user)
        b3.place(relx=0.5, rely=0.75, anchor='n')
        
    def save_user(self):
        """Save user information to users.csv."""

        # Checking if there are any empty fields
        try:
            user_info = [self.username.get().strip(), self.address.get().strip(), self.password.get().strip(), self.balance.get().strip(), self.gender_value.get().strip()]  # here get()(builtin function) is used to excess the value of entry widget
            if any(field == "" for field in user_info):
                raise UserError()

        except UserError as e:
                self.message1 = e.empty_input()
                self.message_window = message_window('Error', self.message1)
                return
        
        # Checking if the password is at least 6 characters long
        try: 
            password = self.password.get()
            if len(password) < 6:
                raise UserError()
            else:
                with open("csv_files/users.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(user_info)

                    # Displaying success message
                    self.result_label = Label(self.root, text="Your account has been created successfully!", font=('Times New Roman', 15), fg='green', bg='#121212')
                    self.result_label.place(relx=0.5, rely=0.8, anchor='n')
                    b13 = Button(self.root, text='View Profile', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.view_profile)
                    b13.place(relx=0.3, rely=0.85, anchor='n')
                    b14 = Button(self.root, text='View Car Inventory', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.view_car_inventory)
                    b14.place(relx=0.7, rely=0.85, anchor='n')

        except UserError as c:
            self.message = c.pass_check()
            self.message_window = message_window('Error', self.message)

    def view_profile(self):
        Log_in.view_profile(self)
        
    def view_car_inventory(self):
        Log_in.view_car_inventory(self)


#Car Rental class
class CarRental:
    """Car Rental system class."""
    def __init__(self, selected_car):
        """Initialize the Car Rental system."""
        # if not hasattr(self, 'root'):
        #     self.root = Tk()
        # else:
        #     #self.root.destroy()
        #     self.root = Tk()
        # self.root.destroy()
        #validation for selected car
        if not selected_car or not self.car_exists(selected_car):
            messagebox.showerror("Error", "Invalid car selection")
            self.root.destroy()
            return
        self.selected_car = selected_car
        self.root = Toplevel()
        self.root.config(bg='#121212')
        self.root.geometry('1000x1000')
        self.root.title('Car Rental')

        # Label, Entry and Button for confirmation details
        Label(self.root, text='Confirming Details', font=('Algerian', 32, 'bold'), fg='#FFFFFF', bg='#121212').place(relx=0.5, rely=0.03, anchor='n')
        Label(self.root, text='Confirm your name:', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF').place(relx=0.5, rely=0.13, anchor='n')
        self.confirmname = Entry(self.root, width=20, font=('Times New Roman', 20))
        self.confirmname.place(relx=0.5, rely=0.20, anchor='n')

        Label(self.root, text='Confirm your address:', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF').place(relx=0.5, rely=0.27, anchor='n')
        self.confirmaddress = Entry(self.root, width=20, font=('Times New Roman', 20))
        self.confirmaddress.place(relx=0.5, rely=0.34, anchor='n')

        Button(self.root, text='Verify', command=self.verify_user).place(relx=0.5, rely=0.42, anchor='n')

        self.root.mainloop()

    def car_exists(self, car_name):
        """Check if the car exists in Cars.csv."""
        self.car_name = car_name

        # Check if the car exists in Cars.csv.
        try:
            with open("csv_files/Cars.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Name"].strip().lower() == self.car_name.lower():
                        return True
            return False
        except FileNotFoundError:
            return False
        
    def verify_user(self):
        """Verify user's name and address from users.csv."""
        name = self.confirmname.get().strip().lower()
        address = self.confirmaddress.get().strip().lower()

        if not name or not address:
            messagebox.showerror("Error", "⚠️ Name and address cannot be empty!")
            return
        
        # Check if the name and address match in users.csv
        try:
            with open("csv_files/users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 4 and row[0].strip().lower() == name and row[1].strip().lower() == address:
                        balance = float(row[3])
                        if self.check_existing_rental(name):
                            messagebox.showerror("Rental Error", "⚠️ You already rented a car. Return it before renting another.")
                            return
                        self.show_confirmation_window(balance, name, address)
                        return

            messagebox.showerror("Error", "⚠️ Name and address do not match our records.")
        except Exception as e:
            messagebox.showerror("Error", f"⚠️ Verification failed: {str(e)}")

    def check_existing_rental(self, name):
        """Check if the user has already rented a car."""

        # Check if the user has already rented a car
        try:
            with open('csv_files/RentedCars.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0].strip().lower() == name:
                        return True
        except FileNotFoundError:
            return False
        else:
            return False

    def show_confirmation_window(self, balance, name, address):
        """Show confirmation window after successful user verification."""
        confirm_window = Toplevel(self.root)
        confirm_window.title("Match Found")
        confirm_window.geometry("400x250")
        confirm_window.config(bg="black")

        Label(confirm_window, text=f"✅ Match Found!\nBalance: {balance:.2f} PKR", font=("Arial", 14), fg="white", bg="black").pack(pady=10)
        Button(confirm_window, text="Confirm Rental", command=lambda: self.check_balance(balance, name, address, confirm_window)).pack(pady=10)

    def check_balance(self, balance, name, address, window):
        """Check balance and proceed with rental."""
        rental_days = simpledialog.askinteger("Rental Duration", "Enter the number of days for rental:")
        if rental_days is None or rental_days <= 0:
            messagebox.showerror("Error", "⚠️ Please enter a valid number of days.")
            return

        car_name = self.selected_car  # Capture correct car name
        if car_name is None:
            return  
        if not self.is_car_available(car_name):
            messagebox.showerror("Error", f"{car_name} is already rented!")
            return
        price_per_day = self.get_rental_price(car_name)
        if price_per_day is None:
            return

        total_price = price_per_day * rental_days

        if balance >= total_price:
            self.ask_bank_details(name, address, car_name, rental_days, price_per_day, total_price, window)
        else:
            messagebox.showerror("Error", "⚠️ Insufficient balance to rent this car.")

    def is_car_available(self, car_name):
        """Check if the car is available for rental."""

        # Check if the car is available for rental
        try:
            with open('csv_files/RentedCars.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[2].strip().lower() == car_name.lower():
                        return False
            return True
        except FileNotFoundError:
            return True


    def get_rental_price(self, car_name):
        """Fetch rental price per day from Cars.csv."""
        self.car_name=car_name

        try:
            with open("csv_files/Cars.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Name"].strip().lower() == self.car_name.strip().lower():
                        return float(row["Rental Price"].strip())
            messagebox.showerror("Error", f"⚠️ Rental price for '{car_name}' not found in the database.")
            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "⚠️ Cars database file not found.")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"⚠️ Failed to fetch rental price: {str(e)}")
            return None
        
    def ask_bank_details(self, name, address, car_name, rental_days, price_per_day, total_price, window):
        """Prompt user for bank authentication."""
        window.destroy()

        # Bank authentication window and Transaction code
        try:
            bank_id = simpledialog.askstring("Bank Authentication", "Enter your Bank ID (6-12 characters):")
            if 6<=len(bank_id)<=12:
                # try:
                self.bank_transcript = simpledialog.askstring("Bank Authentication", "Enter your Bank Transaction Code (8-16 characters):")
                # if not(8<=len(self.bank_transcript)<=16):
                #         raise UserError
                # except UserError as e:
                #     self.message1 = e.invalid_transaction()
                #     self.message_window = message_window('Error', self.message1)
                #     return
            else:
                raise UserError()
        except UserError as e:
            self.message1 = e.invalid_bankid()
            self.message_window = message_window('Error', self.message1)
            return

        # Check if the bank ID and transaction code are valid
        self.save_rental_info(name, address, car_name, rental_days, price_per_day, total_price)
        self.generate_receipt(bank_id, self.bank_transcript, name, address, car_name, rental_days, price_per_day, total_price)

    def save_rental_info(self, name, address, car_name, rental_days, price_per_day, total_price):
        """Save rental information to RentedCars.csv."""

        # Save rental information to RentedCars.csv
        self.name = name
        self.address = address
        self.car_name = car_name
        self.rental_days = rental_days
        self.price_per_day = price_per_day
        self.total_price = total_price

        # Check if the file exists and create it if not
        try:
            with open('csv_files/RentedCars.csv', 'a', newline='') as rented_file:
                writer = csv.writer(rented_file)
                writer.writerow([self.name, self.address, self.car_name, self.rental_days, self.price_per_day, self.total_price])

            messagebox.showinfo("Success", f"✅ {self.car_name} rented successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"⚠️ Failed to save rental info: {str(e)}")

    def generate_receipt(self, bank_id, bank_transcript, name, address, car_name, rental_days, price_per_day, total_price):
        """Generate and display the transaction receipt."""
        self.name = name
        self.address = address
        self.car_name = car_name
        self.bank_id = bank_id
        self.bank_transcript = bank_transcript
        self.rental_days = rental_days
        self.price_per_day = price_per_day
        self.total_price = total_price

        messagebox.showinfo(
            "Transaction Receipt",
            f"✔️ Payment Confirmed\n"
            f"---------------------------------\n"
            f"🏷️ User Name: {self.name}\n"
            f"🏠 Address: {self.address}\n"
            f"🚗 Car Name: {self.car_name}\n"
            f"📅 Rental Days: {self.rental_days}\n"
            f"💰 Price per Day: {self.price_per_day:.2f} PKR\n"
            f"💳 Total Price: {self.total_price:.2f} PKR\n"
            f"---------------------------------\n"
            f"🏦 Bank Details:\n"
            f"🆔 Bank ID: {self.bank_id}\n"
            f"🧾 Transaction Code: {self.bank_transcript}\n"
            f"---------------------------------\n"
            f"✅ Rental Approved. Enjoy your ride!"
        )


# Admin class
class admin:
    """Admin class for managing car rental system."""
    def __init__(self):
        """Initialize the admin window."""

        # Admin window configuration
        self.root = Toplevel()
        self.root.config(bg='#610a0a')
        self.root.geometry('700x750')
        self.root.title('Admin Login')

        # Labels and buttons for admin login
        L8 = Label(self.root, text='Admin Login', font=('Algerian', 32, 'bold'), fg='#FFFFFF', bg='#121212')
        L8.place(relx=0.5, rely=0.1, anchor='n')

        #Hardcoded password for Admin login
        self.admin_pass = 'Admin@92018'

        L7 = Label(self.root, text='Enter The Password: ', font=('Times New Roman', 15, 'bold'), fg='#121212', bg='#FFFFFF', borderwidth=6)
        L7.place(relx=0.5, rely=0.2, anchor='n')
        self.password = Entry(self.root, width=20, font=('Times New Roman', 20))
        self.password.place(relx=0.5, rely=0.3, anchor='n')
        b10 = Button(self.root, text='Submit', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.check_password)
        b10.place(relx=0.5, rely=0.4, anchor='n')

    def check_password(self):
        """Check the entered password for admin login."""

        # Check if there is an empty input
        try:
            entered_pass = self.password.get()
            if entered_pass == '':
                raise UserError()
        except UserError as e:
            self.message1 = e.empty_input()
            self.message_window = message_window('Error', self.message1)
            return
        
        # Check if the entered password matches the admin password
        try:
            if entered_pass != self.admin_pass:
                raise UserError()
            L8 = Label(self.root, text='Welcome Admin ', font=('Times New Roman', 30, 'bold'), fg='#00C853', bg='#610a0a')
            L8.place(relx=0.5, rely=0.5, anchor='n')
        except UserError as p:
            message = p.incorrect_pass()
            self.message_window = message_window("Login Unsuccessful", message)
        else:

            # Label and buttons for admin options
            L9 = Label(self.root, text='⚙️ Choose an option to proceed', font=('Times New Roman', 15), fg='white', bg='black')
            L9.place(relx=0.5, rely=0.6, anchor='n')
            b11 = Button(self.root, text='Add Car', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.add_car)
            b11.place(relx=0.3, rely=0.66, anchor='n')
            b12 = Button(self.root, text='Remove Car', font=('Times New Roman', 20), fg='#FFFFFF', bg='#121212', command=self.delete_car)
            b12.place(relx=0.7, rely=0.66, anchor='n')
            b17 = Button(self.root, text='Cars Reserved', font=('Times New Roman', 20), fg='#FFFFFF', bg='black', command=self.reserved_car)
            b17.place(relx=0.3, rely=0.77, anchor='n')
            b18 = Button(self.root, text='Current Rentals', font=('Times New Roman', 20), fg='#FFFFFF', bg='black', command=self.current_rentals)
            b18.place(relx=0.7, rely=0.77, anchor='n')

    def add_car(self):
        """Open the add car window."""

        # Add car window configuration
        self.root = Tk()
        self.root.title("Add Car")
        self.root.geometry("700x700")
        self.root.config(bg='#222222')

        # Car details labels and entries
        self.fields = ['Name', 'Picture', 'Interior', 'Rental Price', 'Model', 'Fuel Type', 'Engine Condition', 'Colour', 
                       'Navigation System (GPS)', 'Air Conditioning', 'Safety Features','Rear-view Camera or Parking Sensors',
                       'Mileage Limits','Transmission Type','Seating Capacity']
        self.entries = {}
        for idx, field in enumerate(self.fields):
            Label(self.root, text=field, fg='white', bg='#222222', font=('Arial', 15)).grid(row=idx, column=0, padx=10, pady=10)
            entry = Entry(self.root, width=30)
            entry.grid(row=idx, column=1, padx=10, pady=10)
            self.entries[field] = entry
        Button(self.root, text='Add Car', command=self.confirm_adding, font=('Arial', 12),
               fg='white', bg='#333333').grid(row=len(self.fields), column=0, columnspan=2, pady=20)
    
    def confirm_adding(self):
        """Confirm adding a new car to the inventory."""

        # Check if there are any empty fields
        try:
            car_data = {field: self.entries[field].get().strip() for field in self.fields}
            if not all(car_data.values()):
                raise UserError()
        except UserError as a:
            message= a.empty_input()
            self.message_window=message_window("Error",message)
            return
        
        # Check if the rental price is a valid number
        try:
            rental_price = float(car_data['Rental Price'])
        except ValueError:
            self.message_window = message_window("Error", "Invalid rental price. Please enter a valid number.")
            return
        
        # Check if the car name already exists in Cars.csv
        try:
            try:
                with open('csv_files/Cars.csv', 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row['Name'].strip().lower() == car_data['Name'].lower():
                            raise UserError()
            except UserError as m:
                self.message_window = message_window("Error", f"A car with the name {car_data['Name']} already exists!")
            # except FileNotFoundError:
            #     pass
            file_exists = os.path.exists('Cars.csv') and os.path.getsize('Cars.csv') > 0 # Check if Cars.csv exists and is not empty before writing the header
            with open('csv_files/Cars.csv', 'a', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=self.fields)
                    # Write header if file is empty
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(car_data)
                    self.message_window=message_window("Success", "Success!!\n\nCar added successfully!")
        except FileNotFoundError:
            pass
        # except UserError as m:
        #     self.message_window = message_window("Error", f"A car with the name {car_data['Name']} already exists!")

    def delete_car(self):
        """Open the delete car window."""

        # Delete car window configuration
        self.root = Tk()
        self.root.title("Remove Car")
        self.root.geometry("400x400")
        self.root.config(bg='black')

        # Label and entry for car name to delete
        Label(self.root, text="Enter Car Name to Delete", font=('Arial', 14), fg='white', bg='black').pack(pady=20)
        self.name_entry = Entry(self.root, width=30, font=('Arial', 12))
        self.name_entry.pack(pady=10)
        Button(self.root, text="Delete", command=self.delc, font=('Arial', 12), fg='white', bg='#CC0000').pack(pady=20)

    def delc(self):
        """Delete the specified car from the inventory."""
        model_to_delete = self.name_entry.get().strip()
        if not model_to_delete:
            self.message_window = message_window("Error", "Error\nPlease enter a car name.")
            return
        else:
            # Check if the car name exists in Cars.csv
            try:
                with open('csv_files/Cars.csv', 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    cars = list(reader)
                    fieldnames = reader.fieldnames

                new_cars = [car for car in cars if car['Name'].lower() != model_to_delete.lower()]
                deleted_count = len(cars) - len(new_cars)

                if deleted_count == 0:
                    self.message_window = message_window("Not Found", "No car with that Name found.")
                    return
                else:
                    with open('csv_files/Cars.csv', 'w', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(new_cars)
                    self.message_window = message_window("Success", f"Success\nCar with name {model_to_delete} deleted.")
            except Exception as e:
                self.message_window = message_window("Error", f"An error occurred:\n{e}")
        self.root.mainloop()


    def reserved_car(self):
        '''Display the list of reserved cars'''
        try:
            # Reserved cars window configuration
            self.root = Toplevel()
            self.root.title("Reserved Cars Information")
            self.root.geometry("700x650")
            self.root.configure(bg='black')

            # Add a heading label
            heading = Label(self.root, text="RESERVED CARS", font=('Algerian', 32, 'bold'),
                            fg='#FFFFFF', bg='black')
            heading.pack(pady=20)

            # Configure Treeview style
            style = ttk.Style()
            style.theme_use("default")

            style.configure("Treeview",
                            background="black",
                            fieldbackground="black",
                            foreground="#FFFFFF",
                            font=('Arial', 14))

            style.configure("Treeview.Heading",
                            font=('Arial', 15, 'bold'),
                            foreground='#FFFFFF',
                            background='grey')  

            # Create a Treeview widget
            tree = ttk.Treeview(self.root, columns=("col1", "col2"), show='headings')
            tree.heading("col1", text="Car Names")
            tree.heading("col2", text="No of Days Rented")
            tree.pack(fill=BOTH, expand=True)  

            # Read and insert data from CSV
            with open('csv_files/RentedCars.csv', 'r') as f:
                reader = csv.reader(f)
                try:
                    next(reader)  # Skip the header row
                except StopIteration:
                    pass  # File is empty, nothing to display

                for row in reader:
                    if len(row) >= 4:
                        tree.insert('', END, values=(row[2], row[3]))  

        except FileNotFoundError:
            message = 'No cars reserved yet'
            self.message_window = message_window('Error', message)

        # OK button to close the window
        ok_button = Button(self.root, text="OK", font=("Arial", 15), bg="black", fg="white", command=self.root.destroy)
        ok_button.place(relx=0.9, rely=0.9, anchor='center')

    def current_rentals(self):
        '''Display the list of current rentals'''

        
        try:
            # Current rentals window configuration
            self.root = Toplevel()
            self.root.title("Current Rentals")
            self.root.geometry("1920x1080")
            self.root.configure(bg='black')  # Set window background color

            # Add a heading label
            heading = Label(self.root, text="CURRENT RENTALS", font=('Algerian', 32, 'bold'),
                            fg='#FFFFFF', bg='black')
            heading.pack(pady=20)

            # Configure Treeview style
            style = ttk.Style()
            style.theme_use("default")

            style.configure("Treeview",
                            background="black",
                            fieldbackground="black",
                            foreground="#FFFFFF",
                            font=('Arial', 10))

            style.configure("Treeview.Heading",
                            font=('Arial', 15, 'bold'),
                            foreground='#FFFFFF',
                            background='grey')  # Set column headers background to grey

            # Create a Treeview widget
            tree = ttk.Treeview(self.root, columns=("col1", "col2", "col3", "col4", "col5", "col6"), show='headings')
            tree.heading("col1", text="Name")
            tree.heading("col2", text="Address")
            tree.heading("col3", text="Car Name")
            tree.heading("col4", text="Rental Days")
            tree.heading("col5", text="Price per Day in Rs")
            tree.heading("col6", text="Total Price in Rs")
            tree.pack(fill=BOTH, expand=True)  

            # Read and insert data from CSV
            with open('csv_files/RentedCars.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row

                for row in reader:
                    if len(row) >= 5:
                        tree.insert('', END, values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        except FileNotFoundError:
            message='No cars rented yet'
            self.message_window=message_window('Error', message)
        
        # OK button to close the window
        ok_button = Button(self.root, text="OK", font=("Arial", 15), bg="black", fg="white", command=self.root.destroy)
        ok_button.place(relx=0.9, rely=0.9, anchor='center')

# Main program

u1 = user_account()
u1.root.mainloop()
# s1 = Sign_up()
# s1 = Log_in()
