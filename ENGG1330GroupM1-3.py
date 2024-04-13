import time, os

#valueble needed in this game----------------------------------------------
hp = 100
pressure = 0
days = 1
win = 0
serum = 0
item = []
itemchoice = 0
cluesfound = []
availablefloor = ['1','rooftop']
availableroom = ['1','2','3','4']
availablechoiceinroom = ['1','2','3']
availablemenuinfloor = ['1','2','3','4','5','6','7','8','9']
yesnoaction = ['1','2']
achievement  = []
mission = ['Explore all rooms on floor 1, and find a way to floor 2...']
#variable of every room-----------------------------------------------------
floor1room1sedative = 0
floor1room1coffer = 0
floor1room1cofferunlock = 0
floor1room1cluefound = 0
floor1room2dieperson = 0
floor1room2zombie = 1
floor1room2zombieclue = 0
floor1room3key = 0
floor1room3medkit = 0
floor1room4michaelfound = 0
floor1room4script = 0
Michaelbuff = 0
Michaelzombie = 0
door_open_in_floor1_room4 = False

floor2room1torch = 0
floor2room1die = 0
floor2room2zombie = 1
floor2room2clue = 0
floo2room2equip = 0
floor2room3unlock = 0
floor2room3pain = 0
floor2room4right = 0
floor2room4clue = 0
floor2room4wall = 0

floor3room1clue1= 0
floor3room1clue2= 0
floor3room2zombie1 = 1
floor3room2zombie2 = 1
floor3room3zombie = 1
floor3room3nothing = 0
floor3room4daughter = 0
floor3room4daughterrecorver = 0
floor3room4medkit = 0
enter_floor3_room4_times = 0

floor4room1medkit = 0
floor4room1zombie = 1
floor4room2nero = 0
floor4room2key = 0
floor4room3nero = 0
floor4room3zombie = 1
floor4room4serum = 0
floor4room4final = 0
#---------------------------------------------------------------------------

def zombie_art():
    print()
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠯⣤⠼⣳⣄⠠⠴⢆⠹⣾⣥⠏⣱⡼⣿⣿⣿⣽⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡴⣿⡛⢧⡀⢊⡷⣾⠟⣀⣴⣿⣾⣿⣿⣽⣿⣿⡌⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡓⣦⠆⢠⣄⢛⡒⣉⠀⠃⢀⠉⢉⣿⢿⣿⣿⣿⣿⣿⣿⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠡⡏⠀⡀⣀⣲⣿⣄⠀⠀⠀⡴⢿⣿⣿⣏⣻⠹⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣙⢹⣿⡐⠀⣤⣿⡏⠃⠹⣿⣿⣦⠀⢷⣿⣿⠁⠈⠹⣿⣿⣿⡏⠀⣿⠛⣄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢮⡷⠀⡀⢻⣿⣧⣤⣴⣿⣿⡟⠀⢻⣿⣿⡷⣶⣾⣿⣿⣿⡇⡕⣺⢀⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⠁⣿⠰⣅⠹⣿⣿⣾⣿⣿⣿⣿⣧⣾⣿⣿⡟⠿⠿⢻⣽⣿⡇⠐⣿⠀⢿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⡀⢌⣃⢸⣉⠉⣲⣿⣿⡿⠀⣿⡀⣙⢻⡦⣄⡀⠈⣿⣿⣌⣿⣀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⢿⣇⣾⣿⣰⡏⠹⣩⣿⣿⡿⠀⣽⣧⠈⣿⣷⣿⠀⠀⣻⡟⣰⡿⢿⢌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⣿⣿⣿⢿⡇⣼⣿⡿⢿⡗⠀⢹⣿⠆⠹⣿⡧⠠⠀⢸⡇⣿⢣⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⡿⢻⡇⣿⣿⣿⣽⣷⣦⣿⣿⡆⠀⠈⢹⠄⢠⣼⡇⣿⣆⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣇⣿⣠⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠈⠃⣨⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⠛⢿⠿⡿⢿⣿⡿⣿⣆⡀⠘⠃⢸⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣧⣼⣿⣿⣿⣾⡇⢰⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡻⣏⡶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣓⢻⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣧⣻⣿⣿⣾⣿⣽⡛⣿⣿⣿⡏⠌⣿⠏⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡌⠙⢿⣷⣿⣿⣾⣿⣿⣿⣿⣿⢡⡾⠃⢈⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠐⡀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⡴⠀⠐⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡻⠍⢠⣝⢿⡇⠠⠁⠄⣀⣿⣿⣿⣿⣿⣿⣿⡏⠀⠄⡔⠰⢀⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡼⠛⢇⣱⣏⡾⣿⣿⡄⠀⣾⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣄⠀⢀⣾⣿⣿⣿⡟⣻⣯⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠙⠦⣱⣾⣿⣿⣿⣿⣿⣷⣾⣿⢡⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣠⣾⣿⣿⣟⣿⡷⣶⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢐⣿⣿⣯⣿⣿⣻⣝⣩⣿⣷⡄⢹⣿⣿⣿⣿⣿⣿⣾⣦⣿⣿⣿⣿⣿⠟⠛⣷⣿⣿⣼⣿⣿⣿⡟⣫⠛⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢿⡴⣽⣿⣿⡹⣟⣾⣷⣿⡿⣟⡿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⣽⣿⠛⠁⠠⣰⣿⣿⡿⣿⠿⣋⢳⠑⡈⠭⠲⣽⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿')
    print('⡿⠟⠋⠩⠌⢁⠀⠀⠀⠀⡁⢋⡿⣘⠻⡷⣯⣽⣍⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣷⣶⣿⣿⣿⡟⠁⠣⠐⢠⠃⠡⣐⢣⣿⣿⡿⠛⠉⠃⠀⠀⣾⡿⣿')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⣐⠉⣷⢻⡵⣫⠞⡈⢿⡿⣿⣗⣻⣯⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠏⠀⠀⠀⠀⢈⠀⠒⢠⣺⣽⠟⢀⠄⠀⠀⠀⠀⡽⣃⠞')
    print('⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠈⢎⣻⣼⠅⠈⣔⠻⡼⢻⡿⡿⡕⢻⣿⣿⣿⣿⣿⣿⣿⣇⣈⣿⣷⣿⣿⡿⢏⠀⠁⠁⠀⠀⠀⠀⠈⠀⣀⢚⢛⠁⠀⣆⠀⠀⠀⠀⢀⣷⡍⠊')
    print('⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣘⠐⠎⣠⠈⣇⠈⠀⢀⣶⣻⢿⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡹⣿⣿⢻⠿⡄⠈⠛⠀⠀⠀⠀⠀⠈⠈⠁⣨⠂⠁⢸⠯⡄⠀⠀⠀⣼⠟⠀⠁')
    print('⣰⠀⠀⠀⠀⠀⠀⠀⢀⠀⠠⠄⢨⡙⠲⠄⣿⢿⡿⣷⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⣽⣫⢾⣽⣆⣥⣼⣤⣤⣤⣦⣲⡀⠐⠀⠀⢀⡞⢠⠇⠀⢠⣾⠏⠀⠀')
    print('⢐⠁⠀⠀⠀⠀⠀⠀⠀⠂⠄⠠⠀⠀⠑⠆⢿⡳⣹⢖⡿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡟⣿⣻⠞⣧⣿⣟⣿⣿⣿⣙⣏⣏⣧⡟⢻⡗⠀⠀⣘⠀⣿⠀⠀⣾⠃⠀⠀⠀')
    print()

def Michael_art():
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⣤⣶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⣐⣿⣿⣿⣿⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣐⣅⣤⣤⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣤⡏⢩⢇⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣡⣽⢿⣿⣿⣦⠀⠀⡠⠊⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠢⢠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⡆⠈⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⡿⣇⠼⢻⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⡇⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⣏⣻⣾⠁⠀⢀⣿⣿⡇⣿⣿⣿⣿⣇⢏⠁⠈⠀⠄⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢔⣵⣿⣫⣧⣧⣽⢦⣿⣄⣂⣁⣩⢋⠉⠁⣌⠘⠀⡇⠀⠀⠀⠀⠀⠈')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢊⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⡎⠉⠀⠀⠀⠀⠀⠀⠀')
    print('⢀⠔⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⣠⢿⣯⣿⣿⣿⠟⠻⣿⣿⣿⢿⣻⣿⠪⡉⢿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⣠⣾⣿⣩⣺⣿⡿⠋⣠⡴⠾⣿⣧⣤⣿⣧⣠⠶⠾⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣿⣧⣺⣿⣿⣿⣿⡿⣯⣖⢿⢟⣄⠄⣽⣿⣿⣿⣩⣀⠰⠜⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠠⠈⠛⠿⢿⣿⡆⡿⡻⡿⣵⡪⣥⣦⣧⣷⣮⣾⡿⠋⠉⠁⠀⠀⠀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠠⠀⠀⢀⠀⠀⠀⣏⡏⣿⣷⣔⣽⡿⣷⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⠃⠼⠟⠛⠛⠋⠉⠀⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀')
    print()

