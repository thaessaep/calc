import connectToBase
from flask import send_file
import zipfile


def dropFile(name):
    con = connectToBase.connect()
    cur = con.cursor()
    cur.execute(
        "SELECT file_path_to_kp, file_path_to_contract FROM filepath WHERE client_name=%(name)s", {'name': name}
    )
    paths = cur.fetchall()
    result = []
    print(paths[0])
    for i in range(0, len(paths[0])):
        if paths[0][i] is not None:
            result.append(paths[0][i])
    print(result)
    con.commit()
    con.close()
    namezip = name+'.zip'
    zfile = zipfile.ZipFile(r'zip/'+namezip, 'w')
    for i in range(0, len(result)):
        zfile.write(result[i])
    zfile.close()
    return send_file('zip/'+namezip, as_attachment=True)
