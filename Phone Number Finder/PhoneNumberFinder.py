import re,os

phone_num=r"(\d{3})-(\d{3})-(\d{4})"
path='C:\\Users\\Nameless\\Documents\\ProgrammingSideProjects\\Jupyter Course Notes\\instructions\\extracted_content'

for folder,subfolder,file in os.walk(path):
    for f in file:
        fil=open(folder+'\\'+f,'r')
        file_text=fil.read()
        match=re.findall(phone_num,file_text)
        if match!=[]:
            print(f'{folder}{f}')
            print(match)
        fil.close()