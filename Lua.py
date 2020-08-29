from tkinter import*
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

import time

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
#file_name =""
detail = ""

#nodes=[[0,0,0,0] for i in range(100)]
nodes = []

existence = 0


def check_var(temp_var):
    global lua_path, current_path
    os.chdir(lua_path)
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
    text = tabs + text
    text = text + "\n"
    file_pt.write(text)

"""
def FLOW():
    global nodes, node_count
    for i in range(node_count):
        #print(nodes[i])
        try:
            if(nodes[i][0] == 1):
                print(str(i) + "\tStart\n")
            elif(nodes[i][0] == 2):
                print(str(i) + "\tPara:\t" + str(nodes[i][1]) + "\n\n")
            elif(nodes[i][0] == 3):
                print(str(i) + "\tRect:\t" + str(nodes[i][1]) + "\n\n")
            elif(nodes[i][0] == 4):
                print(str(i) + "\tRho:\t" + str(nodes[i][1]) + "\n\n")
            elif(nodes[i][0] == 45):
                #print(str(i) + "\tElse:\t" + str(nodes[i][1]) + "\n\n")
                if(nodes[i][1][0] == 'e'):
                    print(str(i) + "\tRho:\t" + str(nodes[i][1]) + "\n\n")

        except:
            break
        if(i < node_count - 1):
            print("\t  |\n")
            print("\t  |\n")
            print("\t  ↓\n")
    return i"""

def FLOW():
    canvas_width = 400
    canvas_height = 100

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
    global nodes, node_count, tab_count, lua_path, current_path
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
    file_pt.write("\n\n\n--Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n--Input:\t" + content)
    AUTO_IND("")
    if(is_int == 1):
        text = tabs + """io.write('Enter """ + str(var_count) + """ inputs.')"""
        text = text +'\n'
        AUTO_IND(text)
        for variable in variables:
            is_var = check_var(variable)
            if (is_var == 0):
                os.chdir(lua_path)
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

            AUTO_IND("""io.write('Enter a string value of """ + variable + """: ')""")
            AUTO_IND(variable + """ = io.read("*n")""")
    else:
        text = tabs + """io.write('Enter """ + str(var_count) + """ inputs.')"""
        text = text +'\n'
        AUTO_IND(text)
        for variable in variables:
            is_var = check_var(variable)
            if (is_var == 0):
                os.chdir(lua_path)
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
        AUTO_IND("""io.write('Enter a string value of """ + variable + """: ')""")
        AUTO_IND(variable + """ = io.read("*n")""")
    file_pt.write("\n\n\n--Node_" + str(node_count) + "_end\n" )


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
    file_pt.write("\n\n\n--Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n--Output:\t" + content)
    AUTO_IND("")
    #text = tabs + """print("Enter """ + str(var_count) + """ inputs.")"""
    """text = text +'\n'
    file.write(text)"""
    for variable in variables:
        is_var = check_var(variable)
        if (is_var == 0):
            print("The variable " + variable + " has not been defined, and hence won't be displayed.\n")
        else:
            AUTO_IND("""io.write('""" + variable + """ = ' , """ + variable + """ , '.' )""")
            AUTO_IND("""io.write('\\""" + """n')""")
            #AUTO_IND("")
    file_pt.write("\n\n\n--Node_" + str(node_count) + "_end\n" )


def PROCEDURE():
    global nodes, node_count, tab_count, lua_path, current_path, content
    tabs = ""
    for i in range(tab_count):
        tabs = tabs + "\t"
    while(True):
        while(True):
            content = input("Enter the operation\n")
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
                print("The condition doesn't follow the required format.\nPlease try again.\n")
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
            print("Unidentified Variables have been detected in the RHS.\nPlease Try again.\n")
        else:
            break

    variables = re.findall("[A-Za-z0-9]+ ", content)
    variables = [i for i in variables if (i!="")]
    #print(variables)

    var_count = len(variables)
    file_pt.write("\n\n\n--Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n--Procedure:\t" + content)
    AUTO_IND("")
    for variable in variables:
        is_var = check_var(variable)
        if (is_var == 0):
            os.chdir(lua_path)
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
    file_pt.write("\n\n\n--Node_" + str(node_count) + "_end\n" )


def END_COND():
    global nodes, node_count, tab_count, on_going_cond, lua_path, current_path
    tabs = ""
    """#on_going_cond -= 1
    os.chdir(lua_path)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
    file_detail.close()
    #choice = int(input("Enter 1"))
    ind1 = file_content.index("#On_cond")
    ind1 += 9
    ind2 = file_content.index("#On_cond_end")
    cond_heir = file_content[ind1:ind2]
    upd_cond_heir = cond_heir
    cond_heir = cond_heir.split("\n")
    cond_heir = [i for i in cond_heir if (i!="")]"""

    file_pt.write("\n\n\n--TEMP_(Unclosed conditions)\n" )

    if(tab_count > 0):
        while(tab_count != 0):
            tab_count -= 1
            AUTO_IND("")
            AUTO_IND("end")
    file_pt.write("\n\n\n--TEMP_(Unclosed conditions)_END\n" )

    #pass


