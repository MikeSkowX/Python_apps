import c_body
from tkinter import *

calendar = []
status = []
checkbuttons = []
textlist = []

def config():
    global main_root, button_display_list, button_add_task, button_delete_task, button_delete_all_done, button_exit_app
    main_root = Tk()
    main_root.title('Lista zadan')
    main_root.geometry("500x500")
    button_display_list = Button(main_root, text='Display Tasks', width=12, command=display)
    button_display_list.grid(column=0, row=4)
    button_add_task = Button(main_root, text='Add Task', width=12, command=add)
    button_add_task.grid(column=0, row=0)
    button_delete_task = Button(main_root, text='Delete Task', width=12, command=delete)
    button_delete_task.grid(column=0, row=1)
    button_delete_all_done = Button(main_root, text='Delete All Done', width=12, command=del_all_done)
    button_delete_all_done.grid(column=0, row=2)
    button_exit_app = Button(main_root, text='EXIT', width=12, command=exit_window)
    button_exit_app.grid(column=0, row=3)

def add():
    insert_root = Toplevel()
    insert_root.title('Dodaj zadanie:')
    task = Entry(insert_root, width=80)
    task.grid(column=0, row=0, padx=20, pady=20)
    def add_task():
        global task_obj, calendar
        date = c_body.CalendarObj.nowDate()
        time = c_body.CalendarObj.nowTime()
        task_obj = c_body.CalendarObj(task.get(), date, time)
        calendar.append(task_obj)
        textlist.append(StringVar())
        status.append(BooleanVar())
        display()
        insert_root.destroy()
    button_add = Button(insert_root, text='dodaj zadanie', command=add_task)
    button_add.grid(column=0, row=1, sticky=E, padx=20, pady=20)
    insert_root.mainloop()

def delete():
    delete_root = Toplevel()
    delete_root.title('Delete task:')
    deltask = Entry(delete_root, width=80)
    deltask.grid(column=0, row=0, padx=20, pady=20)
    def del_task():
        global task_obj, calendar
        i = int(deltask.get()) - 1
        calendar.remove(calendar[i])
        status.remove(status[i])
        checkbuttons[i].destroy()
        checkbuttons.remove(checkbuttons[i])
        textlist.remove(textlist[i])
        display()
        delete_root.destroy()
    button_add = Button(delete_root, text='delete task', command=del_task)
    button_add.grid(column=0, row=1, sticky=E, padx=20, pady=20)
    delete_root.mainloop()

def del_all_done():
    global calendar, status, checkbuttons, textlist
    bufor_calendar = []
    bufor_status = []
    bufor_checkbuttons = []
    bufor_textlist = []
    for i in range(len(calendar)):
        if calendar[i].stat is not False:
            bufor_calendar.append(i)
            bufor_status.append(i)
            bufor_checkbuttons.append(i)
            bufor_textlist.append(i)
        checkbuttons[i].destroy()
    calendar = bufor_calendar
    status = bufor_status
    checkbuttons = bufor_checkbuttons
    textlist = bufor_textlist
    return calendar, status, checkbuttons, textlist

def display():
    global calendar, textlist, status, checkbuttons
    def callback_on_checkbutton_click():
        print("One of the Checkbuttons clicked!")
        for i in range(len(calendar)):
            print('\tOld calendar[' + str(i) + '] state: ' + calendar[i].displayObj())
            calendar[i].stat = status[i].get()
            print('\t\tNew calendar[' + str(i) + '] state: ' + calendar[i].displayObj())
    checkbuttons.clear()
    for i in range(len(calendar)):
        lp = i + 1
        print("status dla:", lp, calendar[i].stat)
        x = (str(lp) + '. ' + calendar[i].displayObj())
        textlist[i].set(x)
        if calendar[i].stat == False:
            print("display() called. For index i: ", i, ' setting checkbutton value to checked (onvalue=0)')
            status[i].set(False)
        elif calendar[i].stat == True:
            print("display() called. For index i: ", i, ' setting checkbutton value to unchecked (offvalue=1)')
            status[i].set(True)
        checkbuttons.append(
            Checkbutton(
                master=main_root,
                textvariable=textlist[i],
                variable=status[i],
                onvalue=True,
                offvalue=False,
                command=callback_on_checkbutton_click
            )
        )
        checkbuttons[i].grid(column=1, row=i+1, sticky=W)

def exit_window():
    main_root.destroy()

if __name__ == '__main__':
    config()
    main_root.mainloop()


"""
    """
"""def del_all_done():
    global calendar
    bufor_list = []
    for i in calendar:
        if i.stat is False:
            bufor_list.append(i)
        elif i.stat is True:
            del status[-1]
            del textlist[-1]
    calendar = bufor_list

    return calendar"""
"""def change_status():
    calendar.stat = not calendar.stat
def update():
    okno_glowne.after(100, display)
def del_all_done():
    global calendar
    bufor_list = []
    for i in calendar:
        if i.stat is False:
            bufor_list.append(i)
    calendar = bufor_list
    return calendar
    
    def callback_on_checkbutton_click():
    print("One of the Checkbuttons clicked!")
    for i in range(len(calendar)):
        print('\tOld calendar[' + str(i) + '] state: ' + calendar[i].displayObj())
        calendar[i].stat = status[i].get() == 1
        print('\t\tNew calendar[' + str(i) + '] state: ' + calendar[i].displayObj())
    """