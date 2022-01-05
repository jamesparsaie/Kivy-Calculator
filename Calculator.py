import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import re


#Set app size
Window.size = (400, 600)
#Load KV file
Builder.load_file("calc.kv")


class MyLayout(Widget):

    #Clear the calculator input field, set back to zero
    def clear(self):
        self.ids.calc_input.text = '0'
    
    
    #Handle number button presses
    def button_press(self, button):
        #Variable to contain what is in text box, used to detect 0
        previous = self.ids.calc_input.text
        #Remove 0 if present
        if previous == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'  #Remove zero, and then append new button press to text
        else:
            self.ids.calc_input.text += f'{button}'


    #Handle operation button presses, adds text to calculator
    def math_operation(self, sign):
        self.ids.calc_input.text += f'{sign}'   #Adds operators to screen


    #Handle decimal usage operations in calculator, stop multiples
    def dec(self):
        previous = self.ids.calc_input.text
        #Splitting up the box based on operations
        nums = previous.split("+")
        #Fix Needed: Only stops multiple decimals for addition, need to expand to all operations
        if "+" in previous and '.' not in nums[-1]:
            self.ids.calc_input.text += '.'
        else:
            self.ids.calc_input.text += '.'
    

    #Equals function, this is where all math operations are calculated and printed
    def equals(self):
        #Grab text from box
        previous = self.ids.calc_input.text
        try:
            #Evaluate math operations
            answer = eval(previous)
            answer = round(answer, 4)  # Trucate to ensure it fits in screen
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"


    #function to remove last character from text box
    def delete(self):
        self.ids.calc_input.text = self.ids.calc_input.text[:-1]
        #If everything deleted set back to 0
        if self.ids.calc_input.text == '':
            self.ids.calc_input.text = '0'



    #Allow user to change sign of number, allow for negative operations
    def change_sign(self):
        holder = self.ids.calc_input.text
        #Test for negative sign
        if '-' in holder:
            self.ids.calc_input.text = f'{holder.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{holder}'


class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()  #Match class name