def server():
    try:
        while True:
            msg = yield
            print "[ server ]: {}".format(msg)
            yield "echo '{}'".format(msg)
    except GeneratorExit:
        print "Server Connection Closed"

def client():
    serv = server()
    while True:
        serv.next()
        msg = raw_input("chat$: ")
        if msg == "EXIT":
            serv.close()
        response = serv.send(msg)
        print "[ client ]: {}".format(response)

if __name__ == '__main__':
    try:
        client()
    except StopIteration:
        pass
    