def Michael_daughter_art():
    print('⠀⠀⠀⠀⠀⠀⠀⠀⣀⣶⣾⣟⣽⣿⣷⣆⡀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⢿⣿⣿⣿⣿⣆⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀')
    print('⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣇⠀')
    print('⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀')
    print('⠀⠀⠄⣻⣿⣯⣿⣿⡏⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀')
    print('⠀⠀⢴⣟⣿⣿⣿⣿⠻⠴⠄⢐⡻⢿⣿⣿⣿⣿⣿⣿⡄')
    print('⠀⡰⣯⣿⣿⣿⣿⣿⣷⣄⣀⢈⣷⣀⣿⣿⣿⣿⣿⣿⣇')
    print('⡂⠚⣏⣟⣼⣿⣿⣿⣿⣿⡹⠿⠿⢻⣿⣿⣿⣿⡿⣛⠋⠇')
    print('⠷⠨⠋⣡⣶⡿⣻⣿⣿⣿⣧⡀⠀⢈⣿⣿⣿⣷⣧⡀⠸⢾⡄')
    print('⢰⠁⠀⠉⠉⠑⠾⠿⡿⠟⠋⠉⢉⡹⠟⠙⠛⠛⢛⣟⣢⣤⣿⡄')
    print('⢠⠀⠀⠀⠀⡔⣈⡩⠀⠀⠀⠀⣌⡐⠠⠄⡀⠀⠙⠛⠻⠿⣿⣧⠀')
    print('⠀⢁⡶⠂⣤⠭⢥⣇⡀⢀⢠⣆⣛⣉⢵⣦⣤⣁⣒⣄⣀⣀⡠⠎⠀')
    print('⠀⣼⠃⢸⡏⠀⠈⠈⢿⣿⣿⣟⢡⡇⠀⢏⠿⢻⣿⢿⣿⡄⠀')
    print('⠀⡿⠑⢺⣧⠀⢠⠀⢸⣿⣿⣿⣿⠁⠀⡈⠀⣰⣏⣾⣿⢷⡀⠀')
    print('⠀⠃⠀⣸⠏⡆⠈⡄⠘⣿⣿⣿⡇⠀⠐⠀⣠⣿⣿⣿⣿⣸⣧')
    print('⠃⠀⣸⠏⡆⠈⡄⠘⣿⣿⣿⡇⠀⠐⠀⣠⣿⣿⣿⣿⣸⣧⠀')
    print('⡀⣰⣧⣤⣰⠀⠠⠀⣿⣻⡿⠀⠠⠁⣰⣿⣿⣿⣿⣿⣿⣿')
    print('⣷⠁⠀⠀⠨⡆⠀⠁⢸⡟⠁⣰⣡⣾⣿⣿⡿⣛⣻⣿⣿⡇⠀')
    print('⠘⠶⠶⠾⢛⠇⢠⢃⡞⠀⣴⣿⣿⠉⠛⣻⠿⠾⠿⠿⡿⣁⠀⠀')
    print('⠀⠀⣀⠔⠂⢀⣇⡞⠀⣾⣿⣿⠓⠀⠒⠀⢤⠔⠀⠀⠀⠈⠁⠀')
    print('⠀⠀⢸⡟⡄⡖⣼⢪⡄⢀⣋⣻⣿⠄⠂⠉⠁⠀⠀⠀⠀⢀⡀⠠⠄⠀⠀')
    print('⠀⠀⠀⠙⠛⠺⢷⣿⣸⣹⣿⣷⠇⠀⣀⠄⠐⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⡀⠀⠀⠀⠈⠉⠁⠈⠁⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⡀⠀⠀⠀')
    print('⠀⠀⠀⠒⠛⠛⠛⠛⠋⠛⠛⠓⠛⠐⠛⠛⠛⠀⠀⠑⠋⠃⠋⠛⠛⠛⠛⠃')
    print()

def target():

    print('\033[1m'    +  '----------------------|' +   '\033[33m'   +  'TARGET'+   '\033[0m'   +    '\033[1m'   +   '|----------------------')
    time.sleep(3)
    print('\033[1m' +   '1. '   +   '\033[0m'   +   'Find a serum to ward off the zombie virus.')
    print('\033[1m' +   '2. '   +   '\033[0m'   +   'Find the password of the roof gate(floor 5) to escape.')   
    print('\033[31m'    +   '\033[1m'   +   'Remark: If you find the password but not the serum, the game will continue.'+'\033[0m')
    print()

def gamerule():

    print('\033[1m' +   '--------------------|GAME RULES|--------------------')
    time.sleep(3)
    print('\033[1m' +   '1. '   +   '\033[0m'   +   'The character has HP, when HP <= 0, the character dies and the game ends.')
    print('\033[1m' +   '2. '   +   '\033[0m'   +   'The character has a pressure value. When the pressure value is >= 100, the exploration of the day is forced to end!')
    print('\033[1m' +   '3. '   +   '\033[0m'   +   'Players can end the current day on their own and reset health and pressure.')
    print('\033[1m' +   '4. '   +   '\033[0m'   +   'The floor can only be explored after the previous floor has been explored.Otherwise,invalid move.')
    print('\033[1m' +   '5. '   +   '\033[0m'   +   'An item can only be acquired and used once.\n')

def character(hp,pressure):

    print('\033[1m'   +   '----------------------|'  +   '\033[33m'   +   'STATUS'    +   '\033[0m'   +    '\033[1m'   +   '|----------------------')
    time.sleep(1.5)
    print(f'\033[33mhp: {hp}/100')
    print(f'Pressure: {pressure}%\033[0m')
    print() 

def clues(cluesfound):
    if len(cluesfound) == 0:
        print('Nothing!!!')
    for i in range(1,len(cluesfound)+1):
        print(f'{i}. {cluesfound[i-1]}')
    print()

def items(itemchoice):
    global item
    global hp
    global pressure
    global serum
    if len(item) == 0:
        print('Nothing!!!')    
    for i in range(1,len(item)+1):
        print(f'{i}. {item[i-1]}')
    if len(item) > 0 :
        itemchoice = input('Do you want to use anything?(type it)(Enter e to exit):')
        while itemchoice not in item:
            if itemchoice == 'e':
                break
            print('You do not obtain this item')
            itemchoice = input('Do you want to use anything?(type it)(Enter e to exit):')
    if itemchoice == 'sedative' and len(item) > 0:
        del item[item.index('sedative')]
        pressure = 0
        print(f'Pressure: {pressure}%')
        print('You use it successfully, now you feel refreshed.')
        print('You lose an item --> A sedative')
    if itemchoice == 'medkit' and len(item) > 0:
        del item[item.index('medkit')]
        hp = 100
        print(f'hp: {hp}/100')
        print('You use it successfully, now you are healthy.')
        print('You lose an item --> A Medical kit')
    if itemchoice == 'neurotoxin' or itemchoice == 'torch' or itemchoice == 'a broken knife':
        print('You can not use it to your body!')
    if itemchoice == 'script1' and len(item) > 0:
        print('F or I am the king of this land\nO ld ruler of the sky and the earth\nU nification of the world is in my sight\nR ighteousness shall bloom, like a flower in the dawn')
    if itemchoice == 'serum' and len(item) > 0:
        serum = 1
        pressure = 0
        print('With the penetration of the serum, the threat to your life has been lifted.\nNow feel free to find the password for the rooftop gate!')
        print('(Your pressure rate is set to 0%)')
    print()
    
def missions(mission):
    for i in range(1,len(mission)+1):
        print(f'{i}. {mission[i-1]}')
    print()

def check_HP():
    global hp
    global pressure
    if hp <= 0:
        return False

def text_on_menu():
    print('\033[1m'   +   '------------------------|'  +   '\033[33m'   +   'MENU'    +   '\033[0m'   +    '\033[1m'   +   '|------------------------')
    print('\033[33m***Enter a number***\033[0m')
    print('\033[1m' +   '1. '   +   '\033[0m'   +   ' Explore the rooms in this floor')
    print('\033[1m' +   '2. '   +   '\033[0m'   +   ' Exit this floor')
    print('\033[1m' +   '3. '   +   '\033[0m'   +   ' Sleep(reset Hp and pressure)')
    print('\033[1m' +   '4. '   +   '\033[0m'   +   ' Check personal infomation(Hp,Pressure)')
    print('\033[1m' +   '5. '   +   '\033[0m'   +   ' Check clues found')
    print('\033[1m' +   '6. '   +   '\033[0m'   +   ' Check/Use your items')
    print('\033[1m' +   '7. '   +   '\033[0m'   +   ' Check your missions')
    print('\033[1m' +   '8. '   +   '\033[0m'   +   ' Check the target')
    print('\033[1m' +   '9. '   +   '\033[0m'   +   ' Check the game rule')
    print('\033[31m\033[1m' +   '##########Remark: Please enter anything to continue to next step when a sentence is shown##########'   +   '\033[0m')

