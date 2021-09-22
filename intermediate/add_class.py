class Anime :
    def info (self,d,a,b,c):
        self.name = d
        self.genre = a
        self.popularity = b
        self.rating = c

    def detprint(self):
        print(self.name)
        print(self.genre)
        print(self.popularity)
        print(self.rating)

name = str(input("PLease enter the name: "))
genre = str(input("PLease enter the genre: "))
popularity = int(input("PLease enter the popularity: "))
rating = float(input("PLease enter the rating: "))

Konosuba = Anime.info(name,genre,popularity,rating)
# Kirito = Anime("SAO", "Fantasy", 1, 9.9)


Anime.detprint(Konosuba)
