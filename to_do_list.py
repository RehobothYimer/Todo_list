# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:48:04 2025

@author: PC1
"""

def to_do_list():
    
    print("To Do List:")
    options = ["add task", "view task","mark complete","delete task","exit"]
    task = []
    task_completed =[]
    for i,op in enumerate(options,start=1):
        print(f"{i}.{op}")
    
   
    while True:
        enter = input("Enter your option:")
        match enter:
            case '1':
                add_task = input("Enter a task:")
                task.append(add_task)
                print(task)
            case '2':
                print(task)
                
            case '3':
                complete_type =input("what task to complete.")
                if complete_type in task:
                    task_completed.append(complete_type)
                    task.remove(complete_type)
                    print("Task complete.",task_completed)
                    
                else:
                    print("task not found.")
                
            case '4':
               delete= input("Enter task to be removed:")
               task.remove(delete)
               print(task)
               
            case '5':
                break
        cont = input("would you like to continue: y/n.")
        if cont=='y':
            continue
        else:
            break
    
to_do_list()
