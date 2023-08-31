import time

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    message = f"{current_time}: Hello World"
    
    with open("output.txt", "a") as file:
        file.write(message + "\n")
    
    print(message)
    time.sleep(5)
