def run():
    print("Process started running...")

def shut_down():
    print("process is shutting down...")

def email_send():
    print("email_send")

def start_task_1():
    print("started task 1")

def start_task_2():
    print("start task 2")

if __name__ == '__main__': # This is the entry point, it run directly the file will call email_send()
    run()
    start_task_1()
    start_task_2()
    email_send()
    shut_down()