import spacy

nlp = spacy.load('en_core_web_md')

file = open("movies.txt")
movies = file.read()
lines = movies.splitlines()
file.close

# Opening a file containing movie titles and descriptions, reading its content, and splitting it into lines

movies_dict = {}

# Creating an empty dictionary to store movie titles and descriptions

for line in lines:
    for index, letter in enumerate(line, start=0):
        if letter != ":":
            continue
        else:
            movies_dict[line[:index-1].strip()] = line[index+1:].strip()
            break

# Parsing the lines from the file to extract movie titles and descriptions
# The movie title is the text before the ":" character, and the description is the text after it
# The extracted title and description are stripped of leading/trailing whitespace and added to the movies_dict dictionary

planet_hulk = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# Creating a spaCy NLP object for the movie "Planet Hulk"
# This object will be used to calculate the similarity between "Planet Hulk" and other movies in the movies_dict

movies_similarity = movies_dict

# Creating a new dictionary to store movie titles and their similarity scores with "Planet Hulk"

for movie, description in movies_dict.items():
    description_nlp = nlp(description)
    movies_similarity[movie] = description_nlp.similarity(planet_hulk)

# Iterating over the movie titles and descriptions in movies_dict
# Creating an NLP object for each description and calculating its similarity with the "Planet Hulk" NLP object
# Storing the similarity score in movies_similarity dictionary with the corresponding movie title as the key

recommendation = max(movies_similarity, key=lambda k: movies_similarity[k])

# Finding the movie title with the highest similarity score in movies_similarity dictionary

print(f"The film you should watch after Planet Hulk is {recommendation}.")
