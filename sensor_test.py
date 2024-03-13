import RPi.GPIO as GPIO
import time

# Define the GPIO pin number the sensor is connected to
sensor_pin = 17  

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Sensor pin set as input, with pull-down resistor

try:
    print("Monitoring sensor, press CTRL+C to exit")
    while True:
        if GPIO.input(sensor_pin):
            print("Object detected!")
        else:
            print("No object detected.")
        time.sleep(1)  # Check the sensor every 1 second

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    GPIO.cleanup()  # Clean up GPIO state