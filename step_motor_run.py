from time import sleep
import RPi.GPIO as GPIO

# Define GPIO pin numbers
direction_pin = 20  # Connect to DIR pin on CL57T
pulse_pin = 21  # Connect to PUL pin on CL57T
sensor_pin = 17  # Example sensor pin, if used for triggering movement
dir_selection = 1  # 0 for clockwise, 1 for counter-clockwise

# Motor and microstepping configuration
steps_per_revolution = 200  #Set with SW1,Sw2,SW3,SW4 dip switches according to pulse/rev table
rpm = 120  # Desired RPM

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(direction_pin, GPIO.OUT)
GPIO.setup(pulse_pin, GPIO.OUT)
GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def move_motor(direction, steps, rpm):
    global steps_per_revolution
    delay = 60 / (steps_per_revolution * rpm)  # Calculate delay in seconds

    print('Direction:', 'Clockwise' if direction == 0 else 'Counter-Clockwise')
    GPIO.output(direction_pin, direction)
    for _ in range(steps):
        GPIO.output(pulse_pin, GPIO.HIGH)
        sleep(delay / 2)  # Pulse "high" time
        GPIO.output(pulse_pin, GPIO.LOW)
        sleep(delay / 2)  # Pulse "low" time

try:
    while True:
        # Example condition: move the motor when the sensor is triggered
        if GPIO.input(sensor_pin) == GPIO.LOW:  # Assuming LOW signal from sensor triggers movement
            move_motor(dir_selection, steps_per_revolution, rpm)  # Move one revolution based on RPM
            sleep(1)  # Wait for 1 second before next action

except KeyboardInterrupt:
    print("\nScript interrupted by user. Cleaning up...")
    GPIO.cleanup()  # Reset GPIO resources