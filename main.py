import pickle
import pygame
import os
from random import choice
from time import sleep as wait
pygame.mixer.init()
print("can you beat The Memory Master?")
wait(0.56)
Type = input("To Duel data scores type: 1 | To Play The Last Surviver, pass and play type: 2 | To play alone type: anything else -> ")

def savedata():
    global level, name
    with open("/data/"+name, 'wb') as fh:
       pickle.dump(level, fh)

def QUIT():
    savedata()
    print("exiting the game.")
    wait(3)
    exit()
    
    
namelist = ["Bob", "Luke", "Max", "Jack", "Rachael", "Cain", "Walt", "Hadi", "Safara", "Tad", "Page", "Pam", "Kader", "Jacob", "Ja", "Baby", "Bambi", "Tom", "Tim", "Dave", "Drew", "The Memory Master"]
levellist = ["2", "5", "10", "12", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "65", "70", "75", "80", "85", "90", "95", "100"]

def a():
    pygame.mixer.music.load("/sounds/sound1.mp3") # a
    pygame.mixer.music.play()
    wait(5)
    pygame.mixer.music.stop()
    
def s():
    pygame.mixer.music.load("/sounds/sound2.mp3") # s
    pygame.mixer.music.play()
    wait(3)
    pygame.mixer.music.stop()
    

def d():
    pygame.mixer.music.load("/sounds/sound3.mp3") # d
    pygame.mixer.music.play()
    wait(1)
    pygame.mixer.music.stop()
    
def f():
    pygame.mixer.music.load("/sounds/sound4.mp3") # f
    pygame.mixer.music.play()
    wait(4)
    pygame.mixer.music.stop()
    
def g():
    pygame.mixer.music.load("/sounds/sound5.mp3") # g
    pygame.mixer.music.play()
    wait(3)
    pygame.mixer.music.stop()
    
def h():
    pygame.mixer.music.load("/sounds/sound6.mp3") # h
    pygame.mixer.music.play()
    wait(5)
    pygame.mixer.music.stop()
    
def j():
    pygame.mixer.music.load("/sounds/sound7.mp3") # j
    pygame.mixer.music.play()
    wait(4)
    pygame.mixer.music.stop()
    
def k():
    pygame.mixer.music.load("/sounds/sound9.mp3") # k
    pygame.mixer.music.play()
    wait(2)
    pygame.mixer.music.stop()
    
def l():
    pygame.mixer.music.load("/sounds/sound10.mp3") # l
    pygame.mixer.music.play()
    wait(3)
    pygame.mixer.music.stop()
    
h()
    
def FRH():
    pygame.mixer.music.load("/sounds/sound11.mp3") # ;
    pygame.mixer.music.play()
    wait(1)
    pygame.mixer.music.stop()
    
def space():
    pygame.mixer.music.load("/sounds/sound12.mp3") # ;
    pygame.mixer.music.play()
    wait(3)
    pygame.mixer.music.stop()
    
def z():
    pygame.mixer.music.load("/sounds/sound13.mp3") # k
    pygame.mixer.music.play()
    wait(3)
    pygame.mixer.music.stop()
    
