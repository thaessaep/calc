import connectToBase


def dropList():
    con = connectToBase.connect()
    cur = con.cursor()
    cur.execute(
        "SELECT client_name FROM filepath"
    )
    result = cur.fetchall()
    con.commit()
    con.close()
    return result
