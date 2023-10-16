import tkinter as tk
login_user=('hello')

# Set up the main window
root = tk.Tk()
root.title("Forex 100")
root.config(background="#6c5ce7")

class LoginMenu(tk.Tk):

    # Create a label to prompt the user for their username
    username_label = tk.Label(root, text="Username:", font=("Arial", 18))
    # username_label.pack(side="top", pady=10)

    # Create an entry field for the username
    username_entry = tk.Entry(root, font=("Arial", 18))
    #username_entry.pack(side="top", pady=10)

    # Create a label to prompt the user for their password
    password_label = tk.Label(root, text="Password:", font=("Arial", 18))
    #password_label.pack(side="top", pady=10)

    root.columnconfigure(0,weight = 1)
    root.columnconfigure(1,weight = 1)
    root.rowconfigure(0,weight = 1)

    # placing a widget
    username_label.grid(row = 0,column= 0)
    password_label.grid(row = 0,column= 1)

    # Create an entry field for the password
    password_entry = tk.Entry(root, font=("Arial", 18), show="*")
    #password_entry.pack(side="top", pady=10)

    # Create a button to submit the login information
    login_button = tk.Button(root, text="Log In", font=("Arial", 18), command=login_user)
    #login_button.pack(side="top", pady=10)

    def login_user():
        # Get the username and password from the entry fields
        username = username_entry.get()
        password = password_entry.get()

        # Check if the username and password are valid
        if username == "admin" and password == "password":
            # If valid, create a frame for the main application
            main_frame = tk.Frame(root, background="#6c5ce7")
            #main_frame.pack(fill="both", expand=True)

            # Create a label to display the username
            username_label = tk.Label(main_frame, text=f"Welcome, {username}!", font=("Arial", 18))
            #username_label.pack(side="top", pady=10)

            # Create a button to log out
            logout_button = tk.Button(main_frame, text="Log Out", font=("Arial", 18), command=logout_user)
            #logout_button.pack(side="top", pady=10)

            # Create a frame for the main application
            main_frame = tk.Frame(root, background="#6c5ce7")
            #main_frame.pack(fill="both", expand=True)

            # Create a label to display a message
            message_label = tk.Label(main_frame, text="Welcome to the main application!", font=("Arial", 18))
            #message_label.pack(side="top", pady=10)

            # Create a button to close the application
            close_button = tk.Button(main_frame, text="Close", font=("Arial", 18), command=root.destroy)
            #close_button.pack(side="top", pady=10)

            # Start the main loop
            root.mainloop()
        else:
            # If invalid, display an error message
            error_message = tk.Message(root, text="Invalid username and password", font=("Arial", 18))
            #error_message.pack(side="top", pady=10)
    #
    # Define the logout function
    def logout_user():
        # Destroy the main frame and exit the main loop
        main_frame.destroy()
        root.mainloop()

    # Start the main loop
    root.mainloop()



    # Define a grid
    #root.columnconfigure(0,weight = 1)
    #root.columnconfigure(1,weight = 1)
    #root.rowconfigure(0,weight = 1)
    #
    ## placing a widget
    #username_label.grid(row = 0,colum= 0)
    #password_label.grid(row = 0,colum= 1)
