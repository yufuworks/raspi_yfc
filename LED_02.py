#coding:utf-8

import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BOARD)
LED = 11

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

def func_led01():
    GPIO.output(LED, not GPIO.input(LED))
    
root = tk.Tk()

label_led01 = tk.Label(root, text='press button', bg='red')
label_led01.pack()
button_led01 = tk.Button(root, text='LED', command=func_led01)

button_led01.pack()
root.mainloop()
GPIO.cleanup()