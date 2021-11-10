import pymysql

class DbCep:

    def abre_conn(self) -> pymysql.connect:
        configDB = {'host': 'localhost',
                    'user': 'root',
                    'nameDB': 'processo_seletivo',
                    'senha': ''}

        conn = pymysql.connect(
                                host=configDB['host'],
                                user=configDB['user'],
                                password=configDB['senha'],
                                database=configDB['nameDB'],
                                cursorclass=pymysql.cursors.DictCursor
        )
        return conn

    def query_all_cep(self):
        conn = self.abre_conn()

        with conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM cep"
                cursor.execute(sql)
                result = cursor.fetchall()
                conn.commit()
                
        return result

    def query_unique_cep(self, cep):
        conn = self.abre_conn()

        with conn:
            with conn.cursor() as cursor:
                sql = f"SELECT * FROM cep WHERE cep = {cep}"
                cursor.execute(sql)
                result = cursor.fetchone()
                conn.commit()

        return result

    def insert_cep(self, data_cep):
        conn = self.abre_conn()
        try:
            with conn:
                with conn.cursor() as cursor:   
                    sql = "INSERT INTO `cep` (`cep`,`logradouro`,`bairro`,`localidade`,`uf`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (data_cep['cep'], data_cep['logradouro'], data_cep['bairro'], data_cep['localidade'], data_cep['uf'],))
                    conn.commit()
                    return 'Inserção de CEP feita com sucesso'
        except Exception as e:
            return 'Inserção de CEP feita, mas falhou!'