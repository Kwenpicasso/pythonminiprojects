import time

print("countdown from your choosen seconds")


while True:
    secs = int(input("Enter seconds to countdown from: "))
    if secs <= 0:
        print("X please enter a positive number")
        continue
    
    print(f"Starting cuntdown in {secs} seconds!!!")
    for sec in range(secs,0,-1):
        print(f"{sec} seconds remaining ...")
        time.sleep(1)
    print("COUNTDOWN COMPLETE!!")
    retry = input("Start another countdown? (yes/no): ")

    if retry.lower() != 'yes':
        print("Thanks for using the countdown timer")
        break
