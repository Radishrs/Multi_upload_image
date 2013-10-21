import sqlite3 as sql3
from datetime import datetime

sql_connect = sql3.connect('urldata.db')
cursor = sql_connect.cursor()


def time_now():
    """Return date and time with mil sec"""
    return datetime.now().strftime("%Y-%m-%d %I:%M:%S %f")


def add_new_module(module_name):
    """"
    Add new table in DB for new site/module.
    """
    cursor.execute("CREATE TABLE IF NOT EXISTS " + module_name
                   + " (id INTEGER PRIMARY KEY, ident INTEGER, "
                    + "big_url TEXT, small_url TEXT, date TEXT, last_update TEXT)")
    try:
        cursor.execute("ALTER TABLE ident ADD '" + module_name + "' INTEGER NOT NULL DEFAULT '0'")
    except sql3.OperationalError:
    #cursor.execute("ALTER TABLE ident ADD '"+module_name+"' INTEGER")
        #print('Column does exists')
        #TODO Some thing here, duplicate column
        pass
    sql_connect.commit()


def create_empty_db(list_of_module_names):
    """
    Use only if DB not exists.
    It's create table for all add module
    and ident db.
    """

    cursor.execute("CREATE TABLE IF NOT EXISTS ident"
                   + " (id INTEGER PRIMARY KEY, url TEXT, date TEXT)")
    for module in list_of_module_names:
        add_new_module(module)
    print(list_of_module_names)#TODO delete this row
    sql_connect.commit()

def add_url(module_name, ident_url_id, big_url, small_url):
    """Add url to table moduleName."""
    date = time_now()
    cursor.execute("INSERT INTO " + module_name +
                   " (ident, big_url, small_url, date, last_update) VALUES ("
                   + ident_url_id + ", '"
                   + big_url + "', '" + small_url + "', '" + date + "', '" + date + "')")
    sql_connect.commit()


def del_url(ident_url_id):
    """Delete url from DB with all similar links"""
    module_list = get_list_of_module()
    for module in module_list:
        cursor.execute("DELETE FROM " + module + " WHERE ident=" + ident_url_id)
    cursor.execute("DELETE FROM ident WHERE id=" + ident_url_id + "")
    print(cursor.fetchall())
    sql_connect.commit()

def update_url(module_name, ident_url_id):
    """
    Update last download file by this url in proramm
    for update time to delete on site.
    Use this when you download file.
    """
    date = time_now()
    cursor.execute("UPDATE " + module_name +
                   " SET last_update='" + date + "' WHERE ident=" + ident_url_id)
    sql_connect.commit()


def get_all():
    """
    Get all rows from all tables.
    Return two param: list of id with user link and dict of module: id, big, small urls.
    For use: from get id from first list then get url from modules by id.
    """
    #TODO
    cursor.execute("SELECT id, url FROM ident")
    ident_result_list = [row for row in cursor.fetchall()]
    print(ident_result_list)
    module_result_list = {}
    for module in get_list_of_module():
        cursor.execute("SELECT ident, big_url, small_url FROM " + module)
        module_result_list[module] = [row for row in cursor.fetchall()]
    return ident_result_list, module_result_list


def get_by_id(ident_url_id):
    """Get all module link by ident id"""
    #cursor.execute("SELECT ")...
    #TODO this function if need


def get_list_of_module():
    """Return all registered module in db, without ident"""
    cursor.execute("SELECT tbl_name FROM sqlite_master WHERE type='table'")
    return [x[0] for x in cursor.fetchall() if x[0] != 'ident']


def get_all_for_upload():
    """
    Get ident link who need to upload and save url.
    """
    upload_list = {}
    modules = get_list_of_module()
    for module in modules:
        cursor.execute("SELECT id,url FROM ident WHERE " + module + "=0")
        upload_list[module] = [x for x in cursor.fetchall()]

    return upload_list


if "__main__" == __name__:
    #create_empty_db([1,2,3])
    #add_new_module('newtable6')
    #for x in range(3):
    #    add_url('table3', str(x), 'pix.ff/big', 'pix.ff/small')
    #update_url('newtable', '2')
    #print('done')
    #print(get_list_of_module())
    #print()
    #del_url('2')
    #up_list = get_all_for_upload()
    #
    #for x in up_list.keys():
    #    print('key:', x, ' -> ', up_list[x])
    #
    def _get_all():
        ident_ls, module_ls = get_all()
        for ident in ident_ls:
            for module in module_ls.keys():
                print(module, module_ls[module][ident[0]-1], end=' ')
            #print(ident[0])
            print()
        #for module in module_ls.keys():
        #    print(module)
        #print(module_ls[module][ident[0]-1])
    _get_all()
    #create_empty_db(['table1', 'table2', 'table3'])
    #cursor.execute("INSERT INTO ident(url, date) VALUES('ff/55', '%s')" % (time_now(),))
    #sql_connect.commit()