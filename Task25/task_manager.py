#libraries

from datetime import date
import datetime

#global constans viriable
userList = []#This initialise userlist to nothing.
passList = []#this initialise passlist to nothing

#define function
def reg_user():
    newusername = input("Enter New username: ")#This will input the username when user want to log in,it will request a username.             

    while True:#This uses while loop because we want the loop to continue looping if the condition is True.
            if not newusername in userList:#This uses if statement to check the condition of username in userlist.
                break#This also break the loop for infiniting       
            else:
                print("username already exits,try different username!") #This if the condition is false,it will print wrong username
                newusername = input("Enter New username: ")#This ask the user to re-enter the username if it is invalid.
       
    user_password = input("Please enter new password: ")
    confirmation = input("Please confirm the password: ")
    if user_password == confirmation:#This compares the user_password to confirmation.
        userfile = open("user.txt","a")#This open the file in append mode
        userfile.write("\n" + newusername + ', '+ user_password)#This will input username and password in a newline
        userfile.close()
        checker = 1
    else:
            print('password do not match')

def add_task():
# #  if choice == "a":#If the user selected a,the input should ask the user to input the new username,title,task description,date assigned,due dateand completion of the task.
    new_username = input("Who task assigned to:")#This will ask the user,who the task assigned to.
    title = input("Please enter the title of the task:")#This will ask the title of the task.
    task_description = input("What is the task description? ")#This will ask the discription of the task.
    date_assigned = date.today()#This will ask the date,the task assigned.
    due_date = input("Please enter the due date of the task:")#This will ask the due date of the task.
    completion = "No"#This ask the tasks are complete or not,so here since we adding task,we keep adding them,when neceessary to add,there no completion.
    userfile = open("tasks.txt","a")#This will append the task.txt. 
    userfile.write("\n" + new_username + ', '+ title + ', ' + task_description + ', '+ str(date_assigned) + ', ' + due_date + ', '  + completion)#this will continue write tasks in a format way.
    userfile.close()#After writting or reading we close the task.
    return_to_the_main = input('Do you want to return to the main manu?:press -1')

def view_all():

    # if choice == "va":#IF the choice is va,it will need the user to open reading mode of the file.
        with open("tasks.txt","r") as userfile:#THis the reading mode of the text file,and it automatically close after reading or writting.
            for line in userfile:#This will loop the userfile,because we want it to read each and line of the file
                taskslist = line.split(', ')#this split the tasks separated by comma and a space.
            
                print('Task:\t'+taskslist[1])#Task in tasklist is in index[1].
                print('Assing to:\t'+taskslist[0])#assign to in tasklist is in index[0]
                print('Date assigned:\t'+taskslist[3])#Date assigned in tasklist is in index [3]
                print('Due date:\t'+taskslist[4])#Due date in tasklist is in index[4]
                print('Task complete?\t'+taskslist[5])#Task complete in tasklist is in index[5]
                print('Task description:\t'+taskslist[2])#Task description in tasklist is in index[2]


def view_mine():  #This define the function view mine().
    j =0  #This
    i =[]
    tasks = {}
    with open('tasks.txt','r') as myfile: 
        lines = myfile.readlines()

        for num,line in enumerate(lines):
            taskslist = line.split(', ')#this split the tasks separated by comma and a space.
            tasks[num] = taskslist
            if username == taskslist[0]:#This compares username to tasklist[0]
                print(f"The task number is: {num}")
                print('Task:\t'+taskslist[1])#Task in tasklist is in index[1].
                print('Assign to:\t'+taskslist[0])#assign to in tasklist is in index[0]
                print('Date assigned:\t'+taskslist[3])#Date assigned in tasklist is in index [3]
                print('Due date:\t'+taskslist[4])#Due date in tasklist is in index[4]
                print('Task complete?\t'+taskslist[5])#Task complete in tasklist is in index[5]
                print('Task description:\t'+taskslist[2])#Task description in tasklist is in index[2]

        

    task_num = int(input("Please select the input you would like to edit: "))
    task = tasks[task_num]
    edit_option = input('''Would you like to:
                           e-edit task
                      c- mark complete
                          -1 - return to main menu\n''')        
    if edit_option == 'e':
        edit_option2 = input('''Would you like to:
                        d - change due date
                        u - change user name
                        \n''')
        if edit_option2 == 'd':
            new_due_date = input("Enter new_due_date: ") 
            task[-2] = new_due_date
        if edit_option2 == "u":
            task['assigned_to'] = input("Please enter new user: ")
            nu_tasks = [task[tasks]for task in tasks] 
            with open('tasks.txt','r') as userFile:                                  
                num_task = 0
        # if userFile == taskslist[0]:#This compares username to tasklist[0]
        #     print('Task Number: ' + int(num_task) + '\nUsername: ' + taskslist[0] + '\nTitle: ' + taskslist[1] + '\nTask Discription:' + taskslist[2] + '\nDue Date: ' + taskslist[3] + '\nCompleted ' + taskslist[4] + '\n')
            #edit_Task = input('Would you like to edit a task? edit or  return to the manu?(-1)')
        
    elif edit_option == 'c':
        task[5] = input("Mark complete? Yes or No?  ")   
        if task[0]  == "No":
           edit_Task = input('Would you like to edit a task? edit, Yes or No? or  return to the manu?(-1)')


