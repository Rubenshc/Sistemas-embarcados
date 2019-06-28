import Adafruit_BBIO.GPIO as GPIO #Importing Adafruit-BeagleBone-IO-Python GPIO
import Adafruit_BBIO.PWM as PWM #Importing Adafruit-BeagleBone-IO-Python PWM
import time

#GPIOs, PWM and LED name assign according to BBB naming on Adafruit
led1 = "P8_7"
led2 = "P8_9"
led3 = "P8_11"
motor_p = "P8_8"
motor_n = "P8_10"
BUTTON1 = "P9_30"
BUTTON2 = "P9_27"
pwm_motor = "P9_16"
###

#Assigning GPIOs type as  INPUT or OUTPUT
GPIO.setup(motor_p,GPIO.OUT)
GPIO.setup(motor_n,GPIO.OUT)
GPIO.output(motor_p, GPIO.LOW)
GPIO.output(motor_n, GPIO.LOW)

GPIO.setup(BUTTON1,GPIO.IN)
GPIO.setup(BUTTON2,GPIO.IN)

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
###


### Loop for program
while True: 
    
    ### PWM initial parameters for 30 RPM motor base speed
    PWM.start(pwm_motor,35,100)

    ### LEDs initial setup for state 1 as default
    GPIO.output(led1, GPIO.HIGH)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)

    loop = 1
    ### 3 possible states
	state = 1
	print('Selecione o programa desejado:')
    
	### Loop for program/state selection. Each led represent selected current state.
	while loop == 1:
        Button1_State = GPIO.input (BUTTON1)
        if Button1_State == 1:
            time.sleep(0.5)
            if state == 1:
                state = 2
				### Turn LED 2 to indicate second program
                GPIO.output(led2, GPIO.HIGH)
            elif state == 2:
                state = 3
				### Turn LED 3 to indicate third program
                GPIO.output(led3, GPIO.HIGH)
            else:
                state = 1
				### Keep only led 1 on to indicate first program
                GPIO.output(led2, GPIO.LOW)
                GPIO.output(led3, GPIO.LOW)
        
		Button2_State = GPIO.input (BUTTON2)
        ###  Confirming the program/state selection
	if Button2_State == 1:
            print('selecao confirmada')
            time.sleep(0.5)
            loop = 0
        
    loop = 1
    
    ### Running the programs
    while loop == 1:
        if state == 1:
            print('programa 1')
            time.sleep(2)

            ### PWM parameters for 30 RPM motor base speed
            PWM.start(pwm_motor,35,100)
            
            GPIO.output(motor_p, GPIO.HIGH)
            GPIO.output(motor_n, GPIO.LOW)
			
	    ### Program running time of 240 seconds on lower speed
            for inc in range(0,240*2):
                Button2_State = GPIO.input (BUTTON2)
                if Button2_State == 1:
                    time.sleep(0.5)
                    GPIO.output(motor_p, GPIO.LOW)
                    GPIO.output(motor_n, GPIO.LOW)
                    break
                time.sleep(0.5)
            
            
            print('FIM programa 1')
            
        elif state == 2:
            print('programa 2')
            time.sleep(2)
            
            ###PWM  parameters for 45 RPM motor base speed
            PWM.start(pwm_motor,50,100)
            
            GPIO.output(motor_p, GPIO.HIGH)
            GPIO.output(motor_n, GPIO.LOW)
			
			### Program running time of 300 seconds on medium speem
            for inc in range(0,300*2):
                Button2_State = GPIO.input (BUTTON2)
                if Button2_State == 1:
                    time.sleep(0.5)
                    GPIO.output(motor_p, GPIO.LOW)
                    GPIO.output(motor_n, GPIO.LOW)
                    break
                time.sleep(0.5)
            
            
            
            print('FIM programa 2')
        else:
            print('programa 3')
            time.sleep(2)
            
            ###PWM initial parameters for 60 RPM motor base speed
            PWM.start(pwm_motor,80,100)
            
            GPIO.output(motor_p, GPIO.HIGH)
            GPIO.output(motor_n, GPIO.LOW)
    
	    ### Program running time of 240 seconds on higher speed
            for inc in range(0,240*2):
                Button2_State = GPIO.input (BUTTON2)
                if Button2_State == 1:
                    time.sleep(0.5)
                    GPIO.output(motor_p, GPIO.LOW)
                    GPIO.output(motor_n, GPIO.LOW)
                    break
                time.sleep(0.5)
            
            
            
            
            print('FIM programa 3')
            
        GPIO.output(motor_p, GPIO.LOW)
        GPIO.output(motor_n, GPIO.LOW)
        loop = 0
	### END
    
    
