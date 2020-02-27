import socket
HOST = '0.0.0.0'              # Endereco IP do Servidor
PORT = 4533                   # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    conn, cliente = tcp.accept()
    print ("Conectado por"), cliente
    while True:
        data = conn.recv(1024)
        if(len(data) == 0):
          print("close socket")
          conn.close()
          break
        data = data.strip()
        #print("set_pos: " +data)
        print(data)
        #ret = conn.send("set_pos: " +data)
        bla = data.strip()
        ret = conn.send(data)
        #ret = conn.send(bla)
    print ("Finalizando conexao do cliente"), cliente
    conn.close()
