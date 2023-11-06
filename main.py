from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student

class Face_Recognition_System():
    def __init__(self,master):
        #Frame.__init__(self)
        self.master = master
        self.frame= Frame(self.master)
        self.master.title("Face Recognition System")
        self.frame.grid()
        self.canvas_width = 1000
        self.canvas_height = 1000
        self.canvas = Canvas(self.frame, 
                     width=self.canvas_width, 
                     height=self.canvas_height, 
                     bg="white")
        self.canvas.grid()

        img = Image.open("digit_1.jpg")
        img = img.resize((1000,1000), Image.ANTIALIAS)
        img = img.rotate(0)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.frame, image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 1000, height = 1000)
        
        bg_img = Label(self.frame, image = self.photoimg)
        bg_img.place(x = 0, y = 0, width = 1000, height = 1000)

        title_lbl = Label(bg_img, text = "Face Recognition Attendance System Software", font = ("Calibri", 35, "bold"), bg = "white", fg = "black")
        title_lbl.place(x = 0, y = 0, width = 1000, height = 50)

        #student button
        img1 = Image.open("digit_2.jpg")
        img1 = img1.resize((220,220), Image.ANTIALIAS)
        
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(bg_img, image = self.photoimg1, command = self.student_details, cursor = "hand2")
        b1.place(x = 100, y = 100, width = 220, height = 220)

        b1_1 = Button(bg_img, text = "Student Details", command = self.student_details, cursor = "hand2", font=('times new roman', 15, "bold"), bg = "black", fg = 'white')
        b1_1.place(x = 100, y = 300, width = 220, height = 40)

        #detectface button
        img2 = Image.open("digit_3.jpg")
        img2 = img2.resize((220,220), Image.ANTIALIAS)
        
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(bg_img, image = self.photoimg2, cursor = "hand2")
        b2.place(x = 600, y = 100, width = 220, height = 220)

        b2_2 = Button(bg_img, text = "Face Recognition", cursor = "hand2", font=('times new roman', 15, "bold"), bg = "black", fg = 'white')
        b2_2.place(x = 600, y = 300, width = 220, height = 40)

        #Attendance
        img3 = Image.open("digit_4.jpg")
        img3 = img3.resize((220,220), Image.ANTIALIAS)
        
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(bg_img, image = self.photoimg3, cursor = "hand2")
        b3.place(x = 100, y = 400, width = 220, height = 220)
        b3_3 = Button(bg_img, text = "Attendance", cursor = "hand2", font=('times new roman', 15, "bold"), bg = "black", fg = 'white')
        b3_3.place(x = 100, y = 600, width = 220, height = 40)

        #exit button
        img4 = Image.open("digit_1.jpg")  # Reusing the first image for the exit button
        img4 = img4.resize((220, 220), Image.ANTIALIAS)

        

        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(bg_img, image = self.photoimg4, cursor = "hand2")
        b4.place(x = 600, y = 400, width = 220, height = 220)

        b4_4 = Button(bg_img, text = "Exit", cursor = "hand2", font=('times new roman', 15, "bold"), bg = "black", fg = 'white')
        b4_4.place(x = 600, y = 600, width = 220, height = 40)

    def student_details(self):
        self.new_window = Toplevel(self.master)
        self.app = Student(self.new_window)
        

def main():
    root=Tk()
    app = Face_Recognition_System(root)
    root.mainloop()
main()