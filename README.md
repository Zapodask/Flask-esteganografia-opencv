# Lambda flask estenografia opencv

## Setup

1. Configure o arquivo .env

2. Utilize o template.yaml no cloudformation

3. Navegue até a pasta scripts e rode o comando
```
    python update.py
```


## Routes

| Route | Method | Body |
| ------ | ------ | ------ | ------ |
| encrypt/ | POST | image: base64, message |
| decrypt/ | POST | image: base64 |


## License

MIT