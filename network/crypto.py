from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
import socket
from basic import recvall

def handshake_client(sock: socket.socket):
    key = RSA.generate(2048)
    pub_key = key.publickey()

    sock.sendall(pub_key.export_key())

    enc_session_key = sock.recv(key.size_in_bytes())
    nonce = sock.recv(16)

    cipher_rsa = PKCS1_OAEP.new(key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    session = (session_key, nonce)
    return session

def handshake_server(conn: socket.socket):
    recipient_key = RSA.import_key(recvall(conn))
    session_key = get_random_bytes(32)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_GCM)
    nonce = cipher_aes.nonce
    conn.sendall(enc_session_key + nonce)
    return (session_key, nonce)


def srecvall(sock: socket.socket, session, BUFF_SIZE=2048):
    tag = sock.recv(16)
    ciphertext = recvall(sock, BUFF_SIZE=BUFF_SIZE)
    cipher = AES.new(session[0], AES.MODE_GCM, nonce=session[1])
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext, True

    except ValueError:
        return plaintext, False

def srecv(sock: socket.socket, session, buffer):
    tag = sock.recv(16)
    ciphertext = sock.recv(buffer)
    cipher = AES.new(session[0], AES.MODE_GCM, nonce=session[1])
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext, True

    except ValueError:
        return plaintext, False

def ssend(sock: socket.socket, session, data: bytes):
    cipher = AES.new(session[0], AES.MODE_GCM, nonce=session[1])
    ciphertext, tag = cipher.encrypt_and_digest(data)
    sock.sendall(tag + ciphertext)
