import Tkinter as tk
from Tkinter import *
import pymysql
import random
# loading Python Imaging Library
from PIL import ImageTk, Image
import tkFileDialog as filedialog
import train_predict
import tkMessageBox


root = tk.Tk()
root.title("HANDWRITING ANALYSIS")
root.minsize(width=400,height=400)
root.geometry("1000x1000")
title = tk.Label(root, text="WRITING PROMPT", fg="black", font="Times 24 bold")
title.grid(row=0, columnspan=3)

para = tk.Label(root, text="Scan and upload the handwritten image file of the sentence given below:",
                font="Times 16 bold ")
para.grid(row=2, columnspan=3)


def generate():
    sentence = ("Though they may gather some Left-wing support, a large majority of Labour M Ps are likely to turn down the Foot-Griffiths resolution. Mr. Foot's line will be that as Labour M Ps opposed the Government Bill which brought life peers into existence, they should not now put forward nominees. He believes that the House of Lords should be abolished and that Labour should not take any steps which would appear to prop up an out-dated institution.",
                "Mr. Macleod went on with the conference at Lancaster House despite the crisi which had blown up. He has now revealed his full plans to the Africans and Liberals attending. These plans do not give the Africans the overall majority they are seeking. African delegates are studying them today. The conference will meet to discuss the function of a proposed House of Chiefs.",
                "Some of the problems were reviewed yesterday at a meeting in Paris between M. Couve de Murville, French Foreign Minister, and Mr. Heath. Mr. Selwyn Lloyd - a man with troubles enough back home - seems fated to fly into trouble abroad. Last year it was the riots in Instanbul. which enlivened the NATO Council meeting.")
    num = random.randrange(0, 2)
    result = (sentence[num])
    text1_field.insert('end -1 chars', result)

def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='"pen')
    return filename

