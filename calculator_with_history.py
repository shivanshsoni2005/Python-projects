HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found")
    else:
        for line in reversed(lines):
            print(lines.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE,'w')
    file.close()
    print('History cleared.')

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + '=' + str(result)+ '\n')
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) !=3:
        print('Inviled input. Use format number operator number (e.g. 8+8)')
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = 
