import tkinter as tk  # Import the main GUI library
from tkcalendar import DateEntry  # Import a date entry widget
from tkinter import ttk  # Import additional tkinter widgets
from PIL import Image, ImageTk  # Import image processing libraries
import random  # Import the random module for generating random data
import string  # Import the string module for string manipulation
import sqlite3  # Import SQLite for database operations
from datetime import datetime  # Import datetime for handling date and time
import smtplib  # Importing this for sending emails
from email.mime.text import MIMEText  # Import email modules for composing emails
from email.mime.multipart import MIMEMultipart


# Define a function to center the main window on the screen
def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate the position (x, y) for centering the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # Set the window geometry to center it
    window.geometry(f"{width}x{height}+{x}+{y}")


# Define functions to enable and disable the return date entry
def enable_return_date():
    return_date_entry.config(state="normal")


def disable_return_date():
    return_date_entry.config(state="disabled")


# Define a function to toggle the return date entry based on trip type
def toggle_return_date(_):
    if trip_type_var.get():
        trip_type_var.set(False)
        disable_return_date()
    else:
        trip_type_var.set(True)
        enable_return_date()


# Define a function to generate a reference number
def generate_reference_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


# Define a function to save a booking
def save_booking():
    # Get various input values from the user
    from_location = from_label_entry.get()
    to_location = to_label_entry.get()
    traveling_date = departure_date_entry.get()
    return_date = return_date_entry.get() if not return_date_entry.get() else "Oneway Trip"
    adults = adults_combobox.get()
    children = child_combobox.get()
    infants = infants_combobox.get()
    flight_class = class_combobox.get()
    special_fare = Special_combobox.get()
    full_name = name_entry.get()
    email = email_entry.get()
    passport_no = passport_entry.get()
    nationality = nationality_entry.get()
    visa_type = visa_combobox.get()
    booking_date_time = datetime.now()
    reference_number = generate_reference_number()

    # Connect to the database and create a table if it doesn't exist
    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS bookings (full_name text, from_location text, to_location text, "
              "traveling_date text, return_date text, adults text, children text, infants text, flight_class text, "
              "special_fare text, email text, passport_no text, nationality text, visa_type text, booking_date_time "
              "text,"
              "reference text)")

    # Insert the booking data into the database
    c.execute("INSERT INTO bookings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (full_name, from_location, to_location, traveling_date, return_date, adults, children, infants,
               flight_class, special_fare,
               email, passport_no, nationality, visa_type, booking_date_time, reference_number))
    conn.commit()
    conn.close()

    # Clear the input fields for a new booking
    from_label_entry.delete(0, 'end')
    to_label_entry.delete(0, 'end')
    adults_combobox.set("1")
    child_combobox.set("None")
    infants_combobox.set("None")
    class_combobox.set("Economy")
    Special_combobox.set("None")
    name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    passport_entry.delete(0, 'end')
    nationality_entry.delete(0, 'end')
    visa_combobox.set("Tourist")


# Define a function to send a booking confirmation email
def send_booking_email():
    sender_email = 'shahilhaque8786@gmail.com'
    sender_password = 'yvdzkayvtyphdrdq'
    recipient_email = email_entry.get()

    # Define the email subject and body
    subject = "FlyEasy Reservation Confirmation"
    body = "Hello, your booking is successful..."

    # Create an email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(body, "plain"))

    try:
        # Establishing a secure connection with the SMTP server (Gmail)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Close the server connection
        server.quit()

        # Inform the user that the email has been sent
        print("Email sent successfully!")

    except Exception as e:
        print("Email sending failed:", str(e))


# Define a function to handle acceptance of terms and conditions
def handle_terms_acceptance():
    if terms_and_conditions_var.get():
        book_button.config(state="normal")
    else:
        book_button.config(state="disabled")


# Define functions to show and hide a tooltip
def show_tooltip(_, text):
    tooltip_label.config(text=text)
    tooltip_label.place(x=375, y=615)


def hide_tooltip(_):
    tooltip_label.place_forget()


# Create the main window
flight = tk.Tk()
flight.title("FlyEasy")
flight.geometry("650x800")
flight.resizable(False, False)
center_window(flight, 650, 800)
flight.configure(bg="#3D59AB")

# Set the width and height the image
png_width = 150
png_height = 100

# Loading a PNG image, resizing it, and creating a PhotoImage object
image = Image.open("arrow.png")
image = image.resize((png_width, png_height), Image.LANCZOS)
photo_image = ImageTk.PhotoImage(image)

# Create a label to display the resized image
image_label = tk.Label(flight, image=photo_image, bg="#3D59AB")
image_label.place(x=245, y=82)

