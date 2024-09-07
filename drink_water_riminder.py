from plyer import notification
import pygame
import time
n=int(input("Enter the time interval you want to be remined of for drinking water (in minutes):"))



def noti():
    notification_title = "Drink Water!"
    notification_message = f"Its been {n} minutes since you last drunk water!"
    notification_app_name = "NOTIFICATION"  # This will be displayed as the app name in the notification
    notification_timeout = 20  # The notification will disappear after 10 seconds

    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name=notification_app_name,
        timeout=notification_timeout

    
)
    




def play_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    

    for i in range(10):
       

    
        pygame.mixer.music.play()
        time.sleep(1)


time.sleep(n*60)
noti()
play_sound("beep-08b.wav")


