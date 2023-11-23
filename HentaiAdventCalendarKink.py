import os, datetime, base64

RED = '\033[31m'
GREEN = '\033[32m'
GOLD = '\033[1m\033[38;5;214m'
CRIMSON = '\033[38;5;196m'
RESET = '\033[0m'
BOLD = '\033[1m'
BLINK = '\033[5m'

def encrypt():
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".png") or filename.endswith(".mp4"):
            with open(filename, "rb") as file:
                data = file.read()
                data = base64.b64encode(data)
                with open(filename + ".enc", "wb") as file2:
                    file2.write(data)

def decrypt(filename):
    with open(filename, "rb") as file:
        data = file.read()
        data = base64.b64decode(data)
        with open(filename[:-4], "wb") as file2:
            file2.write(data)

def main():
    today = datetime.datetime.now()
    month = today.month
    day = today.day

    tiles = {
        1:f"{GREEN}[{RESET}{GOLD} 1{RESET}{GREEN}]{RESET}",2:f"{GREEN}[{RESET}{GOLD} 2{RESET}{GREEN}]{RESET}",3:f"{GREEN}[{RESET}{GOLD} 3{RESET}{GREEN}]{RESET}",4:f"{GREEN}[{RESET}{GOLD} 4{RESET}{GREEN}]{RESET}",5:f"{GREEN}[{RESET}{GOLD} 5{RESET}{GREEN}]{RESET}",
        6:f"{GREEN}[{RESET}{GOLD} 6{RESET}{GREEN}]{RESET}",7:f"{GREEN}[{RESET}{GOLD} 7{RESET}{GREEN}]{RESET}",8:f"{GREEN}[{RESET}{GOLD} 8{RESET}{GREEN}]{RESET}",9:f"{GREEN}[{RESET}{GOLD} 9{RESET}{GREEN}]{RESET}",10:f"{GREEN}[{RESET}{GOLD}10{RESET}{GREEN}]{RESET}",
        11:f"{GREEN}[{RESET}{GOLD}11{RESET}{GREEN}]{RESET}",12:f"{GREEN}[{RESET}{GOLD}12{RESET}{GREEN}]{RESET}",13:f"{GREEN}[{RESET}{GOLD}13{RESET}{GREEN}]{RESET}",14:f"{GREEN}[{RESET}{GOLD}14{RESET}{GREEN}]{RESET}",15:f"{GREEN}[{RESET}{GOLD}15{RESET}{GREEN}]{RESET}",
        16:f"{GREEN}[{RESET}{GOLD}16{RESET}{GREEN}]{RESET}",17:f"{GREEN}[{RESET}{GOLD}17{RESET}{GREEN}]{RESET}",18:f"{GREEN}[{RESET}{GOLD}18{RESET}{GREEN}]{RESET}",19:f"{GREEN}[{RESET}{GOLD}19{RESET}{GREEN}]{RESET}",20:f"{GREEN}[{RESET}{GOLD}20{RESET}{GREEN}]{RESET}",
        21:f"{GREEN}[{RESET}{GOLD}21{RESET}{GREEN}]{RESET}",22:f"{GREEN}[{RESET}{GOLD}22{RESET}{GREEN}]{RESET}",23:f"{GREEN}[{RESET}{GOLD}23{RESET}{GREEN}]{RESET}",24:f"{GREEN}[{RESET}{GOLD}24{RESET}{GREEN}]{RESET}",25:f"{GREEN}[{RESET}{GOLD}25{RESET}{GREEN}]{RESET}",
    }

    for i in range(day):
        tiles[i+1] = f"{GREEN}[{RESET}{GOLD}  {RESET}{GREEN}]{RESET}"

    board = [
        f"{CRIMSON}╔══{GOLD}[{RESET}{GREEN}Hentai Calendar{RESET}{GOLD}]{RESET}{CRIMSON}═════╗{RESET}",
        f"{CRIMSON}╠════╦════╦════╦════╦════╣{RESET}",
        f"{CRIMSON}║{tiles[1]}{CRIMSON}║{RESET}{tiles[2]}{CRIMSON}║{RESET}{tiles[3]}{CRIMSON}║{RESET}{tiles[4]}{CRIMSON}║{RESET}{tiles[5]}{CRIMSON}║{RESET}{RESET}",
        f"{CRIMSON}╠════╬════╬════╬════╬════╣{RESET}",
        f"{CRIMSON}║{tiles[6]}{CRIMSON}║{RESET}{tiles[7]}{CRIMSON}║{RESET}{tiles[8]}{CRIMSON}║{RESET}{tiles[9]}{CRIMSON}║{RESET}{tiles[10]}{CRIMSON}║{RESET}",        
        f"{CRIMSON}╠════╬════╬════╬════╬════╣{RESET}",
        f"{CRIMSON}║{tiles[11]}{CRIMSON}║{RESET}{tiles[12]}{CRIMSON}║{RESET}{tiles[13]}{CRIMSON}║{RESET}{tiles[14]}{CRIMSON}║{RESET}{tiles[15]}{CRIMSON}║{RESET}",        
        f"{CRIMSON}╠════╬════╬════╬════╬════╣{RESET}",
        f"{CRIMSON}║{tiles[16]}{CRIMSON}║{RESET}{tiles[17]}{CRIMSON}║{RESET}{tiles[18]}{CRIMSON}║{RESET}{tiles[19]}{CRIMSON}║{RESET}{tiles[20]}{CRIMSON}║{RESET}",        
        f"{CRIMSON}╠════╬════╬════╬════╬════╣{RESET}",
        f"{CRIMSON}║{tiles[21]}{CRIMSON}║{RESET}{tiles[22]}{CRIMSON}║{RESET}{tiles[23]}{CRIMSON}║{RESET}{tiles[24]}{CRIMSON}║{RESET}{tiles[25]}{CRIMSON}║{RESET}",        
        f"{CRIMSON}╚════╩════╩════╩════╩════╝{RESET}"
    ]

    for line in board:
        print(line)

    if os.path.exists(f"{day}.png.enc"):
        decrypt()
        os.remove(f"{day}.png.enc")

    for i in ["a", "b", "c", "d", "e"]:
        if day == 25 and os.path.exists(f"{i}.mp4.enc"):
            decrypt()
            os.remove(f"{i}.mp4.enc")

main()