from tkinter import*
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

import time
import os
import re
"""
from cx_Freeze import setup, Executable
import os.path"""

current_path = os.getcwd()
program_path = current_path + "/Program"
file_path = ""
prgm_current_path = ""
on_going_cond = 0

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

def check_var(in_file, temp_var, file_name):
    global python_path, current_path
    os.chdir(python_path)
    #print(in_file,temp_var)
    if (in_file == 0):
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
    else:
        file_detail = open(detail,"r")
        file_content = file_detail.read()
    	#print(co)
        file_var = "#File_" + file_name + "_var"
        #print("-" + file_var + "-")
        ind_beg = file_content.index(file_var)
        ind_beg += len(file_var) + 1
        ind_end = file_content.index("#File_" + file_name + "_var_end")
        ind_end -= 6
        variables = file_content[ind_beg:ind_end]
        variables = variables.replace(" ","")
        variables = variables.split(",")
        """print(variables)
        print(temp_var)"""
        if temp_var in variables:
            os.chdir(current_path)
            return 1
        else:
            os.chdir(current_path)
            return 0


def check_file(temp_var):
    global python_path, current_path
    os.chdir(python_path)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
    ind_beg = file_content.index("#Files")
    ind_beg += 7
    ind_end = file_content.index("#File_end")
    ind_end -= 4
    files = file_content[ind_beg:ind_end]
    files = files.split(",")
    if temp_var in files:
        """file_var = "#File_" + temp_var + "_loc"
        ind_beg = file_content.index(file_var)
        ind_beg += len(file_var) + 1
        ind_end = file_content.index("#File_" + temp_var + "_loc_end")
        ind_end -= 6
        file_loc = file_content[ind_beg:ind_end]
        file_loc = file_loc.replace(" ","")
        AUTO_IND("os.chdir('" + file_loc + "')")"""
        os.chdir(current_path)
        return 1
    else:
        os.chdir(current_path)
        return 0


def check_function(function):
    global python_path, current_path
    os.chdir(python_path)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
    ind_beg = file_content.index("#Functions")
    ind_beg += 11
    ind_end = file_content.index("#Function_end")
    ind_end -= 4
    functions = file_content[ind_beg:ind_end]
    functions = functions.split(",")
    if function in functions:
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

    st_r = """cv = Canvas(FLOW,
           width=canvas_width,
           height=canvas_height)
for i in range(2):

    cv.create_rectangle(box[i][0], box[i][1],box[i][2],box[i][3], fill=colours[i])

cv.create_line(0, 0,                 # origin of canvas
            box[0][0], box[0][1], # coordinates of left upper corner of the box[0]
            fill=colours[0],
            width=3)
cv.create_line(0, canvas_height,     # lower left corner of canvas
            box[0][0], box[0][3], # lower left corner of box[0]
            fill=colours[0],
            width=3)
cv.create_line(box[0][2],box[0][1],  # right upper corner of box[0]
            canvas_width, 0,      # right upper corner of canvas
            fill=colours[0],
            width=3)
cv.create_line(box[0][2], box[0][3], # lower right corner pf box[0]
            canvas_width, canvas_height, # lower right corner of canvas
            fill=colours[0], width=3)

cv.create_text(canvas_width / 2,
            canvas_height / 2,
            text= te)"""

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

"""
def TEMP_END():
    """


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


