def gen_squares(max_root):
    for x in range(max_root):
        yield x**2
        
squares = gen_squares(10)
'''
Standard q

for sq in squares:
    print (sq) 
    
 Extra Credit:  
'''    
for sq in squares:
    print (next(squares))