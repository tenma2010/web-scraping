import requests
from bs4 import BeautifulSoup
import os

def scrape_g1_news():
    """
    Coleta as manchetes das notícias mais recentes do site G1.
    Retorna uma lista de dicionários, onde cada dicionário contém
    'titulo' e 'link' da notícia.
    """
    url = "https://g1.globo.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    news_data = []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('div', class_='feed-post-body')

        for headline in headlines:
            title_tag = headline.find('a', class_='feed-post-link')
            if title_tag and 'href' in title_tag.attrs:
                title = title_tag.get_text(strip=True)
                link = title_tag['href']
                news_data.append({'titulo': title, 'link': link})
            else:
                title_tag = headline.find('div', class_='feed-post-header-text')
                if title_tag:
                    title = title_tag.get_text(strip=True)
                    link_tag = headline.find('a', class_='feed-post-link')
                    link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else 'N/A'
                    news_data.append({'titulo': title, 'link': link})


    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    return news_data

def save_to_file(data, filename="g1_news.txt"):
    """
    Salva os dados coletados em um arquivo de texto.
    """

    file_path = filename

    with open(file_path, "w", encoding="utf-8") as f:
        if data:
            f.write("Manchetes das Notícias do G1:\n\n")
            for i, news in enumerate(data):
                f.write(f"Notícia {i+1}:\n")
                f.write(f"  Título: {news.get('titulo', 'N/A')}\n")
                f.write(f"  Link: {news.get('link', 'N/A')}\n\n")
        else:
            f.write("Nenhuma notícia foi encontrada ou coletada.\n")
    print(f"Dados salvos em '{file_path}'")

if __name__ == "__main__":
    print("Iniciando coleta de notícias do G1...")
    collected_news = scrape_g1_news()

    if collected_news:
        print(f"Coletadas {len(collected_news)} notícias.")
        save_to_file(collected_news)
    else:
        print("Nenhuma notícia foi coletada. Verifique a conexão ou a estrutura do site.")