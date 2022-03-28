"""
    [Api inmuebles]
"""
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#connection

app.config['MYSQL_HOST'] = '3.130.126.210'
app.config['MYSQL_PORT'] = 3309
app.config['MYSQL_USER'] = 'pruebas'
app.config['MYSQL_PASSWORD'] = 'VGbt3Day5R'
app.config['MYSQL_DB'] = 'habi_db'
mysql = MySQL(app)

query = """
    SELECT
        p.id,
        p.address,
        p.city,
        s.name as state,
        p.price,
        p.description,
        p.year
    FROM
        property p
    left join
        (select
        MAX(id) as id,
        property_id,
        status_id
        FROM
            status_history
        group by
            property_id
        ) as sh on
        sh.property_id = p.id
    INNER join status s on
        sh.status_id = s.id
    WHERE
	(s.name = 'pre_venta'
		or s.name = 'en_venta'
		or s.name = 'vendido'
		) AND (address != '' and city !='')
    ORDER BY p.id;
"""

key_list = ['id','address', 'city', 'state', 'price', 'description', 'year', 'update_date']
list_to_dict = []

def get_data():
    list_to_dict = []
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    for row in data:
        dict_row = {}
        for i in range(len(row)):
            dict_row[key_list[i]] = row[i]
        list_to_dict.append(dict_row)
    return fix_errors(list_to_dict)

def filter_data(args):
    year = ''
    city = ''
    state = ''
    if args.get('city'):
        city = args.get('city')
    if args.get('state'):
        state = args.get('state')
    while True:
        try:
            if args.get('year'):
                year = int(args.get('year'))
                break
        except ValueError:
                year = ''
                break

    if len(list_to_dict) == 0:
        data = get_data()
    else:
        data =  list_to_dict

    datafilter = []

    for row in data:
        if (row['year'] == year or year == '') and (row['city'] == city or city == '') and (row['state'] == state or state == ''):
            datafilter.append(row)
    return datafilter

def fix_errors(data):
    for row in data:
        if row['address'] == None:
            row['address'] = 'address_default'
        if row['city'] == None:
            row['city'] = 'city_default'
        if row['price'] == None:
            row['price'] = 0
        if row['description'] == None:
            row['description'] = 'description_default'
        if row['year'] == None:
            row['year'] = 0
    return data


@app.route('/', methods=['GET'])
def Index():
    data = get_data()
    return {'data': data}



#parametros de filtrado por año ciudad y state
@app.route('/filter', methods=['GET'])
def Filter():
    args = request.args

    data = filter_data(args)

    return {
        'filters': args,
        'data': data
    }



if __name__ == '__main__':
    app.run(port = 5000)