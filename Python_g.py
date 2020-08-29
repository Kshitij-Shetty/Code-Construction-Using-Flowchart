from tkinter import*
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

import os
import re
current_path = os.getcwd()
program_path = current_path + "/Program"
file_path = ""
prgm_current_path = ""

flowchart_path = current_path + "/Flowcharts"
if(os.path.exists(flowchart_path)):
    os.chdir(flowchart_path)
else:
    os.mkdir(flowchart_path)
    os.chdir(flowchart_path)


if(os.path.exists(program_path)):
    os.chdir(program_path)
else:
    os.mkdir(program_path)
    os.chdir(program_path)


current_path = current_path.replace("\\", '/')
tab_count = 0
node_count = 0
file_name =""
detail = ""

#nodes=[[0,0,0,0] for i in range(100)]
nodes = []

existence = 0



def check_var(temp_var):
    global python_path, current_path
    os.chdir(python_path)
    #print(in_file,temp_var)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
	#print(co)
    ind_beg = file_content.index("#Variables")
    ind_beg += 11
    ind_end = file_content.index("#Var_end")
    ind_end -= 4
    """print(ind_beg)
    print(ind_end)"""
    variables = file_content[ind_beg:ind_end]
    variables = variables.replace(" ","")
    variables = variables.split(",")
    variables.remove("")
    """print(variables)
    print(temp_var)"""
    if temp_var in variables:
        os.chdir(current_path)
        return 1
    else:
        os.chdir(current_path)
        return 0


def AUTO_IND(text):
    global tab_count, file_pt
    tabs = ""
    for i in range(tab_count):
        tabs=tabs+"\t"
    text=tabs+text
    text=text+"\n"
    file_pt.write(text)


def FLOW():
    canvas_width = 400
    canvas_height = 100

    #colours = ("#476042", "yellow")
    box=[]

    for ratio in ( 0.2, 0.35 ):
        box.append( (canvas_width * ratio,
                        canvas_height * ratio,
                        canvas_width * (1 - ratio),
                        canvas_height * (1 - ratio) ) )
    FLOW= Tk()
    FLOW.geometry("1600x800+0+0")
    FLOW.title("Epicness Generator")

    Tops = Frame(FLOW, width = 1600,height = 20)
    Tops.pack(side=TOP)

    f0 = Frame(FLOW, width = 800,height = 200, relief=SUNKEN)
    f0.pack(side=TOP)
    f1 = Frame(FLOW, width = 800,height = 500, relief=SUNKEN)
    f1.pack(side=TOP)

    lblInfo = Label(Tops, font=('arial',50,'bold'),text="FLOWCHART\n",fg="Dark Blue", bd=5, anchor='w')
    lblInfo.grid(row=0,column=1)
    #LABEL = []
    global nodes, node_count
    LABEL_name = 'lbl_'
    LABEL_id = 1
    ro = 1
    col = 0

    CANVAS_name = 'cv_'
    CANVAS_id = 1
    #FLOW.pack()
    for i in range(node_count):
        cv = CANVAS_name + str(CANVAS_id)
        lb = LABEL_name + str(LABEL_id)
        #print(nodes[i])
        if(nodes[i][0] == 1):
            #w.create_oval(50,50,100,100)
            te = "Start"
            st = """cv = Canvas(f0,
width=190,
height=150)
cv.grid(row = ro, column = col)
cv.create_oval(20,60,180,140, fill= "yellow")
cv.create_text(100,
    100,
    text= te)"""

        elif(nodes[i][0] == 2):
            te = str(i) + ": " + str(nodes[i][1])
            st = """cv = Canvas(f0,
width=canvas_width,
height=canvas_height)
cv.grid(row = ro, column = col)
cv.create_polygon(150, 0, 350, 0, 250, 100, 50, 100, outline = "black", fill= "yellow")
cv.create_text(canvas_width / 2,
    canvas_height / 2,
    text= te)"""
        elif(nodes[i][0] == 3):
            te = str(i) + ": " + str(nodes[i][1])
            st = """cv = Canvas(f0,
width=canvas_width,
height=canvas_height)
cv.grid(row = ro, column = col)
cv.create_rectangle(box[0][0], box[0][1],box[0][2],box[0][3], fill= "yellow")
cv.create_text(canvas_width / 2,
    canvas_height / 2,
    text= te)"""
            #st = """lb = Label(f0, font=('arial',15,'bold'),text= te,fg="Dark Blue", bd=5, anchor='w')
