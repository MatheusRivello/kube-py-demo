# kube-py-demo
API em Python executada com Kubernetes

## Como Utilizar
Adicionar no arquivo `/etc/hosts ` a entrada` appgames.demo.com` para o IP do loadbalancer

## Adicionando dados na base de dados através do curl

    curl -X POST http://appgames.demo.com/games -H "Content-Type: application/json" -d '{
      "name": "The Witcher 3",
      "release_date": "2015-05-19",
      "genre": "RPG"
    }'

## Retornando os dados através do curl

    curl http://appgames.demo.com/games

## Próximos Passos
Implementar build automático da imagem da aplicação com GitHub Actions
Utilizar ConfigMap para otimizar o arquivo de configuração do Postgres
Configurar Volumes para garantir persistência dos dados
Criar um CronJob para realizar backups da base de dados