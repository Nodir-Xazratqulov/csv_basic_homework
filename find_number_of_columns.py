def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    
    f=open(data, mode='r')
    s=f.read()
    list1=[]
    for i in s.split('\n'):
        list1.append(i.split(','))
    
    
    return len(list1[1])
print(find_number_of_columns('data.csv'))

# Read the csv file 