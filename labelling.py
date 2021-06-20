import os

def determine_trait_1(line_spacing,word_spacing,baseline_angle,top_margin):
    # trait_1 = Depression | 1 = detected, 0 = not detected
    if ((line_spacing==0 or line_spacing==2) and (word_spacing==0 or word_spacing==2) and baseline_angle==1 and top_margin==1):
        return 1
    else:
        return 0


def determine_trait_2(slant_angle,line_spacing,baseline_angle):
    # trait_2 = Anxiety | 1 = detected, 0 = not detected
    if ((slant_angle == 3 or slant_angle == 4) and line_spacing==0 and (baseline_angle==0 or baseline_angle==1)):
        return 1
    else:
        return 0


def determine_trait_3(top_margin, baseline_angle,word_spacing):
    # trait_3 = Stress | 1 = detected, 0 = not detected
    if (top_margin == 1 and baseline_angle==0 and (word_spacing==0 or word_spacing==1)):
        return 1
    else:
        return 0


def determine_trait_4(baseline_angle, letter_size):
    # trait_4 = Normal | 1 = normal, 0 = not normal
    if (baseline_angle==2 and (letter_size==1 or letter_size==2)):
        return 1
    else:
        return 0


if os.path.isfile("label_list1"):
    print("Error: label_list1 already exists.")

elif os.path.isfile("feature_list"):
    print("Info: feature_list found.")
    with open("feature_list", "r") as features, open("label_list1", "a") as labels:
        for line in features:
            content = line.split()

            baseline_angle = float(content[0])
            top_margin = float(content[1])
            letter_size = float(content[2])
            line_spacing = float(content[3])
            word_spacing = float(content[4])
            pen_pressure = float(content[5])
            slant_angle = float(content[6])
            page_id = content[7]

            # trait_1 = Depression | 1 = detected, 0 = not detected
            trait_1 = determine_trait_1(line_spacing,word_spacing,baseline_angle,top_margin)

            # trait_2 = Anxiety | 1 = detected, 0 = not detected
            trait_2 = determine_trait_2(slant_angle,line_spacing,baseline_angle)

            # trait_3 = Stress | 1 = detected, 0 = not detected
            trait_3 = determine_trait_3(top_margin, baseline_angle,word_spacing)

            # trait_4 = Normal | 1 = normal, 0 = not normal
            if trait_1==0 and trait_2==0 and trait_3==0:
                trait_4 = 1
            else:
                trait_4 = 0


            labels.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (
            str(baseline_angle), str(top_margin), str(letter_size), str(line_spacing), str(word_spacing),
            str(pen_pressure), str(slant_angle)))
            labels.write("%s\t%s\t%s\t%s\t" % (
            str(trait_1), str(trait_2), str(trait_3), str(trait_4)))
            labels.write("%s" % str(page_id))
            print >> labels, ''
    print "Done!"

else:
    print("Error: feature_list file not found.")