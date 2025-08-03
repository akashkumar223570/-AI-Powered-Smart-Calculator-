from tkinter import *
import math
from pygame import mixer
import speech_recognition
import threading

mixer.init()

import math

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else "Undefined (division by 0)"

def mod(a, b):
    return a % b if b != 0 else "Undefined (mod by 0)"

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def square_root(a):
    return math.sqrt(a) if a >= 0 else "Undefined (sqrt of negative)"

def cube_root(a):
    return a ** (1/3)

def sin_deg(theta):
    return math.sin(math.radians(theta))

def cos_deg(theta):
    return math.cos(math.radians(theta))

def tan_deg(theta):
    rad = math.radians(theta)
    return math.tan(rad) if math.cos(rad) != 0 else "Undefined (cos=0)"

def ln(a):
    return math.log(a) if a > 0 else "Undefined (ln of non-positive)"

def log10(a):
    return math.log10(a) if a > 0 else "Undefined (log10 of non-positive)"

def get_e():
    return math.e

def get_pi():
    return math.pi

def get_2pi():
    return 2 * math.pi

def fact(a):
    return math.factorial(int(a)) if a >= 0 and float(a).is_integer() else "Undefined (negative or non-integer)"

def hcf(a, b):
    return math.gcd(int(a), int(b))

def lcm(a, b):
    return abs(a * b) // math.gcd(int(a), int(b)) if a and b else 0


single_arg_operations = {
    'SQUARE': square, 'SQUARE OF': square,
    'CUBE': cube, 'CUBE OF': cube,
    'SQUARE ROOT': square_root, 'ROOT': square_root,
    'CUBE ROOT': cube_root,
    'SIN': sin_deg, 'SINE': sin_deg,
    'COS': cos_deg, 'COSINE': cos_deg,
    'TAN': tan_deg, 'TANGENT': tan_deg,
    'LN': ln, 'LOG': log10, 'LOG10': log10,
    'FACTORIAL': fact, 'FACT': fact
}

double_arg_operations = {
    'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add, 'TOTAL': add,
    'SUBTRACT': sub, 'SUBTRACTION': sub, 'MINUS': sub, 'DIFFERENCE': sub, 'LESS': sub,
    'MULTIPLY': mul, 'MULTIPLICATION': mul, 'PRODUCT': mul, 'TIMES': mul,
    'DIVIDE': div, 'DIVISION': div, 'QUOTIENT': div, 'DIV': div,
    'MOD': mod, 'MODULUS': mod, 'REMAINDER': mod,
    'HCF': hcf, 'GCD': hcf,
    'LCM': lcm
}

def findNumber(t):
    l = []
    for num in t:
        try:
            l.append(float(num))
        except ValueError:
            continue
    return l
def ak():
    mixer.music.load("beep-24.mp3")
    mixer.music.play()
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(m, duration=0.2)
            voice = recognizer.listen(m)
            text = recognizer.recognize_google(voice)
            print(text)
            mixer.music.load("mus2.wav")
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in single_arg_operations.keys():
                    num_list = findNumber(text_list)
                    answer=single_arg_operations[word.upper()](num_list[0])
                    entryField.delete(0,END)
                    entryField.insert(0,answer)
                elif word.upper() in double_arg_operations.keys():
                    num_list = findNumber(text_list)
                    answer=double_arg_operations[word.upper()](num_list[0],num_list[1])
                    entryField.delete(0,END)
                    entryField.insert(0,answer)
        except:
            entryField.delete(0,END)
            entryField.insert(0, 'Sorry, Not Understand Clearly')

def sound(name):
    entryField.delete(0,END)
    if(name=='♬'):
        entryField.insert(0,'Need ka to keya hai')
        mixer.music.load("Neend - Kaka _ Punjabi Song.mp3")
        mixer.music.play()
    elif(name=='၊၊||၊'):
        entryField.insert(0,'कर हर मैदान फतेह')
        mixer.music.load("Kar Har Maidaan Fateh.mp3")
        mixer.music.play()
    elif(name=='↻ ◁||▷ ↺'):
        entryField.insert(0,'Powerful Hanuman Chalisa')
        mixer.music.load("Powerful Hanuman Chalisa.mp3")
        mixer.music.play()
    elif(name=='𓀎'):
        entryField.insert(0,'ॐ हनुमते नमः')
        mixer.music.load("Jay Bajrangbali.mp3")
        mixer.music.play()
    elif(name=='🎙'):
        entryField.insert(0,'Chak Lein De')
        mixer.music.load("Chak Lein De - Lofi _ Slowed Reverb.mp3")
        mixer.music.play()
    elif(name=='📻'):
        entryField.insert(0,'Guru Me Sansar Samaya')
        mixer.music.load("Guru Me Sansar Samaya _ Guru Purnima 2025.mp3")
        mixer.music.play()
    elif(name=='📀'):
        entryField.insert(0,'Sanam Teri Kasm')
        mixer.music.load("Sanam Teri Kasm - Hemant Raj - Door Jaaoge Tum Mar Jayenge Hum.mp3")
        mixer.music.play()
    else:
        entryField.insert(0,'Saiyaara Tu Toh Badla Nahi Hai')
        mixer.music.load("Saiyaara Tu Toh Badla Nahi Hai - Saiyaara Title Song _ Faheem Abdullah.mp3")
        mixer.music.play()



    
