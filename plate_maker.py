import os 
import csv

file_path = ''
file_list = os.listdir()

try : 
    if not os.path.exists('trash_image') :
        os.makedirs('trash_image')

    if not os.path.exists('plate_image') :
        os.makedirs('plate_image')
except OSError: 
    print('Error : Creating directory.')


for i in file_list :
    file_name = i
    # print(file_name[-3:])

    if(file_name[-3:]=='jpg'):

        if(file_name[-5:-4]=='3') :

            src = file_name
            des = 'plate_image/'+file_name
            os.replace(src,des)
            
        else : 
            src = file_name
            des = 'trash_image/'+file_name
            os.replace(src,des)
    if(file_name[-3:]=='csv'):
        csv_name = file_name
        dict_from_csv = {}
        with open(csv_name, mode='r') as inp:
            reader = csv.reader(inp)
            dict_from_csv = {rows[0]:rows[2] for rows in reader}




plate_file_path = 'plate_image'
plate_file_list = os.listdir('plate_image/')




for j in plate_file_list : 
    # print(j)
    key = j.replace("3.jpg","")
    # print(key)
    

    if key in dict_from_csv :
        print(dict_from_csv[key])
        file_oldname = os.path.join("plate_image/", j)
        file_newname_newfile = os.path.join("plate_image/", dict_from_csv[key]+".jpg")
        
        try : 
            os.rename(file_oldname, file_newname_newfile)
        except : 
            print("동일 번호판 존재 ")
            cnt=0
            
            for cnt in range(1,100):
                if(os.path.exists("plate_image/"+dict_from_csv[key]+"_"+str(cnt)+".jpg")):
                    cnt=cnt+1
                else :
                    break

            file_newname_newfile = os.path.join("plate_image/", dict_from_csv[key]+"_"+str(cnt)+".jpg")
            cnt=cnt+1
            os.rename(file_oldname, file_newname_newfile)

    else : 
        print('없어!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    
    



        
        

    





