import pyb
import utime
import struct

I2C_obj = pyb.I2C(1,pyb.I2C.CONTROLLER,baudrate=100000)

# scan I2C bus to make sure 1 device talking
scan1 = I2C_obj.scan() # Check for devices on bus, output is I2C Device Address

# got rid of quotes b/c that makes string, we want to send just bin number
# 1100b (b on end shouldnt be there, data sheet isnt in python, they think b at end is how to say bin number)
# if hex put 0x in front of it
# if bin put 0b in front of it
I2C_obj.mem_write(0b1100,scan1[0],0x3D) # 0x3D is the register, 1100b is NDOF mode

while True:
    utime.sleep (1)  # Sleep for 1 sec
    try:
        # pull all 
        Euler = I2C_obj.mem_read(6,scan1[0],0x1A)
        
        # unpack
        X,Y,Z = struct.unpack('<hhh',Euler)
        
        # print in degrees
        print('Euler (X,Y,Z) =',X/16,Y/16,Z/16)
    
    except KeyboardInterrupt:
        break
        

