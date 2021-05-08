'''
Created on Oct 15, 2020

@author: Hosein Hadipour
'''

n = 512
num_of_returned_boomerang = 0
for i in list(range(0, n)):
    file_name = "rumi-128-384-22r.o61853-" + str(i)
    with open(file_name, "r") as fileobj:
        flines = fileobj.readlines()
    target_line_line = [ln for ln in flines if "sum = " in ln]
    target_line_line = target_line_line[0]
    target_line_line = target_line_line.replace("\n", "")
    pr_temp = eval(target_line_line.split(" = ")[-1])
    if pr_temp > 0:
        print(i)
        p1 = [ln for ln in flines if "p1: " in ln][0].split(": ")[-1]
        p2 = [ln for ln in flines if "p2: " in ln][0].split(": ")[-1]
        p3 = [ln for ln in flines if "p3: " in ln][0].split(": ")[-1]
        p4 = [ln for ln in flines if "p4: " in ln][0].split(": ")[-1]
        c1 = [ln for ln in flines if "c1: " in ln][0].split(": ")[-1]
        c2 = [ln for ln in flines if "c2: " in ln][0].split(": ")[-1]
        c3 = [ln for ln in flines if "c3: " in ln][0].split(": ")[-1]
        c4 = [ln for ln in flines if "c4: " in ln][0].split(": ")[-1]
        k1 = [ln for ln in flines if "k1: " in ln][0].split(": ")[-1]
        k2 = [ln for ln in flines if "k2: " in ln][0].split(": ")[-1]
        k3 = [ln for ln in flines if "k3: " in ln][0].split(": ")[-1]
        k4 = [ln for ln in flines if "k4: " in ln][0].split(": ")[-1]
        output = "p1: %s\n" % p1[0:-1]
        output += "p2: %s\n" % p2[0:-1]
        output += "p3: %s\n" % p3[0:-1]
        output += "p4: %s\n" % p4[0:-1]
        output += "c1: %s\n" % c1[0:-1]
        output += "c2: %s\n" % c2[0:-1]
        output += "c3: %s\n" % c3[0:-1]
        output += "c4: %s\n" % c4[0:-1]
        output += "k1: %s\n" % k1[0:-1]
        output += "k2: %s\n" % k2[0:-1]
        output += "k3: %s\n" % k3[0:-1]
        output += "k4: %s\n" % k4[0:-1]
        print(output)
    num_of_returned_boomerang += pr_temp
print("%d out of 2^%d" % (num_of_returned_boomerang, 41))
