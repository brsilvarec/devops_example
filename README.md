# Devops Example

Esse projeto apresenta uma demonstração de como criar um microserviço simples com integração do travis e cloud foundry. Como o processo de integração e delivery continuos são ferramentas importantes do processo de DevOps, nesse repositório mostramos como integrar tais ferramentas. Criaremos um microserviço (REST) que recebe requisições para leitura e escrita de recursos simples (para fins de demonstração) via métodos get/put. Essa API utiliza a biblioteca `flask_restx` que permite a documentação automática da API via `Swaggers`.


![](imgs/API_screen_shot.png)*Microserviço simples. Utilizaremos nessa repositorio o Travis e o Cloud Froundry na nuvem da IBM para implementar o processo de integração contínua.*

## Pré-requisitos

### Contas
1- Conta no Github
https://github.com/

2- Conta no Travis-CI
https://travis-ci.com/

3- Conta no IBM Cloud
https://cloud.ibm.com/

### Ferramentas

1- Github instalado na máquina
https://cli.github.com/manual/installation
https://desktop.github.com/

2- Python 3 e virtual env
https://docs.python.org/3/library/venv.html
https://www.python.org/

3- Ferramentas de linha de comando da IBM Cloud
https://cloud.ibm.com/docs/cli?topic=cli-install-ibmcloud-cli


## Receita para instalação e integração do microsserviço.

Para reprodução desse material, deve-se seguir os seguintes passos.

### 1- Fork do Repositório para seu próprio repositório do GitHub.
Com o seu usuário criado faça um fork do repositório assim como na imagem abaixo.

![](imgs/ForkRepository.png)

### 2- Clone do Repositório

Após a criação do FORK, faça o download do projeto para o seu usuário.

```
git clone https://github.com/<NOME_DO_USUARIO_GITHUB>/devops_example.git
```

No exemplo acima, utilizamos o nome do usuario `<NOME_DO_USUARIO>` para referenciar o endereço do repositório no github. No seu caso, é preciso que você troque essa string para o nome do seu usuário. Por exemplo, se criarmos o usuário `temporary-test-username` o endereço do clone será.

```
git clone https://github.com/temporary-test-username/devops_example.git
```

## 3- Criar o ambiente virtual e instalar as dependencias

Entre na pasta do projeto.
```
cd devops_example/
```

Crie o ambiente virtual
```
virtualenv venv --python=python3
```

Ative o ambiente virtual
```
source venv/bin/activate
```

Instale os requisitos do sistema
```
pip install -r requirements.txt
```

### 4- Execute o sistema na sua máquina local

Execute o seguinte comando para execução local do sistema.

```
python application.py
```

Após isso, o microsserviço poderá ser acessado pelo endereço http://0.0.0.0:8080/
