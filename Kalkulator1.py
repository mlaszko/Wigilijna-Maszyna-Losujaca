#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import getpass
import random
import csv


def sendMail(toaddrs, name, name2, password):
    fromaddr ="mlaszkow@gmail.com"
    msg = "\r\n".join([
      "From: mlaszkow@gmail.com",
      "To: "+ toaddrs,
      "Subject: Wigilia",
      "",
      "Hoł hoł hoł "+ name + "!\nW mikołajkowej zabawie wylosowałeś " + name2 +
      "! Kup tej osobie wspaniały prezent za 20zł!\n\nZ poważaniem,\nKomisja Konstroli Gier i Zakładów"
      ])
    username = 'mlaszkow'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


users = []
with open('people.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        users.append(row)

users2 = list(users)
badLottery = True
while badLottery:
    random.shuffle(users2)
    badLottery = False
    for i in range(len(users)):
        if users[i] == users2[i]:
            badLottery = True
            break
        for j in range(2, len(users[i])):
            if users[i][j] == users2[i][0]:
                badLottery = True
                break

password = getpass.getpass()

for i in range(len(users)):
    sendMail(users[i][1], users[i][0], users2[i][0], password)