def click(value):
    mixer.music.load("beep-24.mp3")
    mixer.music.play()
    ex=entryField.get()
    answer=''
    try:
        if(value=='C'):
            ex=ex[0:len(ex)-1]
            entryField.delete(0,END)
            entryField.insert(0,ex)
            return
        elif(value=='CE'):
            entryField.delete(0,END)
            return
        elif(value=="√"):
            answer=math.sqrt(eval(ex))
        elif(value=="π"):
            answer=math.pi
        elif(value=="cosθ"):
            answer=math.cos(math.radians(eval(ex)))
        elif(value=="sinθ"):
            answer=math.sin(math.radians(eval(ex)))
        elif(value=="tanθ"):
            answer=math.tan(math.radians(eval(ex)))
        elif(value=="2π"):
            answer=(2*(math.pi))
        elif(value=="tanh"):
            answer=	math.tanh(eval(ex))
        elif(value=="sinh"):
            answer=	math.sinh(eval(ex))
        elif(value=="cosh"):
            answer=	math.cosh(eval(ex))
        elif(value==chr(8731)):
            answer=eval(ex)**(1/3)
        elif(value=="×\u02b8"):
            entryField.insert(END,'**')
            return
        elif(value=="ln"):
            answer=math.log(eval(ex))
        elif(value=="×\u00b3"):
            answer=eval(ex)**3
        elif(value=="×\u00b2"):
            answer=eval(ex)**2
        elif(value=="log₁₀"):
            answer=math.log10(eval(ex))
        elif(value=="rad"):
            answer=math.radians(eval(ex)) 
        elif(value=="deg"):
            answer=math.degrees(eval(ex)) 
        elif(value=="e"):
            answer= math.e
        elif(value=="x!"):
            answer=math.factorial(eval(ex))
        elif(value==chr(247)):
            entryField.insert(END,'/')
            return
        elif(value=='='): 
            answer=eval(ex)
        else:
            entryField.insert(END,value)
            return
        entryField.delete(0,END)
        entryField.insert(0,answer)
    except:
        pass

    

root = Tk()
root.title("AI-Powered Smart Calculator with Voice Command and Music")
root.config(bg='black')
root.geometry('680x555+100+100')
root.maxsize(680,555)
entryField = Entry(root,font=('arial', 20, 'bold'),bg="#000000",fg="#f6f6f8",bd=10,relief=SUNKEN,width=30)
entryField.grid(row=0, column=0,columnspan=8)

cal_img =PhotoImage(file='cal1.png')
cal = Button(root, image=cal_img,bg='gray4',border=5,relief=SUNKEN)
cal.grid(row=0, column=0)

Mic_img =PhotoImage(file='mic1.png')
cal = Button(root, image=Mic_img, bg='gray5', border=5, relief=SUNKEN,
             command=lambda: threading.Thread(target=ak).start(), activebackground="black")

cal.grid(row=0, column=7)

button_text_list = [
    "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
    "4", "5", "6", "*", chr(8731), "×\u02b8", "×\u00b3", "×\u00b2",
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
    "0", ".", "%", "=", "log₁₀", "(", ")", "x!",
    '♬', '၊၊||၊', '↻ ◁||▷ ↺', '🎙', '📻', '📀', '📟', '𓀎'
]

rowvalue = 1
columnvalue = 0
for i in button_text_list:
    if i == '♬' or i == '၊၊||၊' or i == '↻ ◁||▷ ↺' or i == '🎙' or i == '📻' or i == '📀' or i == '📟' or i == '𓀎':  
        button = Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg="#000430"
        ,fg="#FCD202",font=('arial', 18, 'bold'),activebackground="#000430",command=lambda button=i:sound(button)
        )
    elif i=="C" or i=="CE":
        button = Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg="#e13308"
        ,fg="#0F3701",font=('arial', 18, 'bold'),activebackground="#e13308",command= lambda button=i:click(button))
    elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or \
   i == "6" or i == "7" or i == "8" or i == "9" or i == "0" or \
   i == "." or i == "%":
        button = Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg="#f1950c"
        ,fg="#1425e3",font=('arial', 18, 'bold'),activebackground="#f1950c",command= lambda button=i:click(button))

    else:
        button = Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg="#023F25",fg="#7488A7",font=('arial', 18, 'bold'),activebackground="#023F25",command= lambda button=i:click(button)
        )

    button.grid(row=rowvalue, column=columnvalue)
    
    columnvalue += 1
    if columnvalue > 7:   
        columnvalue = 0
        rowvalue += 1

root.mainloop()     