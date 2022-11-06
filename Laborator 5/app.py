import utils

appInput=input("Dati input ")
while appInput!='q':
    print(utils.process_item(int(appInput)))
    appInput=input("Dati input ")
