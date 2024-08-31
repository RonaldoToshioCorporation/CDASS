# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Requisitos:
1)Estar executando o serviço que deve ser consumido na url localhost:5001

2)Os serviços de POST, PUT E DELETE devem receber os parametros no formato FORM-DATA
    2.1) POST e UPDATE 
        id     int64
        title  string  
        artist string
        price  float64

    2.2)Delete 
        id int64   
    2.3)GET 
        2.3.1)albuns -> lista
        2.3.2)album -> querystring parametro
## Ronaldao instruções:

1)Fazer um clone do projeto

2)Acessar a pasta vite-project

3)Executar o comando abaixo entre aspas duplas:
    "docker build -t front-cdass ."

4)Executar o comando abaixo para iniciar a aplicação no docker.
"docker run -p 5173:5173 front-cdass"

5)Executar o link local: http://localhost:5173/