#lb.grid(row=ro,column=col)"""
            #st = st_r
        elif(nodes[i][0] == 4):
            te = str(i) + ": " + str(nodes[i][1])
            st = """cv = Canvas(f0,
width=canvas_width,
height=canvas_height)
cv.grid(row = ro, column = col)
cv.create_polygon(50, 50, 200, 100, 350, 50, 200, 0, outline = "black", fill= "yellow")
cv.create_text(canvas_width / 2,
    canvas_height / 2,
    text= te)"""
        elif(nodes[i][0] == 45):
            if(nodes[i][1][0] == 'e'):
                te = str(i) + ": " + str(nodes[i][1])
                st = """cv = Canvas(f0,
width=canvas_width,
height=canvas_height)
cv.grid(row = ro, column = col)
cv.create_polygon(50, 50, 200, 100, 350, 50, 200, 0, outline = "black", fill= "yellow")
cv.create_text(canvas_width / 2,
    canvas_height / 2,
    text= te)"""
            #print(str(i) + "\tElse:\t" + str(nodes[i][1]) + "\n\n")
            """if(nodes[i][1][0] == 'e'):
                print(str(i) + "\tRho:\t" + str(nodes[i][1]) + "\n\n")"""
        elif(nodes[i][0] == 5):
            te = str(i) + ": " + str(nodes[i][1])
            st = """cv = Canvas(f0,
width=300,
height=150)
cv.grid(row = ro, column = col)
cv.create_oval(20,60,280,140, fill= "yellow")
cv.create_text(150,
    100,
    text= te)"""
            #print(str(i) + "\tOval:\t" + str(nodes[i][1]) + "\n\n")
        elif(nodes[i][0] == 6):
            te = str(i) + "\tFunction:\t" + str(nodes[i][1])
            st = """lb = Label(f0, font=('arial',15,'bold'),text= te,fg="Dark Blue", bd=5, anchor='w')
lb.grid(row=ro,column=col)"""
            #print(str(i) + "\tFunction:\t" + str(nodes[i][1]) + "\n\n")
        elif(nodes[i][0] == 7):
            te = str(i) + ": " + str(nodes[i][1])
            st = """cv = Canvas(f0,
width=500,
height=100)
cv.grid(row = ro, column = col)
cv.create_rectangle(500, 0, 100, 500, fill= "yellow")
cv.create_text(300,
    100 / 3,
    text= te)"""
            #print(str(i) + "\tDirectory:\t" + str(nodes[i][1]) + "\n\n")
        elif(nodes[i][0] == 8):
            te = str(i) + "\tFunction:\t" + str(nodes[i][1])
            st = """lb = Label(f0, font=('arial',15,'bold'),text= te,fg="Dark Blue", bd=5, anchor='w')
lb.grid(row=ro,column=col)"""
            #print(str(i) + "\tFunction:\t" + str(nodes[i][1]) + "\n\n")
        exec(st)
        LABEL_id += 1
        if(ro == 6):
            ro = 1
            col += 1
        else:
            ro += 1

        """except:
            break"""
        if(i < node_count - 1):
            te ="""        ↓"""
            st = """lb = Label(f0, font=('arial',15,'bold'),text=te,fg="Dark Blue", bd=5, anchor='center')
lb.grid(row=ro,column=col)"""
            exec(st)
            LABEL_id += 1
            if(ro == 6):
                ro = 1
                col += 1
            else:
                ro += 1

    def ExitC():
        FLOW.destroy()
    btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                        text="Exit", bg="orange",command =ExitC).grid(row=10,column=3)

    mainloop()
    return i


def current_flow(flow_content):
    global nodes, node_count
    content = flow_content.split("#NODE")
    content = [i for i in content if i != ""]
    # #NODE1\t\t|para\t\t|content\n
    for i in range(len(content)):
        #print(content[i])
        content_line = content[i].split('|')
        #print(content)
        content_line[0] = content_line[0].replace(" ", "")
        content_line[0] = int(content_line[0])
        content_line[1] = content_line[1].replace(" ", "")
        content_line[1] = int(content_line[1])
        try:
            nodes[i] = [content_line[1], content_line[2], 0]
        except:
            nodes.append([content_line[1], content_line[2], 0])
    node_count = len(content)


def INPUT():
    global nodes, node_count, tab_count, python_path, current_path
    is_int = 1
    tabs = ""
    for i in range(tab_count):
        tabs = tabs + "\t"
    content = nodes[node_count][1]
    if('text' in content or 'Text' in content or 'String' in content or 'string' in content or 'Char' in content or 'char' in content):
        is_int = 0


    variables = content.replace(',' , ' ')
    variables = variables.split()
    variables = [i for i in variables if (i != "Accept" and i != "accept" and i != "Integer" and i != "integer" and i != "Number" and i != "Numbers" and i != "number" and i != "numbers" and i != "read" and i != "Read" and i != "String" and i != "string" and i != "text" and i != "Text")]
    var_count = len(variables)
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n#Input:\t" + content)
    AUTO_IND("")
    if(is_int == 1):
        text = tabs + """print("Enter """ + str(var_count) + """ inputs.")"""
        text = text +'\n'
        AUTO_IND(text)
        for variable in variables:
            is_var = check_var(variable)
            if (is_var == 0):
                os.chdir(python_path)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
            	#print(co)
                ind = file_content.index("#Variables")
                ind += 11
                part1 = file_content[:ind]
                part2 = file_content[ind:]
                text = part1 + variable + ", " + part2
                file_detail = open(detail,"w")
                file_detail.write(text)
                file_detail.close()
                os.chdir(current_path)

            AUTO_IND(variable + """ = int(input('Enter an integer value of """ + variable + """: '))""")
    else:
        text = tabs + """print("Enter """ + str(var_count) + """ inputs.")"""
        text = text +'\n'
        AUTO_IND(text)
        for variable in variables:
            is_var = check_var(variable)
            if (is_var == 0):
                os.chdir(python_path)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
            	#print(co)
                ind = file_content.index("#Variables")
                ind += 11
                part1 = file_content[:ind]
                part2 = file_content[ind:]
                text = part1 + variable + ", " + part2
                file_detail = open(detail,"w")
                file_detail.write(text)
                file_detail.close()
                os.chdir(current_path)
        AUTO_IND(variable + """ = input('Enter a string value of """ + variable + """: ')""")
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )


