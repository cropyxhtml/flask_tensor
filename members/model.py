import sqlite3

class MemberModel:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
    def create(self):
        query = """
            create table if not exists member(
                userid varchar(10) primary key,
                password varchar(10),
                phone varchar(15),
                regdate date default current_timestamp)
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_many(self):
        data = [
            ('lee','1','010-1234-5678'),
            ('kim','1','010-1234-5678'),
            ('park','1','010-1234-5678')
        ]
        stmt = """
            insert into member(userid,password,phone) values(?,?,?)
        """
        self.conn.executemany(stmt,data)
        self.conn.commit()

    def fetch_one(self):
        cursor = self.conn.execute('select * from member where userid like "lee"')
        row = cursor.fetchone()
        print('검색결과 : {}'.format(row))

    def fetch_all(self):
        cursor = self.conn.execute('select * from member')
        rows = cursor.fetchall()
        count = 0
        for i in rows:
            count +=1
        print('총인원 {0}'.format(count))

    def login(self, userid, password):
        query = '''
            select * from member where userid like ? and password like ?
        '''
        data = [userid,password]
        cursor = self.conn.execute(query,data)
        row =cursor.fetchone()
        print('로그인 회원정보 : {0}'.format(row))
        return row