def INPUT_FILE():
    global nodes, node_count, tab_count, python_path, current_path
    os.chdir(python_path)
    is_int = 1
    tabs = ""
    for i in range(tab_count):
        tabs = tabs + "\t"
    content = nodes[node_count][1]

    file_count = 0
    variables = content.replace(',' , ' ')
    variables = variables.split()
    variables = [i for i in variables if (i != "Accept" and i != "accept" and i != "Integer" and i != "integer" and i != "Number" and i != "Numbers" and i != "number" and i != "numbers" and i != "read" and i != "Read" and i != "String" and i != "string" and i != "text" and i != "Text" and i != "from" and i != "File"  and i != "From" and i != "file")]
    var_count = len(variables)
    for variable in variables:
        is_file = check_file(variable)
        if( is_file == 1):
            file_name = variable
            variables.remove(variable)
            file_count += 1
            break

    if(file_count == 0):
        while(True):
            print("An error has occured.\nEither the command didn't consist of a file name to take input from, or the file with the above mentioned file name doesn't exist.\n")
            file_name = input("Enter the name of an existing file\n")
            is_file = check_file(file_name)
            if( is_file == 1):
                content = content.replace("from", "")
                content += "from " + file_name
                break

    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n#Input:\t" + content)
    AUTO_IND("")
    os.chdir(python_path)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
    file_var = "#File_" + file_name + "_loc"
    ind_beg = file_content.index(file_var)
    ind_beg += len(file_var) + 1
    ind_end = file_content.index("#File_" + file_name + "_loc_end")
    ind_end -= 6
    file_loc = file_content[ind_beg:ind_end]
    file_loc = file_loc.replace(" ","")
    AUTO_IND("os.chdir('" + file_loc + "')")

    AUTO_IND("file = open('" + file_name + """.txt',"r")""")
    AUTO_IND("file_content = file.read()")
    for variable in variables:
        is_var = check_var(1, variable, file_name)
        if (is_var == 0):
            print("The variable " + variable + " has not been defined, and hence won't be displayed.\n")
        else:
            AUTO_IND("find_var = '" + variable + "_var'")
            AUTO_IND("var_end = '" + variable + "_end'")
            AUTO_IND("ind_count = len(find_var)")
            AUTO_IND("ind_beg = file_content.index(find_var)")
            AUTO_IND("ind_beg += ind_count + 1")
            AUTO_IND("ind_end = file_content.index(var_end)")
            #AUTO_IND("ind_end -= 1")
            AUTO_IND(variable + " = file_content[ind_beg:ind_end]")
            AUTO_IND("try:")
            AUTO_IND("\t" + variable + " = int(" + variable + ")")
            AUTO_IND("except:")
            AUTO_IND("\tpass")
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
    AUTO_IND("file.close()")
    AUTO_IND("os.chdir(current_path)")
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )


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
            is_var = check_var(0, variable, "")
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
            is_var = check_var(0, variable, "")
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


def OUTPUT_FILE():
    global nodes, node_count, tab_count, current_path
    tabs = ""
    for i in range(tab_count):
        tabs = tabs + "\t"
    content = nodes[node_count][1]

    file_count = 0
    variables = content.replace(',' , ' ')
    variables = variables.split()
    variables = [i for i in variables if (i != "Write" and i != "write" and i != "Display" and i != "display" and i != "Integer" and i != "integer" and i != "Number" and i != "Numbers" and i != "number" and i != "numbers" and i != "print" and i != "Print" and i != "String" and i != "string" and i != "text" and i != "Text" and i != "to" and i != "To"  and i != "From" and i != "file")]
    var_count = len(variables)
    for variable in variables:
        is_file = check_file(variable)
        if( is_file == 1):
            file_name = variable
            variables.remove(variable)
            file_count += 1
            break

    if(file_count == 0):
        while(True):
            print("An error has occured.\nEither the command didn't consist of a file name to take output from, or the file with the above mentioned file name doesn't exist.\n")
            file_name = input("Enter the name of an existing file\n")
            is_file = check_file(file_name)
            if( is_file == 1):
                content = content.replace("from", "")
                content += "from " + file_name
                break


    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n#Output:\t" + content)
    AUTO_IND("")
    os.chdir(python_path)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
    file_var = "#File_" + file_name + "_loc"
    ind_beg = file_content.index(file_var)
    ind_beg += len(file_var) + 1
    ind_end = file_content.index("#File_" + file_name + "_loc_end")
    ind_end -= 6
    file_loc = file_content[ind_beg:ind_end]
    file_loc = file_loc.replace(" ","")
    AUTO_IND("os.chdir('" + file_loc + "')")
    AUTO_IND("file = open('" + file_name + """.txt', "w+")""")
    AUTO_IND("file_content = file.read()")
    for variable in variables:
        is_var = check_var(0, variable, "")
        if (is_var == 0):
            print("The variable '" + variable + "' has not been defined, and hence won't be written onto the file.\n")
        else:
            is_var = check_var(1, variable, file_name)
            if (is_var == 0):
                AUTO_IND("write_var = '" + variable + "_var'")
                AUTO_IND("var_end = '" + variable + "_end'")
                AUTO_IND("""text = write_var + " " + str(""" + variable + """) + " " + var_end""")
                AUTO_IND("file.write(text)")
                #AUTO_IND("file.close()")
                os.chdir(python_path)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
                file_var = "#File_" + file_name + "_var"
                if file_var in file_content:
                    ind = file_content.index(file_var)
                    ind += len(file_var) + 1
                    ind_end = file_content.index("#File_" + file_name + "_var_end")
                    ind_end -= 4
                    part1 = file_content[:ind]
                    part2 = file_content[ind:]
                    text = part1 +  variable + ", " + part2
                    file_detail = open(detail,"w")
                    file_detail.write(text)
                    file_detail.close()
                else:
                    file_content += file_var + "\n" + variable + ", \n\n\n\n\n" + file_var + "_end\n\n\n\n\n"
                    file_detail = open(detail,"w")
                    file_detail.write(file_content)
                    file_detail.close()
            else:
                AUTO_IND("write_var = '" + variable + "_var'")
                AUTO_IND("""text = write_var + " " + str(""" + variable + """) + " " """)
                AUTO_IND("file.close()")
                AUTO_IND("file = open('" + file_name + """.txt', "r")""")
                AUTO_IND("file_content = file.read()")
                AUTO_IND("file.close()")
                AUTO_IND("ind_beg = file_content.index(write_var)")
                AUTO_IND("ind_end = file_content.index(var_end)")
                AUTO_IND("rep_content = file_content[ind_beg:ind_end]")
                AUTO_IND("file_content = file_content.replace(rep_content, text)")
                AUTO_IND("file = open('" + file_name + """.txt', "w")""")
                AUTO_IND("file.write(file_content)")
    AUTO_IND("file.close()")
    AUTO_IND("os.chdir(current_path)")
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )
    os.chdir(current_path)


