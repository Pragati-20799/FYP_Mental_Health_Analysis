import os
import itertools
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import extract
import categorize

import Tkinter as tk
from Tkinter import *
# loading Python Imaging Library
from PIL import ImageTk, Image

# To get the dialog box to open when required
# from Tkinter import filedialog
import random
import cv2
import numpy as np
# from matplotlib import pyplot as plt
import tkFileDialog as filedialog
#
# # Create a window
# root = tk.Tk()
#
# # Set Title as Image Loader
# root.title("Handwriting Analysis")
#
# # Set the resolution of window
# root.geometry("800x500")
#
# # Allow Window to be resizable
# root.resizable(width=True, height=True)
#
# title = tk.Label(root, text="WRITING PROMPT", fg="purple", font="Times 24 bold")
# title.grid(row=0, columnspan=3)
#
# para = tk.Label(root, text="Scan and upload the handwritten image file of the sentence given below:",
#                 font="Times 16 bold ")
# para.grid(row=2, columnspan=3)


def generate():
    # nouns = ("puppy", "car", "rabbit", "girl", "monkey")
    # verbs = ("runs", "hits", "jumps", "drives", "barfs")
    # adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
    # adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    sentence = ("He wondered if it could be called a beach if there was no sand.",
                "If any cop asks you where you were, just say you were visiting Kansas.",
                "The toy brought back fond memories of being lost in the rain forest.")
    num = random.randrange(0, 2)
    # sentence = (nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num])
    result = (sentence[num])
    sent = Label(root, text=result, fg="purple", font="Times 14 bold ")
    sent1 = Label()
    sent.grid(row=5, column=1)


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
    panel = Label(root, image=image)

    # set the image as img
    panel.image = image
    panel.grid(row=20)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='"pen')
    return filename

X_baseline_angle = []
X_top_margin = []
X_letter_size = []
X_line_spacing = []
X_word_spacing = []
X_pen_pressure = []
X_slant_angle = []
y_t1 = []
y_t2 = []
y_t3 = []
y_t4 = []


