import configparser

import os

def readConfigData(section, key):
    config = configparser.ConfigParser()
    path = "D:\\AutomationTestWeb\\configFiles\\config.cfg"
    config.read(path)
    return config.get(section, key)

def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    path = "D:\\AutomationTestWeb\\configFiles\\Elements.cfg"
    config.read(path)
    return config.get(section, key)