import fresh_tomatoes
import media

# media is the file name and Movie is the class name. When we run the code
# toy_story = media.Movie(.....) , __init__ function gets called.

toy_story = media.Movie(
    "Toy Story",
    "November 19, 1995 (El Capitan Theatre) & November 22,"
    ' 1995 (United States)',
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=2BlMNH1QTeE")

avatar = media.Movie(
    "Avatar",
    "December 10, 2009 (London premiere) December 17, 2009 (United Kingdom)"
    ' December 18, 2009 (United States)',
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

cars = media.Movie(
    "cars",
    "June 9, 2006",
    "A story of rookie racecar  Lightning Mcqueen",
    "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
    "https://www.youtube.com/watch?v=SbXIj2T-_uk")

frozen = media.Movie(
    "Frozen",
    "November 19, 2013 (El Capitan Theatre) & November 27,"
    ' 2013 (United States)',
    "A story of a princess who has the power to produce or manipulate ice, "
    'frost and snow at will',    
    "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29"
    '_poster.jpg',
    "https://www.youtube.com/watch?v=FLzfXQSPBOg")

school_of_rock = media.Movie(
    "School_of_Rock", "October 3, 2003",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=5afGGGsxvEA")

minions = media.Movie(
    "Minions",
    "June 11, 2015 (London premiere)[2] & July 10, 2015 (United States)[3]",
    "A story of minions",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
    "https://www.youtube.com/watch?v=o8hxFE7RpSg")

movies = [toy_story, avatar, cars, frozen, school_of_rock, minions]
fresh_tomatoes.open_movies_page(movies)
