try:
    f = open("sajjad.txt", "w")
    f.write("thank you maza")
except FileNotFoundError:
    print("File Not Found")
    f = open("sajjad.txt", "w+")
finally:
    f.close()




