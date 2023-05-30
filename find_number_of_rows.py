def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    
    f=open(data, mode='r')
    r=f.read()
    list1 = []
    for i in r.split('\n'):
        list1.append(i)
    k=0
    for j in list1:
        k+=1
    return k

print(find_number_of_rows('data.csv'))

# Read the csv file
