"""
Created on Wed Dec  1 16:27:01 2021

@author: Guy Royburt
"""

import xml.etree.ElementTree as ET
import json
from distutils.dir_util import copy_tree
import shutil
import os
from os import path
import glob
from flask import Flask,render_template,request
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/FormFilled' , methods=['POST'])

def formFilled():
    
    # def for copying folders with tree
    def copytree2(source, dest):
        dest_dir = os.path.join(dest, os.path.basename(source))
        shutil.copytree(source, dest_dir)
        
    # Getting Data from the form
    DBInstance=request.form['insname']
    server=request.form['servname']
    serverport=request.form['port']
    clientname=request.form['client']
    mailservice=request.form['mail']
    diskdrive=request.form['disk']

    
    # Creating client new folder
    foldername=clientname+"configured"
    os.chdir("..")
    os.makedirs(foldername)
    os.makedirs(foldername+"\Project\Credit_Data\ "+clientname)
    copytree2("DS_MAJOR\API",foldername)
    copytree2("DS_MAJOR\dist", foldername)
    copytree2("QueryBuilder", foldername)
    copy_tree("Project\Credit_Data\Major",foldername+"\Project\Credit_Data\ "+clientname )
    
    
    # Parsing through CWayJobServicefile.exe.config and changing it
    xmlfile = foldername+"\Project\Credit_Data\ "+clientname+"\CWayJobService\CWayJobService.exe.config"
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for elm in root.findall(".//setting[@name='instance']/"):
        elm.text = DBInstance
    tree.write(xmlfile)
    print(os.getcwd)
    
    
    
    # Changing .bat files in client folder
    def ChagingBatFiles(FileName,FolderInClientPath):
        newfile=(foldername+"\Project\Credit_Data\ "+clientname+str(FolderInClientPath)+str(FileName))
        with open(newfile, "rt") as bat_file:
            text = bat_file.readlines()

        new_text = []
        for line in text:
            if "D:\Project\Credit_Data\Major" in line:
                value=diskdrive+":\Project\Credit_Data\ "+clientname
                value=value.replace(" ","")
                new_text.append(line.replace("D:\Project\Credit_Data\Major", value))
                
            elif("d:\Project\Credit_Data\Major" in line):
                value=diskdrive+":\Project\Credit_Data\ "+clientname
                value=value.replace(" ","")
                new_text.append(line.replace("d:\Project\Credit_Data\Major", value))
                
            elif("d:\Project\Credit_Data\Major\AutomationScripts\Maintenance_Plan.bat" in line):
                value=diskdrive+":\Project\Credit_Data\ "+clientname+"\AutomationScripts\Maintenance_Plan.bat"
                value=value.replace(" ","")
                new_text.append(line.replace("d:\Project\Credit_Data\Major\AutomationScripts\Maintenance_Plan.bat", value))
            elif("d:\Project\Credit_Data\Major\XMLFileGenerator\XMLGenerator\XMLFileGenerator.bat" in line):
                value=diskdrive+":\Project\Credit_Data\ "+clientname+"\XMLFileGenerator\XMLGenerator\XMLFileGenerator.bat"
                value=value.replace(" ","")
                new_text.append(line.replace("d:\Project\Credit_Data\Major\XMLFileGenerator\XMLGenerator\XMLFileGenerator.bat",value))
            elif("d:\Project\Credit_Data\Major\XMLForClient" in line):
                value=diskdrive+":\Project\Credit_Data\ "+clientname+"\XMLForClient"
                value=value.replace(" ","")
                new_text.append(line.replace("d:\Project\Credit_Data\Major\XMLForClient",value))
            elif("d:\Project\Credit_Data\Major\XMLFileGenerator\XMLGenerator" in line):
                value=diskdrive+":\Project\Credit_Data\ "+clientname+"\XMLFileGenerator\XMLGenerator"
                value=value.replace(" ","")
                new_text.append(line.replace("d:\Project\Credit_Data\Major\XMLFileGenerator\XMLGenerator",value))   
            elif("d:\Project\Credit_Data\Major\XMLForReload" in line):
                value=diskdrive+":\Project\Credit_Data\ "+clientname+"\XMLForReload"
                value=value.replace(" ","")
                new_text.append(line.replace("d:\Project\Credit_Data\Major\XMLForReload",value))    
            else:
                new_text.append(line)

        with open(newfile, "wt") as bat_file:
            for line in new_text:
                bat_file.write(line)
            
             
    ChagingBatFiles("\CIF_Update_Field.bat","\AutomationScripts")
    ChagingBatFiles("\CMF_Checkpoint_1.bat","\AutomationScripts")
    ChagingBatFiles("\Start_Maintenance.bat","\AutomationScripts")
    ChagingBatFiles("\Start_XML_File_Generator.bat","\AutomationScripts")
    ChagingBatFiles("\Start_XML_Loader.bat", "\AutomationScripts")
    ChagingBatFiles("\TFI_Checkpoint_1.bat", "\AutomationScripts")

    return "Done"
if __name__=="__main__":
    app.run(debug=True)










