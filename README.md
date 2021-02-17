# **Ambiente de Desenvolvimento**
Projeto multicliente para traduçõe do serviço de antecipação que se utilizem dos layouts nexxera.

# Principais Informações do Projeto
- Service: Login System
- Database: MongoDB
- Infra: Docker
- Developer: 
    - Lucas Schmitz dos Santos

- Descripition: 
    - Traduz do layout santander-pagamento-240-v010 para nexxera-compromissos-a-pagar-e-receber-240-v023.
    - Traduz do layout votorantim-pagamento-240-v021 para nexxera-antecipacao-compromissos-a-pagar-e-receber-240-v022.
    - Traduz do layout nexxera-antecipacao-240-v41 para bradesco-antecipacao-massiva-400-v01.
    - Traduz do layout febraban-pagamento-240-v101 para nexxera-antecipacao-compromissos-a-pagar-240-v4.
    - Traduz do layout bradesco-antecipacao-massiva-400-v01 para nexxera-antecipacao-240-v3.
    - Traduz do layout nexxera-compromissos-a-pagar-e-receber-240-v022 para santander-pagamento-v240-v010-retorno.
    - Traduz do layout nexxera-antecipacao-240-v43 para daycoval-pagamento-240-v1501 e quebra o arquivo por segmento 3S.
    - Traduz do layout daycoval-pagamento-240-v1501 para nexxera-antecipacao-240-v3
# Fluxos

## Remessa
```
- principal_lpn_antecipacao.py santander-pagamento-240-v010 nexxera-compromissos-a-pagar-e-receber-240-v023 <entrada> <saida>
- principal_lpn_antecipacao.py votorantim-pagamento-240-v021 nexxera-antecipacao-compromissos-a-pagar-e-receber-240-v022 <entrada> <saida>
- principal_lpn_antecipacao.py bradesco-antecipacao-massiva-inserir-base-csv <entrada>
- principal_lpn_antecipacao.py nexxera-antecipacao-240-v41 bradesco-antecipacao-massiva-400-v01 <entrada> <saida>
- principal_lpn_antecipacao.py bradesco-antecipacao-massiva-expurgar-base <intervalo-dias> ou -1 para limpar toda base
- principal_lpn_antecipacao.py febraban-pagamento-240-v101 nexxera-antecipacao-compromissos-a-pagar-240-v4 <entrada> <saida>
- principal_lpn_antecipacao.py bradesco-antecipacao-massiva-400-v01 nexxera-antecipacao-240-v3 <entrada> <saida>
- principal_lpn_antecipacao.py nexxera-compromissos-a-pagar-e-receber-240-v022 santander-pagamento-v240-v010-retorno <entrada>
- principal_lpn_antecipacao.py nexxera-antecipacao-240-v43 daycoval-pagamento-240-v1501 <entrada> <saida>
- principal_lpn_antecipacao.py daycoval-pagamento-240-v1501 nexxera-antecipacao-240-v3 <entrada> <saida>
```

## Retorno
```
- principal_lpn_antecipacao.py nexxera-antecipacao-240-v31 santander-pagamento-v240-v010-retorno <entrada>
- principal_lpn_antecipacao.py nexxera-compromissos-a-pagar-e-receber-240-v022 santander-pagamento-v240-v010-retorno <entrada>
```
# Ambiente de Desenvolvimento

## Requisitos
- Python 3.6
- VirtualEnv
- Make

## Ambiente Linux
Criar virtualenv dentro do projeto:
```
virtualenv -p /usr/bin/python3.6 .venv
ou
make venv
```

Ativar virtualenv:
```
source .venv/bin/activate
```

## Ambiente Windows
Criar diretório da virtualenv dentro do projeto:
```
mkdir .venv
```

Criar virtualenv:
```
virtualenv.exe .venv
```

Ativar virtualenv:
```
.venv\Scripts\activate
```

# Testes
Efetuar o download do projeto:
```
git@gitlab.nexxera.com:traducao/python/lpn-antecipacao.git
```

Instalar as dependências:
```
make init
```

Efetuar teste na regra de negócio:
```
make test
```

Efetuar teste de cobertura de código:
```
make test-cov
```

Efetuar teste de convenção de código:
```
make code-convention
```

Limpar os dados gerados pelos testes:
```
make clean
```

Executar multiplos passos: clean test test-cov code-convention
```
make new
```

Executar multiplos passos: init new
```
make all
```