import tm1637

import time
import datetime

import RPi.GPIO as GPIO


def some_func():
    print 'in test 1, unproductive'

def clear_display():
       d0 = tm.digit_to_segment[0]
       d1 = tm.digit_to_segment[0]
       d2 = tm.digit_to_segment[0]
       d3 = tm.digit_to_segment[0]
       tm.set_segments([d0, d1, d2, d3])

def update_time():
       #time1 = datetime.datetime.now()
       #time.sleep(0.25)
       time2 = datetime.datetime.now()
       elapsed_time = (time2 - time1) * 1

       #elapsed_time = datetime.datetime.now() - start_time
       # secs = "{:1.0f}".format(time.time() - start_time)
       # print ("secs = " + secs)
       
       secs = elapsed_time.seconds
       m, s = divmod(secs, 60)
       h, m = divmod(m, 60)
       m1, m2 = divmod(m,10)
       s1,s2=divmod(s,10)

       d0 = tm.digit_to_segment[m1]
       d1 = tm.digit_to_segment[m2]
       d2 = tm.digit_to_segment[s1]
       d3 = tm.digit_to_segment[s2]
       tm.set_segments([d0, d1, d2, d3])
       #tm1637.show_time(tm,c)
       time.sleep(1)
       #tm1637.show_clock(tm)
       return secs

def update_signal_lights(secs):
      #print ("here set lights")
      elapsed_minutes = secs / 60
      #print("em = " + str(elapsed_minutes))
      if elapsed_minutes < 1:
          #print(" < 1")
          GPIO.output(4,GPIO.LOW) #p off
          GPIO.output(17,GPIO.HIGH) #class c flag on
      elif elapsed_minutes >= 1 and elapsed_minutes < 4:
          #print(">1 and < 4")
          GPIO.output(4,GPIO.HIGH) #p on
          GPIO.output(17,GPIO.HIGH) # class C on
      elif elapsed_minutes >= 4 and elapsed_minutes < 5:
          #print(">4 and < 5")
          GPIO.output(4,GPIO.LOW) # p off
          GPIO.output(17,GPIO.HIGH)
      elif elapsed_minutes >= 5 and elapsed_minutes < 6:
          #print("> 5 and < 6 mins")
          GPIO.output(4,GPIO.LOW) # p off
          GPIO.output(17,GPIO.LOW) # class c off
          GPIO.output(27,GPIO.HIGH) # class d on
      elif elapsed_minutes >= 6 and elapsed_minutes < 9:
          GPIO.output(4,GPIO.HIGH) # p on
          GPIO.output(27,GPIO.HIGH) # class d on
      elif elapsed_minutes >= 9 and elapsed_minutes < 10:
          GPIO.output(4,GPIO.LOW) # p off
          GPIO.output(27,GPIO.HIGH) # class d on
      elif elapsed_minutes >= 10 and elapsed_minutes < 11:
          GPIO.output(4,GPIO.LOW) # p off
          GPIO.output(27,GPIO.LOW) # class d off
          GPIO.output(22,GPIO.HIGH) # class e on
      elif elapsed_minutes >= 11 and elapsed_minutes < 14:
          GPIO.output(4,GPIO.HIGH) # p on
          GPIO.output(22,GPIO.HIGH) # class e on
      elif elapsed_minutes >= 14 and elapsed_minutes < 15:
          GPIO.output(4,GPIO.LOW) # p off
          GPIO.output(22,GPIO.HIGH) # class e on
      elif elapsed_minutes >= 15:
          GPIO.output(4,GPIO.LOW) # p off
          GPIO.output(22,GPIO.LOW) # class e off

def light_loop():
    secs = 0
    while secs/60 < 15:
       update_signal_lights(secs)
       secs = update_time()

#start_time = datetime.datetime.now()
time1 = datetime.datetime.now()
elapsed_time = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)   # p flag
GPIO.setup(17, GPIO.OUT)  # c flag
GPIO.setup(27, GPIO.OUT)  # d flag
GPIO.setup(22, GPIO.OUT)  # e flag
GPIO.setup(26, GPIO.IN)  # Start switch input
GPIO.output(4,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.output(22,GPIO.LOW)

    #                     BCM
    #leds(7,0); //p       4
    #leds(0,0); //c       17
    #leds(2,0); //d       27
    #leds(3,0); //e       22


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    # tm1637.got_here()
    tm = tm1637.TM1637(21, 20)
    start_time = time.time()
    print ("start time = ")
    #show_ip_address(tm)
    clear_display() 
 
    start_switch = 1
    while start_switch == 1:
       start_switch = GPIO.input(26)
       time.sleep(0.5)
       #print ("start = " + str(start_switch))

    light_loop()