# if os.path.isfile("label_list"):
#     print("Info: label_list found.")
#     # =================================================================
def accu(x):
    with open("label_list", "r") as labels:
        for line in labels:
            content = line.split()

            baseline_angle = float(content[0])
            X_baseline_angle.append(baseline_angle)

            top_margin = float(content[1])
            X_top_margin.append(top_margin)

            letter_size = float(content[2])
            X_letter_size.append(letter_size)

            line_spacing = float(content[3])
            X_line_spacing.append(line_spacing)

            word_spacing = float(content[4])
            X_word_spacing.append(word_spacing)

            pen_pressure = float(content[5])
            X_pen_pressure.append(pen_pressure)

            slant_angle = float(content[6])
            X_slant_angle.append(slant_angle)

            trait_1 = float(content[7])
            y_t1.append(trait_1)

            trait_2 = float(content[8])
            y_t2.append(trait_2)

            trait_3 = float(content[9])
            y_t3.append(trait_3)

            trait_4 = float(content[10])
            y_t4.append(trait_4)

        # ===============================================================

        # Depression
    X_t1 = []
    for a, b, c, d, e, f, g in itertools.izip(X_baseline_angle, X_top_margin, X_letter_size, X_line_spacing, X_word_spacing, X_pen_pressure, X_slant_angle):
        X_t1.append([a, b, c, d, e, f, g])
    #
    # # Anxiety
    # X_t2 = []
    # for a, b,c in itertools.izip(X_slant_angle, X_line_spacing, X_baseline_angle):
    #     X_t2.append([a, b, c])
    #
    # # Stress
    # X_t3 = []
    # for a, b, c in itertools.izip(X_top_margin, X_baseline_angle, X_word_spacing):
    #     X_t3.append([a, b])
    #
    # # Normal
    # X_t4 = []
    # for a, b in itertools.izip(X_baseline_angle, X_word_spacing):
    #     X_t4.append([a, b])

    X_train, X_test, y_train, y_test = train_test_split(X_t1, y_t1, test_size=.20, random_state=4)
    clf1 = SVC(kernel = 'rbf', gamma = 'auto', C=2)
    clf1.fit(X_train, y_train)
    x1 = accuracy_score(clf1.predict(X_test), y_test)
    print "Classifier 1 accuracy(Depression): ", accuracy_score(clf1.predict(X_test), y_test)

    X_train, X_test, y_train, y_test = train_test_split(X_t1, y_t2, test_size=.20, random_state=4)
    clf2 = SVC(kernel = 'rbf', gamma = 'auto', C=2)
    clf2.fit(X_train, y_train)
    x2 = accuracy_score(clf2.predict(X_test), y_test)
    print "Classifier 2 accuracy(Anxiety): ", accuracy_score(clf2.predict(X_test), y_test)

    X_train, X_test, y_train, y_test = train_test_split(X_t1, y_t3, test_size=.20, random_state=4)
    clf3 = SVC(kernel = 'rbf', gamma = 'auto', C=2)
    clf3.fit(X_train, y_train)
    x3 = accuracy_score(clf3.predict(X_test), y_test)
    print "Classifier 3 accuracy(Stress): ", accuracy_score(clf3.predict(X_test), y_test)

    X_train, X_test, y_train, y_test = train_test_split(X_t1, y_t4, test_size=.20, random_state=4)
    clf4 = SVC(kernel = 'rbf', gamma = 'auto', C=2)
    clf4.fit(X_train, y_train)
    x4 = accuracy_score(clf4.predict(X_test), y_test)
    print "Classifier 4 accuracy(Normal): ", accuracy_score(clf4.predict(X_test), y_test)

    Overallaccuracy = float((x1+x2+x3+x4)/4)*100
    print "\n"
    print "Overall Accuracy:" , Overallaccuracy
    print "\n"

    raw_features = extract.start(x)

    raw_baseline_angle = raw_features[0]
    baseline_angle, comment1 = categorize.determine_baseline_angle(raw_baseline_angle)
    print "Baseline Angle: " + comment1

    raw_top_margin = raw_features[1]
    top_margin, comment2 = categorize.determine_top_margin(raw_top_margin)
    print "Top Margin: " + comment2

    raw_letter_size = raw_features[2]
    letter_size, comment3 = categorize.determine_letter_size(raw_letter_size)
    print "Letter Size: " + comment3

    raw_line_spacing = raw_features[3]
    line_spacing, comment4 = categorize.determine_line_spacing(raw_line_spacing)
    print "Line Spacing: " + comment4

    raw_word_spacing = raw_features[4]
    word_spacing, comment5 = categorize.determine_word_spacing(raw_word_spacing)
    print "Word Spacing: " + comment5

    raw_pen_pressure = raw_features[5]
    pen_pressure, comment6 = categorize.determine_pen_pressure(raw_pen_pressure)
    print "Pen Pressure: " + comment6

    raw_slant_angle = raw_features[6]
    slant_angle, comment7 = categorize.determine_slant_angle(raw_slant_angle)
    print "Slant: " + comment7

    Xnew = [baseline_angle, top_margin, letter_size, line_spacing, word_spacing, pen_pressure, slant_angle]
    ynew1 = clf1.predict([Xnew])
    ynew2 = clf2.predict([Xnew])
    ynew3 = clf3.predict([Xnew])
    ynew4 = clf4.predict([Xnew])
    ynew4[0]=0
    if ynew1[0]==0 and ynew2[0]==0 and ynew3[0]==0:
        ynew4[0]==1
    print("---------------------------------------------------")
    print("Depression: {}".format(ynew1[0]))
    print("Anxiety: {}".format(ynew2[0]))
    print("Stress: {}".format(ynew3[0]))
    print("Normal: {}".format(ynew4[0]))

    print("---------------------------------------------------")
    return [x1,x2,x3,x4,Overallaccuracy,comment1,comment2,comment3,comment4,comment5,comment6,comment7,ynew1[0],ynew2[0],ynew3[0], ynew4[0]]
# =================================================================================================

# else:
#     print("Error: label_list file not found.")

# Create a button and place it into the window using grid layout
# btn = Button(root, text ='Upload image', command = open_img).grid(
#                                         row = 7, columnspan = 4)
# btn = Button(root, text ='Generate Sentence', command = generate).grid(
#                                         row = 3, columnspan = 4)
# btn = Button(root, text ='Original', command = main).grid(
#                                         row = 10, columnspan = 4)
#
# root.mainloop()