# Create a label
FlyEasy = tk.Label(flight, text="FlyEasy Reservations", fg="black", bg="#3D59AB", borderwidth=1, relief="groove",
                   font=("Palatino", 25, "normal", "italic"))
FlyEasy.place(x=188, y=25)

# Create a label frame for FROM
from_label_frame = tk.LabelFrame(flight, text="From", bg="#3D59AB", borderwidth=1, relief="solid", font=("Courier", 15))
from_label_frame.place(x=34, y=100, width=200, height=55)
from_label_entry = tk.Entry(from_label_frame, width=21, font=("Times", 14))
from_label_entry.grid(row=1, column=0, padx=3, pady=1)

# Create a label frame for TO
to_label_frame = tk.LabelFrame(flight, text="To", bg="#3D59AB", borderwidth=1, relief="solid", font=("Courier", 15),
                               labelanchor='ne')
to_label_frame.place(x=410, y=100, width=200, height=55)
to_label_entry = tk.Entry(to_label_frame, width=21, font=("Times", 14))
to_label_entry.grid(row=1, column=0, padx=3, pady=1)

# Create a label frame for DEPARTURE DATE
date_label_frame = tk.LabelFrame(flight, text="Departure Date", bg="#3D59AB", borderwidth=1, relief="solid",
                                 font=("Courier", 12), cursor="hand1")
date_label_frame.place(x=34, y=190, width=150, height=55)

# Create a DateEntry widget inside the DEPARTURE DATE frame
departure_date_entry = DateEntry(date_label_frame, width=12, background='white', foreground='black', borderwidth=2,
                                 cursor="hand1")
departure_date_entry.pack(padx=5, pady=5)

# Create a label (button) for round trip
roundtrip_label = tk.Label(
    flight, text="ROUND TRIP", fg="black", bg="#3D59AB", borderwidth=1, relief="solid", font=("Trebuchet MS", 15),
    cursor="hand1"
)
roundtrip_label.place(x=265, y=210)
roundtrip_label.bind("<Button-1>", toggle_return_date)

# Create a label frame for RETURN DATE
return_label_frame = tk.LabelFrame(flight, text="Return Date", bg="#3D59AB", borderwidth=1, relief="solid",
                                   font=("Courier", 13), labelanchor='ne', cursor="hand1")
return_label_frame.place(x=460, y=190, width=150, height=55)

# Create a DateEntry widget inside the RETURN DATE frame
return_date_entry = DateEntry(return_label_frame, width=12, background='white', foreground='black', borderwidth=2,
                              cursor="hand1")
return_date_entry.pack(padx=5, pady=5)
return_date_entry.config(state="disabled")

# Create a variable to store the trip type
trip_type_var = tk.BooleanVar()
trip_type_var.set(False)

# Create a label frame for travelers
travelers_label_frame = tk.LabelFrame(flight, text="Travellers", bg="#3D59AB", borderwidth=1, relief="solid",
                                      font=("Courier", 18), labelanchor='n')
travelers_label_frame.place(x=34, y=280, width=580, height=75)

# Create a label and Combobox for selecting the number of adults
adults_label = tk.Label(travelers_label_frame, text="Adults:", bg="#3D59AB", font=("Courier", 14))
adults_label.place(x=3, y=4)

adults_combobox = ttk.Combobox(travelers_label_frame, values=[str(i) for i in range(1, 11)], state="readonly", width=10)
adults_combobox.set("1")
adults_combobox.place(x=85, y=7)

# Child label
child_label = tk.Label(travelers_label_frame, text="Children:", bg="#3D59AB", font=("Courier", 14))
child_label.place(x=200, y=4)

child_combobox = ttk.Combobox(travelers_label_frame, values=["None"] + [str(i) for i in range(1, 11)], state="readonly",
                              width=9)

child_combobox.set("None")
child_combobox.place(x=305, y=7)

# Infants label
infants_label = tk.Label(travelers_label_frame, text="Infant:", bg="#3D59AB", font=("Courier", 14))
infants_label.place(x=408, y=4)

infants_combobox = ttk.Combobox(travelers_label_frame, values=["None"] + [str(i) for i in range(1, 3)],
                                state="readonly", width=9)
infants_combobox.set("None")
infants_combobox.place(x=490, y=7)

# Class frame
class_label_frame = tk.LabelFrame(flight, text="Class", bg="#3D59AB", borderwidth=1, relief="solid",
                                  font=("Courier", 15))
class_label_frame.place(x=34, y=390, width=200, height=75)

