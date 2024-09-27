from tkinter import *
import re

window = Tk()
window.title('SuperPuperCalculator')
window.geometry('295x450+580+150')
window.configure(bg="black")


def delete_last_char():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text) - 1, END)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tokenize(expression):

    return re.findall(r'\d+\.\d+|\d+|[+\-*/()]', expression)


def input_entry(symbol):
    entry.insert(END, symbol)


def clear():
    entry.delete(0, END)
    label.config(text=" ")


def build_expression_tree(tokens):
    operators = []
    operands = []

    i = 0
    while i < len(tokens):
        token = tokens[i]


        if re.match(r'^\d+\.\d+$|^\d+$', token):
            operands.append(Node(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                operator = operators.pop()
                right_operand = operands.pop()
                left_operand = operands.pop()
                new_node = Node(operator)
                new_node.left = left_operand
                new_node.right = right_operand
                operands.append(new_node)
            operators.pop()
        else:
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(token)):
                operator = operators.pop()
                right_operand = operands.pop()
                left_operand = operands.pop()
                new_node = Node(operator)
                new_node.left = left_operand
                new_node.right = right_operand
                operands.append(new_node)
            operators.append(token)
        i += 1


    while operators:
        operator = operators.pop()
        right_operand = operands.pop()
        left_operand = operands.pop()
        new_node = Node(operator)
        new_node.left = left_operand
        new_node.right = right_operand
        operands.append(new_node)

    return operands[-1]


def count_result(node):
    if node.left is None and node.right is None:
        return float(node.value)


    left_val = count_result(node.left)
    right_val = count_result(node.right)


    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val

    return None


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def equal():
    expression = entry.get()
    tokens = tokenize(expression)

    try:

        count = count_result(build_expression_tree(tokens))
        if count.is_integer():
            count = int(count)

        entry.delete(0, END)
        entry.insert(END, str(count))
        label.config(text=f"{expression} =")
    except Exception as e:

        label.config(text="Ошибка!")
        print(e)


label = Label(window, text=' ', font=('Arial', 14), fg='gray', bg='black', anchor='e')
label.place(x=30, y=28, width=235, height=30)


entry = Entry(window, width=15, font=('Arial', 24), fg='white', justify='right')
entry.place(x=30, y=63, width=235, height=55)
entry.configure(bg="black", font=('Arial', 24, 'bold'), borderwidth=0, highlightthickness=0)


btnC = Button(window, bg='black', fg='white', text='C', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=clear)
btnC.place(x=30, y=127, width=55, height=55)



btnSK1 = Button(window, bg='black', fg='white', text='(', font=('Arial', 19, 'bold'), borderwidth=0,
                highlightthickness=0, command=lambda: input_entry('('))
btnSK1.place(x=90, y=127, width=55, height=55)

btnSK2 = Button(window, bg='black', fg='white', text=')', font=('Arial', 19, 'bold'), borderwidth=0,
                highlightthickness=0, command=lambda: input_entry(')'))
btnSK2.place(x=150, y=127, width=55, height=55)

nazadblack = PhotoImage(file="nazad_black.png")
nazadwhite = PhotoImage(file="nazad_white.png")

btnDel = Button(window, image=nazadwhite, bg='black', borderwidth=0, highlightthickness=0, command=delete_last_char)
btnDel.place(x=150, y=367, width=55, height=55)

btnDiv = Button(window, bg='black', fg='white', text='/', font=('Arial', 19, 'bold'), borderwidth=0,
                highlightthickness=0, command=lambda: input_entry('/'))
btnDiv.place(x=210, y=127, width=55, height=55)

btnMul = Button(window, bg='black', fg='white', text='*', font=('Arial', 19, 'bold'), borderwidth=0,
                highlightthickness=0, command=lambda: input_entry('*'))
btnMul.place(x=210, y=187, width=55, height=55)

btnSub = Button(window, bg='black', fg='white', text='-', font=('Arial', 19, 'bold'), borderwidth=0,
                highlightthickness=0, command=lambda: input_entry('-'))
btnSub.place(x=210, y=247, width=55, height=55)

btnAdd = Button(window, bg='black', fg='white', text='+', font=('Arial', 19, 'bold'), borderwidth=0,
                highlightthickness=0, command=lambda: input_entry('+'))
btnAdd.place(x=210, y=307, width=55, height=55)

btn1 = Button(window, bg='black', fg='white', text='1', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('1'))
btn1.place(x=30, y=307, width=55, height=55)

btn2 = Button(window, bg='black', fg='white', text='2', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('2'))
btn2.place(x=90, y=307, width=55, height=55)

btn3 = Button(window, bg='black', fg='white', text='3', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('3'))
btn3.place(x=150, y=307, width=55, height=55)

btn4 = Button(window, bg='black', fg='white', text='4', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('4'))
btn4.place(x=30, y=247, width=55, height=55)

btn5 = Button(window, bg='black', fg='white', text='5', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('5'))
btn5.place(x=90, y=247, width=55, height=55)

btn6 = Button(window, bg='black', fg='white', text='6', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('6'))
btn6.place(x=150, y=247, width=55, height=55)

btn7 = Button(window, bg='black', fg='white', text='7', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('7'))
btn7.place(x=30, y=187, width=55, height=55)

btn8 = Button(window, bg='black', fg='white', text='8', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('8'))
btn8.place(x=90, y=187, width=55, height=55)

btn9 = Button(window, bg='black', fg='white', text='9', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('9'))
btn9.place(x=150, y=187, width=55, height=55)

btn0 = Button(window, bg='black', fg='white', text='0', font=('Arial', 19, 'bold'), borderwidth=0, highlightthickness=0,
              command=lambda: input_entry('0'))
btn0.place(x=90, y=367, width=55, height=55)

btnDot = Button(window, bg='black', fg='white', text='.', font=('Arial', 19, 'bold'), borderwidth=0,
                highlightthickness=0, command=lambda: input_entry('.'))
btnDot.place(x=30, y=367, width=55, height=55)

btnEqual = Button(window, bg='black', fg='white', text='=', font=('Arial', 19, 'bold'), borderwidth=0,
                  highlightthickness=0, command=equal)
btnEqual.place(x=210, y=367, width=55, height=55)

window.mainloop()