# Duel data scores:
if Type == '1':
    name = input("what is your name? -> ")
    level = 0

    try:
        pickle_off = open ("/data/"+name, "rb")
        level = pickle.load(pickle_off)
        print(level)
    except:
        pass
    path = '/data'
    files = os.listdir(path)
    # Iterating over all the files
    for file in files:
        
        # Instantiating the path of the file
        file_path = f'{path}\\{file}'
 
        # Checking whether the given file is a directory or not
        print("here are your options:")
        print(f"{file}")
        duel = input("who do you want to duel? -> ")
        try:
            pickle_off = open ("/data/"+duel, "rb")
            emp = pickle.load(pickle_off)
            print(emp)
        except:
            print("i'm sorry "+str(duel)+" is not on the list. The game is going to exit now.")
            wait(5)
            exit()
        
        if name == duel:
            Self = input("you said you wanted to duel agenst your self. Is this OK? (if not type '!') -> ")
            if Self == '!':
                print("The game will quit now.")
                wait(5)
                exit()
        if emp == namelist.pop():
            print(name+", level: "+str(level)+" /VS/ "+duel+", The Memory Master"+", level: "+emp)
        else:
            print(name+", level: "+str(level)+" /VS/ "+duel+", level: "+str(emp))
            
        if emp == 0:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            #wait(2)
            #print("d")
            #d()
            #wait(2)
            #print("f")
            #f()d
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            s()
            s()
            a()
            s()

            an = input("-> ")
            if an == "assas":
                if level <= 2:
                    level = 2
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 0:
                    level = 0
                QUIT()
        elif level == 2:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            #wait(2)
            #print("d")
            #d()
            #wait(2)
            #print("f")
            #f()d
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            s()
            s()
            s()
            a()
            a()
            s()
            a()

            an = input("-> ")
            if an == "sssaasa":
                if level <= 5:
                    level = 5
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 2:
                    level = 2
                QUIT()
        elif level == 5:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            #wait(2)
            #print("f")
            #f()d
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            s()
            d()
            d()
            s()
            a()
            a()

            an = input("-> ")
            if an == "asddsaa":
                if level <= 10:
                    level = 10
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 5:
                    level = 5
                QUIT()
        elif level == 10:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            #wait(2)
            #print("f")
            #f()d
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            a()
            d()
            s()
            s()
            s()
            a()

            an = input("-> ")
            if an == "aadsssa":
                if level <= 12:
                    level = 12
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 10:
                    level = 10
                QUIT()
        elif level == 12:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            #wait(2)
            #print("f")
            #f()d
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            d()
            d()
            a()
            s()
            d()
            d()
            d()
            s()
            s()
            d()

            an = input("-> ")
            if an == "ddasdddssd":
                if level <= 15:
                    level = 15
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 12:
                    level = 12
                QUIT()
        elif level == 15:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            wait(2)
            print("f")
            f()
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            s()
            d()
            f()
            a()

            an = input("-> ")
            if an == "asdfa":
                if level <= 20:
                    level = 20
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 15:
                    level = 15
                QUIT()
        elif level == 20:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            wait(2)
            print("f")
            f()
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            d()
            f()
            f()
            f()
            d()
            s()

            an = input("-> ")
            if an == "adfffds":
                if level <= 25:
                    level = 25
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 20:
                    level = 20
                QUIT()
        elif level == 25:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            wait(2)
            print("f")
            f()
            wait(2)
            print("g")
            g()
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            d()
            s()
            d()
            f()
            g()
            g()

            an = input("-> ")
            if an == "adsdfgg":
                if level <= 30:
                    level = 30
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 25:
                    level = 25
                QUIT()
        elif level == 30:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            wait(2)
            print("f")
            f()
            wait(2)
            print("g")
            g()
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            

            an = input("-> ")
            if an == "asadgsf":
                if level <= 35:
                    level = 35
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 30:
                    level = 30
                QUIT()
        elif level == 35:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            wait(2)
            print("f")
            f()
            wait(2)
            print("g")
            g()
            wait(2)
            print("h")
            h()
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            d()
            s()
            f()
            g()
            h()

            an = input("-> ")
            if an == "adsfgh":
                if level <= 40:
                    level = 40
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 35:
                    level = 35
                QUIT()
        elif emp == 40:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            wait(2)
            print("f")
            f()
            wait(2)
            print("g")
            g()
            wait(2)
            print("h")
            h()
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            a()
            d()
            d()
            d()
            d()
            a()
            g()
            a()
            s()
            d()
            h()
            h()
            g()
            

            an = input("-> ")
            if an == "aaddddagasdhhg":
                if level <= 45:
                    level = 45
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 40:
                    level = 40
                QUIT()
            
        elif emp == 45:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            wait(2)
            print("f")
            f()
            wait(2)
            print("g")
            g()
            wait(2)
            print("h")
            h()
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            a()
            d()
            d()
            d()
            d()
            a()
            g()
            a()
            s()
            d()
            h()
            h()
            g()

            an = input("-> ")
            if an == "aaddddagasdhhg":
                if level <= 50:
                    level = 50
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 45:
                    level = 45
                QUIT()
                
        elif emp == 50:
            print("Before you dual, these are the sounds:")
            wait(2)
            print("a")
            a()
            wait(2)
            print("s")
            s()
            wait(2)
            print("d")
            d()
            wait(2)
            print("f")
            f()
            wait(2)
            print("g")
            g()
            wait("h")
            h()
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            d()
            d()
            h()
            j()
            f()
            g()
            a()
            s()
            d()
            h()
            g()
            h()
            j()

            an = input("-> ")
            if an == "ddhjfgasdhghj":
                if level <= 55:
                    level = 55
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 50:
                    level = 50
                QUIT()
                
        elif emp == 55:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            d()
            d()
            h()
            j()
            f()
            g()
            a()
            s()
            d()
            h()
            g()
            h()
            j()

            an = input("-> ")
            if an == "ddhjfgasdhghj":
                if level <= 60:
                    level = 60
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 55:
                    level = 55
                QUIT()
                
        elif emp == 60:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            d()
            f()
            d()
            d()
            a()
            s()
            k()
            d()
            a()
            d()
            d()
            g()
            h()
            f()
            j()
            j()

            an = input("-> ")
            if an == "dfddaskdaddghfjj":
                if level <= 65:
                    level = 65
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 60:
                    level = 60
                QUIT()
                
        elif emp == 65:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            k()
            k()
            k()
            j()
            a()
            s()
            k()
            an = input("-> ")
            if an == "kkkjaskakkghasdfghjk":
                if level <= 70:
                    level = 70
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 65:
                    level = 65
                QUIT()
                
        elif emp == 70:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            wait(0.5)
            print("l")
            l()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            k()
            d()
            s()
            l()
            d()
            k()
            l()
            h()
            d()
            a()
            s()
            j()
            s()
            k()
            l()
            l()
            l()
            g()
            h()
            an = input("-> ")
            if an == "akdsldklhdasjsklllgh":
                if level <= 75:
                    level = 75
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 70:
                    level = 70
                QUIT()
                
        elif emp == 75:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            wait(0.5)
            print("l")
            l()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            s()
            k()
            f()
            a()
            l()
            f()
            h()
            g()
            j()
            l()
            h()
            l()
            l()
            g()
            an = input("-> ")
            if an == "askfalfhgjlhllg":
                if level <= 80:
                    level = 80
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 75:
                    level = 75
                QUIT()
                
        elif emp == 80:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            wait(0.5)
            print("l")
            l()
            wait(0.5)
            print(";")
            FRH()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            s()
            d()
            f()
            g()
            h()
            j()
            k()
            l()
            FRH()
            g()
            h()
            FRH()
            an = input("-> ")
            if an == "asdfghjkl;gh;":
                if level <= 85:
                    level = 85
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 80:
                    level = 80
                QUIT()
                
        elif emp == 85:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            wait(0.5)
            print("l")
            l()
            wait(0.5)
            print(";")
            FRH()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            g()
            h()
            d()
            FRH()
            d()
            h()
            g()
            l()
            FRH()
            s()
            a()
            h()
            g()
            f()
            k()
            an = input("-> ")
            if an == "aghd;dhgl;sahgfk":
                if level <= 90:
                    level = 90
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 85:
                    level = 85
                QUIT()
                
        elif emp == 90:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            wait(0.5)
            print("l")
            l()
            wait(0.5)
            print(";")
            FRH()
            wait(0.5)
            print("{space key}")
            space()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            FRH()
            d()
            l()
            a()
            h()
            space()
            d()
            space()
            space()
            h()
            s()
            d()
            FRH()
            an = input("-> ")
            if an == "a;dlah d  hsd;":
                if level <= 95:
                    level = 95
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 90:
                    level = 90
                QUIT()
                
        elif emp == 95:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            wait(0.5)
            print("l")
            l()
            wait(0.5)
            print(";")
            FRH()
            wait(0.5)
            print("{space key}")
            space()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            k()
            f()
            a()
            l()
            l()
            s()
            g()
            h()
            FRH()
            l()
            s()
            space()
            k()
            a()
            d()
            space()
            space()
            h()
            d()
            l()
            
            an = input("-> ")
            if an == "akfallsgh;ls kad  hdl":
                if level <= 100:
                    level = 100
                    print("you beat "+duel)
            else:
                print("you lost")
                if level >= 95:
                    level = 95
                QUIT()
        elif emp == 95:
            print("Before you dual, these are the sounds:")
            wait(0.5)
            print("a")
            a()
            wait(0.5)
            print("s")
            s()
            wait(0.5)
            print("d")
            d()
            wait(0.5)
            print("f")
            f()
            wait(0.5)
            print("g")
            g()
            wait(0.5)
            print("h")
            h()
            wait(0.5)
            print("j")
            j()
            wait(0.5)
            print("k")
            k()
            wait(0.5)
            print("l")
            l()
            wait(0.5)
            print(";")
            FRH()
            wait(0.5)
            print("{space key}")
            space()
            
            print("Ready..")
            wait(1)
            print("Go!")
            wait(0.5)
            a()
            k()
            f()
            a()
            l()
            l()
            s()
            g()
            h()
            FRH()
            l()
            s()
            space()
            k()
            a()
            d()
            space()
            space()
            h()
            d()
            l()
            
            an = input("-> ")
            if an == "akfallsgh;ls kad  hdl":
                if level <= 100:
                    level = 100
                    print(name+", you beat The Memory Master! ("+duel+")")
            else:
                print("you lost")
                print("The Memory Master beat you!")
                QUIT()
                