def DISPLAY():
    global nodes, node_count, tab_count
    tabs = ""
    for i in range(tab_count):
        tabs = tabs + "\t"
    content = nodes[node_count][1]


    """elif('number' in content or 'integer' in content or 'Number' in content or 'Integer' in content):
        num = 1
        n = content.count(",")
        n = n + 1
    else:
        n = content.count(",")
        n = n + 1"""


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
        is_var = check_var(0, variable, "")
        if (is_var == 0):
            print("The variable " + variable + " has not been defined, and hence won't be displayed.\n")
        else:
            AUTO_IND("""print('""" + variable + """ = ' + str(""" + variable + """) + '.')""")
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )


def PROCEDURE():
    global nodes, node_count, tab_count, python_path, current_path, content
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
                is_var = check_var(0, variable, "")
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
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n#Procedure:\t" + content)
    AUTO_IND("")
    for variable in variables:
        is_var = check_var(0, variable, "")
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


def COND_MANAGE():
    global nodes, node_count, tab_count, on_going_cond, python_path, current_path
    tabs = ""
    #on_going_cond -= 1
    os.chdir(python_path)
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
            file_pt.write("\n\n\n#Node_" + str(cond_node) + "_end\n" )
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
                file_pt.write("\n\n\n#Node_" + str(cond_node) + "_end\n" )
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
                cond_count += 1
                on_going_cond -= 1
                try:
                    temp_cond = cond_heir[cond_count]
                except:
                    print("All the conditions have been closed.\n")
        if is_else == 2:
            content = condition
            file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
            file_pt.write("\n#Condition:\tElse section of\t" + content + "\n")
            temp_content = "else of " + content
            nodes.append([45, temp_content, 0])
            os.chdir(python_path)
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
            write_cont = "else:"
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
            file_pt.write("\n\n\n#Node_" + str(cond_node) + "_end\n" )
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
                file_pt.write("\n\n\n#Node_" + str(cond_node) + "_end\n" )
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
            file_pt.write("\n\n\n#Node_" + str(cond_node) + "_end\n" )
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
                file_pt.write("\n\n\n#Node_" + str(cond_node) + "_end\n" )
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
                cond_count += 1
                on_going_cond -= 1
                try:
                    temp_cond = cond_heir[cond_count]
                except:
                    print("All the conditions have been closed.\n")


    #wr = part1 + content + "\n" + part2 + content + "\n" + part3 + "#tab_count " + str(tab_count - 1) + " #tab_count_end\n\n\n\n\n#on_going_cond " + str(on_going_cond) + " #on_going_cond_end\n\n\n\n\n"
    #tab_count -= 1


def CONDITION():
    global nodes, node_count, tab_count, on_going_cond, python_path, current_path, content
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
                    is_var = check_var(0, variable, "")
                    if (is_var == 0):
                        undef_var += 1
            if undef_var != 0:
                print("Unidentified Variables have been detected.\nPlease Try again.\n")
            else:
                break
        if choice == '1':
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
            flow_pt.write("#NODE" + str(node_count) + "\t\t|4\t\t|" + content + "\n")
            #file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )
            break

        elif choice == '2':
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
            flow_pt.write("#NODE" + str(node_count) + "\t\t|4\t\t|" + content + "\n")
            #file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )
            break

        elif choice == 'HELP':
            #print()
            pass
        else:
            print("Please refrain from entering an invalid input.\n")



