#Projeto de Web Scraping: Coletando Notícias do G1
Este projeto Python demonstra como realizar web scraping para extrair manchetes e links de notícias da página inicial do G1, um dos maiores portais de notícias do Brasil.

#Como Usar
Siga os passos abaixo para configurar e executar o scraper:

Clone o Repositório (ou baixe os arquivos):

Se você estiver em um ambiente Git, pode clonar este repositório:

Bash

git clone <link_do_seu_repositorio>
cd <nome_do_seu_repositorio>
Caso contrário, apenas baixe os arquivos g1_scraper.py e, se existir, o g1_news.txt (que será gerado).

#Instale as Dependências:

Este projeto requer as bibliotecas requests e BeautifulSoup4. Você pode instalá-las usando pip:

Bash

pip install requests beautifulsoup4
Execute o Script:

Navegue até o diretório onde você salvou o arquivo g1_scraper.py e execute-o usando o Python:

Bash

python g1_scraper.py

#O que o Código Faz
O script g1_scraper.py executa as seguintes ações:

Faz uma requisição HTTP para a página inicial do G1 (https://g1.globo.com/) usando a biblioteca requests.

Analisa o conteúdo HTML da página usando BeautifulSoup para encontrar elementos específicos que contêm as manchetes e os links das notícias.

Extrai o título e o link de cada notícia encontrada.

Salva os dados coletados (título e link) em um arquivo de texto chamado g1_news.txt no mesmo diretório do script.

#Saída
Após a execução bem-sucedida do script, um arquivo chamado g1_news.txt será gerado (ou atualizado) no mesmo diretório. Este arquivo conterá uma lista formatada das manchetes e seus respectivos links
