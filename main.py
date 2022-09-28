alfavit='абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print('Введите 1, если хотите зашифровать текст и 2, если расшифровать')
otvet=int(input())

if otvet==1:
    print('Напишите текст (на русском языке), который нужно зашифровать')
    text=input()
    print('Сдвиг шифровки')
    sdvig=int(input())

    text_z=text.lower() 
    text_new='' 

    for ic in text_z:
        position=alfavit.find(ic)
        new_position=position+sdvig
        if ic in alfavit:
            text_new=text_new + alfavit[new_position]
        else:
            text_new=text_new+ic
    print ('Зашифрованный текст:', text_new)

if otvet==2:
    print('Напишите текст (на русском языке), который нужно расшифровать')
    text=input()
    print('Сдвиг шифровки')
    sdvig=int(input())

    text_z=text.lower() 
    text_new='' 

    for ic in text_z:
        position=alfavit.find(ic)
        new_position=position-sdvig
        if ic in alfavit:
            text_new=text_new + alfavit[new_position]
        else:
            text_new=text_new+ic
    print ('Расшифрованный текст:', text_new)    
            
