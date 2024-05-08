# Protótipo de Chatbot BCC-UFRN

A ideia é um chatbot no Telegram que possa responder dúvidas sobre o PPC do curso de Ciência da Computação (BCC) na UFRN.

![image](https://github.com/isaacmsl/pergunta-bot-cc/assets/31693006/95820034-ce6d-4fa9-83ca-a9987c23d970)

## Ferramentas

- Python 3
- LangChain
- OpenAI

## Estado

- [x] Busca de páginas por similaridade de texto
- [x] Estruturar/sumarizar conteúdos de páginas
- [x] Bot Telegram: Hello, world!
- [x] Bot Telegram processa/responde mensagens dos usuários
- [ ] Evalutation para qualificar as respostas da IA
- [ ] Deixar no ar (alguém financia, por favor?)

## Como rodar

1. Tenha Python 3 instalado
1. Tenha uma chave de API OpenAI
1. Instale os pacotes py necessários: pymupdf, langchain-community, langchain_openai, faiss-gpu (ou faiss-cpu), telebot
1. Vá executando os códigos em `notebook.ipynb`
1. Ou se queres rodar o bot do telegram, cria um falando com o @BotFather
1. Põe o token no `telegram.py`

## Autor

@isaacmsl
