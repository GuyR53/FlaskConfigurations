"""
Created on Wed Dec  1 16:27:01 2021

@author: Guy Royburt
"""

import xml.etree.ElementTree as ET
import json
import configparser
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
    
    
     # Changing DCPRunEngine.exe.config
    filepath=foldername+"\Project\Credit_Data\ "+clientname+"\DCPRunEngine\DCPRunEngine.exe.config"
    with open(filepath, 'r') as f:
        res = f.read().replace('HMS-SQL2\major', (DBInstance+"\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.34\major', (server+"\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
        
    
     # Changing XMLAgent.exe.config 
    filepath=foldername+"\Project\Credit_Data\ "+clientname+"\XMLLoader\CIFLoader\XMLAgent.exe.config"
    with open(filepath, 'r') as f:
        res = f.read().replace('HMS-SQL2\major', (DBInstance+"\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.33\d$\Project\Credit_Data\major', (server+"\ "+diskdrive+"$\Project\Credit_Data\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
        
        
     # Changing XMLCMFLoader.exe.config 
    filepath=foldername+"\Project\Credit_Data\ "+clientname+"\XMLLoader\CMFLoader\XMLCMFLoader.exe.config"
    with open(filepath, 'r') as f:
        res = f.read().replace('hms-sql2\major', (DBInstance+"\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.33\d$\Project\Credit_Data\Major', (server+"\ "+diskdrive+"$\Project\Credit_Data\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
        
        
        
    # Changing config.bat
    filepath=foldername+"\Project\Credit_Data\ "+clientname+"\config.bat"
    with open(filepath, 'r') as f:
        res = f.read().replace('HMS-SQL2\major', (DBInstance+"\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.33\d$\Project\Credit_Data\major', (server+"\ "+diskdrive+"$\Project\Credit_Data\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.33\d$\Project\Credit_Data\Major', (server+"\ "+diskdrive+"$\Project\Credit_Data\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.27', (mailservice).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.33:8081', (mailservice+":"+serverport).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    
        
        
      # Changing XMLIMFLoader.exe.config 
    filepath=foldername+"\Project\Credit_Data\ "+clientname+"\XMLLoader\IMFLoader\XMLIMFLoader.exe.config"
    with open(filepath, 'r') as f:
        res = f.read().replace('HMS-SQL2\major', (DBInstance+"\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.33\d$\Project\Credit_Data\major', (server+"\ "+diskdrive+"$\Project\Credit_Data\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    
    
    
    
        
    # Changing RasModuleEngine.exe.config 
    filepath=foldername+"\Project\Credit_Data\ "+clientname+"\RasModuleEngine\RasModuleEngine.exe.config"
    with open(filepath, 'r') as f:
        res = f.read().replace('192.168.1.33', (server))
    with open(filepath,'w') as f:
        f.write(res)
        
        
    # Changing XMLCMF_FileGenerator.exe.config 
    filepath=foldername+"\Project\Credit_Data\ "+clientname+"\XMLFileGenerator\XMLCMFGenerator\XMLCMF_FileGenerator.exe.config"
    with open(filepath, 'r') as f:
        res = f.read().replace('hms-sql2\major',(DBInstance+"\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
        
        
    # Changing XMLFileGenerator.exe.config
    filepath=foldername+"\Project\Credit_Data\ "+clientname+"\XMLFileGenerator\XMLGenerator\XMLFileGenerator.exe.config"
    with open(filepath, 'r') as f:
        res = f.read().replace('HMS-SQL2\major',(DBInstance+"\ "+clientname).replace(" ",""))
    with open(filepath,'w') as f:
        f.write(res)
    
     # Parsing through CWayEmailService.exe.config and changing it
    xmlfile = foldername+"\Project\Credit_Data\ "+clientname+"\CwayEmailService\CWayEmailService.exe.config"
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for elm in root.findall(".//setting[@name='instance']/"):
        elm.text = DBInstance
    tree.write(xmlfile)
    
     # Parsing through CwayJobService_Version_4.6.5\CWayEmailService.exe.config and changing it
    xmlfile = foldername+"\Project\Credit_Data\ "+clientname+"\CwayJobService_Version_4.6.5\CWayJobService.exe.config"
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for elm in root.findall(".//setting[@name='instance']/"):
        elm.text = DBInstance
    for elm in root.findall(".//setting[@name='RasModule']/"):
        elm.text="\\"+server+"\c$\Program Files\HMS\RAS_API\RAS_API.exe"
    for elm in root.findall(".//setting[@name='SMTPModule']/"):
        val=("\\"+server+"\ "+diskdrive+"\Project\Credit_Data\ "+clientname+"\ reportMailSendEngine\ reportMailSendEngine.exe").replace(" ","")
        elm.text=val
    tree.write(xmlfile)
    
    
    
    
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
            elif("D:\Project\Credit_Data\major" in line):
                value=diskdrive+":\Project\Credit_Data\ "+clientname
                value=value.replace(" ","")
                new_text.append(line.replace("D:\Project\Credit_Data\major", value))  
            elif("d:\Project\Credit_Data\major" in line):
                value=diskdrive+":\Project\Credit_Data\ "+clientname
                value=value.replace(" ","")
                new_text.append(line.replace("d:\Project\Credit_Data\major", value))  
            elif("192.168.1.33\d$\Project\Credit_Data\Major" in line):
                value=server+"\ "+diskdrive+":\Project\Credit_Data\ "+clientname
                value=value.replace(" ","")
                new_text.append(line.replace("192.168.1.33\d$\Project\Credit_Data\Major", value)) 
            
            
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
    for filename in os.listdir(foldername+"\Project\Credit_Data\ "+clientname+"\AutomationScriptsManually"):
         filename="\ "+filename
         l=list(filename)
         l[1]=""
         filename="".join(l)
         ChagingBatFiles(filename, "\AutomationScriptsManually")
    ChagingBatFiles("\Start_CIF_Update_Field - Yahav.bat", "\AutomationScriptsManually")
    ChagingBatFiles("\Start_CIF_Update_Field.bat", "\AutomationScriptsManually")
    ChagingBatFiles("\Start_CIF_Update_Field_isracard.bat", "\AutomationScriptsManually")
    
    

   
    
    

    return "Done"
if __name__=="__main__":
    app.run(debug=True)