def generate_taskOverview():
    taskfile = open('tasks.txt','r')
    tasklist = taskfile.readlines()
    taskfile.close()
    total_numb_task = len(tasklist)
    numb_of_incompleted_tasks = 0
    numb_of_completed_tasks = 0
    overdue_tasks = 0

        
    for task in tasklist:
        compl = task.strip('\n').split(', ')[-1]
        print(compl)
        if compl.lower() == 'yes':
            numb_of_completed_tasks += 1
        else:
            numb_of_incompleted_tasks += 1

            strdate = task.strip('\n').split(', ')[-2]
            dObject = datetime.datetime.strptime(strdate, '%d %b %Y')
            currentdate = datetime.datetime.now()

            if dObject < currentdate:
                overdue_tasks +=1   

            

    percentage_incompleted = (numb_of_incompleted_tasks/total_numb_task) * 100
    percentage_completed = (numb_of_completed_tasks/total_numb_task) * 100
    percentage_overdue = (overdue_tasks/total_numb_task)*100

    task_overview_file = open('task_overview.txt', 'w')
    task_overview_file.write(f'The total number of task is {total_numb_task}\n' )
    task_overview_file.write(f'The total number of completed tasks generated by taskmanager.py is {numb_of_completed_tasks}\n')
    task_overview_file.write(f'The total number of incompleted tasks generated by taskmanager.py is {numb_of_incompleted_tasks}\n ')
    
    task_overview_file.write(f'The total percentage of completed tasks generated by taskmanager.py is {percentage_completed}%\n ')
    task_overview_file.write(f'The total percentage of incompleted tasks generated by taskmanager.py is {percentage_incompleted}%\n ')

    print(f'The total number of incompleted tasks that are overdue generated by taskmanager.py is {overdue_tasks} \n')
    print(f'The total percentage of incompleted tasks that are overdue generated by taskmanager.py is {percentage_overdue}%\n')     


def for_each_user(tn, user_n = 'admin'):
    taskfile = open('tasks.txt','r')
    tasklist = taskfile.readlines()
    taskfile.close()
    total_numb_task = 0  #This initialises the total number of task
    numb_of_completed_tasks = 0  #This Initialises the completed task
    numb_0f_incompleted_tasks = 0  #This initialises the incompleted task
    task_count = 0  #This Initialises the number of task.
    currentdate = datetime.datetime.now()  #This initialises the date and time.
    


    for t in tasklist:  #This will loop through the tasklist and tis a temporal variable.
        task_count += 1  #This increment the number of task
        user = t.split(', ')[0]  #This will split the user with comma and space. 
        compl = t.strip('\n').split(', ')[-1]
        if user == user_n:  #This compare the user with user_n
            
            total_numb_task += 1  #This increment the number of task 
            if compl.lower() == 'yes': #This compares the completed task with yes
                numb_of_completed_tasks += 1  #This increment the numb_of_completed task.
            else:  #This shows if the task are incomplete,its a no
                 numb_0f_incompleted_tasks +=1  #This will increment the number task that are not complete.


    

    percentage_of_task = (total_numb_task/task_count)*100  #This calculate the percentage of task
    percentage_completed =  (numb_of_completed_tasks/total_numb_task) * 100  #This calculate the percentage of completed task
    percentage_incompleted =  (numb_0f_incompleted_tasks/total_numb_task) * 100  #This calculate the percentage of incompleted task.

    user_overview_file = open('user_overview.txt','w')  #This open the file user_overview on writting mode.
    user_overview_file.write(f'Details for user {user_n}\n______')  #This will desplay the user.
    user_overview_file.write(f'The total number of task are {total_numb_task}\n') #This will dessplay the number of task that are assigned to the user.
    user_overview_file.write (f'The percentage of task assigned to user are {percentage_of_task} %\n')  #This will desplay the percentage of task that assigned to the user.
    user_overview_file.write(f'The total percentage of completed tasks by user is {percentage_completed}%\n ')  #This will display the total percentage of task that are completed by a user.
    user_overview_file.write(f'The total percentage of tasks that are not yet completed and overdue by user is {percentage_incompleted}%\n ')  #This will display the task that are incomplete

