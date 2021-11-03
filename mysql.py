import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='test')
#增
def insert(learno, name, sex, age, learnage):
    cursor = db.cursor()
    sql = "INSERT INTO student (学号, 姓名, 性别, 年龄, 入学年龄) VALUES ('{0}','{1}', '{2}', '{3}', '{4}')".format(learno, name, sex, age, learnage)
    print(sql)
    try:
        db.ping(reconnect=True)
        cursor.execute(sql)
        db.commit()
    except:
        print("error")
        db.rollback()
    db.close()

#查
def find(learno):
    cursor = db.cursor()
    sql = "SELECT * FROM student where 学号='%s'"%(learno)
    try:
        db.ping(reconnect=True)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(cursor.fetchall().count())
        for row in results:
            learno = row[0]
            name = row[1]
            sex = row[2]
            age = row[3]
            learnage = row[4].strftime('%Y-%m-%d')
    except:
        print("Error: unable to fetch data")
    db.close()
    try:
        return [learno, name, sex, age, learnage]
    except:
        return None

def update(name, sex, age, learnage, learno):
    cursor = db.cursor()
    sql = "UPDATE student SET 姓名='%s',性别='%s',年龄='%s',入学年龄='%s'  WHERE 学号 = '%s'" % (name, sex, age, learnage, learno)

    print(sql)
    try:
        db.ping(reconnect=True)
        cursor.execute(sql)
        db.commit()
    except:
        print("error")
        db.rollback()
    db.close()

if __name__=='__main__':
    find("s001")