def goback():

    back = input('Enter "\033[33m\033[1mback\033[0m" to go back to the menu: ')
    if back == 'Back' or back == 'back' or back =='BACK':
        text_on_menu()
    else:
        print('Invalid text, please try again!')
        
def game_menu():
    text_on_menu()
    menu_choice = input('\033[96m'    +   'Please take your action: '     +      '\033[0m')
    while menu_choice not in availablemenuinfloor:
        print('\033[31m\033[1m' +   'Invalid input, please try again!'   +   '\033[0m')
        menu_choice = input('\033[96m'    +   'Please take your action: '     +      '\033[0m')

    if menu_choice == '1' or menu_choice == '2' or menu_choice == '3':
        return menu_choice
        
    else:
        while True:
            if menu_choice == '4':
                character(hp,pressure)
                time.sleep(1)
                goback()
            elif menu_choice == '5':
                clues(cluesfound)
                time.sleep(1)
                goback()
            elif menu_choice == '6':
                items(itemchoice)
                time.sleep(1)
                goback()
            elif menu_choice == '7':
                missions(mission)
                time.sleep(1)
                goback()
            elif menu_choice == '8':
                target()
                time.sleep(1)
                goback()
            elif menu_choice == '9':    
                gamerule()
                time.sleep(1)
                goback()
            menu_choice = input('\033[96m'    +   'Please take your action: '     +      '\033[0m')
            while menu_choice not in availablemenuinfloor:
                print('\033[31m\033[1m' +   'Invalid input, please try again!'   +   '\033[0m')
                menu_choice = input('\033[96m'    +   'Please take your action: '     +      '\033[0m')    
            if menu_choice == '1' or menu_choice == '2' or menu_choice == '3':
                return menu_choice
       
def action_in_room():
    print('\033[1m'    +  '----------------------|' +   '\033[33m'   +  'ACTION'+   '\033[0m'   +    '\033[1m'   +   '|----------------------')
    print('\033[1m' +   '1. '   +   '\033[0m'   +' Check left side')
    print('\033[1m' +   '2. '   +   '\033[0m'   +' Check right side')
    print('\033[1m' +   '3. '   +   '\033[0m'   +' Exit this room')
    print()
    print('\033[1m'    +  '----------------------------------------------------')
    action = input('\033[96m'    +   'Please take your action: '     +      '\033[0m')
    while action not in availablechoiceinroom:
        print('\033[31m\033[1m' +   'Invalid move, please try again!'   +   '\033[0m')
        action = input('\033[96m'    +   'Please take your action: '     +      '\033[0m')
        if action == '1' or action == '2' or action == '3':
            return action
    return action

def opening():
    print()
    print("\033[1m"+'\033[94m'+'███████╗ ██████╗ ███╗   ███╗██████╗ ██╗███████╗         █████╗ ███████╗██╗   ██╗██╗     ██╗   ██╗███╗   ███╗')
    print('╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗██║██╔════╝        ██╔══██╗██╔════╝╚██╗ ██╔╝██║     ██║   ██║████╗ ████║')
    print('  ███╔╝ ██║   ██║██╔████╔██║██████╔╝██║█████╗          ███████║███████╗ ╚████╔╝ ██║     ██║   ██║██╔████╔██║')
    print(' ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██╗██║██╔══╝          ██╔══██║╚════██║  ╚██╔╝  ██║     ██║   ██║██║╚██╔╝██║')
    print('███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║███████╗        ██║  ██║███████║   ██║   ███████╗╚██████╔╝██║ ╚═╝ ██║')
    print('╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝        ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝     ╚═╝'+'\033[0m')
    print()
    time.sleep(2)
    print('\033[1m' +   'Fugitive, what is your name?')
    name = input('Name: '   +   '\033[0m')
    print('\033[1m' +   '  '    +   name    +   ', a fugitive. Today, you were attacked by a horde of zombies and unfortunately injured. Although')
    time.sleep(2)
    print('you have been vaccinated against the zombie virus, you will still be infected as a zombie after 7 days (Day8)')
    time.sleep(2)
    print('You carried enough supplies and finally escaped from the zombies and escaped to an abandoned hospital. When')
    time.sleep(2)
    print('you came to the hospital, you did a cursory inspection of the hospital. You found that the hospital has a')
    time.sleep(2)
    print('total of 4 floors, and each floor has 3 unlocked rooms and 1 room with a combination lock.')
    time.sleep(2)
    print()