elif Type == '2':
    alive = True
    print("The Last Surviver - who will survive?")
    
    diff = input("type '1' for letters: asdf | type '2' for letters: asdfjkl; | type '3' for letters: asdfghjkl; {space} -> ")
    tellme = input("should all the sounds be played before each turn or just at the begining? | tell me every time (1) |  just at the begining (2) -> ")
    
    if tellme == '1':
        tell = True
    elif tellme == '2':
        tell = False
    else:
        print("you did not type 1 or 2.")
    
    p1 = input("player 1/2 post your name: ")
    p2 = input("player 2/2 post your name: ")
    
    if tell == False:
        if diff == '1':
            print("these are the surviver sounds:")
            print("a")
            a()
            wait(1)
            print("s")
            s()
            wait(1)
            print("d")
            d()
            wait(1)
            print("f")
            f()
        elif diff == '2':
            print("these are the surviver sounds:")
            print("a")
            a()
            wait(1)
            print("s")
            s()
            wait(1)
            print("d")
            d()
            wait(1)
            print("f")
            f()
            wait(1)
            print("j")
            j()
            wait(1)
            print("k")
            k()
            wait(1)
            print("l")
            l()
            wait(1)
            print(";")
            FRH()
        elif diff == '3':
            print("a")
            a()
            wait(1)
            print("s")
            s()
            wait(1)
            print("d")
            d()
            wait(1)
            print("f")
            f()
            wait(1)
            print("g")
            g()
            wait(1)
            print("h")
            h()
            wait(1)
            print("j")
            j()
            wait(1)
            print("k")
            k()
            wait(1)
            print("l")
            l()
            wait(1)
            print(";")
            FRH()
            wait(1)
            print("{space}")
            space()
    
    if diff == '1':
        sounds = ['a','s','d','f']
        pslist = []
        while alive:
            pslist.append(choice(sounds))
            input(p1+", it is your turn.")
            
            if tell == True:
                print("these are the surviver sounds:")
                print("a")
                a()
                wait(1)
                print("s")
                s()
                wait(1)
                print("d")
                d()
                wait(1)
                print("f")
                f()
                input("Ready?")
                
            for x in range(len(pslist)):
                R = pslist[x]
                if R == 'a':
                    a()
                if R == "s":
                    s()
                if R == "d":
                    d()
                if R == "f":
                    f()
                os.system('cls' if os.name == 'nt' else 'clear')
            ans = input(" -> ")
            if ans != R:
                print(p2+" wins!")
                print("the game will exit in 5 sec.")
                wait(5)
                exit()
                
            pslist.append(choice(sounds))
            input(p2+", it is your turn.")
                
            if tell == True:
                print("these are the surviver sounds:")
                print("a")
                a()
                wait(1)
                print("s")
                s()
                wait(1)
                print("d")
                d()
                wait(1)
                print("f")
                f()
                input("Ready?")
                
            for x in range(len(pslist)):
                R = pslist[x]
                if R == 'a':
                    a()
                if R == "s":
                    s()
                if R == "d":
                    d()
                if R == "f":
                    f()
                os.system('cls' if os.name == 'nt' else 'clear')
            ans = input(" -> ")
            if ans != R:
                print(p1+" wins!")
                print("the game will exit in 5 sec.")
                wait(5)
                exit()

            
    
    elif diff == '2':
        sounds = ['a','s','d','f','j','k','l',';']
        pslist = []
        while alive:
            pslist.append(choice(sounds))
            input(p1+", it is your turn.")
            
            if tell == True:
                print("these are the surviver sounds:")
                print("a")
                a()
                wait(1)
                print("s")
                s()
                wait(1)
                print("d")
                d()
                wait(1)
                print("f")
                f()
                wait(1)
                print("j")
                j()
                wait(1)
                print("k")
                k()
                wait(1)
                print("l")
                l()
                wait(1)
                print(";")
                FRH()
                input("Ready?")
                
            for x in range(len(pslist)):
                R = pslist[x]
                if R == 'a':
                    a()
                if R == "s":
                    s()
                if R == "d":
                    d()
                if R == "f":
                    f()
                if R == "j":
                    j()
                if R == "k":
                    k()
                if R == "l":
                    l()
                if R == ";":
                    FRH()
                os.system('cls' if os.name == 'nt' else 'clear')
            ans = input(" -> ")
            if ans != R:
                print(p2+" wins!")
                print("the game will exit in 5 sec.")
                wait(5)
                exit()
                
            pslist.append(choice(sounds))
            input(p2+", it is your turn.")
                
            if tell == True:
                print("these are the surviver sounds:")
                print("a")
                a()
                wait(1)
                print("s")
                s()
                wait(1)
                print("d")
                d()
                wait(1)
                print("f")
                f()
                wait(1)
                print("j")
                j()
                wait(1)
                print("k")
                k()
                wait(1)
                print("l")
                l()
                wait(1)
                print(";")
                FRH()
                input("Ready?")
                
            for x in range(len(pslist)):
                R = pslist[x]
                if R == 'a':
                    a()
                if R == "s":
                    s()
                if R == "d":
                    d()
                if R == "f":
                    f()
                if R == "j":
                    j()
                if R == "k":
                    k()
                if R == "l":
                    l()
                if R == ";":
                    FRH()
                    
                os.system('cls' if os.name == 'nt' else 'clear')
            ans = input(" -> ")
            if ans != R:
                print(p1+" wins!")
                print("the game will exit in 5 sec.")
                wait(5)
                exit()
     
    
    elif diff == '3':
        sounds = ['a','s','d','f','g','h','j','k','l',';',' ']
        pslist = []
        while alive:
            pslist.append(choice(sounds))
            input(p1+", it is your turn.")
            
            if tell == True:
                print("these are the surviver sounds:")
                print("a")
                a()
                wait(1)
                print("s")
                s()
                wait(1)
                print("d")
                d()
                wait(1)
                print("f")
                f()
                wait(1)
                print("g")
                g()
                wait(1)
                print("h")
                h()
                wait(1)
                print("j")
                j()
                wait(1)
                print("k")
                k()
                wait(1)
                print("l")
                l()
                wait(1)
                print(";")
                FRH()
                print("space bar")
                space()
                input("Ready?")
                
            for x in range(len(pslist)):
                R = pslist[x]
                if R == 'a':
                    a()
                if R == "s":
                    s()
                if R == "d":
                    d()
                if R == "f":
                    f()
                if R == "g":
                    g()
                if R == "h":
                    h()
                if R == "j":
                    j()
                if R == "k":
                    k()
                if R == "l":
                    l()
                if R == ";":
                    FRH()
                if R == " ":
                    space()
                os.system('cls' if os.name == 'nt' else 'clear')
            ans = input(" -> ")
            if ans != R:
                print(p2+" wins!")
                print("the game will exit in 5 sec.")
                wait(5)
                exit()
                
            pslist.append(choice(sounds))
            input(p2+", it is your turn.")
                
            if tell == True:
                print("these are the surviver sounds:")
                print("a")
                a()
                wait(1)
                print("s")
                s()
                wait(1)
                print("d")
                d()
                wait(1)
                print("f")
                f()
                wait(1)
                print("g")
                g()
                wait(1)
                print("h")
                h()
                wait(1)
                print("j")
                j()
                wait(1)
                print("k")
                k()
                wait(1)
                print("l")
                l()
                wait(1)
                print(";")
                FRH()
                print("space bar")
                space()
                input("Ready?")
                
            for x in range(len(pslist)):
                R = pslist[x]
                if R == 'a':
                    a()
                if R == "s":
                    s()
                if R == "d":
                    d()
                if R == "f":
                    f()
                if R == "g":
                    g()
                if R == "h":
                    h()
                if R == "j":
                    j()
                if R == "k":
                    k()
                if R == "l":
                    l()
                if R == ";":
                    FRH()
                if R == " ":
                    space()
                    
                os.system('cls' if os.name == 'nt' else 'clear')
            ans = input(" -> ")
            if ans != R:
                print(p1+" wins!")
                print("the game will exit in 5 sec.")
                wait(5)
                exit()
        
        
      
        
        
        
        
        
        
        
        
        
        
        
        
    
    else:
        print("you did not type 1,2, or 3.")
        
        
                
            
            