def Call_FUNCTION():
    global nodes, node_count, tab_count
    function_name = input("Enter the name of the function you want to call\n")
    AUTO_IND(function_name + "()")
    return(function_name)


def GENERATE_FUNCTION():
    global nodes, node_count, tab_count, name, file_pt, python_path, current_path
    os.chdir(python_path)
    file_pt.close()
    while(True):
        function_name = input("Enter the name of the function you want to define\n")
        is_func = check_function(function_name)
        if is_func == 1:
            choice = int(input("There already exists a function under this name.\nEnter 1 to create a function under a different name\n2 to overwrite the function.\n3 to skip the function generation procedure.\n"))
            if choice == 1:
                pass
            elif choice == 2:
                os.chdir(python_path)
                file_pt = open(name,'r')
                file_content = file_pt.read()
                file_pt.close()
                func_beg = "def " + function_name
                func_end = function_name + "_end"
                ind_beg = file_content.index(func_beg)
                ind_end = file_content.index(func_end) + len(func_end)
                part1 = file_content[:ind_beg]
                part2 = file_content[ind_end:]
                pass_var = input("Enter the variables that need to be passed.\n")
                fn_write = "def " + function_name + "(" + pass_var + "):"
                print("Enter the contents of the function.\nYou  can enter the function line by line, and when you're done enter 'STOP'\nRefrain from writing the return statement before the 'STOP' command.\n")
                while(True):
                    function_line = input()
                    if(function_line == 'STOP'):
                        break
                    else:
                        fn_write = fn_write + "\n\t" + function_line

                return_var = input("Enter the variable to be returned.\nEnter 'DONT' in case you don't want to return anything.\n")
                if 'DONT' in return_var:
                    ret = 0
                else:
                    ret = 1
                    fn_write += "\n\treturn(" + return_var + ")"

                fn_write += "\n#" + function_name + "_end"
                ind = file_content.index("#FUNCTION GENERATION")
                ind += 23
                write = part1 + fn_write + part2
                os.chdir(python_path)
                file_pt = open(name,"w")
                file_pt.write(write)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
                ind = file_content.index("#Functions")
                ind += 11
                part1 = file_content[:ind]
                part2 = file_content[ind:]
                text = part1 + function_name + ", " + part2
                parameters = len(pass_var.split(","))

                func_para = "#Func_" + function_name + "_para"
                para_new = func_para + ' ' + str(parameters) + " " + func_para + "_end\n\n\n\n\n"
                old_ind_beg = file_content.index(func_para)
                old_ind_end = file_content.index(func_para + "_end") + len(func_para + "_end")
                para_old = file_content[old_ind_beg:old_ind_end]
                file_content.replace(para_old, para_new)

                func_ret = "#Func_" + function_name + "_ret"
                ret_new = func_ret + ' ' + str(ret) + " " + func_ret + "_end\n\n\n\n\n"
                old_ind_beg = file_content.index(func_ret)
                old_ind_end = file_content.index(func_ret + "_end") + len(func_ret + "_end")
                ret_old = file_content[old_ind_beg:old_ind_end]
                file_content.replace(ret_old, ret_new)

                file_detail = open(detail,"w")
                file_detail.write(file_content)
                file_detail.close()
                return (function_name)
                #break
            else:
                return ("NO FUNCTION")
        else:

            pass_var = input("Enter the variables that need to be passed.\n")
            fn_write = "def " + function_name + "(" + pass_var + "):"
            print("Enter the contents of the function.\nYou  can enter the function line by line, and when you're done enter 'STOP'\nRefrain from writing the return statement before the 'STOP' command.\n")
            while(True):
                function_line = input()
                if(function_line == 'STOP'):
                    break
                else:
                    fn_write = fn_write + "\n\t" + function_line

            return_var = input("Enter the variable to be returned.\nEnter 'DONT' in case you don't want to return anything.\n")
            if 'DONT' in return_var:
                ret = 0
            else:
                ret = 1
                fn_write += "\n\treturn(" + return_var + ")"

            fn_write += "\n#" + function_name + "_end"
            os.chdir(python_path)
            file_pt = open(name,'r')
            file_content = file_pt.read()
            file_pt.close()
            ind = file_content.index("#FUNCTION GENERATION")
            ind += 23
            part1 = file_content[:ind]
            part2 = file_content[ind:]
            write = part1 + "\n\n\n#Custom Function\n" + fn_write + part2
            file_pt = open(name,"w")
            file_pt.write(write)
            file_detail = open(detail,"r")
            file_content = file_detail.read()
            file_detail.close()
            #print(co)
            ind = file_content.index("#Functions")
            ind += 11
            part1 = file_content[:ind]
            part2 = file_content[ind:]
            text = part1 + function_name + ", " + part2
            parameters = len(pass_var.split(","))
            func_para = "#Func_" + function_name + "_para"
            func_ret = "#Func_" + function_name + "_ret"
            file_content = text + func_para + ' ' + str(parameters) + " " + func_para + "_end\n\n\n\n\n"
            file_content += func_ret + ' ' + str(ret) + " " + func_ret + "_end\n\n\n\n\n"
            file_detail = open(detail,"w")
            file_detail.write(file_content)
            file_detail.close()
            return (function_name)
    os.chdir(current_path)


