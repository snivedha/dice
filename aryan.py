from tkinter import *
import random

root=Tk()

root.title("unlucky ways to die in minecraft")
root.geometry("500x500")

list1 = ["Struck by lightning", "Squished to mutch", "Blown up by a creeper whilst escaping skeliton.", "Priked to death by swwet berry bush whilsttrying to escape MinecraftSweet987" , "Killed By a firework from MinecraftPro useing  NoobslayerCrossbow whilst escaping MinecraftGuy" ]
print(list1)

def random_number():
    random_no = random.randint(0,4)
    print(random_no)
    random_way_to_die_in_minecraft = list1[random_no]
    print("You died buy getting " +   random_way_to_die_in_minecraft)
    
    
btn1 = Button(root, text="Who is your Lucky Friend?  ", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

root.mainloop()