def DISPLAY():
    global nodes, node_count, tab_count
    tabs = ""
    for i in range(tab_count):
        tabs = tabs + "\t"
    content = nodes[node_count][1]


    variables = content.replace(',' , ' ')
    variables = variables.split()
    variables = [i for i in variables if (i != "Display" and i != "display" and i != "Integer" and i != "integer" and i != "Number" and i != "Numbers" and i != "number" and i != "numbers" and i != "print" and i != "Print" and i != "String" and i != "string" and i != "text" and i != "Text")]
    var_count = len(variables)
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n#Output:\t" + content)
    AUTO_IND("")
    #text = tabs + """print("Enter """ + str(var_count) + """ inputs.")"""
    """text = text +'\n'
    file.write(text)"""
    for variable in variables:
        is_var = check_var(variable)
        if (is_var == 0):
            messagebox.showinfo("ERROR", "The variable " + variable + " has not been defined, and hence won't be displayed.")
            #print("The variable " + variable + " has not been defined, and hence won't be displayed.\n")
        else:
            AUTO_IND("""print('""" + variable + """ = ' + str(""" + variable + """) + '.')""")
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )


def PROCEDURE():
    global nodes, node_count, tab_count, python_path, current_path, content, Menu
    tabs = ""
    for i in range(tab_count):
        tabs = tabs + "\t"
    while(True):
        while(True):
            content = simpledialog.askstring("Rectangle Content", "Enter the Operation to be performed.", parent = Menu)
            #content = input("Enter the operation\n")
            content =  content + " "
            variables = re.findall("[A-Za-z0-9]+ ", content)
            try:
                temp_content = content.split("=")
                check = 1
                temp_content = [i for i in temp_content if (i!="")]
                if len(temp_content) != 2:
                    check = 0
            except:
                check = 0
            #check = re.findall("[=]+ ", content)
            operators = re.findall("[+*/]+ ", content)
            if check == 0 :
                messagebox.showinfo("ERROR", "The coperation doesn't follow the required format.\nPlease try again.")
                #print("The condition doesn't follow the required format.\nPlease try again.\n")
            else:
                break

        RHS = temp_content[1]
        RHS_variables = re.findall("[A-Za-z0-9]+ ", RHS)
        RHS_variables = [i for i in RHS_variables if (i!="")]
        undef_var = 0
        for variable in RHS_variables:
            try:
                int(variable)
            except:
                variable = str(variable.split(" ")[0])
                is_var = check_var(variable)
                if (is_var == 0):
                    undef_var += 1
        if undef_var != 0:
            messagebox.showinfo("ERROR", "Unidentified Variables have been detected in the RHS.\nPlease Try again.")
            #print("Unidentified Variables have been detected in the RHS.\nPlease Try again.\n")
        else:
            break

    nodes[node_count][1] = content
    variables = re.findall("[A-Za-z0-9]+ ", content)
    variables = [i for i in variables if (i!="")]
    #print(variables)

    var_count = len(variables)
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n#Procedure:\t" + content)
    AUTO_IND("")
    for variable in variables:
        is_var = check_var(variable)
        if (is_var == 0):
            os.chdir(python_path)
            file_detail = open(detail,"r")
            file_content = file_detail.read()
            file_detail.close()
        	#print(co)
            ind = file_content.index("#Variables")
            ind += 11
            part1 = file_content[:ind]
            part2 = file_content[ind:]
            wr = part1 + variable + ", " + part2
            file_detail = open(detail,"w")
            file_detail.write(wr)
            file_detail.close()
            os.chdir(current_path)

    AUTO_IND(content)
    flow_pt.write("#NODE" + str(node_count) + "\t\t|3\t\t|" + content + "\n")
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )

