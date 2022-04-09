import random
import sys
import time
import http
import socket
import socketserver
import http.server
from mysql.connector import connect, Error
import hashlib
import qrcode
import time
import random
import requests
import io
from PIL import Image
import numpy as np

def h256(a):
    b = bytes(a, 'utf-8')
    c = hashlib.sha256(b).hexdigest()
    return c
def h512(a):
    b = bytes(a, 'utf-8')
    c = hashlib.sha512(b).hexdigest()
    return c
def md5(a):
    b = bytes(a, 'utf-8')
    c = hashlib.md5(b).hexdigest()
    return c
def r(a, b):
    n = random.randint(a, b)
    return n
def rmd5():
    text = rh()
    a = md5(text)
    return a
def rh():
    a = r(0, 1000)
    b = r(0, 1000)
    c = r(0, 1000)
    d = r(0, 1000)
    e = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
    f = h256(e)
    return f
def itb(pa):
    try:
        with open(pa, "rb") as image:
            f = image.read()
            b = bytearray(f)
        a = "".join(str(b))
        b = h256(a)
        return b
    except:
        return False
def cnft(iname,token,author,pinc):
    try:
        with connect(
                host="localhost",
                user="root",
                password="93029302",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("USE nftd")

                cursor.execute("SELECT token FROM nf WHERE token='" + token + "'")
                row = cursor.fetchone()
                if row == None:
                    cursor.execute(
                        "INSERT INTO nf(iname,token,author,pinc) VALUES('" + iname + "','" + token + "','" + author + "','" + str(
                            pinc) + "')")
                    connection.commit()
                    print("")
                    return True
                else:
                    print("Token is already created!")
    except Error as e:
        print(e)


def getaddressfromid(a):
    try:
        with connect(
                host="localhost",
                user="root",
                password="93029302",
        ) as connection:
            if connection.is_connected():
                print("Connected to database")
            time.sleep(1)
            with connection.cursor() as cursor:
                cursor.execute("USE gfpdb")
                cursor.execute("SELECT address FROM tt WHERE id='" + str(a) + "'")
                row = cursor.fetchone()
                if row == None:
                    return None
                else:
                    print(row)
                    return row
    except Error as e:
        print(e)