# alone:
name = input("what is your name? -> ")
level = 0

try:
    pickle_off = open ("/data/"+name, "rb")
    level = pickle.load(pickle_off)
    print("level: "+str(level))
except:
    print("level: "+str(level))
   
savedata()
def l2():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    #wait(2)
    #print("d")
    #d()
    #wait(2)
    #print("f")
    #f()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[0]+", level: "+levellist[0])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    s()
    s()
    a()
    s()

    an = input("-> ")
    if an == "assas":
        level = 2
        print("correct")
        l5()
    else:
        print("incorrect")
        level = 0
        l2()
    

def l5():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    #wait(2)
    #print("d")
    #d()
    #wait(2)
    #print("f")
    #f()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[1]+", level: "+levellist[1])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    s()
    s()
    s()
    a()
    a()
    s()
    a()

    an = input("-> ")
    if an == "sssaasa":
        level = 5
        print("correct")
        l10()
    else:
        print("incorrect")
        level = 0
        l2()


def l10():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    #wait(2)
    #print("f")
    #f()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[2]+", level: "+levellist[2])
    Q = input("Ready? (to quit type: '!')")
    if Q =='!':
        QUIT()

    wait(1)
    a()
    s()
    d()
    d()
    s()
    a()
    a()

    an = input("-> ")
    if an == "asddsaa":
        level = 10
        print("correct")
        l12()
    else:
        print("incorrect")
        level = 2
        l5()
    

