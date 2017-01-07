import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                  "Toys are donated and try to find a way out", 
                  "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710", 
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", 
                  "Humans are at war with Avatar creatures", 
                  "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg", 
                  "https://youtu.be/5PSNL1qE6VY")

warcraft = media.Movie("Warcraft", 
                  "Orcs lost their world and now they want to invade a new one", 
                  "http://cdn1-www.comingsoon.net/assets/uploads/gallery/warcraft-1387407720/warcraft_ver8_xlg.jpg", 
                  "https://www.youtube.com/watch?v=65AjY_nRdqE")

ratatoulle = media.Movie("Ratatouille", 
                  "What happens when a rat loves to cook :)", 
                  "http://www.impawards.com/2007/posters/ratatouille.jpg", 
                  "https://www.youtube.com/watch?v=c3sBBRxDAqk")

the_lion_king = media.Movie("The Lion King", 
                  "The story of a young lion called Simba", 
                  "http://www.impawards.com/1994/posters/lion_king_ver1.jpg", 
                  "https://www.youtube.com/watch?v=4sj1MT05lAA")

leon_the_professional = media.Movie("Leon the professional", 
                  "A hitman meets a girl in need", 
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgzMzg4MDkwNF5BMl5BanBnXkFtZTcwODAwNDg3OA@@._V1_UY1200_CR105,0,630,1200_AL_.jpg", 
                  "https://www.youtube.com/watch?v=DcsirofJrlM")

movies = [toy_story, avatar, warcraft, ratatoulle, the_lion_king, leon_the_professional]

fresh_tomatoes.open_movies_page(movies)