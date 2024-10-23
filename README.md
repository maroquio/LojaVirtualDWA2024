# Loja Virtual

(22 de outubro de 2024)

Loja virtual desenvolvida durante a disciplina de Desenvolvimento Web Avançado no Ifes Cachoeiro.

## Como Usar Este Projeto

Para usar este projeto e modificá-lo em sua máquina, siga os passos abaixo:

1. Faça um fork deste repositório para a sua conta do GitHu;
2. Clone o repositório para a sua máquina;
3. Abra o Visual Studio Code e abra a pasta do projeto;
4. Digite o comando a seguir para configurar o repositório remoto para o seu fork:

```bash
git remote add origin https://usuariogit@github.com/usuariogit/LojaVirtualDWA2024.git
git remote set-url origin
git branch -M main
```

5. Configure o GitHub para fazer o push e pull sem solicitar a senha. Veja a seção Configuração para GitHub a seguir.

## Configuração do GitHub

Para configurar o Visual Studio Code para fazer o push e pull sem solicitar a senha do GitHub, é necessário gerar uma chave SSH no sistema operacional e adicionar as configurações no arquivo .git/config do repositório. O comando para gerar uma chave SSH é o seguinte:

```bash
ssh-keygen -t ed25519 -C "emailusuariogit@dominio.com" -f ~/.ssh/github-pessoal
```

O comando acima gera uma chave SSH do tipo ed25519 com o e-mail do usuário do GitHub. O comando pode solicitar onde a chave será salva e a qual é a senha para proteger a chave. Neste caso, a chave será salva na pasta ~/.ssh com o nome github-pessoal. Não é necessário fornecer um *passphrase* se solicitado. Agora você deve copiar o conteúdo do arquivo .pub e adicionar no GitHub em Settings > SSH and GPG keys > New SSH key. Para visualizar o conteúdo do arquivo .pub, execute o comando abaixo:

```bash
cat ~/.ssh/github-pessoal.pub
```

Depois de gerar a chave SSH no sistema operacional e adicionar o conteúdo do arquivo .pub ao GitHub, adicione as configurações no arquivo .git/config do repositório para que o Visual Studio Code possa fazer o push e pull sem solicitar a senha do GitHub. O arquivo .git/config deve ficar parecido com o exemplo abaixo:

```bash
[core]
    repositoryformatversion = 0
    filemode = false
    bare = false
    logallrefupdates = true
    symlinks = false
    ignorecase = true
    sshCommand = ssh -i ~/.ssh/github-pessoal -F /dev/null
[remote "origin"]
    url = https://github.com/SeuUsuarioGit/LojaVirtualDWA2024.git
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
    remote = origin
    merge = refs/heads/main
    vscode-merge-base = origin/main
[user]
    email = emailusuariogit@dominio.com
    name = Fulano de Tal
```

Isso é necessário para que o Visual Studio Code possa fazer o push e pull sem solicitar a senha do GitHub.

## Instalação dos Pacotes

Para instalar os pacotes necessários para o projeto, execute o comando abaixo:

```bash
pip install -r requirements.txt
```

## Execução do Projeto

Para executar o projeto no Visual Studio Code, basta pressionar F5. O Visual Studio Code executará a aplicação localmente na porta 8000. Isso pode ser configurado no arquivo `launch.json` na pasta `.vscode`. Portanto, para acessar a aplicação, basta abrir o navegador e digitar `http://localhost:8000`.

## Criação do Arquivo .env

Para criar o arquivo `.env`, basta copiar o arquivo `.env.example` e renomear para `.env`. O arquivo `.env` deve conter as seguintes variáveis de ambiente:

```bash
ACCESS_TOKEN_MP_TEST=""
PUBLIC_KEY_MP_TEST=""
CLIENT_ID_MP=""
CLIENT_SECRET_MP=""
USER_ID_MP_TEST=""
APPLICATION_ID_MP_TEST=""
CLIENTE_ID_MP_TEST=""
CLIENTE_PW_MP_TEST=""
URL_TEST="http://localhost:8000"
MAILERSEND_TOKEN=""
```

## Configuração do MailerSender

Para configurar o MailerSender, siga as instruções no arquivo [mailersend.md](mailersend.md).

## Configuração do Mercado Pago

Para configurar o Mercado Pago, siga as instruções no arquivo [mercadopago.md](mercadopago.md).

# Extensões Úteis para VSCode

 - Bootstrap 5 Quick Snippets
 - GitLens
 - HTML CSS Support
 - IntelliCode
 - IntelliSense for CSS class names in HTML
 - Jinha
 - Python
 - Reload
 - SQLite Viewer
 - vscode-icons

## Referências

- [How To Work With Multiple Github Accounts on a single Machine](https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3)
- [Git Credential Manager: Multiple Users](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/multiple-users.md)
- [Integração com Mercado Pago](https://github.com/mercadopago/sdk-python)