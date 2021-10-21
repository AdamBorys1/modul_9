import random

class Film:
    def __init__(self, title, year, genre, number_of_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.number_of_plays = number_of_plays

    def play(self):
        self.number_of_plays += 1

    def __str__(self):
        return f"{self.title} ({self.year})"

    __repr__ = __str__


class Series(Film):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"

    __repr__ = __str__ # wyświetlanie w princie tego co jest w str

simpsons = Series(title="The Simpsons", year="1978", genre="Comedy", episode="03", season="02", number_of_plays=320)
pulp_fiction = Film(title="Pulp Fiction", year="1994", genre="Crime", number_of_plays=472)

game_of_thrones = Series(title="Game Of Thrones", year="2010", genre="Fantasy", episode="07", season="05", number_of_plays=750)
inception = Film(title="Inception", year="2016", genre="Sci-fi", number_of_plays=2517)

list = [simpsons, pulp_fiction, game_of_thrones, inception] 

films = []
series = []

"""for x in list:
    print(x)
    print(isinstance(x, Film)) # sprawdza czy x jest Film"""

def get_movies():
    for x in list:
        if isinstance(x, Film) == True:
            films.append(x.title)
    sorted_films = sorted(films, key=lambda x: x)
    print(sorted_films)
            
        
def get_series():
    for x in list:
        if isinstance(x, Series) == True:
            series.append(x.title)
    sorted_series = sorted(series, key=lambda x: x)
    print(sorted_series)

def search(title_of_video):
    for i in list:
        if i.title == title_of_video:
            print(title_of_video)

number_list = []
for z in range(1, 101):
    number_list.append(z)


def generate_views():
    object = random.choice(list)
    object.number_of_plays += int(random.choice(number_list))
    print(object.title, object.number_of_plays)
    
def generate_views_10():
    for w in range(1,11):
        generate_views()
    

def top_titles(number):
    for x in list:
        sorted_number_of_plays = sorted(list, key=lambda x:x.number_of_plays, reverse=True)
    print(sorted_number_of_plays[0:int(number)])

