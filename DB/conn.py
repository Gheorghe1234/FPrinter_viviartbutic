"""
Librariea pentru conexiunea la Baza de date
Library for connection to the Database
"""
import logging
import cx_Oracle as Cxo
import time


logger = logging.getLogger(__name__)


class DB_Method:

    def __init__(self, p_db_name, p_db_pass, p_db_server, p_oracle_home=r"C:\oracle\instantclient_12_2"):
        logger.info(f'p_db_name: [{p_db_name}], p_db_server: [{p_db_server}], p_oracle_home: [{p_oracle_home}]')
        self.v_lib_err = None
        try:
            Cxo.init_oracle_client(lib_dir=p_oracle_home)
        except Cxo.ProgrammingError as err:
            print(f'ProgrammingError: {err}')
            logger.error(err)
        except Cxo.DatabaseError as err:
            print(f'DatabaseError: {err}')
            logger.error(err)
            self.v_lib_err = err

        # time.sleep(1)
        self.conn = Cxo.connect(p_db_name, p_db_pass, p_db_server, encoding="UTF-8")

    def select(self, table, row = '*', p_where = "rowid is not null"):
        """
         - table: Numele tabelului din care selectam datele
         - row: lista cimpurilor care dorim sa le extragem, (cimpurile se delimiteaza prin virgula)
         - p_where: conditia completa pentru afisare
                (Ex: NRDOC > -1,
                NRDOC > -1 and NRDOC < 5)
        Aceasta functie selecteaza datele din tabelul indicat in parametru 'table' cu conditia din cimpul 'p_where'
         - table: The name of the table from which we select the data
         - row: the list of fields that we want to extract, (the fields are delimited by a comma)
         - p_where: full condition for display
                (Ex: NRDOC> -1,
                NRDOC> -1 and NRDOC <5)
        This function selects the data from the table indicated in the parameter 'table' provided the field 'p_where'
        """
        res = []
        cur = self.conn.cursor()
        query = 'SELECT '+row+' FROM ' + table +' where '+ p_where + ' order by rowid'
        print (query)
        cur.execute(query)
        for result in cur:
            res.append(result)
        cur.close()

        return res
        ##################################################################################
    def get_date_product(self, p_sc):
        res = []
        cur = self.conn.cursor()
        query = f"""
SELECT  DENUMIREA,
        NSIZE,
        PRET,
        ID
FROM VMS_MPT_ALL_FP_MULTI
WHERE ID = {p_sc}
"""
        print(query)
        ##################################################################################
        cur.execute(query)
        for result in cur:
            res.append(result)
        cur.close()

        return res

    def get_date_product_mat(self, p_sc):
        res = []
        cur = self.conn.cursor()
        query = f"""SELECT a.* FROM YLIN_VMS_UNIV_KUH a where a.COD = {p_sc}"""
        cur.execute(query)
        for result in cur:
            res.append(result)
        cur.close()

        return res

    def get_check_una(self, p_id):
        res = []
        cur = self.conn.cursor()
        query = f"""select * from TMDB_FP_PYTHON_HIST t where id={p_id}"""
        cur.execute(query)
        for result in cur:
            res.append(result)
        cur.close()

        return res

    def update_fp_res(self, p_id, p_msg, p_is_pos=False):
        res = []
        cur = self.conn.cursor()
        v_msg = str(p_msg).replace('\'', '')
        print(p_id, v_msg, p_is_pos)

        if p_is_pos:
            query = f"""update TMDB_FP_PYTHON_HIST set resp_fp2='{v_msg}' where id={p_id}"""
        else:
            query = f"""update TMDB_FP_PYTHON_HIST set resp_fp='{v_msg}' where id={p_id}"""
        cur.execute(query)
        self.conn.commit()
        cur.close()