def COND_MANAGE():
    global nodes, node_count, tab_count, on_going_cond, lua_path, current_path
    tabs = ""
    #on_going_cond -= 1
    os.chdir(lua_path)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
    file_detail.close()
    #choice = int(input("Enter 1"))
    ind1 = file_content.index("#On_cond")
    ind1 += 9
    ind2 = file_content.index("#On_cond_end")
    cond_heir = file_content[ind1:ind2]
    upd_cond_heir = cond_heir
    cond_heir = cond_heir.split("\n")
    cond_heir = [i for i in cond_heir if (i!="")]

    ind1 = file_content.index("#On_if_cond")
    ind1 += 12
    ind2 = file_content.index("#On_if_cond_end")
    if_conditions = file_content[ind1:ind2]
    new_on_ifs = if_conditions
    if_conditions = if_conditions.split("\n")
    if_conditions = [i for i in if_conditions if (i!="")]

    ind1 = file_content.index("#On_else")
    ind1 += 9
    ind2 = file_content.index("#On_else_end")
    elses = file_content[ind1:ind2]
    new_on_elses = elses
    elses = elses.split("\n")
    elses = [i for i in elses if (i!="")]

    ind1 = file_content.index("#On_while_cond")
    ind1 += 15
    ind2 = file_content.index("#On_while_cond_end")
    while_conditions = file_content[ind1:ind2]
    new_on_whiles = while_conditions
    while_conditions = while_conditions.split("\n")
    while_conditions = [i for i in while_conditions if (i!="")]

    if(len(while_conditions) != 0 and len(if_conditions) != 0 and len(elses) != 0):
        choice = int(input("Enter 1 to manage an IF condition.\n2 to end a WHILE loop.\n3 to end an ELSE section.\n"))
    elif(len(while_conditions) == 0 and len(elses) == 0):
        print("There's no ongoing WHILE loop or an ELSE section.\nYou'll be directed to manage the ongoing IF condition.\n")
        choice = 1
    elif(len(if_conditions) == 0 and len(elses) == 0):
        print("There's no ongoing IF condition or ELSE section.\nYou'll be directed to manage the ongoing WHILE loop.\n")
        choice = 2
    elif(len(if_conditions) == 0 and len(while_conditions) == 0):
        print("There's no ongoing IF condition or WHILE loop.\nYou'll be directed to manage the ongoing ELSE sections.\n")
        choice = 3
    elif(len(while_conditions) == 0):
        choice = int(input("Enter 1 to manage IF.\n3 to manage ELSE.\n"))
    elif(len(if_conditions) == 0):
        choice = int(input("Enter 2 to manage WHILE.\n3 to manage ELSE.\n"))
    else:
        choice = int(input("Enter 1 to manage IF.\n2 to manage WHILE.\n"))
    if(choice == 1):
        print("Select one of the following.\n")
        count = 1
        temp_dict = []
        for condition in if_conditions:
            print(str(count) + " for " + condition + "\n")
            temp_dict.append(condition)
            count += 1
        choice = int(input())
        choice -= 1
        is_else = int(input("Enter 1 to simply end the IF condition.\n2 to generate an ELSE section for this particular IF condition.\n"))
        condition = temp_dict[choice]
        temp_cond = "if " + condition
        if (temp_cond == cond_heir[0]):
            cond_node = 1
            while (cond_node < node_count):
                if(nodes[cond_node][1] == temp_cond):
                    break
                cond_node += 1
            print(cond_node)
            condition = condition + "\n"
            new_on_ifs = new_on_ifs.split(condition)
            try:
                new_on_ifs = new_on_ifs[0] + new_on_ifs[1]
            except:
                new_on_ifs = str(new_on_ifs[0])
            upd_cond_heir = upd_cond_heir.split(condition)
            try:
                upd_cond_heir = upd_cond_heir[0] + upd_cond_heir[1]
            except:
                upd_cond_heir = str(upd_cond_heir[0])

            ind1 = file_content.index("#On_if_cond")
            ind1 += 12
            ind2 = file_content.index("#On_if_cond_end")
            ind3 = file_content.index("#On_cond")
            ind3 += 9
            ind4 = file_content.index("#On_cond_end")
            ind5 = file_content.index("#tab_count")
            part1 = file_content[:ind1]
            part2 = file_content[ind2:ind3]
            part3 = file_content[ind4:ind5]

            wr = part1 + new_on_ifs + part2 + upd_cond_heir + part3 + "#tab_count " + str(tab_count - 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
            file_detail = open(detail,"w")
            file_detail.write(wr)
            file_detail.close()
            os.chdir(current_path)
            tab_count -= 1
            AUTO_IND("")
            if(is_else != 2):
                AUTO_IND("end")
            file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
            on_going_cond -= 1
        else:
            temp_if = temp_cond
            temp_cond = cond_heir[0]
            cond_count = 0
            while (temp_cond != temp_if):
                cond_count += 1
                temp_cond = cond_heir[cond_count]

            cond_limit = cond_count
            temp_cond = cond_heir[0]
            cond_count = 0
            while(cond_count <= cond_limit):
                cond_node = 1
                while (cond_node < node_count):
                    if(nodes[cond_node][1] == temp_cond):
                        break
                    cond_node += 1
                condition = condition + "\n"
                upd_cond_heir = upd_cond_heir.split(condition)
                #upd_cond_heir = upd_cond_heir[0] + upd_cond_heir[1]
                upd_cond_heir = str(upd_cond_heir[0])
                if(temp_cond[0] == 'i'):
                    new_on_ifs = new_on_ifs.split(condition)
                    try:
                        new_on_ifs = new_on_ifs[0] + new_on_ifs[1]
                    except:
                        new_on_ifs = str(new_on_ifs[0])

                    ind1 = file_content.index("#On_if_cond")
                    ind1 += 12
                    ind2 = file_content.index("#On_if_cond_end")
                elif(temp_cond[0] == 'w'):
                    new_on_whiles = new_on_whiles.split(condition)
                    try:
                        new_on_whiles = new_on_whiles[0] + new_on_whiles[1]
                    except:
                        new_on_whiles = str(new_on_whiles[0])

                    ind1 = file_content.index("#On_while_cond")
                    ind1 += 15
                    ind2 = file_content.index("#On_while_cond_end")
                else:
                    new_on_elses = new_on_elses.split(condition)
                    try:
                        new_on_elses = new_on_elses[0] + new_on_elses[1]
                    except:
                        new_on_elses = str(new_on_elses[0])

                    ind1 = file_content.index("#On_else")
                    ind1 += 9
                    ind2 = file_content.index("#On_else_end")

                ind3 = file_content.index("#On_cond")
                ind3 += 12
                ind4 = file_content.index("#On_cond_end")
                ind5 = file_content.index("#tab_count")
                part1 = file_content[:ind1]
                part2 = file_content[ind2:ind3]
                part3 = file_content[ind4:ind5]

                wr = part1 + new_on_ifs + part2 + upd_cond_heir + part3 + "#tab_count " + str(tab_count - 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
                file_detail = open(detail,"w")
                file_detail.write(wr)
                file_detail.close()
                os.chdir(current_path)
                tab_count -= 1
                AUTO_IND("")
                AUTO_IND("end")
                file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
                cond_count += 1
                on_going_cond -= 1
                try:
                    temp_cond = cond_heir[cond_count]
                except:
                    print("All the conditions have been closed.\n")
        if is_else == 2:
            content = condition
            file_pt.write("\n\n\n--Node_" + str(node_count) + "_beg\n" )
            file_pt.write("\n--Condition:\tElse section of\t" + content + "\n")
            temp_content = "else of " + content
            nodes.append([45, temp_content, 0])
            os.chdir(lua_path)
            file_detail = open(detail,"r")
            file_content = file_detail.read()
            file_detail.close()
            #print(co)
            ind1 = file_content.index("#Else")
            ind1 += 6
            ind2 = file_content.index("#On_else")
            ind2 += 9
            ind3 = file_content.index("#On_cond")
            ind3 += 9
            ind4 = file_content.index("#tab_count")

            part1 = file_content[:ind1]
            part2 = file_content[ind1:ind2]
            part3 = file_content[ind2:ind3]
            part4 = file_content[ind3:ind4]
            on_going_cond += 1
            wr = part1 + content + "\n" + part2 + content + "\n" + part3 + "else of " + content + "\n" + part4 + "#tab_count " + str(tab_count + 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
            file_detail = open(detail,"w")
            file_detail.write(wr)
            file_detail.close()
            os.chdir(current_path)
            write_cont = "else"
            AUTO_IND(write_cont)
            tab_count += 1
            content = "else of " + content
            flow_pt.write("#NODE" + str(node_count) + "\t\t|4\t\t|" + content + "\n")
            node_count += 1


    elif(choice == 2):
        print("Select one of the following.\n")
        count = 1
        temp_dict = []
        for condition in while_conditions:
            print(str(count) + " for " + condition + "\n")
            temp_dict.append(condition)
            count += 1
        choice = int(input())
        choice -= 1
        condition = temp_dict[choice]
        temp_cond = "while " + condition
        if (temp_cond == cond_heir[0]):
            cond_node = 1
            while (cond_node < node_count):
                if(nodes[cond_node][1] == temp_cond):
                    break
                cond_node += 1
            print(cond_node)
            #file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
            condition = condition + "\n"
            new_on_whiles = new_on_whiles.split(condition)
            try:
                new_on_whiles = new_on_whiles[0] + new_on_whiles[1]
            except:
                new_on_whiles = str(new_on_whiles[0])
            upd_cond_heir = upd_cond_heir.split(condition)
            try:
                upd_cond_heir = upd_cond_heir[0] + upd_cond_heir[1]
            except:
                upd_cond_heir = str(upd_cond_heir[0])

            ind1 = file_content.index("#On_while_cond")
            ind1 += 15
            ind2 = file_content.index("#On_while_cond_end")
            ind3 = file_content.index("#On_cond")
            ind3 += 9
            ind4 = file_content.index("#On_cond_end")
            ind5 = file_content.index("#tab_count")
            part1 = file_content[:ind1]
            part2 = file_content[ind2:ind3]
            part3 = file_content[ind4:ind5]

            wr = part1 + new_on_whiles + part2 + upd_cond_heir + part3 + "#tab_count " + str(tab_count - 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
            file_detail = open(detail,"w")
            file_detail.write(wr)
            file_detail.close()
            os.chdir(current_path)
            tab_count -= 1
            AUTO_IND("")
            AUTO_IND("end")
            file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
            on_going_cond -= 1
        else:
            temp_while = temp_cond
            temp_cond = cond_heir[0]
            cond_count = 0
            while (temp_cond != temp_while):
                cond_count += 1
                temp_cond = cond_heir[cond_count]

            cond_limit = cond_count
            temp_cond = cond_heir[0]
            cond_count = 0
            while(cond_count <= cond_limit):
                cond_node = 1
                while (cond_node < node_count):
                    if(nodes[cond_node][1] == temp_cond):
                        break
                    cond_node += 1
                #file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
                condition = condition + "\n"
                upd_cond_heir = upd_cond_heir.split(condition)
                #upd_cond_heir = upd_cond_heir[0] + upd_cond_heir[1]
                upd_cond_heir = str(upd_cond_heir[0])
                if(temp_cond[0] == 'i'):
                    new_on_ifs = new_on_ifs.split(condition)
                    try:
                        new_on_ifs = new_on_ifs[0] + new_on_ifs[1]
                    except:
                        new_on_ifs = str(new_on_ifs[0])

                    ind1 = file_content.index("#On_if_cond")
                    ind1 += 12
                    ind2 = file_content.index("#On_if_cond_end")
                elif(temp_cond[0] == 'w'):
                    new_on_whiles = new_on_whiles.split(condition)
                    try:
                        new_on_whiles = new_on_whiles[0] + new_on_whiles[1]
                    except:
                        new_on_whiles = str(new_on_whiles[0])

                    ind1 = file_content.index("#On_while_cond")
                    ind1 += 15
                    ind2 = file_content.index("#On_while_cond_end")
                else:
                    new_on_elses = new_on_elses.split(condition)
                    try:
                        new_on_elses = new_on_elses[0] + new_on_elses[1]
                    except:
                        new_on_elses = str(new_on_elses[0])

                    ind1 = file_content.index("#On_else")
                    ind1 += 9
                    ind2 = file_content.index("#On_else_end")

                ind3 = file_content.index("#On_cond")
                ind3 += 12
                ind4 = file_content.index("#On_cond_end")
                ind5 = file_content.index("#tab_count")
                part1 = file_content[:ind1]
                part2 = file_content[ind2:ind3]
                part3 = file_content[ind4:ind5]

                wr = part1 + new_on_whiles + part2 + upd_cond_heir + part3 + "#tab_count " + str(tab_count - 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
                file_detail = open(detail,"w")
                file_detail.write(wr)
                file_detail.close()
                os.chdir(current_path)
                tab_count -= 1
                AUTO_IND("")
                AUTO_IND("end")
                file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
                cond_count += 1
                on_going_cond -= 1
                #NODED NODED NODED
                try:
                    temp_cond = cond_heir[cond_count]
                except:
                    print("All the conditions have been closed.\n")
    else:
        print("Select one of the following.\n")
        count = 1
        temp_dict = []
        for condition in elses:
            print(str(count) + " for " + condition + "\n")
            temp_dict.append(condition)
            count += 1
        choice = int(input())
        choice -= 1
        condition = temp_dict[choice]
        temp_cond = "else of " + condition
        if (temp_cond == cond_heir[0]):
            temp_cond += "\n"
            cond_node = 1
            while (cond_node < node_count):
                #print ("1 " + nodes[cond_node][1] + str(len(nodes[cond_node][1])) + "\n2 " + temp_cond + str(len(temp_cond)) + "\n\n")
                if(nodes[cond_node][1] == temp_cond):
                    break
                cond_node += 1
            print(cond_node)
            #file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
            condition = condition + "\n"
            new_on_elses = new_on_elses.split(condition)
            try:
                new_on_elses = new_on_elses[0] + new_on_elses[1]
            except:
                new_on_elses = str(new_on_elses[0])
            upd_cond_heir = upd_cond_heir.split(condition)
            try:
                upd_cond_heir = upd_cond_heir[0] + upd_cond_heir[1]
            except:
                upd_cond_heir = str(upd_cond_heir[0])

            ind1 = file_content.index("#On_else")
            ind1 += 12
            ind2 = file_content.index("#On_else_end")
            ind3 = file_content.index("#On_cond")
            ind3 += 9
            ind4 = file_content.index("#On_cond_end")
            ind5 = file_content.index("#tab_count")
            part1 = file_content[:ind1]
            part2 = file_content[ind2:ind3]
            part3 = file_content[ind4:ind5]

            wr = part1 + new_on_ifs + part2 + upd_cond_heir + part3 + "#tab_count " + str(tab_count - 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
            file_detail = open(detail,"w")
            file_detail.write(wr)
            file_detail.close()
            os.chdir(current_path)
            tab_count -= 1
            AUTO_IND("")
            AUTO_IND("end")
            file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
            on_going_cond -= 1
        else:
            temp_else = temp_cond
            temp_cond = cond_heir[0]
            cond_count = 0
            print(temp_else + "\n\n\n")
            while (temp_cond != temp_else):
                print(temp_cond)
                cond_count += 1
                temp_cond = cond_heir[cond_count]

            cond_limit = cond_count
            temp_cond = cond_heir[0]
            cond_count = 0
            while(cond_count <= cond_limit):
                cond_node = 1
                while (cond_node < node_count):
                    if(nodes[cond_node][1] == temp_cond):
                        break
                    cond_node += 1
                #file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
                condition = condition + "\n"
                upd_cond_heir = upd_cond_heir.split(condition)
                #upd_cond_heir = upd_cond_heir[0] + upd_cond_heir[1]
                upd_cond_heir = str(upd_cond_heir[0])
                if(temp_cond[0] == 'i'):
                    new_on_ifs = new_on_ifs.split(condition)
                    try:
                        new_on_ifs = new_on_ifs[0] + new_on_ifs[1]
                    except:
                        new_on_ifs = str(new_on_ifs[0])

                    ind1 = file_content.index("#On_if_cond")
                    ind1 += 12
                    ind2 = file_content.index("#On_if_cond_end")
                elif(temp_cond[0] == 'w'):
                    new_on_whiles = new_on_whiles.split(condition)
                    try:
                        new_on_whiles = new_on_whiles[0] + new_on_whiles[1]
                    except:
                        new_on_whiles = str(new_on_whiles[0])

                    ind1 = file_content.index("#On_while_cond")
                    ind1 += 15
                    ind2 = file_content.index("#On_while_cond_end")
                else:
                    new_on_elses = new_on_elses.split(condition)
                    try:
                        new_on_elses = new_on_elses[0] + new_on_elses[1]
                    except:
                        new_on_elses = str(new_on_elses[0])

                    ind1 = file_content.index("#On_else")
                    ind1 += 9
                    ind2 = file_content.index("#On_else_end")

                ind3 = file_content.index("#On_cond")
                ind3 += 12
                ind4 = file_content.index("#On_cond_end")
                ind5 = file_content.index("#tab_count")
                part1 = file_content[:ind1]
                part2 = file_content[ind2:ind3]
                part3 = file_content[ind4:ind5]

                wr = part1 + new_on_ifs + part2 + upd_cond_heir + part3 + "#tab_count " + str(tab_count - 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
                file_detail = open(detail,"w")
                file_detail.write(wr)
                file_detail.close()
                os.chdir(current_path)
                tab_count -= 1
                AUTO_IND("")
                AUTO_IND("end")
                file_pt.write("\n\n\n--Node_" + str(cond_node) + "_end\n" )
                cond_count += 1
                on_going_cond -= 1
                try:
                    temp_cond = cond_heir[cond_count]
                except:
                    print("All the conditions have been closed.\n")


def CONDITION():
    global nodes, node_count, tab_count, on_going_cond, lua_path, current_path, content
    tabs = ""
    on_going_cond += 1
    for i in range(tab_count):
        tabs = tabs + "\t"
    print("The different conditional statements possible are an if else statement, or a looping statement.\n")
    while(True):
        choice = input("Enter 1 to create an if else statement.\n2 to create a loop.\nEnter 'HELP' to get a clearer picture about the different conditional statements.\n")
        while(True):
            while(True):
                content = input("Enter the condition\n")
                content =  content + " "
                variables = re.findall("[A-Za-z0-9]+ ", content)
                check = re.findall("[<>=]+ ", content)
                operators = re.findall("[+*/]+ ", content)
                if not check :
                    print("The condition doesn't follow the required format.\nPlease try again.\n")
                else:
                    format = content.split(str(check[0]))
                    format = [i for i in format if (i!="")]
                    if len(format) == 1:
                        print("The condition doesn't follow the required format.\nPlease try again.\n")
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
                print("Unidentified Variables have been detected.\nPlease Try again.\n")
            else:
                break
        if choice == '1':
            file_pt.write("\n\n\n--Node_" + str(node_count) + "_beg\n" )
            file_pt.write("\n--Condition:\tIf type\t" + content + "\n")
            os.chdir(lua_path)
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
            write_cont = "if (" + content + ")"
            AUTO_IND(write_cont)
            write_cont = "then"
            AUTO_IND(write_cont)
            tab_count += 1
            content = "if " + content
            flow_pt.write("#NODE" + str(node_count) + "\t\t|4\t\t|" + content + "\n")
            #file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )
            break

        elif choice == '2':
            file_pt.write("\n\n\n--Node_" + str(node_count) + "_beg\n" )
            file_pt.write("\n--Condition:\tWhile type\t" + content + "\n")
            os.chdir(lua_path)
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
            write_cont = "while (" + content + ")"
            AUTO_IND(write_cont)
            write_cont = "do"
            AUTO_IND(write_cont)
            tab_count += 1
            content = "while " + content
            flow_pt.write("#NODE" + str(node_count) + "\t\t|4\t\t|" + content + "\n")
            #file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )
            break

        elif choice == 'HELP':
            #print()
            pass
        else:
            print("Please refrain from entering an invalid input.\n")


def NODE_INS(node_ind):
    global nodes, node_count, current_path, lua_path, flowchart_path, file_pt, flow_pt
    if node_ind == node_count:
        print("The position of the node, coincides with the position the system would give the node, so no further actions are necessary.")
    else:
        nodes.append([0, 0, 0])
        flow_pt.close()
        os.chdir(flowchart_path)
        #flow_name = name + ".txt"
        flow_pt = open(flow_name,"r")
        flow_content = flow_pt.read()
        flow_pt.close()
        content = flow_content.split("\n")
        content = [i for i in content if i != ""]
        content.append(0)
        file_pt.close()


        ind = node_count
        #print(node_count)
        while (ind > node_ind):
            #print(a[ind])
            content[ind] = content[ind - 1]
            nodes[ind] = nodes[ind - 1]

            os.chdir(lua_path)
            file = open(name,"r")
            file_content = file.read()
            file.close()
            ind -= 1
            beg = "--Node_" + str(ind) + "_beg"
            end = "--Node_" + str(ind) + "_end"
            print(beg)
            print(end)
            ind_beg = file_content.index(beg)
            ind_beg += 6
            ind_end = file_content.index(end)
            ind_end += 6
            content_1 = file_content[:ind_beg]
            content_2 = file_content[ind_beg + 1:ind_end]
            content_3 = file_content[ind_end + 1:]
            file_content = content_1 + str(ind + 1) + content_2 + str(ind + 1) + content_3
            file_pt = open(name,"w")
            file_pt.write(file_content)
            file_pt.close()
        """else:
            del nodes[ind]
            del content[ind]"""
        os.chdir(flowchart_path)
        flow_content = ""
        for node_line in content:
            flow_content = flow_content + node_line + "\n"
        #flow_name = name + ".txt"
        flow_pt = open(flow_name, "w")
        flow_pt.write(flow_content)
        os.chdir(lua_path)
        x = input("Yes")
        #file_pt = open(name,"w")
        os.chdir(current_path)


def NODE_DEL(node_ind):
    global nodes, node_count, current_path, lua_path, flowchart_path, file_pt, flow_pt
    if node_ind == node_count:
        os.chdir(flowchart_path)
        #flow_name = name + ".txt"
        del nodes[-1]
        flow_pt = open(flow_name,"r")
        flow_content = flow_pt.read()
        flow_pt.close()
        content = flow_content.split("\n")
        content = [i for i in content if i != ""]
        del content[-1]
        flow_pt = open(flow_name, "w")
        flow_pt.write(flow_content)
        file_pt.close()
        os.chdir(lua_path)
        file = open(name,"r")
        file_content = file.read()
        file.close()
        beg = "--Node_" + str(node_ind) + "_beg"
        end = "--Node_" + str(node_ind) + "_end"
        ind_beg = file_content.index(beg)
        ind_beg -= 3
        ind_end = file_content.index(end)
        ind_end += 12
        content_1 = file_content[:ind_beg]
        content_2 = file_content[ind_end:]
        file_content = content_1 + content_2
        file_pt = open(name,"w")
        file_pt.write(file_content)
    else:
        flow_pt.close()
        os.chdir(flowchart_path)
        #flow_name = name + ".txt"
        flow_pt = open(flow_name,"r")
        flow_content = flow_pt.read()
        flow_pt.close()
        content = flow_content.split("\n")
        content = [i for i in content if i != ""]
        file_pt.close()
        os.chdir(lua_path)
        file = open(name,"r")
        file_content = file.read()
        file.close()
        beg = "--Node_" + str(node_ind) + "_beg"
        end = "--Node_" + str(node_ind) + "_end"
        print(beg)
        print(end)
        ind_beg = file_content.index(beg)
        ind_beg -= 3
        ind_end = file_content.index(end)
        ind_end += 12
        content_1 = file_content[:ind_beg]
        content_2 = file_content[ind_end:]
        file_content = content_1 + content_2
        file_pt = open(name,"w")
        file_pt.write(file_content)
        file_pt.close()

        ind = node_ind
        print(node_count)
        while (ind < node_count-1):
            #print(a[ind])
            content[ind] = content[ind + 1]
            nodes[ind] = nodes[ind + 1]

            file = open(name,"r")
            file_content = file.read()
            file.close()
            ind += 1
            beg = "--Node_" + str(ind) + "_beg"
            end = "--Node_" + str(ind) + "_end"
            print(beg)
            print(end)
            ind_beg = file_content.index(beg)
            ind_beg += 6
            ind_end = file_content.index(end)
            ind_end += 6
            content_1 = file_content[:ind_beg]
            content_2 = file_content[ind_beg + 1:ind_end]
            content_3 = file_content[ind_end + 1:]
            file_content = content_1 + str(ind - 1) + content_2 + str(ind - 1) + content_3
            file_pt = open(name,"w")
            file_pt.write(file_content)
            file_pt.close()
        else:
            del nodes[ind]
            del content[ind]
        os.chdir(flowchart_path)
        flow_content = ""
        for node_line in content:
            flow_content = flow_content + node_line + "\n"
        #flow_name = name + ".txt"
        print("-" + flow_content + "-")
        flow_pt = open(flow_name, "w")
        flow_pt.write(flow_content)
        file_pt = open(name,"w")


def RESUME_WORK(file_name):
    global file_path, lua_path, tab_count
    name = file_name
    file_name = name + ".lua"
    file = open(file_name,"r")
    file_content = file.read()
    file.close()
    file_pt = open(file_name,"w")
    #print(file_content)
    file_pt.write(file_content)
    file_path = lua_path + "/" + name + "_files"
    prgm_file_path = """'/' + '""" + name + "_files'\n"
    prgm_file_path = lua_path + prgm_file_path
    temp_path = os.getcwd()
    os.chdir(flowchart_path)
    flow_name = name + ".txt"
    file = open(flow_name,"r")
    flow_content = file.read()
    file.close()
    flow_pt = open(flow_name,"w")
    flow_pt.write(flow_content)
    os.chdir(temp_path)

    try:
        find_temp = "\n\n\n--TEMP_(Unclosed conditions)"
        temp_end = "\n\n\n--TEMP_(Unclosed conditions)_END\n"
        ind_beg = file_content.index(find_temp) - 1
        ind_end = file_content.index(temp_end) + len(temp_end)
        temp_del = file_content[ind_beg:ind_end]
        file_content = file_content[:ind_beg]
        file_pt.close()
        file_pt = open(file_name,"w")
        file_pt.write(file_content)
        #file_pt.close()
    except:
        pass

    current_flow(flow_content)

    return(file_pt, flow_pt)


def START_NEW(file_name):
    global file_path, lua_path, prgm_current_path
    name = file_name
    file_name = name + ".lua"
    file = open(file_name,"w+")
    file.close()
    file_pt = open(file_name,"w")
    file_pt.write("--This is an attempt.\n")

    file_path = lua_path + "/" + name + "_files"
    prgm_file_path = """/""" + name + "_files"
    prgm_file_path = lua_path + prgm_file_path
    prgm_file_path = prgm_file_path.replace("\\", '/')

    file_pt.write("--file_path = current_path + '" + prgm_file_path + "'\n")
    #file_pt.write()
    prgm_current_path = lua_path

    file_pt.write("\n\n\n--Node_0_end\n\n\n")
    detail = name + "_d.txt"
    file_detail = open(detail, "w+")
    file_detail.write("#Variables\n\n\n\n\n#Var_end\n\n\n\n\n#If_cond\n\n\n\n\n#If_cond_end\n\n\n\n\n#On_if_cond\n\n\n\n\n#On_if_cond_end\n\n\n\n\n#While_cond\n\n\n\n\n#While_cond_end\n\n\n\n\n#On_while_cond\n\n\n\n\n#On_while_cond_end\n\n\n\n\n#Else\n\n\n\n\n#Else_end\n\n\n\n\n#On_else\n\n\n\n\n#On_else_end\n\n\n\n\n#On_cond\n\n\n\n\n#On_cond_end\n\n\n\n\n#node_val 0 #node_val_end\n\n\n\n\n#tab_count 0 #tab_count_end\n\n\n\n\n#on_going_cond 0 #on_going_cond_end\n\n\n\n\n")
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



choice = int(input("Welcome to the Lua programs section.\nEnter 1 if you want to create a new program.\n2 to continue working on a different program.\n"))
lua_path = program_path + "/Lua"
if(os.path.exists(lua_path)):
    os.chdir(lua_path)
    existence = 1
else:
    os.mkdir(lua_path)
    os.chdir(lua_path)
if choice == 1:
    while(True):
        file_name = input("Enter the name you want to give to your program.\n")
        gen_file_path = lua_path + "/" + file_name + ".lua"
        if(os.path.exists(gen_file_path)):
            choice = int(input("This name has already been used for another program.\nEnter 1 resume working on that file.\n2 to sart anew by rewriting that file.\n3 to provide a different name to start working on a new program.\n"))
            if choice == 1:
                file_pt, flow_pt = RESUME_WORK(file_name)
                break
            elif choice == 2:
                file_pt, flow_pt = START_NEW(file_name)
                break
        else:
            file_pt, flow_pt = START_NEW(file_name)
            break

else:
    if existence == 0:
        print("We have determined that no workable files exist, yet.\nSo you will be redirected to the New Program Creation Portal.\n")
        file_name = input("Enter the name you want to give to your program.\n")
        file_pt, flow_pt = START_NEW(file_name)
    else:
        while(True):
            file_name = input("Enter the name of the file you want to resume working on.\n")
            file_path = lua_path + "/" + file_name + ".lua"
            if(os.path.exists(file_path)):
                print("Okay, the file has been found.\nYou may resume working on the file.\n")
                file_pt, flow_pt = RESUME_WORK(file_name)
                break
            else:
                print("The file name you entered doesn't exist.\n")
                choice = int(input("Enter 1 to create a file of this name.\n2 to attempt again at guessing the file name.\n"))
                if choice == 1:
                    file_pt, flow_pt = START_NEW(file_name)
                    break


name = file_name + ".lua"
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



if(node_count != 0):
    choice = int(input("1 to print flowchart.\n"))
    if(choice == 1):
        FLOW()
while(True):
    if(node_count == 0):
        choice = int(input("Enter:\n1:\tStart\n"))
        #nodes[node_count][0]=ch
        nodes.append([choice,0,0])
        flow_pt.write("#NODE0\t\t|1\t\t|Start\n")
    else:
        if (on_going_cond == 0):
            choice = int(input("Enter:\n1:\tStop\n2:\tParallelogram (Input/Display)\n3:\tRectangle (Process)\n4:\tRhombus (Decision)\n5:\tFlowchart\n6:\tManipulate nodes.\n7:\tSave and quit, for now.\n"))
        else:
            choice = int(input("Enter:\n1:\tStop\n2:\tParallelogram (Input/Display)\n3:\tRectangle (Process)\n4:\tRhombus (Decision)\n45:\tCondition Management\n5:\tFlowchart\n6:\tManipulate nodes.\n7:\tSave and quit, for now.\n"))

            #nodes[node_count][0]=ch
        if(choice < 5 ):
            nodes.append([choice,0,0])
        if(choice == 1):
            print("Stop\n")
            #flow_pt.write("#NODE" + str(node_count) + "\t\t|1\t\t|Stop\n")
            break
        elif(choice == 2):
            print("Parallelogram\n")
            while(True):
                content = input("Enter content\n")
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
        elif(choice == 3):
            print("Rectangle\n")
            PROCEDURE()
            #content=input("Enter content\n")
            nodes[node_count][1] = content
        elif(choice == 4):
            print("Rhombus\n")
            CONDITION()
            nodes[node_count][1] = content
        elif(choice == 45):
            print("Rhombus Management\n")
            COND_MANAGE()
            node_count -= 1
            #nodes[node_count][1] = content
        elif(choice == 5):
            print("Flow\n")
            node_connect = FLOW()
            """ch=int(input("Enter the node number you want to connect the current node to, 0 to continue further.\n"))
            if(ch!=0):
                nodes[ch][2]=i"""
            node_count = node_count-1


        elif(choice == 6):
            print("Flow\n")
            node_connect = FLOW()
            choice = int(input("Enter:\n1 to insert node.\n2 to delete node."))
            if(choice == 1):
                node_ind = int(input("Enter the node number you want to insert the node to.\n"))
                NODE_INS(node_ind)
                #node_count -= 1
                temp_count = node_count
                node_count = node_ind
                """#file_pt.close()
                os.chdir(lua_path)
                file_pt = open(name, "r")
                content = file_pt.read()
                file_pt.close()"""
                if(os.path.exists(file_path)):
                    os.chdir(file_path)
                else:
                    os.mkdir(file_path)
                    os.chdir(file_path)
                #os.chdir(file_path)
                file_pt = open("temp.txt", "w")
                #file_pt.write(content)
                #os.chdir(current_path)
                choice = int(input("Enter:\n2:\tParallelogram (Input/Display)\n3:\tRectangle (Process)\n4:\tRhombus (Decision)\n"))


                if(choice == 2):
                    print("Parallelogram\n")
                    while(True):
                        content = input("Enter content\n")
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
                elif(choice == 3):
                    print("Rectangle\n")
                    """content=input("Enter content\n")"""
                    PROCEDURE()
                    nodes[node_count][1] = content
                elif(choice == 4):
                    print("Rhombus\n")
                    CONDITION()
                    nodes[node_count][1] = content
                node_count = temp_count
                file_pt.close()
                os.chdir(file_path)
                file_pt = open("temp.txt", "r")
                content_ins = file_pt.read()
                file_pt.close()
                os.chdir(lua_path)
                file_pt = open(name, "r")
                file_content = file_pt.read()
                file_pt.close()
                file_pt = open(name, "w")

                beg = "--Node_" + str(node_ind - 1) + "_end"
                end = "--Node_" + str(node_ind + 1) + "_beg"
                ind_beg = file_content.index(beg)
                ind_beg += 12
                try:
                    ind_end = file_content.index(end)
                    ind_end -= 3
                    content_1 = file_content[:ind_beg]
                    content_2 = file_content[ind_end:]
                    file_content = content_1 + content_ins + content_2
                except:
                    content_1 = file_content[:ind_beg]
                    file_content = content_1 + content_ins
                file_pt = open(name,"w")
                file_pt.write(file_content)

                if(node_count != node_ind):
                    flow_pt.close()
                    os.chdir(flowchart_path)
                    #flow_name = name + ".txt"
                    flow_pt = open(flow_name,"r")
                    flow_content = flow_pt.read()
                    flow_pt.close()
                    content = flow_content.split("\n")
                    content = [i for i in content if i != ""]
                    print(content)
                    content[node_ind] = content[-1]
                    del content[-1]
                    print(content)
                    os.chdir(flowchart_path)
                    flow_content = ""
                    for node_line in content:
                        flow_content = flow_content + node_line + "\n"
                    #flow_name = name + ".txt"
                    flow_pt = open(flow_name, "w")
                    flow_pt.write(flow_content)
                    current_flow(flow_content)
                    print(nodes)
                    print(node_count)
                    node_count -= 1


            elif(choice == 2):
                no_nodes = int(input("Enter the node number of nodes you want to delete.\n"))
                node_del = []
                for i in range(no_nodes):
                    node_del.append(int(input("Enter node number as per the flowchart:\t")))
                node_del = [i for i in node_del if i <= node_count]
                for ind in range(len(node_del)):
                    temp = node_del[0]
                    NODE_DEL(node_del[0])
                    node_count -= 1
                    del node_del[0]
                    try:
                        for i in range(len(node_del)):
                            if(node_del[i] > temp):
                                node_del[i] -= 1
                    except:
                        break
                print(len(node_del))

                node_count -= 1

        else:
            print("The current progress will be saved.\nYou can resume working on the project later.\n")
            END_COND()
            #file_pt.write("time.sleep(60)")
            file_pt.close()
            flow_pt.close()
            os.chdir(lua_path)
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
            break
    node_count += 1
    #print(node_count)
#print(nodes)
choice = int(input("1 to print flowchart.\n"))
if(choice == 1):
    #node_count -= 1
    FLOW()
    print("\t  |\n")
    print("\t  |\n")
    print("\t  ↓\n")
    print(str(node_count)+"\tStop\n")
