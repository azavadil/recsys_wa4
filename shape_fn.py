import numpy as np

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def shape_ratings_rows(movie_ratings): 
	titles = [row[0] for row in movie_ratings]
	temp = [row[1:] for row in movie_ratings]
	
	ratings = []
	for row in temp:
		ratings.append(tuple([float(elem) if is_number(elem) else np.nan for elem in row]))
		
	return ratings, titles
		
	
