# @author : Thalakotunage A.H.
# author_email : thalakotunage@gmail.com
# Created on Tue Apr 13 18:34:10 2021

import glob
import os
os.chdir(r'C:\Users\athalako\PycharmProjects\velocityProfile')
dataFiles = glob.glob('*.txt')
outputFiles = [name[:-4] + '_interpolated.txt' for name in dataFiles]

interpolated_vel = []
for infile, outfile in zip(dataFiles, outputFiles):
    with open(infile, 'r', encoding='utf-8') as dataFile, open(os.path.join(
            r'C:\Users\athalako\PycharmProjects\velocityProfile\outfile',outfile), 'a', encoding='utf-8') as output:
        input = dataFile.readlines()
        for i in range(len(input[:-1])):
            velocity = (float(input[i].strip()) + float(input[i + 1].strip()))/2
            interpolated_vel.append(float(input[i].strip()))
            interpolated_vel.append(velocity)
        for vel in interpolated_vel:
            output.write(str('{:.4f}'.format(vel)) + '\n')
