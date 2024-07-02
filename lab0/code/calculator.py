import socket
HOST = "10.214.160.13"  # IP address
PORT = 11002            # Port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create socket

s.connect((HOST, PORT))    # connect to this challenge

def recv_one_line(socket):
    buf = b""
    while True:
        data = socket.recv(1)
        if data == b'\n':
            return buf
        buf += data

def recv_one_question(socket):
    buf = b""
    while True:
        data = socket.recv(1)
        if data == b'=':
            return buf
        buf += data


recv_one_line(s)    # ================================================
recv_one_line(s)    # Mom: finish these 10 super simple calculations,
recv_one_line(s)    #       and you will get a flag
recv_one_line(s)    # Melody: that's easy...
recv_one_line(s)    # Mom: yep, in 10 seconds
recv_one_line(s)    # ================================================   #
for i in range(10):
    print(recv_one_line(s)) 
    s.send(b"%d\n"%(eval(recv_one_question(s))))
    recv_one_line(s) #        
    print(recv_one_line(s))
recv_one_line(s)
print(recv_one_line(s))
s.close()