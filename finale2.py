#we import the Buzzer and DistanceSensor and sleep
from gpiozero import Buzzer
from gpiozero import DistanceSensor
from time import sleep
ultrasonic = DistanceSensor(echo=14,trigger=15)
buzzer=Buzzer(4)
i=0
#we make two functions to turn the buzzer on and off and printing the distance
def far():
    print(f"the distance{i}=",format(dis,'.2f'))
    buzzer.off()
    sleep(1)
def close():
    print(f"the distance{i}=",format(dis,'.2f'))
    buzzer.on()
    sleep(1)
while True:
    dis=ultrasonic.distance*100
    #if the distance is more than 15cm then we get the first function
    if dis>=15:
        far()
    #if the distance is less than 15cm then we get the first function
    elif dis<=14:
        close()
    i=i+1