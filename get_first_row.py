def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   
   f=open(data, mode='r')
   r=f.read()
   list1=[]
   list2=[]
   for i in r.split('\n'):
      list1.append(i.split(','))
#    for k in list1:
#       list2.append(k[-1])
   return list1[0]
print(get_first_row('data.csv'))

# Read the csv file