def CONDITION():
    global nodes, node_count, tab_count, on_going_cond, python_path, current_path, content, Menu
    tabs = ""
    on_going_cond += 1
    for i in range(tab_count):
        tabs = tabs + "\t"
    #print("The different conditional statements possible are an if else statement, or a looping statement.\n")
    cond_choice = 0
    choice = Tk()
    choice.geometry("1600x800+0+0")
    choice.title("Epicness Generator")

    Tops = Frame(choice, width = 1600,height = 50)
    Tops.pack(side=TOP)

    f0 = Frame(choice, width = 800,height = 200, relief=SUNKEN)
    f0.pack(side=TOP)
    f1 = Frame(choice, width = 800,height = 500, relief=SUNKEN)
    f1.pack(side=TOP)

    lblInfo = Label(Tops, font=('arial',50,'bold'),text="Following are your options:\n",fg="Dark Blue", bd=5, anchor='w')
    lblInfo.grid(row=0,column=0)



    def IF():
        global content, cond_choice, node_count, tab_count, on_going_cond, python_path, current_path, file_pt, flow_pt
        while(True):
            while(True):
                #print("OI")
                content = simpledialog.askstring("Conditional Statement", "Enter the condition.", parent = choice)
                #content = input("Enter the condition\n")
                content =  content + " "
                variables = re.findall("[A-Za-z0-9]+ ", content)
                check = re.findall("[<>=]+ ", content)
                operators = re.findall("[+*/]+ ", content)
                if not check :
                    messagebox.showinfo("ERROR", "The condition doesn't follow the required format.\nPlease try again.")
                    #print("The condition doesn't follow the required format.\nPlease try again.\n")
                else:
                    format = content.split(str(check[0]))
                    format = [i for i in format if (i!="")]
                    if len(format) == 1:
                        messagebox.showinfo("ERROR", "The condition doesn't follow the required format.\nPlease try again.")
                        #print("The condition doesn't follow the required format.\nPlease try again.\n")
                    else:
                        break
            variables = [i for i in variables if (i!="")]
            undef_var = 0
            for variable in variables:
                try:
                    int(variable)
                except:
                    variable = str(variable.split(" ")[0])
                    is_var = check_var(variable)
                    if (is_var == 0):
                        undef_var += 1
            if undef_var != 0:
                messagebox.showinfo("ERROR", "Unidentified Variables have been detected.\nPlease Try again.")
                #print("Unidentified Variables have been detected.\nPlease Try again.\n")
            else:
                print("OI")
                #global node_count, tab_count, on_going_cond, python_path, current_path, file_pt, flow_pt
                file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
                file_pt.write("\n#Condition:\tIf type\t" + content + "\n")
                os.chdir(python_path)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
                #print(co)
                ind1 = file_content.index("#If_cond")
                ind1 += 9
                ind2 = file_content.index("#On_if_cond")
                ind2 += 12
                ind3 = file_content.index("#On_cond")
                ind3 += 9
                ind4 = file_content.index("#tab_count")

                part1 = file_content[:ind1]
                part2 = file_content[ind1:ind2]
                part3 = file_content[ind2:ind3]
                part4 = file_content[ind3:ind4]
                wr = part1 + content + "\n" + part2 + content + "\n" + part3 + "if " + content + "\n" + part4 + "#tab_count " + str(tab_count + 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
                file_detail = open(detail,"w")
                file_detail.write(wr)
                file_detail.close()
                os.chdir(current_path)
                write_cont = "if (" + content + "):"
                AUTO_IND(write_cont)
                tab_count += 1
                content = "if " + content
                nodes[node_count][1] = content
                flow_pt.write("#NODE" + str(node_count) + "\t\t|4\t\t|" + content + "\n")
                #file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )
                break
        """global cond_choice
        cond_choice = 1
        CONTINUE()"""
        choice.destroy()

    def WHILE():
        global content, cond_choice, node_count, tab_count, on_going_cond, python_path, current_path, file_pt, flow_pt
        while(True):
            while(True):
                #print("OI")
                content = simpledialog.askstring("Conditional Statement", "Enter the condition.", parent = choice)
                #content = input("Enter the condition\n")
                content =  content + " "
                variables = re.findall("[A-Za-z0-9]+ ", content)
                check = re.findall("[<>=]+ ", content)
                operators = re.findall("[+*/]+ ", content)
                if not check :
                    messagebox.showinfo("ERROR", "The condition doesn't follow the required format.\nPlease try again.")
                    #print("The condition doesn't follow the required format.\nPlease try again.\n")
                else:
                    format = content.split(str(check[0]))
                    format = [i for i in format if (i!="")]
                    if len(format) == 1:
                        messagebox.showinfo("ERROR", "The condition doesn't follow the required format.\nPlease try again.")
                        #print("The condition doesn't follow the required format.\nPlease try again.\n")
                    else:
                        break
            variables = [i for i in variables if (i!="")]
            undef_var = 0
            for variable in variables:
                try:
                    int(variable)
                except:
                    variable = str(variable.split(" ")[0])
                    is_var = check_var(variable)
                    if (is_var == 0):
                        undef_var += 1
            if undef_var != 0:
                messagebox.showinfo("ERROR", "Unidentified Variables have been detected.\nPlease Try again.")
                #print("Unidentified Variables have been detected.\nPlease Try again.\n")
            else:
                file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
                file_pt.write("\n#Condition:\tWhile type\t" + content + "\n")
                os.chdir(python_path)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
                #print(co)
                ind1 = file_content.index("#While_cond")
                ind1 += 12
                ind2 = file_content.index("#On_while_cond")
                ind2 += 15
                ind3 = file_content.index("#On_cond")
                ind3 += 9
                ind4 = file_content.index("#tab_count")

                part1 = file_content[:ind1]
                part2 = file_content[ind1:ind2]
                part3 = file_content[ind2:ind3]
                part4 = file_content[ind3:ind4]
                wr = part1 + content + "\n" + part2 + content + "\n" + part3 + "while " + content + "\n" + part4 + "#tab_count " + str(tab_count + 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
                file_detail = open(detail,"w")
                file_detail.write(wr)
                file_detail.close()
                os.chdir(current_path)
                write_cont = "while (" + content + "):"
                AUTO_IND(write_cont)
                tab_count += 1
                content = "while " + content
                nodes[node_count][1] = content
                flow_pt.write("#NODE" + str(node_count) + "\t\t|4\t\t|" + content + "\n")
                break
        """global cond_choice
        cond_choice = 2
        CONTINUE()"""
        choice.destroy()

    def ExitC():
        choice.destroy()

    btnIf=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20, text="IF condition", bg="orange",command = IF).grid(row=3,column=1)

    btnWhile=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20, text="WHILE condition", bg="orange",command = WHILE).grid(row=3,column=3)

    #btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,text="No", bg="orange",command =ExitC).grid(row=7,column=3)
    #choice.mainloop()
    #choice = input("Enter 1 to create an if else statement.\n2 to create a loop.\nEnter 'HELP' to get a clearer picture about the different conditional statements.\n")
    choice.mainloop()


