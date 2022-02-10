from gpiozero import LED,MotionSensor
from time import sleep

#initialisation
led= LED(4)
senseur=MotionSensor(17)

def mouvement():
    print("Ca bouge!")
    led.on()
    sleep(1)
    led.off()

#Mise en place de l'évènement de detection et appel de la methode.
senseur.when_motion = mouvement