def user_overview():   #This define the function.
    taskfile = open('tasks.txt','r')  #This open the file tasks.txt in a reading mode
    tasklist = taskfile.readlines()  #This read the file each and every line.
    taskfile.close()  #This close the file.
    total_numb_tasks = len( tasklist)  #This measure the length of the tasklist.
    userfile = open('user.txt','r')  #This open the user.txt in a reading mode.
    userlist = userfile.readlines()  #This read the file(userlist) each and every line.
    userfile.close()  #This closes the file(userfile)
    total_numb_users = len( userlist)

    print(f'The total number of users is {total_numb_users}\n' )  #This will print the total nuber of users.
    print(f'The total number of task is {total_numb_tasks}\n' )  #This will print the total number of task
    for_each_user(tn=total_numb_tasks) 



def generate_reports(): #This is defining the function.
    generate_taskOverview()  #This is defining the function
    user_overview()  #This is calling

def display_statistics():  #This define the function of the stats
    generate_taskOverview()
    user_overview()
    
    print("Displaying statistics for admin:\n")  #This will print(Display statistics for admin:) and jump to new line.
   
    with open('task_overview.txt','r') as f:  #This will open the file (task_overview.txt) in a reading mode.
        fil = f.read()  #This read each and every line in a file
        print(fil) #this will print the information inside the file(fil) 
    with open("user_overview.txt",'r') as time:  #This will open the file in a reading mode
        tell = time.read()  #This will read the lines of the file
        print(tell)  #This will print the information inside(tell)



#main function

userFile = open("user.txt", "r")#This read the file in userfile.
for line in userFile:#This loop the userfile
        usern, passw = line.strip("\n").split(", ") #This strip the characters in usern and passw which are initialised by line,after after striping the empty spaces from left to right in to new line,it split usern with a comma  and space to passw.
        userList.append(usern)#This will append the usern.
        passList.append(passw)#This will also append the passw 


username = input("Enter username: ")#This will input the username when user want to log in,it will request a username.             

while True:#This uses while loop because we want the loop to continue looping if the condition is True.
    if username in userList:#This uses if statement to check the condition of username in userlist.
        for index, user in enumerate(userList):#This uses for loop to numerate index and user in userlist.
            if user == username:#This compare user to username
                passwordIndex = index
                break#The loop is True,it does not stop until you break it.
        break#This also break the loop for infiniting       
    else:
        print("wrong user name, try again.")#This if the condition is false,it will print wrong username
        username = input("Enter username: ")#This ask the user to re-enter the username if it is invalid.
        
password = input("Enter the password: ")#This ask the user to input the password

while True:#This also True,so the user uses while loop to make the loop run until it is True.
    if password == passList[passwordIndex]:#This initialises passwordIndex to password
             break#This stops the loop from running
    else:
      print("Invalid password,re-enter the password")#This print wrong password if the condition is falls
    password = input("Enter the password: ")#This Will ask the user to re enter the password until the condition is True.
pass
#while 1:
    
if username == 'admin':#This compares admin to username
    choice=input('''Please select one of the following options:
    
r - register user
a - add task:
va - veiw all tasks:
vm - view my tasks:
gr - generate reports:
ds - display statistics:
e - exit\n''')#This ask the user  to input the option.
else:
    choice=input('''Please select one of the following options:
a - add task:
va - veiw all tasks:
vm - view my tasks:
e - exit\n''')


if choice == 'gr':  #This if the user chose the option gr
    generate_reports()  #This is calling the function
if choice == 'ds':  #This is the choice of the user
    display_statistics()     #This is calling the function. 
    

if choice == "r":#This shows if the user chose the first option,the following will be asked as input
    reg_user()  #This is calling the function

if choice == 'a':
    add_task()  #This is calling the function

if choice == "va":#IF the choice is va,it will need the user to open reading mode of the file
    view_all()

if choice == "vm":#if the choice is vm,the user will open the file in a reading mode
    view_mine()  #This is calling the function



                # print('Assing to:\t'+taskslist[0])#assign to in tasklist is in index[0]
                # print('Date assigned:\t'+taskslist[3])#Date assigned in tasklist is in index [3]
                # print('Due date:\t'+taskslist[4])#Due date in tasklist is in index[4]
                # print('Task complete?\t'+taskslist[5])#Task complete in tasklist is in index[5]
                # print('Task description:\t'+taskslist[2])#Task description in tasklist is in index[2]
