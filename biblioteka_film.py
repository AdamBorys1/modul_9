class Film:
    def __init__(self, title, year, genre, number_of_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.number_of_plays = number_of_plays

    def play(self):
        self.number_of_plays += 1

    def __str__(self):
        print(f"{self.title} ({self.year})")


class Series:
    def __init__(self, title, year, genre, episode, season, number_of_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.episode = episode
        self.season = season
        self.number_of_plays = number_of_plays

    def play(self):
        self.number_of_plays += 1

    def __str__(self):
        print(f"{self.title} S{self.season}E{self.episode}")

simpsons = Series(title="The Simpsons", year="1978", genre="Comedy", episode="03", season="02", number_of_plays=320)
pulp_fiction = Film(title="Pulp Fiction", year="1994", genre="Crime", number_of_plays=472)

game_of_thrones = Series(title="Game Of Thrones", year="2010", genre="Fantasy", episode="07", season="05", number_of_plays=750)
inception = Film(title="Inception", year="2016", genre="Sci-fi", number_of_plays=2517)

list = [simpsons, pulp_fiction, game_of_thrones, inception]

def get_movies():
    for i in list:                                  # pokombinowac inaczej
        if type(i) == "<class '__main__.Series'>":
            print(f"Serial : {i}")
        

get_movies()