def RESUME_WORK(file_name):
    global file_path, python_path, tab_count
    name = file_name
    file_name = name + ".py"
    file = open(file_name,"r")
    file_content = file.read()
    file.close()
    file_pt = open(file_name,"w")
    #print(file_content)
    file_pt.write(file_content)
    file_path = python_path + "/" + name + "_files"
    prgm_file_path = """'/' + '""" + name + "_files'\n"
    prgm_file_path = python_path + prgm_file_path
    temp_path = os.getcwd()
    os.chdir(flowchart_path)
    flow_name = name + ".txt"
    file = open(flow_name,"r")
    flow_content = file.read()
    file.close()
    flow_pt = open(flow_name,"w")
    flow_pt.write(flow_content)
    os.chdir(temp_path)
    find_temp = "\n\n\n#TEMP_(Sleep)"
    temp_end = "\n\n\n#TEMP_(Sleep)_END\n"
    ind_beg = file_content.index(find_temp) - 1
    ind_end = file_content.index(temp_end) + len(temp_end)
    temp_del = file_content[ind_beg:ind_end]
    file_content = file_content[:ind_beg]

    current_flow(flow_content)

    return(file_pt, flow_pt)


def START_NEW(file_name):
    global file_path, python_path, prgm_current_path
    name = file_name
    file_name = name + ".py"
    file = open(file_name,"w+")
    file.close()
    file_pt = open(file_name,"w")
    file_pt.write("#This is an attempt.\n")
    file_pt.write("import os\n")
    file_pt.write("import time\n")

    file_pt.write("current_path = os.getcwd()\n")
    file_path = python_path + "/" + name + "_files"
    prgm_file_path = """/""" + name + "_files"
    prgm_file_path = python_path + prgm_file_path
    prgm_file_path = prgm_file_path.replace("\\", '/')

    file_pt.write("file_path = current_path + '" + prgm_file_path + "'\n")
    #file_pt.write()
    prgm_current_path = python_path
    file_pt.write("\n\n#FUNCTION GENERATION\n\n\n\n\n\n\n\n")
    file_pt.write("""

def MAKE_DIR(new_dir):
    folders = new_dir.split('/')
    dir = folders[0]
    #dir_exists = 0
    for folder in folders:
        if(folder != folders[0]):
            dir += "/" + folder
        if(os.path.exists(dir)):
            pass
        else:
            os.mkdir(dir)

def CHANGE_DIR(change_dir):
    folders = change_dir.split('/')
    dir = folders[0]
    #dir_exists = 0
    for folder in folders:
        if(folder != folders[0]):
            dir += "/" + folder
        if(os.path.exists(dir)):
            pass
        else:
            print(dir)
            os.mkdir(dir)
    os.chdir(dir)

    """)


    file_pt.write("\n\n\n#Node_0_end\n\n\n")
    detail = name + "_d.txt"
    file_detail = open(detail, "w+")
    file_detail.write("#Variables\n\n\n\n\n#Var_end\n\n\n\n\n#If_cond\n\n\n\n\n#If_cond_end\n\n\n\n\n#On_if_cond\n\n\n\n\n#On_if_cond_end\n\n\n\n\n#While_cond\n\n\n\n\n#While_cond_end\n\n\n\n\n#On_while_cond\n\n\n\n\n#On_while_cond_end\n\n\n\n\n#Else\n\n\n\n\n#Else_end\n\n\n\n\n#On_else\n\n\n\n\n#On_else_end\n\n\n\n\n#On_cond\n\n\n\n\n#On_cond_end\n\n\n\n\n#Files\n\n\n\n\n#File_end\n\n\n\n\n#Functions\n\n\n\n\n#Function_end\n\n\n\n\n#node_val 0 #node_val_end\n\n\n\n\n#tab_count 0 #tab_count_end\n\n\n\n\n#on_going_cond 0 #on_going_cond_end\n\n\n\n\n")
    file_detail.close()
    #file.close()
    temp_path = os.getcwd()
    os.chdir(flowchart_path)
    flow_name = name + ".txt"
    file = open(flow_name,"w+")
    file.close()
    flow_pt = open(flow_name,"w")
    #flow_pt.write("#This is the beginning.\n")
    os.chdir(temp_path)
    return(file_pt, flow_pt)