def MAKE_DIR(new_dir):
    global current_path, prgm_current_path, node_count
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n\n\n#Make Directory:\t" + new_dir + "\n")
    AUTO_IND("new_dir = '" + new_dir + "'")
    AUTO_IND("MAKE_DIR(new_dir)")
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )


def CHANGE_DIR(change_dir):
    global current_path, prgm_current_path, node_count
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n\n\n#Change Directory:\t" + change_dir + "\n")
    AUTO_IND("change_dir = '" + change_dir + "'")
    AUTO_IND("CHANGE_DIR(change_dir)")
    AUTO_IND("current_path = change_dir")
    prgm_current_path = change_dir
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )


def CREATE_FILE(file, Target_dir):
    global current_path, python_path, prgm_current_path, file_path
    AUTO_IND("current_path = os.getcwd()")
    if(Target_dir == " "):
        choice = int(input("Enter:\n1 to create file in a specified location.\n2 to create it in the current location.\n3 to create it in an auto generated directory.\nNOTE: The auto generated directory is generated for separately for each project.\n"))
        if (choice == 1):
            Target_dir = input("Enter the directory, the file needs to be in.\n")
            Target_dir = Target_dir.replace("\\", '/')
            CHANGE_DIR(Target_dir)
            AUTO_IND("Target_dir = '" + Target_dir + "'")
        elif (choice == 2):
            Target_dir = prgm_current_path
            try:
                Target_dir = Target_dir.replace("\\", '/')
            except:
                pass
            AUTO_IND("Target_dir = current_path")
        else:
            Target_dir = file_path
            Target_dir = Target_dir.replace("\\", '/')
            AUTO_IND("Target_dir = file_path")
    else:
        try:
            Target_dir = Target_dir.replace("\\", '/')
        except:
            pass
        CHANGE_DIR(Target_dir)
        AUTO_IND("Target_dir = '" + Target_dir + "'")
    if '.' not in file:
        file_name = file + ".txt"
    else:
        file_name = file
    AUTO_IND("os.chdir(Target_dir)")
    """AUTO_IND("if current_path != Target_dir:")
    AUTO_IND("\tif(os.path.exists(Target_dir)):")
    AUTO_IND("\t\tos.chdir(Target_dir)")
    AUTO_IND("\telse:")
    AUTO_IND("\t\tos.mkdir(Target_dir)")
    AUTO_IND("\t\tos.chdir(Target_dir)")"""
    AUTO_IND("file = open('" + file_name + """', "w+")""")
    AUTO_IND("file.close()")
    AUTO_IND("os.chdir(current_path)")
    os.chdir(python_path)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
    file_detail.close()
    ind = file_content.index("#Files")
    ind += 7
    part1 = file_content[:ind]
    part2 = file_content[ind:]
    text = part1 + file + ", " + part2
    file_var = "#File_" + file + "_var"
    text = text + file_var + '\n' + " \n\n\n\n\n" + file_var + "_end\n\n\n\n\n"
    file_loc = "#File_" + file + "_loc"
    #current_path = os.getcwd()
    file_content = text + file_loc + '\n' + Target_dir + " \n\n\n\n\n" + file_loc + "_end\n\n\n\n\n"
    file_detail = open(detail,"w")
    file_detail.write(file_content)
    file_detail.close()
    os.chdir(current_path)


def GET_DIRECTORY(file):
    global nodes, python_path, current_path
    os.chdir(python_path)
    file_detail = open(detail,"r")
    file_content = file_detail.read()
    file_detail.close()
    if '.' not in file:
        file_name = file + ".txt"
    else:
        file_name = file
        file = file.split(".")
        file = str(file[0])
    file_loc = "#File_" + file + "_loc"
    file_loc_end = "#File_" + file + "_loc_end"
    ind_beg = file_content.index(file_loc)
    ind_beg += len(file_loc) + 1
    ind_end = file_content.index(file_loc_end)
    ind_end -= 5
    file_loc = file_content[ind_beg:ind_end]
    os.chdir(current_path)
    return(file_loc)