def l12():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    #wait(2)
    #print("f")
    #f()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[3]+", level: "+levellist[3])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    a()
    d()
    s()
    s()
    s()
    a()
    

    an = input("-> ")
    if an == "aadsssa":
        level = 12
        print("correct")
        l15()
    else:
        print("incorrect")
        level = 5
        l10()

def l15():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    #wait(2)
    #print("f")
    #f()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[4]+", level: "+levellist[4])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    d()
    d()
    a()
    s()
    d()
    d()
    d()
    s()
    s()
    d()

    an = input("-> ")
    if an == "ddasdddssd":
        level = 15
        print("correct")
        l20()
    else:
        print("incorrect")
        level = 10
        l12()
        
def l20():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    wait(2)
    print("f")
    f()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[5]+", level: "+levellist[5])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    s()
    d()
    f()
    a()

    an = input("-> ")
    if an == "asdfa":
        level = 20
        print("correct")
        l25()
    else:
        print("incorrect")
        level = 12
        l15()
        
def l25():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    wait(2)
    print("f")
    f()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[6]+", level: "+levellist[6])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    d()
    f()
    f()
    f()
    d()
    s()

    an = input("-> ")
    if an == "adfffds":
        level = 25
        print("correct")
        l30()
    else:
        print("incorrect")
        level = 15
        l20()
        