def floor_1():
    global hp
    global pressure
    global days
    global floor1room1sedative 
    global floor1room1coffer 
    global floor1room1cofferunlock 
    global floor1room1cluefound 
    global floor1room2dieperson 
    global floor1room2zombie 
    global floor1room2zombieclue 
    global floor1room3key 
    global floor1room3medkit 
    global floor1room4michaelfound 
    global floor1room4script 
    global Michaelbuff 
    global Michaelzombie 
    global door_open_in_floor1_room4
    print('\033[1m------------------------------------------------------')
    print('\033[33m\033[1m' +'You are now on floor 1'   +   '\033[0m')

    while True:
        if check_HP() == False:
            break
        menu_choice = game_menu()
        if menu_choice == '2':
            break            
        elif menu_choice == '3':
            hp = 100
            pressure = 0
            days+=1
            break
        elif menu_choice == '1':

            if check_HP() == False:
                break
            print()
            print('\033[96m\033[1m(Available room: 1, 2, 3, 4)\033[0m')
            floor1room = input('\033[96m'    +   'Which room you want to go: '  +   '\033[0m')
            while floor1room not in availableroom:
                print('\033[31m\033[1m' +   'Invalid move, please try again!'   +   '\033[0m')
                floor1room = input('\033[96m'    +   'Which room you want to go: '  +   '\033[0m')
            print('You try to open the door of this room\nbut the wind blowing in front of you is making you feel nervous')
            print('\033[91m\033[1mRemark: When you try to enter a room, your pressure rate will increase by 5%\033[0m')
            pressure+=5
            character(hp,pressure)
            
            if pressure>=100:
                print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                pressure = 0
                days+=1
                break
            while floor1room == '1':#Floor1 Room 1-----------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 1, Room {floor1room}\033[0m')

                action = action_in_room()
                if action == '1':
                    if floor1room1sedative == 1:
                        print('You get nothing......')

                    if floor1room1sedative == 0:
                        floor1room1sedative = 1
                        print('\033[37mYou obtain a sedative\033[0m')
                        print('(---Please check your item---)')
                        item.append('sedative')
                        for i in range(1,len(item)+1):
                            print(f'{i}. {item[i-1]}')

                elif action == '2':
                    if floor1room1coffer == 1:
                        if 'Coffer key' in item:
                            continue1 = input('Enter 1 to unlock the coffer: ')
                            if continue1 != '1':
                                print('You leave here...')
                            if continue1 == '1':
                                print('You try to unlock the coffer....')

                                if floor1room1cofferunlock == 1:
                                    print('You get nothing from the coffer')
                                if floor1room1cofferunlock == 0:
                                    floor1room1cofferunlock = 1
                                    print('\033[37mYou obtain a script!\033[0m')
                                    cluesfound.append('4%^4%^1%^1  (Found in Coffer from Floor1 Room1)')
                                    print('(---Please check your clues found---)')
                                    clues(cluesfound)
                        else:
                            print('It seems you need a key to open it......')
                    if floor1room1coffer == 0:
                        floor1room1coffer = 1
                        print('\033[37mYou discover a coffer.\033[0m')
                        print('It seems you need a key to open it......')
                        print('(---Please check your cluesfound---)')
                        cluesfound.append('There is a coffer in Floor1 Room1')
                        clues(cluesfound)

                elif action == '3':
                    break

            while floor1room == '2':#Floor1 Room 2-----------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 1, Room {floor1room}\033[0m')
                action = action_in_room()

                if action == '1':
                    if floor1room2dieperson == 0:
                        print('You found a dead person\nThere seems to be a zombie bite mark on the neck\nYou immediately alerted the existence of zombies in the hospital')
                        print('(---Please check your cluesfound---)')
                        cluesfound.append('There are ZOMBIES in this hospital')
                        clues(cluesfound)                   
                        print('\033[37mYou found a broken knife from the dead person.\033[0m')
                        print('(---Please check your items---)')
                        item.append('a broken knife')
                        for i in range(1,len(item)+1):
                            print(f'{i}. {item[i-1]}')
                        pressure+=50
                        character(hp,pressure)
                        if pressure>=100:
                            print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                            days+=1
                            break
                    if floor1room2dieperson == 1:
                        print('\033[37mYou rummaged through the corpse and found a sedative\033[0m')
                        print('---Please check your item---')
                        item.append('sedative')
                        for i in range(1,len(item)+1):
                            print(f'{i}. {item[i-1]}')

                    if floor1room2dieperson >= 2:
                        print('You rummaged through the deadperson for a while and found nothing...')

                    floor1room2dieperson+=1

                elif action == '2':
                    if floor1room2zombie == 1:
                        print('You are searching something......')

                        print('\033[91m\033[1m(Zombie sound)')
                        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m')
                        time.sleep(2)
                        zombie_art()
                        time.sleep(1)
                        print('You look back and a zombie knocking you down')
                        if floor1room2zombieclue == 0:
                            floor1room2zombieclue = 1
                            cluesfound.append('A zombie is in Floor1 Room2 ')
                            print('---Please check your clues found---')
                            clues(cluesfound)
  
                        if 'a broken knife' in item and 'neurotoxin' not in item: 
                            del item[item.index('a broken knife')]
                            print('You took up the broken knife and temporarily drove the zombies away\nBut the zombies might wake up later,You quickly fled the scene...')
                            print('You lose an item --> a broken knife')
                            for i in range(1,len(item)+1):
                                print(f'{i}. {item[i-1]}')

                            continue
                        if 'torch' in item and 'neurotoxin' not in item:
                            print('You hurriedly threw the torch out\nAttracting the attention of the zombies, and you fled in the chaos')

                            del item[item.index('torch')]
                            print('You lose an item --> torch')
                            print('---Please check your item---')
                            for i in range(1,len(item)+1):
                                print(f'{i}. {item[i-1]}') 

                            continue
                        if 'neurotoxin' in item:
                            print('\033[1m------------------------------------------------------')
                            print('Do you want to kill this zombie?')
                            print('1. Yes')
                            print('2. No')
                            continue1 = input('Please take your action: ')
                            while continue1 not in yesnoaction:
                                print('Invalid action, Please try again!')
                                continue1 = input('Please take your action: ')
                            if continue1 =='1':
                                floor1room2zombie = 0
                                del item[item.index('neurotoxin')]
                                print('You lose an item --> neurotoxin')
                                print('You kill this zombie...but you find something......')
                                print('You found a hidden serum!')
                                achievement.append('Found the hidden serum in Floor1 Room2')
                                item.append('serum')

                                print('---Please check your item---')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}')

                                continue
                            if continue1 == '2':
                                print('Zombies seem to be terrified of the smell\nYou found nothing and left')      
                                continue               
                        if 'torch' and 'neurotoxin' and 'a broken knife' not in item:
                            if Michaelbuff == 0:
                                print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                hp-=50
                                character(hp,pressure)
                                if hp<=0:
                                    break
                            if Michaelbuff == 1:
                                print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                hp-=50
                                character(hp,pressure)
                                if hp<=0:
                                    hp+=50
                                    Michaelbuff = 0
                                    Michaelzombie = 1
                                    print('When you were about to die, Michael showed up and save your life\n But he seemed to be infected...')  
                                    character(hp,pressure)
                                    mission.append('Save Michael (optional)(Use one serum)(Michael is in Floor1 Room4')
                                    missions(mission)
                    if floor1room2zombie == 0:
                        print("You found nothing but a zombie's body on the ground")

                elif action == '3':                    
                    break
            
            while floor1room == '3':#Floor1 Room 3-----------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 1, Room {floor1room}\033[0m')
                action = action_in_room()

                if action == '1':
                    if floor1room3key == 0:
                        print('\033[37mYou got a coffer key!\033[0m')
                        item.append('Coffer key')
                        print('---Please check your item---')
                        for i in range(1,len(item)+1):
                            print(f'{i}. {item[i-1]}')
                    if floor1room3key > 0:
                        print('You got nothing!')
                    floor1room3key+=1
                
                if action == '2':
                    if floor1room3medkit == 0:
                        print('\033[37mYou got a Medical kit!\033[0m')
                        item.append('medkit')
                        print('---Please check your item---')
                        for i in range(1,len(item)+1):
                            print(f'{i}. {item[i-1]}')
                    if floor1room3medkit > 0:
                        print('You got nothing!')
                    floor1room3medkit+=1
                
                if action == '3':
                    break
            
            while floor1room == '4':#Floor1 Room 4-----------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 1, Room {floor1room}\033[0m')
                if door_open_in_floor1_room4 == False:
                    continue1 = input('There is a combination lock there,...(Press 1 to enter password)(Press e to exit): ')
                    while continue1 != 'e' and continue1 !='1':
                        print('Invalid move! Please try again!')
                        continue1 = input('There is a combination lock there,...(Press 1 to enter password)(Press e to exit): ')
                    if continue1 == 'e':
                            break
                    if continue1 == '1':
                        continue1 = input('Please enter the password : ')
                    if continue1 == '4411':
                        print('\033[1m(------Password correct------)')
                        door_open_in_floor1_room4 = True
       
                    else:
                        print('\033[91m\033[1m(------Password wrong------)')
                        print('You feel more tense......\033[0m')
                        pressure+=20
                        character(hp,pressure)
                        if pressure>=100:
                            print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                            days+=1
                            break
                        break
                    
                if door_open_in_floor1_room4 == True:
                    action = action_in_room()
                    if action == '1':
                        if floor1room4michaelfound == 0:
                            Michael_art()
                            print('\033[1m------------------------------------------------------')
                            print('\033[92m\033[1mYou: Hey,who are you!\033[0m')
                            time.sleep(1)
                            print('\033[96m\033[1mMichael: I am also a survivor......but I am injured right now...\033[0m')
                            print()
                            time.sleep(2)
                            print('\033[1m------------------------------------------------------')
                            print('\033[35m\033[1mDo you want to save him?\033[0m')
                            print('\033[32m\033[1m1. Yes (lose a Medical kit)\033[0m')
                            print('\033[91m\033[1m2. No\033[0m')
                            continue1 = input('Please take your action: ')
                            while continue1 not in yesnoaction:
                                print('Invalid move , Please try again!')
                                continue1 = input('Please take your action: ')
                            if continue1 == '1':
                                if 'medkit' not in item:
                                    print('You do not have any Medical Kit in your item list')
                                    
                                if 'medkit' in item:
                                    Michaelbuff = 1
                                    del item[item.index('medkit')]
                                    print('\033[37mYou lose a item---> Medical Kit\033[0m')
                                    print('\033[96m\033[1mMichael: Thanks for your help......If you need any help, I will do my best.\033[0m')
                                    time.sleep(1)
                            cluesfound.append('A survivor called Michael is in Floor1 Room4')
                            print('---Please check your clues found---')
                            clues(cluesfound)
                            print('\033[96m\033[1mMichael: Can you do me a favour? I can not find my daughter......\033[0m')
                            mission.append('Find his daughter(Michael)')
                            print('---Please check your missions---')
                            missions(mission)
                        if floor1room4michaelfound >0:
                            if Michaelzombie == 0:
                                print('\033[96m\033[1mMichael: I just want to find my daughter and leave here......\033[0m')
                                print()
                            if Michaelzombie == 1:
                                print('\033[1m------------------------------------------------------')
                                print('\033[35m\033[1mDo you want to help Michael?\033[0m')
                                print('\033[32m\033[1m1. Yes(lose a serum)\033[0m')
                                print('\033[91m\033[1m2. No\033[0m')
                                continue1 = input('Please take your action: ')
                                while continue1 not in yesnoaction:
                                    print('Invalid move , Please try again!')
                                    continue1 = input('Please take your action: ')
                                if continue1 == '1':
                                    if 'serum' not in item:
                                        print('You do not have any serum in your item list')
                                        continue1 = input()
                                    if 'serum' in item:
                                        Michaelzombie = 0
                                        del item[item.index('serum')]
                                        print('\033[37mYou lose a item---> serum\033[0m')
                                        achievement.append('Love and righteousness(Saved Michael from being infected)')
                        floor1room4michaelfound+=1
                    if action == '2':
                        if floor1room4script == 0:
                            print('You found a script!(about roof gate password)')
                            print('HINT: you can check it in item')
                            item.append('script1')
                            print('---Please check your item---')
                            for i in range(1,len(item)+1):
                                print(f'{i}. {item[i-1]}')
                            print('\033[91m\033[1mYou have found a way to go up to the second floor and are terrified of the unknown floors\033[0m')
                            availablefloor.append('2')
                            print('---Mission update---')
                            mission.append('Explore all rooms on floor 2, and find a way to floor 3...')
                            pressure+=20
                            character(hp,pressure)
                            
                            if pressure>=100:
                                print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                                days+=1
                                break
                            character(hp,pressure)
                            
                        if floor1room4script>0:
                            print('You got nothing!')
                        floor1room4script+=1
                    if action == '3':
                        break
            if pressure>=100:
                pressure = 0
                break     
                