def GET_VAR(file_name, dir):
    global current_path, python_path
    os.chdir(dir)
    file_name_copy = file_name + ".txt"
    file = open(file_name_copy, "r")
    file_content = file.read()
    if(file_content == ""):
        os.chdir(current_path)
        return("Empty")
    else:
        file_content = file_content.replace("_var", " ")
        file_content = file_content.replace("_end", " ")
        contents = file_content.split()
        variables = [i for i in contents if contents.count(i) == 2]
        #variables = [i for i in  if variables.count(i) == 0]
        print(variables)
        for variable in variables:
            print(variable, file_name)
            is_var = check_var(1, variable, file_name)
            if (is_var == 0):
                os.chdir(python_path)
                file_detail = open(detail,"r")
                file_content = file_detail.read()
                file_detail.close()
                file_var = "#File_" + file_name + "_var"
                if file_var in file_content:
                    ind = file_content.index(file_var)
                    ind += len(file_var) + 1
                    ind_end = file_content.index("#File_" + file_name + "_var_end")
                    ind_end -= 4
                    part1 = file_content[:ind]
                    part2 = file_content[ind:]
                    text = part1 +  variable + ", " + part2
                    file_detail = open(detail,"w")
                    file_detail.write(text)
                    file_detail.close()
                else:
                    file_content += file_var + "\n" + variable + ", \n\n\n\n\n" + file_var + "_end\n\n\n\n\n"
                    file_detail = open(detail,"w")
                    file_detail.write(file_content)
                    file_detail.close()

        os.chdir(current_path)
        return 0

    print(file_content)


def FILE_MANAGEMENT():
    global nodes, node_count, tab_count, current_path, python_path, prgm_current_path
    content = nodes[node_count][1]
    files = content.split()
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
    file_pt.write("\n\n\n#File Creation:\t" + content)
    AUTO_IND("")
    tabs = ""
    for i in range(tab_count):
        tabs = tabs + "\t"
    """AUTO_IND("current_path = os.getcwd()")
    AUTO_IND("if current_path != file_path:")
    AUTO_IND("\tif(os.path.exists(file_path)):")
    AUTO_IND("\t\tos.chdir(file_path)")
    AUTO_IND("\telse:")
    AUTO_IND("\t\tos.mkdir(file_path)")
    AUTO_IND("\t\tos.chdir(file_path)")"""
    files =[i for i in files if (i != "Create" and i != "create" and i != "File" and i != "file" and i != "allow" and i != "Allow" and i != "accept" and i != "Accept" and i != "access" and i != "Access")]
    file = str(files[0])
    while(True):
        is_file = check_file(file)
        if( is_file == 1):
            print("This file already exists.\n")
            os.chdir(python_path)
            file_detail = open(detail,"r")
            file_content = file_detail.read()
            file_detail.close()
            file_loc = GET_DIRECTORY(file)
            #current_path = os.getcwd()
            if(file_loc != prgm_current_path):
                choice = int(input("But the file is not in the current directory.\nEnter 1 to go to the directory holding the file.\n2 to create a file with a slightly different name in the current directory.\n"))
                if(choice == 1):
                    file_loc = file_loc.replace("\\", '/')
                    CHANGE_DIR(file_loc)
                    break
                else:
                    file = input("Enter the name you want to give the file.\n")
            #Check directory of the file if it exists, if its not in the current directory, give an option to create file in the current directory or to go to that directory (found at ...).
        else:
            if("create" in content or "Create" in content):
                CREATE_FILE(file, " ")
                break
            else:
                while(True):
                    dir = input("Enter the directory where the file to be accepted is located.\n")
                    dir = dir.replace("\\", '/')
                    if(os.path.exists(dir)):
                        file_loc = dir + "/" + file + ".txt"
                        if(os.path.exists(file_loc)):
                            file_name = file + ".txt"
                            os.chdir(python_path)
                            file_detail = open(detail,"r")
                            file_content = file_detail.read()
                            file_detail.close()
                            ind = file_content.index("#Files")
                            ind += 7
                            part1 = file_content[:ind]
                            part2 = file_content[ind:]
                            text = part1 + file + ", " + part2
                            file_var = "#File_" + file + "_var"
                            text += file_var + "\n\n\n\n\n" + file_var + "_end\n\n\n\n\n"
                            file_detail = open(detail,"w")
                            file_detail.write(text)
                            file_detail.close()
                            print(text)
                            var_details = GET_VAR(file, dir)
                            os.chdir(python_path)
                            file_detail = open(detail,"r")
                            file_content = file_detail.read()
                            file_detail.close()
                            file_loc = "#File_" + file + "_loc"
                            text = file_content + file_loc + "\n" + dir + " \n\n\n\n\n" + file_loc + "_end\n\n\n\n\n"
                            file_detail = open(detail,"w")
                            file_detail.write(text)
                            file_detail.close()
                            os.chdir(current_path)
                            break
                        else:
                            choice = int(input("The file by the given doesn't exist in this directory.\nEnter 1 to create the file here, 2 to find the file in another directory.\n"))
                            if choice == 1:
                                #os.chdir(dir)

                                CREATE_FILE(file, dir)
                                os.chdir(current_path)
                                break

                    else:
                        print("This directory doesn't exist.\n")
                        choice = int(input("Enter 1 to generate this directory and create the file.\n2 to provide a different directory.\n"))
                        if choice == 1:
                            MAKE_DIR(dir)
                            CREATE_FILE(file, dir)
                            os.chdir(current_path)
                            break
                break

    flow_pt.write("#NODE" + str(node_count) + "\t\t|5\t\t|" + nodes[node_count][1] + "\n")
    file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )


