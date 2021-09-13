def max_val(arr):
  max_ml = 0
  for i in ml:
    if i>max_ml:
      max_ml = i
  return(max_ml)
  print("the maximum value in the array is = ", max_ml)
  
def min_val(arr,mx):
  ml = arr
  min_ml = mx
  for j in ml:
    if j<min_ml:
      min_ml = j
  return(min_ml)
  print("the minimum value in the array is = ", min_ml)
  
  
  
def max_profit(arr):
  my_arr = arr
  
  max_stock = max_val(my_arr)
  min_stock = min_val(my_arr,max_stock)
  
  max_index = my_arr.index(max_stock)
  min_index = my_arr.index(min_stock)
  
  if max_index > min_index:
    max_profit = max_stock - min_stock
    print(max_profit)
  elif max_index == 0:
    print(int(-1))
  else:
    new_arr = my_arr[0:max_index]
    max_narr = max_val(new_arr)
    min_narr = min_val(new_arr,max_narr)
    
    max_profit = max_stock - min_narr
    print(max_profit)
    
 
print(max_profit(input()))

  
