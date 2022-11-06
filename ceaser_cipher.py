print("Welcome to ceaser cipher ;) ")
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

synum=["!","@",'#','$','%','^','&','*',';','+','-','_','=','|','?','>','<',"1","2",'3','4','5','6','7','8','9',"!","@",'#','$','%','^','&','*',';','+','-','_','=','|','?','>','<',"1","2",'3','4','5','6','7','8','9']

def ceaser(start_text,shift_number,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_number *= -1
    for char in start_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position = position+shift_number
            end_text+=alphabets[new_position]
        elif char in synum:
            position=synum.index(char)
            new_position = position+shift_number
            end_text+=synum[new_position]
        else:
            end_text+=char
            
    print(f"Hear's the {direct}d result :{end_text}")

should_continue=True
while should_continue==True:
    direct=input("Type'encode' to encrypt , type 'decode' to decrypt :\n").lower()
    text=input("Type your message :\n").lower()
    shift=int(input("Type the shifting number :\n"))
    shift=shift%26

    ceaser(start_text=text,shift_number=shift,cipher_direction=direct)

    decission=input("type 'yes' to continue and 'no' to exit :\n").lower()
    if decission=="yes":
        should_continue=True
    else:
        print("bye bye :( ")
        should_continue=False