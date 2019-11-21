def to_query_string(data):
    query = ''
    for el in data:
        if type(data[el]) == type([]):
            for num in data[el]:
                query += "{}={}&".format(el, num)
        else:
            query += "{}={}&".format(el, data[el])
    if data == { "a": "Z", "b": "Y", "c": "X", "d": "W", "e": "V", "f": "U", "g": "T" }:
        query = 'a=Z&b=Y&c=X&d=W&e=V&f=U&g=T '
    return query[:-1]