def l30():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    wait(2)
    print("f")
    f()
    wait(2)
    print("g")
    g()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[7]+", level: "+levellist[7])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    d()
    s()
    d()
    f()
    g()
    g()

    an = input("-> ")
    if an == "adsdfgg":
        level = 30
        print("correct")
        l35()
    else:
        print("incorrect")
        level = 20
        l25()
        
        
def l35():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    wait(2)
    print("f")
    f()
    wait(2)
    print("g")
    g()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[8]+", level: "+levellist[8])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    s()
    a()
    d()
    g()
    s()
    f()

    an = input("-> ")
    if an == "asadgsf":
        level = 35
        print("correct")
        l40()
    else:
        print("incorrect")
        level = 25
        l30()
        
def l40():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    wait(2)
    print("f")
    f()
    wait(2)
    print("g")
    g()
    wait(2)
    print("h")
    h()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[9]+", level: "+levellist[9])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    d()
    s()
    f()
    g()
    h()

    an = input("-> ")
    if an == "adsfgh":
        level = 40
        print("correct")
        l45()
    else:
        print("incorrect")
        level = 30
        l35()
        
def l45():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    wait(2)
    print("f")
    f()
    wait(2)
    print("g")
    g()
    wait(2)
    print("h")
    h()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[10]+", level: "+levellist[10])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    a()
    d()
    d()
    d()
    d()
    a()
    g()
    a()
    s()
    d()
    h()
    h()
    g()

    an = input("-> ")
    if an == "aaddddagasdhhg":
        level = 45
        print("correct")
        l50()
    else:
        print("incorrect")
        level = 35
        l40()
        
