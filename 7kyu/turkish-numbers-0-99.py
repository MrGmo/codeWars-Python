def get_turkish_number(num):
    dic1={0:'sıfır',1:'bir',2:'iki',3:'üç',4:'dört',5:'beş',6:'altı',7:'yedi',8:'sekiz',9:'dokuz'}
    dic2={10:'on',20:'yirmi',30:'otuz',40:'kırk',50:'elli',60:'altmış',70:'yetmiş',80:'seksen',90:'doksan'}
    n=str(num)
    if len(n)==1:
        return dic1[int(n)]
    elif len(n)==2:
        a=int(n[1])
        b=int(n[0]+'0')
        if a==0: 
            return dic2[b]
        else:
            return dic2[b]+' '+dic1[a]