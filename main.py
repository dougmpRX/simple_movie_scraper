import os, csv, requests
from dotenv import load_dotenv
from datetime import datetime
from bs4 import BeautifulSoup
from movie import Movie


load_dotenv()
BASE_URL = os.getenv('BASE_URL')
MOVIES_URL = os.getenv('MOVIES_URL')


def get_movies() -> list:
    response = requests.get(MOVIES_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('div', class_='grid-item')

def parse_movie(movie) -> Movie:
    movie_title = movie.find('div', class_='meta-title').text.strip()
    movie_code = movie.findAll('a')[0].get('href').split('/')[-2]
    release_date = movie.find('div', class_='meta-data').text
    actor_name = movie.find('span', itemprop='name').text

    thumbnail_url = movie.find('img', class_='media-image').get('src')

    movie_url = BASE_URL + movie.find('a', itemprop='url').get('href')
    image_url = movie_url.replace('index.html', 'images/l_l.jpg')

    return Movie(movie_code, movie_title, release_date, movie_url, image_url, thumbnail_url, actor_name)

def generate_list_parsed_movies() -> list:
    parsed_movies = []
    raw_movies = get_movies()

    for movie in raw_movies[1:]:
        parsed_movies.append(parse_movie(movie))

    return parsed_movies
    
def generate_csv() -> None:
    parsed_movies = generate_list_parsed_movies()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    file_name ='movies_' + str(len(parsed_movies)) + '_' + timestamp + '.csv'
    output_folder_path = './output/'

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        
    with open(f'{output_folder_path}{file_name}', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['code', 'title', 'releaseDate', 'movieUrl', 'imageUrl', 'thumbNailUrl', 'actorName'])
        
        for movie in parsed_movies[1:]:
            writer.writerow([movie.movie_code, movie.movie_title, movie.release_date, movie.movie_url, movie.image_url, movie.thumbnail_url, movie.actor_name])


if __name__ == "__main__":
    generate_csv()