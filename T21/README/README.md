watch_next.py

This README provides an overview and instructions for using the code contained in the associated file. The file includes code that reads movie titles and descriptions from a file, calculates the similarity between a specific movie and the others, and recommends the most similar movie. Each section of the code is described below along with an example of how to use it.

Movie Recommendation
The code reads movie titles and descriptions from a file, creates an NLP object for a specific movie, calculates the similarity between that movie and others, and recommends the movie with the highest similarity score.

Usage
To use the movie recommendation code, follow these steps:

Prepare a file named "movies.txt" containing movie titles and descriptions, with each line following the format: "Title: Description".
Load the required spaCy model by executing nlp = spacy.load('en_core_web_md').
Open the "movies.txt" file and read its content into the movies variable.
Split the content into lines using lines = movies.splitlines().
Create an empty dictionary to store movie titles and descriptions using movies_dict = {}.
Parse the lines from the file to extract movie titles and descriptions, and store them in movies_dict using a loop.
Create an NLP object for the movie of interest using planet_hulk = nlp("Movie description"), replacing "Movie description" with the actual description.
Create a new dictionary, movies_similarity, to store movie titles and their similarity scores with the movie of interest.
Iterate over the movie titles and descriptions in movies_dict, create an NLP object for each description, calculate its similarity with planet_hulk, and store the similarity score in movies_similarity.
Find the movie title with the highest similarity score using recommendation = max(movies_similarity, key=lambda k: movies_similarity[k]).
Print the recommended movie using print(f"The film you should watch after Planet Hulk is {recommendation}.").
Example:

python
Copy code
import spacy

nlp = spacy.load('en_core_web_md')

file = open("movies.txt")
movies = file.read()
lines = movies.splitlines()
file.close

movies_dict = {}

for line in lines:
    for index, letter in enumerate(line, start=0):
        if letter != ":":
            continue
        else:
            movies_dict[line[:index-1].strip()] = line[index+1:].strip()
            break

planet_hulk = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

movies_similarity = movies_dict

for movie, description in movies_dict.items():
    description_nlp = nlp(description)
    movies_similarity[movie] = description_nlp.similarity(planet_hulk)

recommendation = max(movies_similarity, key=lambda k: movies_similarity[k])

print(f"The film you should watch after Planet Hulk is {recommendation}.")
Output
The code will recommend a movie that is most similar to the given movie. The recommended movie title will be printed as output.

Output:

csharp
Copy code
The film you should watch after Planet Hulk is [Recommended Movie Title].
Notes
The code requires the spacy library and the en_core_web_md model to be installed.
The movie titles and descriptions should be stored in a file named "movies.txt" with each line in the format