python_path = program_path + "/Python"


if(os.path.exists(python_path)):
    os.chdir(python_path)
    existence = 1
else:
    os.mkdir(python_path)
    os.chdir(python_path)



root= Tk()
root.geometry("1600x800+0+0")
root.title("Epicness Generator")

Tops = Frame(root, width = 1600,height = 50)
Tops.pack(side=TOP)

f0 = Frame(root, width = 800,height = 200, relief=SUNKEN)
f0.pack(side=TOP)
f1 = Frame(root, width = 800,height = 500, relief=SUNKEN)
f1.pack(side=TOP)

lblInfo = Label(Tops, font=('arial',50,'bold'),text="Welcome to the Python programs section.\n",fg="Dark Blue", bd=5, anchor='w')
lblInfo.grid(row=0,column=0)
def ExitC():
    root.destroy()

def force_resume():
    global file_name, file_pt, flow_pt
    file_path = python_path + "/" + file_name + ".py"
    root.destroy()
    file_pt, flow_pt = RESUME_WORK(file_name)

def force_overwrite():
    global file_name, file_pt, flow_pt
    file_path = python_path + "/" + file_name + ".py"
    root.destroy()
    file_pt, flow_pt = START_NEW(file_name)


def Create():
    global file_name, root, file_pt, flow_pt

    file_name = simpledialog.askstring("Program Name", "Enter a name for the program.", parent = root)

    #file_name = input("Enter the name you want to give to your program.\n")
    gen_file_path = python_path + "/" + file_name + ".py"
    if(os.path.exists(gen_file_path)):
        #root.destroy()

        root = Tk()
        root.geometry("1600x800+0+0")
        root.title("Epicness")
        Tops = Frame(root, width = 1600,height = 50)
        Tops.pack(side=TOP)
        f0 = Frame(root, width = 800,height = 200, relief=SUNKEN)
        f0.pack(side=TOP)
        f1 = Frame(root, width = 800,height = 500, relief=SUNKEN)
        f1.pack(side=TOP)

        def ExitC():
            root.destroy()

        def force_resume():
            global file_name, file_pt, flow_pt
            file_path = python_path + "/" + file_name + ".py"
            root.destroy()
            file_pt, flow_pt = RESUME_WORK(file_name)

        def force_overwrite():
            global file_name, file_pt, flow_pt
            file_path = python_path + "/" + file_name + ".py"
            root.destroy()
            file_pt, flow_pt = START_NEW(file_name)


        lblInfo = Label(Tops, font=('arial',20,'bold'),text="A program by this name exists.\n",fg="Dark Blue", bd=5, anchor='w')
        lblInfo.grid(row=0,column=0)
        lblInfo = Label(Tops, font=('arial',20,'bold'),text="Try one of the following commands.\n",fg="Dark Blue", bd=5, anchor='w')
        lblInfo.grid(row=1,column=0)

        #Button(text='Work on this program', command = force_resume).pack(fill=X)
        btnFr=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20,
                        text="Work on this program", bg="orange",command = force_resume).grid(row=3,column=3)
        #Button(text='Rewrite this program', command = force_overwrite).pack(fill=X)
        btnFr=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20,
                        text="Rewrite this program", bg="orange",command = force_overwrite).grid(row=5,column=3)
        #Button(text='Try creating a different program', command = Create).pack(fill=X)
        btnFr=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20,
                        text="Try creating a different program", bg="orange",command = Create).grid(row=7,column=3)

        mainloop()
    else:
        root.destroy()
        file_pt, flow_pt = START_NEW(file_name)


def Work():
    global file_name, root, file_pt, flow_pt
    if existence == 0:
        messagebox.showinfo("Unfortunate", "No workable files found.\nYou will be redirected to the New Program Creation Portal.\n")
        #print("We have determined that no workable files exist, yet.\nSo you will be redirected to the New Program Creation Portal.\n")
        """root= Tk()
        """
        #application_window = Tk()

        file_name = simpledialog.askstring("Program Name", "Enter a name for the program.", parent = root)
        gen_file_path = python_path + "/" + file_name + ".py"
        root.destroy()
        file_pt, flow_pt = START_NEW(file_name)
    else:
        #root1 = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = python_path,title = "Select file",filetypes = (("Python files","*.py"),("all files","*.*")))
        file_name = (root.filename)
        parts = file_name.split("/")
        file_name = parts[-1]
        parts = file_name.split(".")
        file_name = parts[0]
        #file_name = input("Enter the name of the file you want to resume working on.\n")
        file_path = python_path + "/" + file_name + ".py"
        root.destroy()
        file_pt, flow_pt = RESUME_WORK(file_name)



btnCreate=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20,
                text="Create New Program", bg="orange",command = Create).grid(row=3,column=3)

btnWork=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20,
                text="Work on an Old Program", bg="orange",command = Work).grid(row=5,column=3)

btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="Exit", bg="orange",command =ExitC).grid(row=7,column=3)
root.mainloop()