def NODE_INS(node_ind):
    global nodes, node_count, current_path, python_path, flowchart_path, file_pt, flow_pt
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

            os.chdir(python_path)
            file = open(name,"r")
            file_content = file.read()
            file.close()
            ind -= 1
            beg = "#Node_" + str(ind) + "_beg"
            end = "#Node_" + str(ind) + "_end"
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
        os.chdir(python_path)
        x = input("Yes")
        #file_pt = open(name,"w")
        os.chdir(current_path)
        #flow_pt.close()


def NODE_DEL(node_ind):
    global nodes, node_count, current_path, python_path, flowchart_path, file_pt, flow_pt
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
        os.chdir(python_path)
        file = open(name,"r")
        file_content = file.read()
        file.close()
        beg = "#Node_" + str(node_ind) + "_beg"
        end = "#Node_" + str(node_ind) + "_end"
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
        os.chdir(python_path)
        file = open(name,"r")
        file_content = file.read()
        file.close()
        beg = "#Node_" + str(node_ind) + "_beg"
        end = "#Node_" + str(node_ind) + "_end"
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
            beg = "#Node_" + str(ind) + "_beg"
            end = "#Node_" + str(ind) + "_end"
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
        #flow_pt.close()


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
    file_pt.close()
    file_pt = open(file_name,"w")
    file_pt.write(file_content)

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



choice = int(input("Welcome to the Python programs section.\nEnter 1 if you want to create a new program.\n2 to continue working on a different program.\n"))
python_path = program_path + "/Python"
if(os.path.exists(python_path)):
    os.chdir(python_path)
    existence = 1
else:
    os.mkdir(python_path)
    os.chdir(python_path)