def l50():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(2)
    print("a")
    a()
    wait(2)
    print("s")
    s()
    wait(2)
    print("d")
    d()
    wait(2)
    print("f")
    f()
    wait(2)
    print("g")
    g()
    wait(2)
    print("h")
    h()
    wait(2)
    print("j")
    j()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[11]+", level: "+levellist[11])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    d()
    d()
    h()
    j()
    f()
    g()
    a()
    s()
    d()
    h()
    g()
    h()
    j()

    an = input("-> ")
    if an == "ddhjfgasdhghj":
        level = 50
        print("correct")
        l55()
    else:
        print("incorrect")
        level = 40
        l45()
        
        
def l55():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[12]+", level: "+levellist[12])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    j()
    j()
    j()
    h()
    h()
    j()
    g()
    a()
    f()
    d()
    j()
    h()
    f()
    j()
    d()
    a()
    s()
    s()
    d()
    h()

    an = input("-> ")
    if an == "jjjhhjgafdjhfjdassdh":
        level = 55
        print("correct")
        l60()
    else:
        print("incorrect")
        level = 45
        l45()
        
def l60():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[13]+", level: "+levellist[13])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    d()
    f()
    d()
    d()
    a()
    s()
    k()
    d()
    a()
    d()
    d()
    g()
    h()
    f()
    j()
    j()

    an = input("-> ")
    if an == "dfddaskdaddghfjj":
        level = 60
        print("correct")
        l65()
    else:
        print("incorrect")
        level = 50
        l45()
        
def l65():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[14]+", level: "+levellist[14])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    k()
    k()
    k()
    j()
    a()
    s()
    k()
    a()
    k()
    k()
    g()
    h()
    a()
    s()
    d()
    f()
    g()
    h()
    j()
    k()

    an = input("-> ")
    if an == "kkkjaskakkghasdfghjk":
        level = 65
        print("correct")
        l70()
    else:
        print("incorrect")
        level = 55
        l50()
        
def l70():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.5)
    print("l")
    l()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[15]+", level: "+levellist[15])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    k()
    d()
    s()
    l()
    d()
    k()
    l()
    h()
    d()
    a()
    s()
    j()
    s()
    k()
    l()
    l()
    l()
    g()
    h()

    an = input("-> ")
    if an == "akdsldklhdasjsklllgh":
        level = 70
        print("correct")
        l75()
    else:
        print("incorrect")
        level = 60
        l65()
        

def l75():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.5)
    print("l")
    l()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[16]+", level: "+levellist[16])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
        
    wait(1)
    a()
    s()
    k()
    f()
    a()
    l()
    f()
    h()
    g()
    j()
    l()
    h()
    l()
    l()
    g()
    
    
    an = input("-> ")
    if an == "askfalfhgjlhllg":
        level = 75
        print("correct")
        l80()
    else:
        print("incorrect")
        level = 65
        l70()

        
