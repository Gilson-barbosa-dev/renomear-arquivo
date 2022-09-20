from hashlib import new
import random
import os

#============ Renomear fotos ===============

pasta = r"imagens"
os.chdir(pasta)

for f in os.listdir():
    #======== Formula para renomear ============

    foto = 'IMG'
    ano = random.randint(2015,2022)
    mes = ['01','02','03','04','05','06','07','08','09','10','11','12']
    mes1 = random.choice(mes)
    dia = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
    dia1 = random.choice(dia)
    nome = random.randint(123456,999999)

    #======== Formula para renomear ============
    
    f_name, f_ext = os.path.splitext(f)

    f_nome = f_name.split()
    f_nome = f_name.strip()
    
    try:
        new_name = (f"{foto}-{ano}{mes1}{dia1}-{nome}{f_ext}")
        #
        os.rename(f, new_name)
        
    except Exception as e:
        print('Não concluiu')

print('Renomeado')

#============ Renomear fotos ===============