if choice == 1:
    while(True):
        file_name = input("Enter the name you want to give to your program.\n")
        gen_file_path = python_path + "/" + file_name + ".py"
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
            file_path = python_path + "/" + file_name + ".py"
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
#AUTO_IND("ind_end -= 1")
#node_count = node_count.split()
#node_count = int(node_count)
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
            choice = int(input("Enter:\n1:\tStop\n2:\tParallelogram (Input/Display)\n3:\tRectangle (Process)\n4:\tRhombus (Decision)\n5:\tOval (File management)\n6:\tFunction\n7:\tMake/Change Directory\n8:\tFlowchart\n9:\tManipulate nodes.\n10:\tSave and quit, for now.\n"))
        else:
            choice = int(input("Enter:\n1:\tStop\n2:\tParallelogram (Input/Display)\n3:\tRectangle (Process)\n4:\tRhombus (Decision)\n45:\tCondition Management\n5:\tOval (File management)\n6:\tFunction\n7:\tMake/Change Directory\n8:\tFlowchart\n9:\tManipulate nodes.\n10:\tSave and quit, for now.\n"))

            #nodes[node_count][0]=ch
        if(choice < 8):
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
                if('File' in content or 'file' in content):
                    if('read' in content or 'accept' in content or 'Read' in content or 'Accept' in content):
                        INPUT_FILE()
                        break
                    elif('Display' in content or 'display' in content or 'Print' in content or 'print' in content or 'Write' in content or 'write' in content):
                        OUTPUT_FILE()
                        break
                    else:
                        print("The content of the node is ambigous, try simplifying it.\n")
                else:
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
            print("Oval\n")
            content = input("Enter content\n")
            nodes[node_count][1] = content
            FILE_MANAGEMENT()
        elif(choice == 6):
            print("Function\n")
            choice_fn = int(input("Enter:\n1:\tDefine function\n2:\tCall function\n"))
            if(choice_fn  == 1):
                function_name = GENERATE_FUNCTION()
                content = "Define function: " + function_name
                file_pt.write("\n\n\n#Node_" + str(node_count) + "_beg\n" )
                file_pt.write("\n\n\n#Function " + function_name + " defined\n" )
                file_pt.write("\n\n\n#Node_" + str(node_count) + "_end\n" )
            else:
                function_name = Call_FUNCTION()
                content = "Call function: " + function_name
            nodes[node_count][1] = content
            flow_pt.write("#NODE" + str(node_count) + "\t\t|6\t\t|" + nodes[node_count][1] + "\n")
        elif(choice == 7):
            print("Directory\n")
            choice_dir = int(input("Enter:\n1:\tMake Directory\n2:\tChange Current Working Directory\n"))
            if(choice_dir  == 1):
                content = "Make Directory: "
                new_dir = input("Enter the address of the new directory to be created.\n")
                new_dir = new_dir.replace("\\", '/')
                content += new_dir
                MAKE_DIR(new_dir)
            else:
                content = "Change Working Directory: "
                change_dir = input("Enter the address of the directory to make it the working directory.\n")
                change_dir = change_dir.replace("\\", '/')
                content += change_dir
                CHANGE_DIR(change_dir)
            nodes[node_count][1] = content
            flow_pt.write("#NODE" + str(node_count) + "\t\t|7\t\t|" + nodes[node_count][1] + "\n")
        elif(choice == 8):
            print("Flow\n")
            node_connect = FLOW()

            node_count = node_count-1


        elif(choice == 9):
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
                os.chdir(python_path)
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
                choice = int(input("Enter:\n2:\tParallelogram (Input/Display)\n3:\tRectangle (Process)\n4:\tRhombus (Decision)\n5:\tOval (File management)\n6:\tFunction\n7:\tMake/Change Directory\n"))


                if(choice == 2):
                    print("Parallelogram\n")
                    while(True):
                        content = input("Enter content\n")
                        nodes[node_count][1] = content
                        if('File' in content or 'file' in content):
                            if('read' in content or 'accept' in content or 'Read' in content or 'Accept' in content):
                                INPUT_FILE()
                                break
                            elif('Display' in content or 'display' in content or 'Print' in content or 'print' in content or 'Write' in content or 'write' in content):
                                OUTPUT_FILE()
                                break
                            else:
                                print("The content of the node is ambigous, try simplifying it.\n")
                        else:
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
                elif(choice == 5):
                    print("Oval\n")
                    content = input("Enter content\n")
                    nodes[node_count][1] = content
                    FILE_MANAGEMENT()
                elif(choice == 6):
                    print("Function\n")
                    function_name = Call_FUNCTION()
                    content = "Call function: " + function_name
                    nodes[node_count][1] = content
                    flow_pt.write("#NODE" + str(node_count) + "\t\t|6\t\t|" + nodes[node_count][1] + "\n")
                elif(choice == 7):
                    print("Directory\n")
                    choice_dir = int(input("Enter:\n1:\tMake Directory\n2:\tChange Current Working Directory\n"))
                    if(choice_dir  == 1):
                        content = "Make Directory: "
                        new_dir = input("Enter the address of the new directory to be created.\n")
                        new_dir = new_dir.replace("\\", '/')
                        content += new_dir
                        MAKE_DIR(new_dir)
                    else:
                        content = "Change Working Directory: "
                        change_dir = input("Enter the address of the directory to make it the working directory.\n")
                        change_dir = change_dir.replace("\\", '/')
                        content += change_dir
                        CHANGE_DIR(change_dir)
                    nodes[node_count][1] = content
                    flow_pt.write("#NODE" + str(node_count) + "\t\t|7\t\t|" + nodes[node_count][1] + "\n")
                node_count = temp_count
                file_pt.close()
                os.chdir(file_path)
                file_pt = open("temp.txt", "r")
                content_ins = file_pt.read()
                file_pt.close()
                os.chdir(python_path)
                file_pt = open(name, "r")
                file_content = file_pt.read()
                file_pt.close()
                file_pt = open(name, "w")

                beg = "#Node_" + str(node_ind - 1) + "_end"
                end = "#Node_" + str(node_ind + 1) + "_beg"
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



ch=int(input("1 to run.\n"))
if(ch == 1):
    exec(open(name).read())
