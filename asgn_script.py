import argparse as ap
import csv
import numpy as np
from shape_fn import shape_ratings_rows

# argparse makes it easy to create command line arguments
# create an argument parsing object
argparser = ap.ArgumentParser(description="TODO")

# add arguments to our argparser object   
# don't have to specify that type is "string", default is string
argparser.add_argument("infile")
argparser.add_argument("curr_uid")

# this is a list that contains the arguments
args = argparser.parse_args()
   
  
print "Input file: " + args.infile
print "Current user id: " + args.curr_uid
print "---"
curr_uid = args.curr_uid
# set up an empty list to store our order information
movie_ratings = []

# opening our files with the "with" command ensures that they close automatically
# you don't have to tell python to close the file, the file closes automatically if you use with
# r = read, U = universal
# we have to use the U because the input file is not well formatted, there's a , instead of /n at the 
# end of each row
with open(args.infile, "rU") as infile:
	# set up our reading objects
	reader = csv.reader(infile, "excel")  	## reader object
    
    # read the header information separately
	user_ids = reader.next()
	# strip off the empty leading cell
	user_ids = user_ids[1:]
	
	# read in the rows
	for row in reader:
		movie_ratings.append(row)
 
# create dictionaries to map from user id to column and vice versa
uid2col = dict([(y,x) for (x,y) in enumerate(user_ids)])
col2uid = dict(enumerate(user_ids))

# convert numbers to float, empty space to np.nan
rating_rows, row_labels = shape_ratings_rows(movie_ratings)

# make a numpy arr
arr = np.array(rating_rows)
	
# extract the column corresponding the user id provided as a command line arg	
# we use the condition > 0 to create a mask (i.e. we'll ignore NaN elements) 
this_uid = arr[:, uid2col[curr_uid]]
index_this = this_uid > 0
sums = []

# sum the values where both arrays have elements  
# ex. [nan, 1, 1, nan, 1], [1, nan, 2, nan, 2]
# [nan, nan, 3, nan, 3] => 
# => 6 

for index, uid in enumerate(user_ids): 
	if uid != curr_uid: 
			
		other_uid = arr[:, uid2col[uid]]
		index_other = other_uid > 0						
		index_union = index_this * index_other
		acc = np.add(this_uid[index_union], other_uid[index_union])
		sums.append( (np.sum(acc), index))
		
for row in sums: 
	print("Index: {0}, Sum: {1:.2f}".format(row[1],row[0]))
	