# Create a Combobox with both numeric and text options
class_combobox = ttk.Combobox(class_label_frame, values=["Economy", "Premium Economy", "Business", "First Class"],
                              state="readonly", width=23)
class_combobox.set("Economy")
class_combobox.place(x=20, y=10)

# Create a Special Fares frame
Special_label_frame = tk.LabelFrame(flight, text="Special Fares", bg="#3D59AB", borderwidth=1, relief="solid",
                                    font=("Courier", 15),
                                    labelanchor='n')
Special_label_frame.place(x=410, y=390, width=200, height=75)

Special_combobox = ttk.Combobox(Special_label_frame,
                                values=["None", "Arm Forces", "Student", "Senior Citizen", "Friends & Family"],
                                state="readonly", width=23)
Special_combobox.set("None")
Special_combobox.place(x=20, y=10)

# Detail Frame
details_label_frame = tk.LabelFrame(flight, text="Passenger's Detail", bg="#3D59AB", borderwidth=1, relief="solid",
                                    font=("Courier", 15), labelanchor='n')
details_label_frame.place(x=34, y=500, width=345, height=245)

name_label = tk.Label(details_label_frame, text="Full Name:", bg="#3D59AB", font=("Times", 13))
name_label.grid(row=0, column=0, padx=3, pady=10, sticky="w")

name_entry = tk.Entry(details_label_frame, width=25, font=("Times", 13))
name_entry.grid(row=0, column=1, padx=2, pady=10)

email_label = tk.Label(details_label_frame, text="E-mail:", bg="#3D59AB", font=("Times", 13))
email_label.grid(row=1, column=0, padx=3, pady=10, sticky="w")

email_entry = tk.Entry(details_label_frame, width=25, font=("Times", 13))
email_entry.grid(row=1, column=1, padx=2, pady=10)

passport_label = tk.Label(details_label_frame, text="Passport No.", bg="#3D59AB", font=("Times", 13))
passport_label.grid(row=2, column=0, padx=3, pady=10, sticky="w")

passport_entry = tk.Entry(details_label_frame, width=25, font=("Times", 13))
passport_entry.grid(row=2, column=1, padx=2, pady=10)

nationality_label = tk.Label(details_label_frame, text="Nationality:", bg="#3D59AB", font=("Times", 13))
nationality_label.grid(row=3, column=0, padx=3, pady=10, sticky="w")

nationality_entry = tk.Entry(details_label_frame, width=25, font=("Times", 13))
nationality_entry.grid(row=3, column=1, padx=2, pady=10)

visa_label = tk.Label(details_label_frame, text="Visa Type:", bg="#3D59AB", font=("Times", 13))
visa_label.grid(row=4, column=0, padx=3, pady=4, sticky="w")

visa_combobox = ttk.Combobox(details_label_frame,
                             values=["Tourist", "Business", "Dependent", "Resident", "Migrant", "Employee", "Hajj"],
                             state="readonly", width=35)
visa_combobox.set("Tourist")
visa_combobox.place(x=100, y=185)

terms_and_conditions_var = tk.BooleanVar()
terms_and_conditions_var.set(False)

# Create a variable to store the state of the terms and conditions checkbox
terms_and_conditions_var = tk.BooleanVar()
terms_and_conditions_var.set(False)

# Create a checkbox for terms and conditions
terms_checkbox = tk.Checkbutton(flight, text="I accept the Terms and Conditions",
                                variable=terms_and_conditions_var, onvalue=True, offvalue=False,
                                borderwidth=1, relief="solid", cursor="hand2",
                                bg="#3D59AB", font=("Times", 11), command=handle_terms_acceptance)
terms_checkbox.place(x=390, y=680)

# Create a tooltip label widget (invisible by default)
tooltip_label = tk.Label(flight, text="", fg="black", bg="#ADFF2F", font=("Times", 11), relief="solid", borderwidth=1)
tooltip_label.place_forget()

# Bind the events to the Checkbutton
terms_checkbox.bind('<Enter>', lambda event: show_tooltip(event,
                                                          "This project illustrates the data-saving \n process in "
                                                          "database and how users \n receive email notifications for "
                                                          "their bookings."))
terms_checkbox.bind('<Leave>', hide_tooltip)

# Create a "Book" button (initially disabled)
book_button = tk.Button(flight, text="Book", fg="white", bg="#DC143C", cursor="hand2", borderwidth=3, relief="raised",
                        font=("Trebuchet MS", 15), state="disabled",
                        command=lambda: [send_booking_email(), save_booking()])
book_button.place(x=470, y=717, width=100, height=30)

# Start the main event loop
flight.mainloop()
