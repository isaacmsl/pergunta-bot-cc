# Protótipo de Chatbot BCC-UFRN

A ideia é um chatbot no Telegram que possa responder dúvidas sobre o PPC do curso de Ciência da Computação (BCC) na UFRN.

## Ferramentas

- Python 3
- LangChain
- OpenAI

## Estado

- [x] Busca de páginas por similaridade de texto
- [ ] Estruturar/sumarizar conteúdos de páginas
- [ ] Bot Telegram: Hello, world!
- [ ] Bot Telegram processa/responde mensagens dos usuários

## Como rodar

1. Tenha Python 3 instalado
1. Tenha uma chave de API OpenAI
1. Instale os pacotes py necessários: pymupdf, langchain-community, langchain_openai, faiss-gpu (ou faiss-cpu), telebot
1. Vá executando os códigos em `notebook.ipynb`
1. Ou se queres rodar o bot do telegram, cria um falando com o @BotFather
1. Põe o token no `telegram.py`

## Autor

@isaacmsl
