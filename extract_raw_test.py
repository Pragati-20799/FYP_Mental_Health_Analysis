import os
import extract

path = 'C:\Users\DELL\Downloads\uploads\uploads\img'

if os.path.isfile("raw_feature_list"):
    print("Info: raw_feature_list already exists.")
    with open("raw_feature_list", "a") as label:
        for file_name in os.listdir(path):
            print(file_name)
            features = extract.start(file_name)
            features.append(file_name)
            for i in features:
                label.write("%s\t" % i)
            print >> label, ''
        print("Done!")
