					HELLO

Project Description: The FlyEasy Reservation System is a Python application designed to facilitate flight bookings,
	               saving booking data to a database, and sending booking confirmation emails. 
	               The application's graphical user interface (GUI) is built using the Tkinter library, and it leverages
	               various Python libraries for handling date and time, email communications, image processing and 
	               database operations.

Password Expiry Alert: FlyEasy provides a notification alert to remind users when the application's email password for 
	     	   sending confirmation emails has expired. Users are prompted to update their email credentials to continue receiving booking 
	     	   confirmation emails and maintain the functionality of the GUI.

GUI Features:

Interface: The application's layout is designed to be responsive and user-friendly.

Location Selection: Users can select their departure and destination locations for flight bookings.

Date Selection: FlyEasy provides a user-friendly date entry widget to select the departure date.

Trip Type Selection: Users can toggle between one-way and round-trip flights.

Return Date Selection: For round-trip flights, users can select the return date using the date entry widget.

Flexible Passenger Configuration: Users can configure the number of passengers (adults, children, and infants) to meet their specific travel needs.

Flight Class Selection: FlyEasy offers a choice of flight classes, including Economy, Premium Economy, Business and First Class.

Special Fares: Users can select special fares for their flights, such as Arm Forces, Student, Senior Citizen or Friends & Family discounts.

Passenger Information: Users can provide personal information, including their full name, email, passport number, nationality, and visa type.

Terms and Conditions: Users can accept the Terms and Conditions before pressing book.

Tooltip Information: Tooltips provide users with information about the application's features when they hover over terms and coditions.

Booking Confirmation Email: After a successful booking, users receive a confirmation email of their reservation.

Database Storage: FlyEasy stores booking information in an SQLite database for future reference and record-keeping.

Here's a brief overview of the libraries which I used in the project:

Tkinter: Tkinter is the standard GUI library in Python and provides the framework for creating graphical user interfaces.

tkcalendar: Tkcalendar is a widget that extends Tkinter, offering a user-friendly date entry interface.

Pillow (PIL): Pillow, often referred to as the Python Imaging Library (PIL), is used for image processing and manipulation, including loading
	 and displaying images in the application.

sqlite3: sqlite3 is a Python library that facilitates SQLite database operations, allowing data to be stored and retrieved from a local database.

smtplib: smtplib is a library for sending email messages. In your code, it's used for sending booking confirmation emails to users.

email: The email library provides modules for composing and sending email messages, including the MIMEText and MIMEMultipart modules
            for constructing email content.
