import connectToBase


def createBase(clientName, filePath, fileType):
    con = connectToBase.connect()
    cur = con.cursor()  # create cursor
    # cur.execute(
    #     "DELETE FROM filepath *;"  # delete all record
    #     "ALTER SEQUENCE filepath_id_seq RESTART WITH 1"  # reboot counter id
    # )
    cur.execute(
        "SELECT client_name FROM filepath", {'clientName': clientName}
    )
    name = cur.fetchall()  # take id and client_name
    check = checkTable(name, clientName)
    if check['value'] == 1:
        switchUpdate(cur, fileType, filePath, check)
    else:
        switchInsert(cur, fileType, clientName, filePath)
    con.commit()
    con.close()


def switchUpdate(cur, fileType, filePath, check):
    if fileType == "KP":
        cur.execute(
            "UPDATE filepath SET file_path_to_kp=%(filePathToKP)s WHERE client_name=%(name)s",
            {'filePathToKP': filePath, 'name': check['clientName']}
        )
    else:  # if fileType == "CONT"
        cur.execute(
            "UPDATE filepath SET file_path_to_contract=%(file_path_to_contract)s WHERE client_name=%(name)s",
            {'file_path_to_contract': filePath, 'name': check['clientName']}
        )


def switchInsert(cur, fileType, clientName, filePath):
    #print(INN)
    if fileType == "KP":
        cur.execute(
            "INSERT INTO filepath (client_name, file_path_to_kp) VALUES (%(clientName)s, %(filePathToKP)s)",
            {'clientName': clientName, 'filePathToKP': filePath}
        )
    else:  # if fileType == "CONT"
        cur.execute(
            "INSERT INTO filepath (client_name, file_path_to_contract) "
            "VALUES (%(clientName)s, %(file_path_to_contract)s)",
            {'clientName': clientName, 'file_path_to_contract': filePath}
        )


def checkTable(name, clientName):
    if len(name) == 0:
        return {'value': 0}
    for i in range(0, len(name)):
        if name[i][0] == clientName:  # 1 = column of client_name
            return {'value': 1, 'clientName': name[i][0]}  # second i = column of id
    return {'value': 0}