name = file_name + ".py"
detail = file_name + "_d.txt"
flow_name = file_name + ".txt"

file_detail = open(detail,"r")
file_content = file_detail.read()
file_detail.close()
find_count = "#node_val"
count_end = "#node_val_end"
ind_count = len(find_count)
ind_beg = file_content.index(find_count)
ind_beg += ind_count + 1
ind_end = file_content.index(count_end)
node_count = int(file_content[ind_beg:ind_end])
find_tab = "#tab_count"
tab_end = "#tab_count_end"
ind_tab = len(find_tab)
ind_beg = file_content.index(find_tab)
ind_beg += ind_tab + 1
ind_end = file_content.index(tab_end)
tab_count = int(file_content[ind_beg:ind_end])
find_cond = "#on_going_cond"
cond_end = "#on_going_cond_end"
ind_cond = len(find_cond)
ind_beg = file_content.index(find_cond)
ind_beg += ind_cond + 1
ind_end = file_content.index(cond_end)
on_going_cond = int(file_content[ind_beg:ind_end])
print(node_count)
if(node_count != 0):
    choice = Tk()
    choice.geometry("1600x800+0+0")
    choice.title("Epicness Generator")

    Tops = Frame(choice, width = 1600,height = 50)
    Tops.pack(side=TOP)

    f0 = Frame(root, width = 800,height = 200, relief=SUNKEN)
    f0.pack(side=TOP)
    f1 = Frame(root, width = 800,height = 500, relief=SUNKEN)
    f1.pack(side=TOP)

    lblInfo = Label(Tops, font=('arial',50,'bold'),text="Do you want to display the flowchart?\n",fg="Dark Blue", bd=5, anchor='w')
    lblInfo.grid(row=0,column=0)

    def Yes():
        FLOW()
        root.destroy()

    def ExitC():
        root.destroy()

    btnYES=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20,
                    text="Yes", bg="orange",command = Yes).grid(row=3,column=3)

    btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                    text="No", bg="orange",command =ExitC).grid(row=7,column=3)
    root.mainloop()


