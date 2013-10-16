I found working in excel frustrating so I switched to python. 

To make this work I had to learn a little numpy. 

I thought that others might be interested in the same approach.  

I've linked to a python script. 

The script does not do the homework. 

Rather, the script performs a useless operation to demonstrate some basic functionality.

The script outline is: 
* read the data into a 2D numpy array  
* extract certain columns from the array  
* create an index to filter out empty entries of the column (i.e. NaN entries)   
* create an accumulator column that sums the ratings if both users rated the movie  
* return the sum of the accumulator    

Here's an example of what happens. 2 columns are extracted from a 
hypothetical 2D array, we aggregrate the columns in an accumulator column, 
and take the sum of the accumlulator column. 

col1 = [4, nan, 2, 2, nan, nan]  
col2 = [5, nan, nan, 4, nan, 3]   
acc  = [9, nan, nan, 6, nan, nan]  
sum of acc = 15  

The purpose of the script is to demonstrate some basic numpy operations of 
reading in data, creating a numpy arr, and creating an index to filter elements.
 
Also, I'm new to numpy so if any numpy experts have suggestions, corrections
are gratefully received. 

to run the script you would navigate to the directory where the script is saved
and call the following command (if for example you were summing 3712)

    $ python asgn_script.py data.csv 3712 

