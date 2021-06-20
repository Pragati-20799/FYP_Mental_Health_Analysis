import os

if os.path.isfile("class_predict_list1"):
    print("Error: class_predict_list1 already exists.")

elif os.path.isfile("label_list1"):
    print("Info: label_list found.")
    with open("label_list1", "r") as features, open("class_predict_list1", "a") as labels:
        for line in features:
            content = line.split()
            baseline_angle = float(content[0])
            top_margin = float(content[1])
            letter_size = float(content[2])
            line_spacing = float(content[3])
            word_spacing = float(content[4])
            pen_pressure = float(content[5])
            slant_angle = float(content[6])
            depression = float(content[7])
            anxiety = float(content[8])
            stress = float(content[9])
            normal = float(content[10])

            page_id = content[11]
            '''
            1 - depression anxiety stress
            2 - depression anxiety
            3 - depression stress
            4 - depression 
            5 - anxiety stress
            6 - anxiety
            7 - stress
            8 - normal'''
            # trait_1 = Depression | 1 = detected, 0 = not detected
            if depression==1 and anxiety==1 and stress==1:
                classlabel = 1

            elif depression == 1 and anxiety == 1:
                classlabel = 2

            elif depression == 1 and stress == 1:
                classlabel = 3

            elif depression == 1:
                classlabel = 4

            elif anxiety == 1 and stress == 1:
                classlabel = 5

            elif anxiety == 1:
                classlabel = 6

            elif stress == 1:
                classlabel = 7

            else:
                classlabel = 8

            labels.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (
                str(baseline_angle), str(top_margin), str(letter_size), str(line_spacing), str(word_spacing),
                str(pen_pressure), str(slant_angle)))
            labels.write("%s\t%s\t%s\t%s\t%s\t" % (
                str(depression), str(anxiety), str(stress), str(normal), str(classlabel)))
            labels.write("%s" % str(page_id))
            print >> labels, ''
    print "Done!"

else:
    print("Error: label_list file not found.")