while(True):
    exit = 0
    if(node_count == 0):
        choice = Tk()
        choice.geometry("1600x800+0+0")
        choice.title("Epicness Generator")

        Tops = Frame(choice, width = 1600,height = 50)
        Tops.pack(side=TOP)

        f0 = Frame(choice, width = 800,height = 200, relief=SUNKEN)
        f0.pack(side=TOP)
        f1 = Frame(choice, width = 800,height = 500, relief=SUNKEN)
        f1.pack(side=TOP)

        lblInfo = Label(Tops, font=('arial',50,'bold'),text="Following are your options:\n",fg="Dark Blue", bd=5, anchor='w')
        lblInfo.grid(row=0,column=0)

        def Start():
            nodes.append([1,0,0])
            flow_pt.write("#NODE0\t\t|1\t\t|Start\n")
            choice.destroy()

        def ExitC():
            choice.destroy()

        btnStart=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20, text="1: Start", bg="orange",command = Start).grid(row=3,column=3)

        #btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,text="No", bg="orange",command =ExitC).grid(row=7,column=3)
        choice.mainloop()


    else:
        if (on_going_cond == 0):
            Menu = Tk()
            Menu.geometry("1600x800+0+0")
            Menu.title("Epicness Generator")

            Tops = Frame(Menu, width = 1600,height = 50)
            Tops.pack(side=TOP)

            f0 = Frame(Menu, width = 800,height = 200, relief=SUNKEN)
            f0.pack(side=TOP)
            f1 = Frame(Menu, width = 800,height = 500, relief=SUNKEN)
            f1.pack(side=TOP)

            lblInfo = Label(Tops, font=('arial',50,'bold'),text="Following are your options:\n",fg="Dark Blue", bd=5, anchor='w')
            lblInfo.grid(row=0,column=0)


            def Para():
                global nodes, node_count
                nodes.append([2,0,0])
                while(True):
                    content = simpledialog.askstring("Parallelogram Content", "Enter the content of the Parallelogram.", parent = Menu)
                    nodes[node_count][1] = content
                    if('read' in content or 'accept' in content or 'Read' in content or 'Accept' in content):
                        INPUT()
                        break
                    elif('Display' in content or 'display' in content or 'Print' in content or 'print' in content or 'Write' in content or 'write' in content):
                        DISPLAY()
                        break
                    else:
                        print("The content of the node is ambigous, try simplifying it.\n")
                flow_pt.write("#NODE" + str(node_count) + "\t\t|2\t\t|" + content + "\n")
                Menu.destroy()

            def Rect():
                global nodes, node_count
                nodes.append([3,0,0])
                PROCEDURE()
                #nodes[node_count][1] = content
                Menu.destroy()

            def Rho():
                global nodes, node_count
                nodes.append([3,0,0])
                CONDITION()
                #nodes[node_count][1] = content
                Menu.destroy()

            def FLO():
                global nodes, node_count
                node_connect = FLOW()
                node_count = node_count - 1
                Menu.destroy()


            def ExitC():
                global nodes, node_count, flow_pt, file_pt, python_path, detail, Menu, exit
                file_pt.write("\n\n\n#TEMP_(Sleep)\n" )
                file_pt.write("time.sleep(60)")
                file_pt.write("\n\n\n#TEMP_(Sleep)_END\n" )
                file_pt.close()
                flow_pt.close()
                os.chdir(python_path)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
                ind_beg = file_content.index("#node_val")
                ind_end = file_content.index("#node_val_end")
                ind_beg += 10
                part1 = file_content[:ind_beg]
                part2 = file_content[ind_end:]
                text = part1 + " " + str(node_count) + " " + part2
                file_detail = open(detail,"w")
                file_detail.write(text)
                file_detail.close()
                Menu.destroy()
                exit = 1


            btnPara = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="1: Parallelogram (Input/Display)", bg="orange",command = Para).grid(row=3,column=1)

            btnRect = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="2: Rectangle (Procedure)", bg="orange",command = Rect).grid(row=3,column=3)

            btnRho = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="3: Rhombus (Decision)", bg="orange",command = Rho).grid(row=3,column=5)

            btnFlow = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="4: Flowchart", bg="orange",command = FLO).grid(row=5,column=1)

            """btnMani = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="5: Manipulate Nodes", bg="orange",command = Mani).grid(row=5,column=3)"""

            btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                            text="Save and Exit", bg="orange",command =ExitC).grid(row=7,column=3)
            Menu.mainloop()
        else:
            Menu = Tk()
            Menu.geometry("1600x800+0+0")
            Menu.title("Epicness Generator")

            Tops = Frame(Menu, width = 1600,height = 50)
            Tops.pack(side=TOP)

            f0 = Frame(Menu, width = 800,height = 200, relief=SUNKEN)
            f0.pack(side=TOP)
            f1 = Frame(Menu, width = 800,height = 500, relief=SUNKEN)
            f1.pack(side=TOP)

            lblInfo = Label(Tops, font=('arial',50,'bold'),text="Following are your options:\n",fg="Dark Blue", bd=5, anchor='w')
            lblInfo.grid(row=0,column=0)

            def Para():
                global nodes, node_count
                nodes.append([2,0,0])
                while(True):
                    content = simpledialog.askstring("Parallelogram Content", "Enter the content of the Parallelogram.", parent = Menu)
                    nodes[node_count][1] = content
                    if('read' in content or 'accept' in content or 'Read' in content or 'Accept' in content):
                        INPUT()
                        break
                    elif('Display' in content or 'display' in content or 'Print' in content or 'print' in content or 'Write' in content or 'write' in content):
                        DISPLAY()
                        break
                    else:
                        print("The content of the node is ambigous, try simplifying it.\n")
                flow_pt.write("#NODE" + str(node_count) + "\t\t|2\t\t|" + content + "\n")
                Menu.destroy()

            def Rect():
                global nodes, node_count
                nodes.append([3,0,0])
                PROCEDURE()
                #nodes[node_count][1] = content
                Menu.destroy()

            def Rho():
                global nodes, node_count
                nodes.append([3,0,0])
                CONDITION()
                #nodes[node_count][1] = content
                Menu.destroy()

            """def Rho_M():
                global nodes, node_count
                nodes.append([3,0,0])
                COND_MANAGE()
                #nodes[node_count][1] = content
                Menu.destroy()"""

            def FLO():
                global nodes, node_count
                node_connect = FLOW()
                node_count = node_count - 1
                Menu.destroy()


            def ExitC():
                global nodes, node_count, flow_pt, file_pt, python_path, detail, Menu, exit
                file_pt.write("\n\n\n#TEMP_(Sleep)\n" )
                file_pt.write("time.sleep(60)")
                file_pt.write("\n\n\n#TEMP_(Sleep)_END\n" )
                file_pt.close()
                flow_pt.close()
                os.chdir(python_path)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
                ind_beg = file_content.index("#node_val")
                ind_end = file_content.index("#node_val_end")
                ind_beg += 10
                part1 = file_content[:ind_beg]
                part2 = file_content[ind_end:]
                text = part1 + " " + str(node_count) + " " + part2
                file_detail = open(detail,"w")
                file_detail.write(text)
                file_detail.close()
                Menu.destroy()
                exit = 1


            btnPara = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="1: Parallelogram (Input/Display)", bg="orange",command = Para).grid(row=3,column=3)

            btnRect = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="2: Rectangle (Procedure)", bg="orange",command = Rect).grid(row=3,column=5)

            btnRho = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="3: Rhombus (Decision)", bg="orange",command = Rho).grid(row=5,column=1)

            """btnRho = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="3.5: Rhombus 2.0 (Condition Management)", bg="orange",command = Rho_M).grid(row=5,column=1)"""

            btnFlow = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30, text="4: Flowchart", bg="orange",command = FLO).grid(row=5,column=3)

            """btnMani = Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20, text="5: Manipulate Nodes", bg="orange",command = Mani).grid(row=5,column=5)"""

            btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                            text="Exit", bg="orange",command =ExitC).grid(row=7,column=3)
            Menu.mainloop()
            #nodes[node_count][0]=ch

    node_count += 1
    if(exit == 1):
        break