def open_img():
    # Select the Imagename  from a folder
    x = openfilename()

    # opens the image
    global image;
    image = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    image = image.resize((250, 250), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    image = ImageTk.PhotoImage(image)

    # create a label
    # panel = Label(root, image=image)
    #
    # # set the image as img
    # panel.image = image
    # panel.grid(row=9,column=9)
    frame4 = LabelFrame(root, text="Uploaded Image", height=30, width=30, borderwidth=2, font="Times 13 bold")
    frame4.grid(row=20, column=4, pady=80, padx=20)
    panel = Label(frame4, image=image)
    panel.grid(row=20, column=4)
    accuracy = train_predict.accu(x)
    Entry11.insert('end -1 chars', accuracy[0])
    Entry12.insert('end -1 chars', accuracy[1])
    Entry13.insert('end -1 chars', accuracy[2])
    Entry14.insert('end -1 chars', accuracy[3])
    Entry15.insert('end -1 chars', accuracy[4])

    Entry1.insert('end -1 chars', accuracy[5])
    Entry2.insert('end -1 chars', accuracy[6])
    Entry3.insert('end -1 chars', accuracy[7])
    Entry4.insert('end -1 chars', accuracy[8])
    Entry5.insert('end -1 chars', accuracy[9])
    Entry6.insert('end -1 chars', accuracy[10])
    Entry7.insert('end -1 chars', accuracy[11])
    
    if accuracy[12]==0:
        Entry8.insert('end -1 chars', 'Not Detected')
    else:
        Entry8.insert('end -1 chars', 'Detected')
        
    if accuracy[13]==0:
        Entry9.insert('end -1 chars', 'Not Detected')
    else:
        Entry9.insert('end -1 chars', 'Detected')
    
    if accuracy[14]==0:
        Entry10.insert('end -1 chars', 'Not Detected')
    else:
        Entry10.insert('end -1 chars', 'Detected')
    

    if accuracy[12]==1.0:
        tkMessageBox.showinfo("Mental Health Analysis Result", "The writer is Depressed")
    elif accuracy[13]==1.0:
        tkMessageBox.showinfo("Mental Health Analysis Result", "The writer is Anxious")
    elif accuracy[14]==1.0:
        tkMessageBox.showinfo("Mental Health Analysis Result", "The writer is Stressed")
    elif accuracy[15]==1.0:
        tkMessageBox.showinfo("Mental Health Analysis Result", "No Mental Illness detected")
    elif accuracy[12]==1.0 and accuracy[13]==1.0:
        tkMessageBox.showinfo("Mental Health Analysis Result", "The writer is Depressed and Anxious")
    elif accuracy[13]==1.0 and accuracy[14]==1.0:
        tkMessageBox.showinfo("Mental Health Analysis Result", "The writer is Anxious and Stressed")
    elif accuracy[12]==1.0 and accuracy[14]==1.0:
        tkMessageBox.showinfo("Mental Health Analysis Result", "The writer is Depressed and Stressed")
    elif accuracy[12]==0 and accuracy[13]==0 and accuracy[14]==0:
        tkMessageBox.showinfo("Mental Health Analysis Result", "No Mental Illness detected")
    else:
        tkMessageBox.showinfo("Mental Health Analysis Result", "The writer is Depressed, Anxious and Stressed")



text1_field = Text(root, height = 4, width = 70, font = "lucida 13")
text1_field.grid(row = 5, column = 1)



frame1 = LabelFrame(root, text="Features Extracted", height= 30, width=30, borderwidth=2, font="Times 13 bold")
frame1.grid(row=20,columnspan=2, pady=80)
label1 = Label(frame1, text="Baseline Angle:",font="Times 12")
label1.grid(row=21, column=1)
Entry1 = Text(frame1, height=1, width=15)
Entry1.grid(row=21, column=2)

label2 = Label(frame1, text="Top Margin:",font="Times 12")
label2.grid(row=22, column=1)
Entry2= Text(frame1, height=1, width=15)
Entry2.grid(row=22, column=2)

label3 = Label(frame1, text="Letter Size:",font="Times 12")
label3.grid(row=23, column=1)
Entry3 = Text(frame1, height=1, width=15)
Entry3.grid(row=23, column=2)

label4 = Label(frame1, text="Line Spacing:",font="Times 12")
label4.grid(row=24, column=1)
Entry4 = Text(frame1, height=1, width=15)
Entry4.grid(row=24, column=2)

label5= Label(frame1, text="Word Spacing:",font="Times 12")
label5.grid(row=25, column=1)
Entry5 = Text(frame1, height=1, width=15)
Entry5.grid(row=25, column=2)

label6 = Label(frame1, text="Pen Pressure:",font="Times 12")
label6.grid(row=26, column=1)
Entry6 = Text(frame1, height=1, width=15)
Entry6.grid(row=26, column=2)

label7 = Label(frame1, text="Slant Angle:",font="Times 12")
label7.grid(row=27, column=1)
Entry7 = Text(frame1, height=1, width=15)
Entry7.grid(row=27, column=2)


frame2 = LabelFrame(root, text="Mental Illness", height= 30, width=30, borderwidth=2, font="Times 13 bold")
frame2.grid(row=32,columnspan=2, pady=20)
label8 = Label(frame2, text="Depression:",font="Times 12")
label8.grid(row=33, column=1)
Entry8 = Text(frame2, height=1, width=15)
Entry8.grid(row=33, column=2)

label9 = Label(frame2, text="Anxiety:",font="Times 12")
label9.grid(row=34, column=1)
Entry9= Text(frame2, height=1, width=15)
Entry9.grid(row=34, column=2)

label10 = Label(frame2, text="Stress:",font="Times 12")
label10.grid(row=35, column=1)
Entry10 = Text(frame2, height=1, width=15)
Entry10.grid(row=35, column=2)


frame3 = LabelFrame(root, text="Classifier Accuracy", height= 30, width=30, borderwidth=2, font="Times 13 bold")
frame3.grid(row=32,column=4, pady=20, padx=60)
label11 = Label(frame3, text="Classifier 1(Depression):",font="Times 12")
label11.grid(row=33, column=4)
Entry11 = Text(frame3, height=1, width=15)
Entry11.grid(row=33, column=5)

label12 = Label(frame3, text="Classifier 2(Anxiety):",font="Times 12")
label12.grid(row=34, column=4)
Entry12= Text(frame3, height=1, width=15)
Entry12.grid(row=34, column=5)

label13 = Label(frame3, text="Classifier 3(Stress):",font="Times 12")
label13.grid(row=35, column=4)
Entry13 = Text(frame3, height=1, width=15)
Entry13.grid(row=35, column=5)

label14 = Label(frame3, text="Classifier 4(Normal):",font="Times 12")
label14.grid(row=36, column=4)
Entry14 = Text(frame3, height=1, width=15)
Entry14.grid(row=36, column=5)

label15 = Label(frame3, text="Overall Accuracy",font="Times 12")
label15.grid(row=37, column=4)
Entry15 = Text(frame3, height=1, width=15)
Entry15.grid(row=37, column=5)





# Create a button and place it into the window using grid layout
btn = Button(root, text ='Generate Sentence', command = generate).grid(row = 3, columnspan = 4)
btn = Button(root, text ='Upload Image', command = open_img).grid(row = 7, columnspan = 4)




root.mainloop()