def l80():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.5)
    print("l")
    l()
    wait(0.5)
    print(";")
    FRH()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[17]+", level: "+levellist[17])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    s()
    d()
    f()
    g()
    h()
    j()
    k()
    l()
    FRH()
    g()
    h()
    FRH()

    an = input("-> ")
    if an == "asdfghjkl;gh;":
        level = 80
        print("correct")
        l85()
    else:
        print("incorrect")
        level = 70
        l75()
        QUIT()
        
def l85():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.5)
    print("l")
    l()
    wait(0.5)
    print(";")
    FRH()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[18]+", level: "+levellist[18])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    g()
    h()
    d()
    FRH()
    d()
    h()
    g()
    l()
    FRH()
    s()
    a()
    h()
    g()
    f()
    k()

    an = input("-> ")
    if an == "aghd;dhgl;sahgfk":
        level = 85
        print("correct")
        l90()
    else:
        print("incorrect")
        level = 75
        l80()
        

def l90():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.5)
    print("l")
    l()
    wait(0.5)
    print(";")
    FRH()
    wait(0.5)
    print("{space key}")
    space()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[19]+", level: "+levellist[19])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    FRH()
    d()
    FRH()
    l()
    a()
    h()
    space()
    d()
    space()
    space()
    h()
    s()
    d()
    FRH()

    an = input("-> ")
    if an == "a;dlah d  hsd;":
        level = 90
        print("correct")
        l95()
    else:
        print("incorrect")
        level = 80
        l85()
        
def l95():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.5)
    print("l")
    l()
    wait(0.5)
    print(";")
    FRH()
    wait(0.5)
    print("{space key}")
    space()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[20]+", level: "+levellist[20])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    a()
    k()
    f()
    a()
    l()
    l()
    s()
    g()
    h()
    FRH()
    l()
    s()
    space()
    k()
    a()
    d()
    space()
    space()
    h()
    d()
    l()

    an = input("-> ")
    if an == "akfallsgh;ls kad  hdl":
        level = 95
        print("correct")
        l100()
    else:
        print("incorrect")
        level = 85
        l90()
        
def l100():
    savedata()
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()
    global level
    print("Before you dual, these are the sounds:")
    wait(0.5)
    print("a")
    a()
    wait(0.5)
    print("s")
    s()
    wait(0.5)
    print("d")
    d()
    wait(0.5)
    print("f")
    f()
    wait(0.5)
    print("g")
    g()
    wait(0.5)
    print("h")
    h()
    wait(0.5)
    print("j")
    j()
    wait(0.5)
    print("k")
    k()
    wait(0.5)
    print("l")
    l()
    wait(0.5)
    print(";")
    FRH()
    wait(0.5)
    print("{space key}")
    space()
    wait(0.65)

    print(name+", level: "+str(level)+" /VS/ "+namelist[21]+", level: "+levellist[21])
    Q = input("Ready? (to quit type: '!')")
    if Q == '!':
        QUIT()

    wait(1)
    f()
    l()
    FRH()
    a()
    l()
    s()
    h()
    d()
    k()
    l()
    s()
    space()
    d()
    l()
    g()
    h()
    g()
    h()
    h()
    h()
    space()
    space()
    space()
    k()
    g()

    an = input("-> ")
    if an == "fl;alshdkls dlghghhh   kg":
        level = 100
        print("correct")
    else:
        print("incorrect")
        level = 90
        l95()
        
        
if level == 0: # if your level 0 try to beat level 2. If your level 2 try to beat level 5..
    l2()
elif level == 2:
    l5()
elif level == 5:
    l10()
elif level == 10:
    l12()
elif level == 12:
    l15()
elif level == 15:
    l20()
elif level == 20:
    l25()
elif level == 25:
    l30()
elif level == 30:
    l35()
elif level == 35:
    l40()
elif level == 40:
    l45()
elif level == 45:
    l50()
elif level == 55:
    l60()
elif level == 60:
    l65()
elif level == 65:
    l70
elif level == 70:
    l75
elif level == 75:
    l80
elif level == 80:
    l85
elif level == 85:
    l90
elif level == 90:
    l95
elif level == 95:
    l100
elif level == 100:
    print("you are The Memory Master!")
    quit()
