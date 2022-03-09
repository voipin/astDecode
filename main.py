
import os

from requests.auth import HTTPBasicAuth

from xml.etree import ElementTree

from datetime import datetime

import requests

import logging




class Ast():

    def __init__(self,host,username,password):

        self.alert_list = []
        self.alert_dic = {}
        self.basic = HTTPBasicAuth(username, password)
        self.host = host
        self.response = {}
        self.tree = {}
        self.cache = {}



    def get_alert_summary(self):

        response = self.gen_response()

        self.tree = ElementTree.fromstring(response.content)

        for x in self.tree[0]:

            print(x.tag, x.attrib)
            self.alert_dic = x.attrib
            self.alert_list.append(self.alert_dic)

            for alert in self.alert_list:

                print(alert)


    def get_alert_summary_active(self):

        response = requests.get("https://"+self.host+"/ast/AstIsapi.dll?GetAlertSummaryList",verify=False, auth=self.basic)
        self.tree = ElementTree.fromstring(response.content)
        print(self.tree)

        for x in self.tree[0]:

            print(x.tag, x.attrib)
            self.alert_dic = x.attrib
            self.alert_list.append(self.alert_dic)


            for alert in self.alert_list:

                print(alert)


        print("Is Triggered:\n")

        for x in self.tree[0]:

            #print(x.tag, x.attrib)
            self.alert_dic = x.attrib
            self.alert_list.append(self.alert_dic)


        for alert in self.alert_list:

            #print(alert.get('DisplayName'))
            #print(alert.get('IsTriggered'))


            if int(alert.get('IsTriggered')) > 0 :

                ts = int(alert.get('TimeStamp'))/1000
                time_now = datetime.fromtimestamp(ts)



                print(alert.get('DisplayName'),time_now)

                time_now = datetime.fromtimestamp(ts)

    def gen_response(self):
        response = requests.get("https://"+self.host+"/ast/AstIsapi.dll?GetAlertSummaryList",verify=False, auth=self.basic)


if __name__ == '__main__':

    uc_sub1 = Ast("1.1.1.1","username", "password")
    uc_sub1.get_alert_summary()
    uc_sub1.get_alert_summary_active()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
