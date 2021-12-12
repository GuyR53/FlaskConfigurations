"""
Created on Wed Dec  1 16:27:01 2021

@author: Guy Royburt
"""

import xml.etree.ElementTree as ET
import json
from distutils.dir_util import copy_tree
import shutil
import os
import glob
from flask import Flask,render_template,request
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/FormFilled' , methods=['POST'])
def formFilled():
    def copytree2(source, dest):
        dest_dir = os.path.join(dest, os.path.basename(source))
        shutil.copytree(source, dest_dir)

    DBInstance=request.form['insname']
    server=request.form['servname']
    serverport=request.form['port']
    clientname=request.form['client']
    mailservice=request.form['mail']
    diskdrive=request.form['disk']
    foldername=clientname+"configured"
    os.chdir("..")
    os.makedirs(foldername)
    os.makedirs(foldername+"\Project\Credit_Data\ "+clientname)
    copytree2("DS_MAJOR\API",foldername)
    copytree2("DS_MAJOR\dist", foldername)
    copytree2("QueryBuilder", foldername)
    copy_tree("Project\Credit_Data\Major",foldername+"\Project\Credit_Data\ "+clientname )
    xmlfile = foldername+"\Project\Credit_Data\ "+clientname+"\CWayJobService\CWayJobService.exe.config"
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for elm in root.findall(".//setting[@name='instance']/"):
        elm.text = DBInstance
    tree.write(xmlfile)
    xmlfile1 = r"QueryBuilder\appsettings.json"
    return "Done"
if __name__=="__main__":
    app.run(debug=True)










