import os
import shutil

file_dir=os.path.dirname(os.path.realpath(__file__)) ## Knowing where we stand now ... the file path





#--------> Arrange image into image folder  <-------- 

for namefile in os.listdir(file_dir): 
    if namefile.endswith((".png",".jpg")):
        if not os.path.exists("Image"): # If the image file does not exist, create a file and call it image
            os.mkdir('Image')
        shutil.copy(namefile,"Image") # Copies files and places them in an image file
        os.remove(namefile) 
        print("succeeded image")


#--------> Arrange Coding files into Coding folder  <-------- 

for namefile in os.listdir(file_dir): 
    if namefile.endswith(("cc","html","js","py")):
        if not os.path.exists("Coding"): # If the image file does not exist, create a file and call it image
            os.mkdir('Coding')
        shutil.copy(namefile,"Coding") # Copies files and places them in an image file
        os.remove(namefile) 
        print("succeeded coding")



#--------> Arrange video files into videos folder  <-------- 

for namefile in os.listdir(file_dir): 
    if namefile.endswith(("mp4","mp3")):
        if not os.path.exists("videos"): # If the image file does not exist, create a file and call it image
            os.mkdir('videos')
        shutil.copy(namefile,"videos") # Copies files and places them in an image file
        os.remove(namefile) 
        print("succeeded video ")


#--------> Arrange Docs files into Documentes folder  <-------- 

for namefile in os.listdir(file_dir): 
    if namefile.endswith(("pdf","docx","pptx")):
        if not os.path.exists("Documentes"): # If the image file does not exist, create a file and call it image
            os.mkdir('Documentes')
        shutil.copy(namefile,"Documentes") # Copies files and places them in an image file
        os.remove(namefile) 
        print("succeeded Documentes")

#--------> Arrange Apps files into App folder  <-------- 

for namefile in os.listdir(file_dir): 
    if namefile.endswith(("exe")):
        if not os.path.exists("Apps"): # If the image file does not exist, create a file and call it image
            os.mkdir('Apps')
        shutil.copy(namefile,"Apps") # Copies files and places them in an image file
        os.remove(namefile) 
        print("succeeded Apps")


#--------> Arrange archive files into Archives folder  <-------- 

for namefile in os.listdir(file_dir): 
    if namefile.endswith(("zip","rar")):
        if not os.path.exists("Archives"): # If the image file does not exist, create a file and call it image
            os.mkdir('Archives')
        shutil.copy(namefile,"Archives") # Copies files and places them in an image file
        os.remove(namefile) 
        print("succeeded Archives")

