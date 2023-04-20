from tkinter import *
from tkinter import messagebox
import random
import smtplib

def timer():
    global temp_otp, email_var, otp, response
    if temp_otp != otp or response != "Ok":
        window.title("OTP Verification Failed")
        messagebox.showerror(" Verification Failed", "Time Out")
        window.title("OTP Verification")
        otp_var.set("")
        otp = None

def send_otp():
    global email_var, otp, timer_id
    otp = str(random.randint(100000,1000000))
    send_otp_btn.config(text = "Resend OTP")

    sender_email_address = "example@gmail.com"
    sender_email_password = "app-password"

    try:
        message = (f"Your OTP for Verification is {otp}")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email_address, sender_email_password)
        server.sendmail(sender_email_address, email_var.get(), message)
        server.quit()
        window.title("OTP Verification, OTP Sent")
        window.after_cancel(timer_id)
        timer_id = window.after(60000, timer)
    except:
        messagebox.showerror("Sent Failed", "Message Can't Be Sent.")
        email_var.set("")

def verify_otp():
    global email_var, otp_var, otp, response, temp_otp
    temp_otp = otp_var.get()
    if otp_var.get() == otp:
        response = messagebox.showinfo("OTP Verification", "OTP Verified: Click 'Ok' ")
        window.title("OTP Verification, OTP Verified!")
        if response == "Ok":
            email_var.set("")
            otp_var.set("")
    else:
        window.title("OTP Verification------OTP Verification")
        messagebox.showerror("OTP Verification","OTP NOT VERIFIED: Resend the OTP for Verification")
        otp_var.set("")
        otp = None


window = Tk()
window.title("OTP Verification")
window.geometry("500x500")
window.resizable(False,False)
window.config(bg="grey")

#Label for GUI title
Label(window,text="OTP - VERIFICATION",font=("poppins", 20,"bold"), bg="grey" ,fg="black").place(x=115, y=35)

#frame for all widgets
frame = Frame(window,bg="light grey",height=300,width=400,relief=RAISED,highlightbackground="light grey",highlightthickness=3)
frame.place(x=50,y=100)

#Email 
Label(frame,text="Email: ",bg="light grey" ,fg="black",font=("poppins",14,"bold"),relief=FLAT).place(x=50,y=48)

#Variable for accepting email address of the user
email_var = StringVar()

#Email TextBox
Entry(frame,textvariable=email_var,font=("poppins",12),bg="snow",fg="black",relief=RAISED, width=22).place(x=150,y=50)

#timer_id
timer_id  = window.after(60000,quit)

#Send OTP Button
send_otp_btn = Button(frame,text="Send OTP",fg="light grey",bg="black",font=("poppins",12,"bold"),relief=RAISED,command=send_otp)
send_otp_btn.place(x=200,y=90)

#Enter OTP
Label(frame,text="Enter OTP: ",bg="light grey",fg="black",font=("poppins",14,"bold"),relief=FLAT).place(x=30,y=160)

otp_var = StringVar()

#OTP TextBox
Entry(frame,textvariable=otp_var,font=("poppins",12),bg="snow",fg="black",relief=RAISED, width=22).place(x=150,y=160)

otp = None
response = None
temp_otp = None

#Verify OTP Button
Button(frame,text="Verify OTP",fg="light grey",bg="black",font=("poppins",12,"bold"),relief=RAISED,command=verify_otp).place(x=198,y=200)

window.mainloop()