def floor_2():
    global hp
    global pressure
    global days
    global Michaelbuff 
    global Michaelzombie 
    global floor2room1torch 
    global floor2room1die 
    global floor2room2zombie 
    global floor2room2clue 
    global floo2room2equip 
    global floor2room3unlock 
    global floor2room3pain 
    global floor2room4right 
    global floor2room4clue 
    global floor2room4wall 
    print('\033[1m------------------------------------------------------')
    print('\033[33m\033[1m' +'You are now on floor 2'   +   '\033[0m')

    while True:
        if check_HP() == False:
            break
        menu_choice = game_menu()      
        if menu_choice == '2':
            break
        
        elif menu_choice == '3':
            hp = 100
            pressure = 0
            days+=1
            break
        
        elif menu_choice == '1':

            if check_HP() == False:
                break
            print()
            print('\033[96m\033[1m(Available room: 1, 2, 3, 4)\033[0m')
            floor2room = input('\033[96m'    +   'Which room you want to go: '  +   '\033[0m')
            while floor2room not in availableroom:
                print('\033[31m\033[1m' +   'Invalid move, please try again!'   +   '\033[0m')
                floor2room = input('\033[96m'    +   'Which room you want to go: '  +   '\033[0m')
            print('You try to open the door of this room\nbut the wind blowing in front of you is making you feel nervous')
            print('\033[91m\033[1mRemark: When you try to enter a room, your pressure rate will increase by 5%\033[0m')
            pressure+=5
            character(hp,pressure)

            if pressure>=100:
                print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                pressure = 0
                days+=1
                break
        
            while floor2room == '1':#Floor2 Room1--------------------------------------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 2, Room {floor2room}\033[0m')

                action = action_in_room()
                if action == '1':
                    if floor2room1torch == 0:
                        print('\033[37mYou got a torch!\033[0m')
                        print('You: Maybe it can save my life......')
                        item.append('torch')
                        print('---Please check your item---')
                        for i in range(1,len(item)+1):
                            print(f'{i}. {item[i-1]}')                   
                    if floor2room1torch >0:
                        print('You got nothing!')
                    floor2room1torch +=1
                elif action == '2':
                    if floor2room1die == 0:
                        print('\033[37mYou got a sedative from a dead person!\033[0m')
                        print('\033[91m\033[1mBut you were frightened by the tragic dead person\033[0m')
                        pressure+=10
                        if pressure>=100:
                            print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                            days+=1
                            break
                        character(hp,pressure)
                        item.append('sedative')
                        print('---Please check your item---')
                        for i in range(1,len(item)+1):
                            print(f'{i}. {item[i-1]}')  
                        floor2room1die += 1
                    if floor2room1die > 0 :
                        print("There's nothing here but the corpse")                   
                elif action == '3':
                    break
            
            while floor2room == '2':#Floor2 Room2--------------------------------------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 2, Room {floor2room}\033[0m')

                action = action_in_room()
                if action == '1':
                    if floor2room2zombie == 0:
                        print('\033[91m\033[1mThere is nothing but a zombie corpse on the ground.\033[0m')
                    if floor2room2zombie == 1:
                        if 'neurotoxin' in item:
                            print('\033[1m------------------------------------------------------')
                            print('Do you want to kill this zombie?')
                            print('\033[1m1. Yes\033[0m')
                            print('\033[91m\033[1m2. No\033[0m')
                            continue1 = input('Please take your action: ')
                            while continue1 not in yesnoaction:
                                print('\033[91m\033[1mInvalid action, Please try again!\033[0m')
                                continue1 = input('Please take your action: ')
                            if continue1 =='1':
                                floor2room2zombie = 0
                                del item[item.index('neurotoxin')]
                                print('You lose an item --> neurotoxin')
                                print('You kill this zombie...but you find something......')
                                print('\033[37mYou found a hidden serum!\033[0m')
                                item.append('serum')
                                print('---Please check your item---')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}')

                        else:
                            print('You see a sleeping zombie')
                            print("\033[91m\033[1mYou didn't want to disturb him, so you quietly left\033[0m")
                            if floor2room2clue == 0:
                                print('---Please check your clues found---')
                                cluesfound.append('There is a zombie in Floor2 Room2')
                                clues(cluesfound)
                                pressure+=10
                                if pressure>=100:
                                    print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                                    days+=1
                                    break
                                character(hp,pressure)
                            floor2room2clue = 1
                elif action == '2':
                    if floo2room2equip == 0:
                        print('\033[37mYou find a needle and a contaminated bandage\033[0m')
                        item.append('needle')
                        item.append('contaminated bandage')
                        print("You: Maybe I can find a workbench to make a lockpicker.....")
                        print('---Please check your item---')

                        for i in range(1,len(item)+1):
                            print(f'{i}. {item[i-1]}')
                    if floo2room2equip > 0:
                        print('You got nothing!')
                    floo2room2equip +=1               
                elif action == '3':
                    break
            
            while floor2room == '3':#Floor2 Room3-----------------------------------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 2, Room {floor2room}\033[0m')

                action = action_in_room()
                if action == '1':
                    if floor2room3unlock == 0:
                        character(hp,pressure)
                        print('\033[1mYou found an unpowered machine that seems to be able to make a lock pick...')
                        print('\033[1m------------------------------------------------------')
                        print('Do you want to use machine synthesis or manual synthesis?(force to choose)')
                        print('\033[1m------------------------------------------------------')
                        print('1.Machine(lose torch*1, needle*1, contaminated bandage*1, Obtain lockpick*1)')
                        print('2.Handmade(obtain lockpick*1, hp-30)')
                        continue1 = input('Please take your action: ')
                        while continue1 not in yesnoaction:
                            print('\033[91m\033[1mInvalid move , Please try again!\033[0m')
                            continue1 = input('Please take your action: ')
                        if continue1 == '1':
                            if 'torch' and 'needle' and 'contaminated bandage' not in item:
                                print('You did not get enough items!')
                                print('(You are forced to make a lockpick by hand)')
                                print('You pushed so hard that you reinjured your infected wound')
                                hp-=30
                                character(hp,pressure)
                                if hp<=0:
                                    break
                                item.append('unlocker')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}')  
                            else:
                                print('---Please check your item---')
                                del item[item.index('torch')]
                                del item[item.index('needle')]
                                del item[item.index('contaminated bandage')]
                                item.append('unlocker')
                                print('---Please check your item---')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}') 
                         
                        if continue1 == '2':
                            print('You pushed so hard that you reinjured your infected wound')
                            hp-=30
                            character(hp,pressure)
                            if hp<=0:
                                break
                            item.append('unlocker')
                            for i in range(1,len(item)+1):
                                print(f'{i}. {item[i-1]}')  
                    if floor2room3unlock > 0:  
                        print('There is only one broken machine here.....')      
                    floor2room3unlock+=1                
                elif action == '2':
                    if floor2room3pain == 0: 
                        print('\033[37mYou find a painkiller!\033[0m')
                        hp+=30
                        if hp>=100:
                            hp = 100
                        character(hp,pressure)

                    if floor2room3pain > 0: 
                        print('You got nothing!')
                    floor2room3pain+=1
                elif action == '3':
                    break
            while floor2room == '4':#Floor2 Room4--------------------------------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 2, Room {floor2room}\033[0m')
                if 'unlocker' in item:
                    print('You use a unlocker to unlock this door')
                    print('You lose an item --->unlocker')
                    del item[item.index('unlocker')]
                    floor2room4right = 1
        
                if floor2room4right == 1:
                    action = action_in_room()
                    
                    if action == '1':
                        if floor2room4clue == 0:
                            print('You found a small note')
                            print('---Please check your clues found---')
                            cluesfound.append('The clue provided by the last room on each floor is the key to opening the roof door(Found in Floor2 Room4)')
                            clues(cluesfound)


                        if floor2room4clue > 0:
                            print("You didn't find anything but that note")
                        floor2room4clue+=1
                    
                    elif action == '2':
                        if floor2room4wall == 0:
                            print("\033[91m\033[1mYou see a bloody number '3' carved on the wall")
                            print('You feel frustrated')
                            print('(They die !!??)\033[0m')
                            pressure+=20
                            if pressure>=100:
                                print('Your spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                                days+=1
                                break
                            cluesfound.append('A bloody number 3(Found in Floor2 Room4)')
                            clues(cluesfound)
                            availablefloor.append('3')
                            print('\033[91m\033[1mYou hear tons of zombies, they all seem to be on the third floor......\033[0m')
                            pressure+=10
                            if pressure>=100:
                                print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                                days+=1
                                break
                        if floor2room4wall>0:
                            print("That bloody number '3' is still there")
                        floor2room4wall+=1
                    
                    elif action == '3':
                        break

                else:
                    print('It looks like you need some tools to open this door.......')
                    break
            if pressure>=100:
                pressure = 0
                break   
def floor_3():
    
    global Michaelzombie
    global hp
    global pressure
    global days
    global Michaelbuff 
    global floor3room1clue1
    global floor3room1clue2
    global floor3room2zombie1
    global floor3room2zombie2 
    global floor3room3zombie 
    global floor3room3nothing 
    global floor3room4daughter 
    global floor3room4daughterrecorver 
    global floor3room4medkit 
    global enter_floor3_room4_times

    print('\033[1m------------------------------------------------------')
    print('\033[33m\033[1m' +'You are now on floor 3'   +   '\033[0m')

    while True:
        if check_HP() == False:
            break
        menu_choice = game_menu()

        if menu_choice == '2':
            break
        elif menu_choice == '3':
            hp = 100
            pressure = 0
            days+=1
            break

        elif menu_choice == '1':
            if check_HP() == False:
                break
            print()
            print('\033[96m\033[1m(Available room: 1, 2, 3, 4)\033[0m')
            
            floor3room = input('\033[96m'    +   'Which room you want to go: '  +   '\033[0m')
            while floor3room not in availableroom:
                print('\033[31m\033[1m' +   'Invalid move, please try again!'   +   '\033[0m')
                floor3room = input('\033[96m'    +   'Which room you want to go: '  +   '\033[0m')

            print('You try to open the door of this room\nbut the wind blowing in front of you is making you feel nervous')
            print('\033[91m\033[1mRemark: When you try to enter a room, your pressure rate will increase by 5%\033[0m')
            pressure+=5
            character(hp,pressure)

            if pressure>=100:
                print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                pressure = 0
                days+=1
                break
            while floor3room == '1':#Floor3 Room1--------------------------------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 3, Room {floor3room}\033[0m')

                action = action_in_room()
                if action == '1':
                    if floor3room1clue1 == 0 :
                        print('\033[37myou found a medical staff manuscript\033[0m')
                        print('-----Please check your clues found-----')
                        cluesfound.append('The serum is in Floor4 Room4!!!')
                        clues(cluesfound)
     
                    if floor3room1clue1 > 0 :
                        print('You got nothing!')
                    floor3room1clue1+=1
                
                elif action == '2':
                    if floor3room1clue2 == 0 :
                        print('\033[37myou found a soldier manuscript\033[0m')
                        print('-----Please check your clues found-----')
                        cluesfound.append('The zombies on the third floor are very special, as long as your stress level is 80 or above, they will attack you')
                        clues(cluesfound)
                           
                    if floor3room1clue2 > 0 :
                        print('You got nothing!')
                    floor3room1clue2+=1
                
                elif action == '3':
                    break
            
            while floor3room == '2':#Floor3 Room2--------------------------------------------------------------------------------------------------
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 3, Room {floor3room}\033[0m')
                action = action_in_room()

                if action == '1':
                    if floor3room2zombie1 == 1:
                        print('\033[91m\033[1mYou found a sleeping zombie\033[0m')
                        if pressure>=80:
                            print('\033[91m\033[1mYou woke up this zombie!!!\033[0m')
                            if 'a broken knife' in item and 'neurotoxin' not in item:
                                del item[item.index('a broken knife')]
                                print('You took up the broken knife and temporarily drove the zombies away\nBut the zombies might wake up later\You quickly fled the scene...')
                                print('You lose an item --> a broken knife')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}')
 
                                continue
                            if 'torch' in item and 'neurotoxin' not in item:
                                print('You hurriedly threw the torch out\nAttracting the attention of the zombies, and you fled in the chaos')

                                del item[item.index('torch')]
                                print('You lose an item --> torch')
                                print('---Please check your item---')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}') 

                                continue  
                            if 'neurotoxin' in item:
                                print('\033[1m------------------------------------------------------')
                                print('\033[1mDo you want to kill this zombie?')
                                print('1. Yes')
                                print('\033[91m\033[1m2. No\033[0m')
                                continue1 = input('Please take your action: ')
                                while continue1 not in yesnoaction:
                                    print('\033[91m\033[1mInvalid action, Please try again!\033[0m')
                                    continue1 = input('Please take your action: ')
                                if continue1 =='1':
                                    floor3room2zombie1 = 0
                                    del item[item.index('neurotoxin')]
                                    print('You lose an item --> neurotoxin')
                                    print('You kill this zombie...You feel relaxed......')
                                    pressure = 0

                                    continue 
                                if continue1 == '2':
                                    print('Zombies seem to be terrified of the smell\nYou found nothing and left')  
                                    continue                   
                            if 'torch' and 'neurotoxin' and 'a broken knife' not in item:
                                if Michaelbuff == 0:
                                    print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                    hp-=50
                                    character(hp,pressure)
                                    if hp<=0:
                                        break
                                if Michaelbuff == 1:
                                    print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                    hp-=50
                                    if hp<=0:
                                        hp+=50
                                        Michaelbuff = 0
                                        Michaelzombie = 1
                                        print('When you were about to die, Michael showed up and save your life\n But he seemed to be infected...')  
                                        continue1 = input()
                                        character(hp,pressure)
                                        mission.append('Save Michael (optional)(Use one serum)(Michael is in Floor1 Room4')
                                        missions(mission)
                        if pressure<80:
                            print("Your stress level isn't enough to wake them up, you're lucky")
                    if floor3room2zombie1 == 0:
                        print("There's a dead zombie on the ground, and there's nothing left")
                
                elif action == '2':
                    if floor3room2zombie2 == 1:
                        print('\033[91m\033[1mYou found a sleeping zombie\033[0m')
                        if pressure>=80:
                            print('\033[91m\033[1mYou woke up this zombie!!!\033[0m')
                            if 'a broken knife' in item and 'neurotoxin' not in item:
                                del item[item.index('a broken knife')]
                                print('You took up the broken knife and temporarily drove the zombies away\nBut the zombies might wake up later\You quickly fled the scene...')
                                print('You lose an item --> a broken knife')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}')

                                continue
                            if 'torch' in item and 'neurotoxin' not in item:
                                print('You hurriedly threw the torch out\nAttracting the attention of the zombies, and you fled in the chaos')
     
                                del item[item.index('torch')]
                                print('You lose an item --> torch')
                                print('---Please check your item---')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}') 

                                continue  
                            if 'neurotoxin' in item:
                                print('\033[1m------------------------------------------------------')
                                print('\033[1mDo you want to kill this zombie?')
                                print('1. Yes')
                                print('\033[91m\033[1m2. No\033[0m')
                                continue1 = input('Please take your action: ')
                                while continue1 not in yesnoaction:
                                    print('\033[91m\033[1mInvalid action, Please try again!\033[01m')
                                    continue1 = input('Please take your action: ')
                                if continue1 =='1':
                                    floor3room2zombie2 = 0
                                    del item[item.index('neurotoxin')]
                                    print('You lose an item --> neurotoxin')
                                    print('You kill this zombie...You feel relaxed......')
                                    pressure = 0
                                 
                                    continue 
                                if continue1 == '2':
                                    print('Zombies seem to be terrified of the smell\nYou found nothing and left')  
                                    continue                   
                            if 'torch' and 'neurotoxin' and 'a broken knife' not in item:
                                if Michaelbuff == 0:
                                    print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                    hp-=50
                                    character(hp,pressure)
                                    if hp<=0:
                                        break
                                if Michaelbuff == 1:
                                    print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                    hp-=50
                                    if hp<=0:
                                        hp+=50
                                        Michaelbuff = 0
                                        Michaelzombie = 1
                                        print('When you were about to die, Michael showed up and save your life\n But he seemed to be infected...')  
                                        continue1 = input()
                                        character(hp,pressure)
                                        mission.append('Save Michael (optional)(Use one serum)(Michael is in Floor1 Room4')
                                        missions(mission)
                        if pressure<80:
                            print("Your stress level isn't enough to wake them up, you're lucky")
                    if floor3room2zombie2 == 0:
                        print("There's a dead zombie on the ground, and there's nothing left")
                
                elif action == '3':
                    break
            
            while floor3room == '3':
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 3, Room {floor3room}\033[0m')
                action = action_in_room()

                if action == '1':
                    print('\033[1mYou saw a zombie tied to a hospital bed and it looked painful')
                    print('\033[1m------------------------------------------------------')
                    print('Do you want to save this guy?')
                    print('1. Yes(lose a serum)')
                    print('\033[91m\033[1m2. No\033[0m')
                    continue1 = input('Please take your action: ')
                    while continue1 not in yesnoaction:
                        print('\033[91m\033[1mInvalid move , Please try again!\033[0m')
                        continue1 = input('Please take your action: ')
                    if continue1 == '1':
                        if 'serum' not in item:
                            print('You do not have any serum in your item list')

                        if 'serum' in item:
                            del item[item.index('serum')]
                            print('You lose a item---> serum')
                            achievement.append('Love and righteousness(Saved a stranger from being infected)')
                
                elif action == '2':
                    if floor3room3nothing == 0 :
                        print('You got nothing')
                        print("\033[91m\033[1mYou heard zombie's noise")
                        print('You feel nervous\033[0m')
                        pressure+=20
                        character(hp,pressure)
                        if pressure>=100:
                            print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                            days+=1
                            break     
                    if floor3room3nothing >0 :
                        print('You got nothing')
                    floor3room3nothing+=1             
                
                elif action == '3':
                    break
            
            while floor3room == '4':
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 3, Room {floor3room}\033[0m')

                action = action_in_room()
                if action == '1':
                    if floor3room4daughter == 0:
                        print('\033[91m\033[1mStranger:$%^&*($%^&*.......\033[0m')
                        time.sleep(1)
                        print('\033[1mYou: Who is there!\033[0m')
                        time.sleep(1)
                        print('\033[91m\033[1m(No one reply)\033[0m')
                        time.sleep(2)
                        print('When you get closer, you see a little girl lying on the ground, twitching a little, it looks like she needs a sedative......')
                        print('\033[1m------------------------------------------------------')
                        print('\033[1mDo you want to save this girl?')
                        print('1. Yes(lose a sedative)')
                        print('\033[91m\033[1m2. No\033[0m')
                        continue1 = input('Please take your action: ')
                        while continue1 not in yesnoaction:
                            print('\033[91m\033[1mInvalid move , Please try again!\033[0m')
                            continue1 = input('Please take your action: ')
                        if continue1 == '1':
                            if 'sedative' not in item:
                                print('You do not have any sedative in your item list!')

                            if 'sedative' in item:
                                Michael_daughter_art()
                                floor3room4daughterrecorver = 1
                                del item[item.index('sedative')]
                                print('You lose a item---> sedative')    
                        if continue1 == '2':
                            print("Seems that you lose something......")  
                        if floor3room4daughterrecorver == 1 and Michaelzombie == 0:
                            print('\033[1mGirl :who are you? Are you not a zombie? ? So have you seen my father?\nYou:Michael?')
                            print('Girl:Yes!!!\033[0m')
                            print('(After a while, you called michael over, the father and daughter finally reunited)......') 
                        if floor3room4daughterrecorver == 1:
                            print('To thank you, I will tell you the clues I found in this room......')
                            cluesfound.append('Four legs in the morning, two in the afternoon, and three in the evening(important!)')
                            clues(cluesfound)
             
                elif action == '2':
                    if enter_floor3_room4_times == 0:
                        availablefloor.append('4')
                        print('It seems that you can go to floor 4 now...')
                        mission.append('Explore all rooms on floor4 ,and finally get the password of roof gate')
                        print('Please check your mission')
                        missions(mission)
                        enter_floor3_room4_times += 1
                    if floor3room4medkit == 0:
                        print('\033[37mYou got a Medical kit!\033[0m')
                        print('---Please check your item---')
                        item.append('medkit')
                    if floor3room4medkit > 0 :
                        print('You got nothing!')
                    floor3room4medkit += 1
                
                elif action == '3':
                    break
            if pressure>=100:
                pressure = 0
                break  
def floor_4():
    global Michaelbuff
    global Michaelzombie
    global hp   
    global pressure
    global days
    global floor4room1medkit
    global floor4room1zombie
    global floor4room2nero
    global floor4room2key
    global floor4room3nero
    global floor4room3zombie
    global floor4room4serum
    global floor4room4final 

    print('\033[1m------------------------------------------------------')
    print('\033[33m\033[1m' +'You are now on floor 4'   +   '\033[0m')


    while True:

        if check_HP() == False:
            break
        menu_choice = game_menu()
     
        if menu_choice == '2':
            break

        elif menu_choice == '3':
            hp = 100
            pressure = 0
            days+=1
            break

        elif menu_choice == '1':

            print()
            print('\033[96m\033[1m(Available room: 1, 2, 3, 4)\033[0m')
            

            floor4room = input('\033[96m'    +   'Which room you want to go: '  +   '\033[0m')
            while floor4room not in availableroom:
                print('\033[31m\033[1m' +   'Invalid move, please try again!'   +   '\033[0m')
                floor4room = input('\033[96m'    +   'Which room you want to go: '  +   '\033[0m')

            print('You try to open the door of this room\nbut the wind blowing in front of you is making you feel nervous')
            print('\033[91m\033[1mRemark: When you try to enter a room, your pressure rate will increase by 5%\033[0m')
            pressure+=5
            character(hp,pressure)
            if pressure>=100:
                print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m')
                days+=1
                break
            while floor4room == '1':
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 4, Room {floor4room}\033[0m')

                action = action_in_room()
                
                if action == '1':
                    if floor4room1medkit == 0:
                        print('\033[37mYou got a Medical kit!\033[0m')
                        print('---Please check your item---')
                        item.append('medkit')
                    if floor4room1medkit > 0 :
                        print('You got nothing!')
                    floor4room1medkit += 1
                
                elif action == '2':
                    if floor4room1zombie == 1:
                        print('\033[91m\033[1mYou found a sleeping zombie!\033[0m')
                        if pressure>=80:
                            print('\033[91m\033[1mYou woke up this zombie!!!\033[0m')
                            if 'a broken knife' in item and 'neurotoxin' not in item:
                                del item[item.index('a broken knife')]
                                print('You took up the broken knife and temporarily drove the zombies away\nBut the zombies might wake up later\You quickly fled the scene...')
                                print('You lose an item --> a broken knife')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}')
                                
                                continue
                            if 'torch' in item and 'neurotoxin' not in item:
                                print('You hurriedly threw the torch out\nAttracting the attention of the zombies, and you fled in the chaos')
                                
                                del item[item.index('torch')]
                                print('You lose an item --> torch')
                                print('---Please check your item---')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}') 
                                
                                continue  
                            if 'neurotoxin' in item:
                                print('\033[1mDo you want to kill this zombie?')
                                print('1. Yes')
                                print('\033[91m\033[1m2. No\033[0m')
                                continue1 = input('Please take your action: ')
                                while continue1 not in yesnoaction:
                                    print('\033[91m\033[1mInvalid action, Please try again!\033[0m')
                                    continue1 = input('Please take your action: ')
                                if continue1 =='1':
                                    floor4room1zombie = 0
                                    del item[item.index('neurotoxin')]
                                    print('You lose an item --> neurotoxin')
                                    print('You kill this zombie...You feel relaxed......')
                                    pressure = 0
                                     
                                    continue 
                                if continue1 == '2':
                                    print('Zombies seem to be terrified of the smell\nYou found nothing and left')  
                                    continue                   
                            if 'torch' and 'neurotoxin' and 'a broken knife' not in item:
                                if Michaelbuff == 0:
                                    print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                    hp-=50
                                    character(hp,pressure)
                                    if hp<=0:
                                        break
                                if Michaelbuff == 1:
                                    print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                    hp-=50
                                    if hp<=0:
                                        hp+=50
                                        Michaelbuff = 0
                                        Michaelzombie = 1
                                        print('When you were about to die, Michael showed up and save your life\n But he seemed to be infected...')  
                                        
                                        character(hp,pressure)
                                        mission.append('Save Michael (optional)(Use one serum)(Michael is in Floor1 Room4')
                                        missions(mission)
                        if pressure<80:
                            print("Your stress level isn't enough to wake them up, you're lucky")
                            if 'neurotoxin' in item:
                                print('\033[1mDo you want to kill this zombie?')
                                print('1. Yes')
                                print('\033[91m\033[1m2. No\033[0m')
                                continue1 = input('Please take your action: ')
                                while continue1 not in yesnoaction:
                                    print('\033[91m\033[1mInvalid action, Please try again!\033[0m')
                                    continue1 = input('Please take your action: ')
                                if continue1 =='1':
                                    floor4room1zombie = 0
                                    del item[item.index('neurotoxin')]
                                    print('You lose an item --> neurotoxin')
                                    print('You kill this zombie...You feel relaxed......')
                                    pressure = 0
                                    
                                    continue 
                                if continue1 == '2':
                                    print('Zombies seem to be terrified of the smell\nYou found nothing and left')  
                                    continue   
                    if floor4room1zombie == 0:
                        print("There's a dead zombie on the ground, and there's nothing left")
                
                elif action == '3':
                    break
            
            while floor4room == '2':
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 4, Room {floor4room}\033[0m')

                action = action_in_room()
                if action == '1':
                    if floor4room2nero == 0:
                        print('\033[37mYou got neurotoxin*3!!!(You can kill the zombies)\033[0m')
                        item.append('neurotoxin')
                        item.append('neurotoxin')
                        item.append('neurotoxin')
                        print('---Please check your item---')
                        
                    if floor4room2nero > 0:
                        print('You got nothing!')
                    floor4room2nero+=1
                
                elif action == '2':
                    if floor4room2key == 0:
                        print('\033[37mYou received a special key!\033[0m')
                        item.append('special key')
                        print('---Please check your item---')
                    if floor4room2key >0:
                        print('You got nothing!')
                    floor4room2key +=1    
                
                elif action == '3':
                    break
            
            while floor4room == '3':
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 4, Room {floor4room}\033[0m')

                action = action_in_room()
                
                if action == '1':
                    if floor4room3nero == 0:
                        print('\033[37mYou got neurotoxin*1!!!(You can kill the zombie)\033[0m')
                        item.append('neurotoxin')
                        print('---Please check your item---')
                        
                    if floor4room3nero > 0:
                        print('You got nothing!')
                    floor4room3nero+=1                
                
                elif action == '2':
                    if floor4room3zombie == 1:
                        print('\033[91m\033[1mYou found a sleeping zombie!\033[0m')
                        if pressure>=80:
                            print('You woke up this zombie!!!')
                            if 'a broken knife' in item and 'neurotoxin' not in item:
                                del item[item.index('a broken knife')]
                                print('You took up the broken knife and temporarily drove the zombies away\nBut the zombies might wake up later\You quickly fled the scene...')
                                print('You lose an item --> a broken knife')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}')
                                 
                                continue
                            if 'torch' in item and 'neurotoxin' not in item:
                                print('You hurriedly threw the torch out\nAttracting the attention of the zombies, and you fled in the chaos')
                                
                                del item[item.index('torch')]
                                print('You lose an item --> torch')
                                print('---Please check your item---')
                                for i in range(1,len(item)+1):
                                    print(f'{i}. {item[i-1]}') 
                                
                                continue  
                            if 'neurotoxin' in item:
                                print('\033[1mDo you want to kill this zombie?')
                                print('1. Yes\033[0m')
                                print('\033[91m\033[1m2. No\033[0m')
                                continue1 = input('Please take your action: ')
                                while continue1 not in yesnoaction:
                                    print('\033[91m\033[1mInvalid action, Please try again!\033[0m')
                                    continue1 = input('Please take your action: ')
                                if continue1 =='1':
                                    floor4room3zombie = 0
                                    del item[item.index('neurotoxin')]
                                    print('You lose an item --> neurotoxin')
                                    print('You kill this zombie...You feel relaxed......')
                                    pressure = 0
                                    
                                    continue 
                                if continue1 == '2':
                                    print('Zombies seem to be terrified of the smell\nYou found nothing and left')  
                                    continue                   
                            if 'torch' and 'neurotoxin' and 'a broken knife' not in item:
                                if Michaelbuff == 0:
                                    print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                    hp-=50
                                    character(hp,pressure)
                                    if hp<=0:
                                        break
                                if Michaelbuff == 1:
                                    print('\033[91m\033[1mYou have suffered a serious attack!\033[0m')
                                    hp-=50
                                    if hp<=0:
                                        hp+=50
                                        Michaelbuff = 0
                                        Michaelzombie = 1
                                        print('\033[33mWhen you were about to die, Michael showed up and save your life\n But he seemed to be infected...\033[0m')  
                                        
                                        character(hp,pressure)
                                        mission.append('Save Michael (optional)(Use one serum)(Michael is in Floor1 Room4')
                                        missions(mission)
                        if pressure<80:
                            print("Your stress level isn't enough to wake them up, you're lucky")
                            if 'neurotoxin' in item:
                                print('\033[1mDo you want to kill this zombie?')
                                print('1. Yes\033[0m')
                                print('\033[91m\033[1m2. No\033[0m')
                                continue1 = input('Please take your action: ')
                                while continue1 not in yesnoaction:
                                    print('\033[91m\033[1mInvalid action, Please try again!\033[0m')
                                    continue1 = input('Please take your action: ')
                                if continue1 =='1':
                                    floor4room3zombie = 0
                                    del item[item.index('neurotoxin')]
                                    print('You lose an item --> neurotoxin')
                                    print('You kill this zombie...You feel relaxed......')
                                    pressure = 0
                                    
                                    continue 
                                if continue1 == '2':
                                    print('Zombies seem to be terrified of the smell\nYou found nothing and left')  
                                    continue   
                    if floor4room3zombie == 0:
                        print("There's a dead zombie on the ground, and there's nothing left")
                
                elif action == '3':
                    break
            while floor4room == '4':
                time.sleep(2)
                print('\033[1m------------------------------------------------------')
                print(f'\033[33mYou are now on floor 4, Room {floor4room}\033[0m')

                action = action_in_room()
                
                if 'special key' in item:
                    print('You are unlocking the door......')
                else:
                    print('It seems that you need a key to unlock the door...')
                    break

                if action == '1':
                    if floor4room4serum == 0:
                        print('\033[37mYou find serum*2\033[0m')
                        print('You feel really relaxed right now!!!')
                        pressure = 0
                        character(hp,pressure)
                        print('Please check your clues,missions,maybe someone is waiting for your help......')
                        item.append('serum')
                        item.append('serum')
                        print('You can use serum in your item list')
                    if floor4room4serum > 0:
                        print('You got nothing!!!')
                    floor4room4serum +=1
                
                elif action == '2':
                    if floor4room4final == 0:
                        print('\033[37mYou got a sedative!\033[0m')
                        print('---Please check your item---')
                        item.append('sedative')
                        
                        print("You also found a script write a huge number '2'")
                        cluesfound.append('A huge number 2 in Floor 4 Room 4')
                        print("You got all clues in this game , please unlock the roof door password, and don't forget to use the serum")
                    if floor4room4final > 0:
                        print('You got nothing!')
                        print("You got all clues in this game , please unlock the roof door password, and don't forget to use the serum")
                    floor4room4final += 1
                
                if action == '3':
                    break
            if pressure>=100:
                pressure = 0
                break  
def floor_5():
    global pressure
    global serum
    global win 
    global hp
    global days
    print('\033[1m------------------------------------------------------')
    print('\033[33m\033[1m' +'You are now on rooftop'   +   '\033[0m')


    while True:
        print('\033[33mYou are entering the password of combination lock......\033[0m')
        password = input('Enter your password: ')
        if password == '423':
            if serum == 1:
                win = 1
                break
            elif serum == 0:
                print('\033[91m\033[1mYou do not have any serum!!!')
                print('\033[91m\033[1mGo and Find it to get the hell out of here!!\033[0m ')
                break
        else:
            print('\033[91m\033[1mEnter a wrong password. You feel nervous right now......\033[0m')
            print('\033[91m\033[1mYou have to find a password for the rooftop door in order to get the hell out of here!!!!\033[0m')
            pressure+=20
            character(hp,pressure)
            if pressure>=100:
                print('\033[91m\033[1mYour spirits start to trance\nYou have to go sleep......(Only reset pressure)\033[0m') 
                pressure = 0                
                days+=1           
                break  
            break
#main-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
os.system('clear')
opening()
target()
gamerule()
character(hp,pressure)
time.sleep(1)
print('\033[31m' +   '\033[1m'   +   'The game is started. GOD BlESS YOU, survivor!')
time.sleep(1)
print('Remark: Checking your items, clues found, missions is really helpful for you.'    +   '\033[0m')
while days<8:
    if check_HP() == False:
        print('\033[91m\033[1mYou Loss\033[0m')
        break
    print('\033[1m------------------------------------------------------')
    print('Day',days)
    print('\033[1m------------------------------------------------------')
    availablefloor = sorted(availablefloor) 
    print('Available Floor',availablefloor)
    floor = input('Which floor do you want to explore: ')
    while floor not in availablefloor:
        print('\033[91m\033[1mInvalid move, please try again!\033[0m')
        floor = input('Which floor do you want to explore: ')
    while floor == '1':
        floor_1()
        break
    while floor == '2':
        floor_2()
        break
    while floor == '3':
        floor_3()
        break
    while floor == '4':
        floor_4()
        break
    while floor == 'rooftop':
        floor_5()
        break
    if win == 1:
        break


if win == 1:
    print('\033[33m\033[1mYou finally got the serum to save yourself\nand soon after you left, the hospital was overrun by zombies\nYou were lucky, but you also knew that the real challenge lay ahead........\033[0m')
    print('\033[1m------------------------------------------------------end------------------------------------------------------')
elif win == 0 and serum == 1:
    print('\033[91m\033[1mYou are unfortunate, although you received the serum treatment\nbut you still died under the apocalypse, You are all alone in this life........\033[0m')
    print('\033[1m------------------------------------------------------end------------------------------------------------------')
elif win == 0 and serum == 0:
    print('\033[91m\033[1mYou lost everything.\nLife, and hope of living. Someone is waiting for you ,but you lived up to their expectations.........\033[0m')
    print('\033[1m------------------------------------------------------end------------------------------------------------------')
if floor3room4daughterrecorver == 0 and win == 1:
    achievement.append('Groping in the dark')
print('-------------You get following achievement--------------')
if len(achievement) == 0:
    print('You do not have any achievement.')
for i in range(1,len(achievement)-1):
    print(f'{i}: {achievement[i-1]}')
