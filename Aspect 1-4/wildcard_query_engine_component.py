# this method will format a given query to support prefix matching
def formatQueries(query):
    queries = []
    parts = query.split('*')
    if len(parts) == 3:
        #case 1: *X
        if parts[0] == '':
            query = parts[0]
        #case 4: X*Y*Z
        else:
            queries.append(parts[2] + "$" + parts[0])
            queries.append(parts[1])
    #case 1: X*
    elif parts[1] == '':
        queries.append(parts[0])
    #case 2:
    elif parts[0] == '':
        queries.append(parts[1] + '$')
    #case 3: X*Y
    elif parts[0] != '' and parts[1] != '':
        queries.append(parts[1] + "$" + parts[0])     

    return queries

# This method will return all the terms where the prefix matches the rotation
def prefixMatch(prefix, permuterm):
    terms = []
    for term in permuterm.keys():
        if term.startswith(prefix):
            terms.append(permuterm[term])
    print(terms)
    return terms

# This method will match the term with the positional index
def termMatch(terms, positionalIndex):
    positions = []
    for term in terms:
        positions.append({term: positionalIndex[term]})
    return positions
    

def query(query, permuterm, positionalIndex):
    terms = []
    queries = formatQueries(query)
    if len(queries) == 1:
        terms = prefixMatch(queries[0], permuterm)
    
    return termMatch(terms, positionalIndex)
