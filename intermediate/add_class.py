class Anime :
    num_of_ent = 0
    avg_rate = 7.95
    # name = Asuna
    def __init__ (self,d,a,b,c):
        self.name = d
        self.genre = a
        self.popularity = b
        self.rating = c
        Anime.num_of_ent += 1

    def detprint(self):
        print(self.name)
        print(self.genre)
        print(self.popularity)
        print(self.rating)
        print(Anime.num_of_ent)

    print(avg_rate)

    @classmethod
    def change_rate(cls,num):
        cls.avg_rate = num

    print(avg_rate)


name = str(input("PLease enter the name: "))
genre = str(input("PLease enter the genre: "))
popularity = int(input("PLease enter the popularity: "))
rating = float(input("PLease enter the rating: "))

Konosuba = Anime(name,genre,popularity,rating)
# Kirito = Anime("SAO", "Fantasy", 1, 9.9)
# Kirito.change_rate(9.999)

# print(Anime.change_rate("Kirito"))
# print(Anime.detprint(Kirito))

Konosuba.detprint()
# print(Kirito.__dict__)
# print(Anime.__dict__)

