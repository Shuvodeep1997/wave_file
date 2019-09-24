import struct
f=open("1.wav","rb")
s=f.read(4)
size=struct.unpack('I',s)
print(size)
