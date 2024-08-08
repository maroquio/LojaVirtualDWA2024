# Configuração do MailerSend

O MailerSend é um serviço de envio de e-mails. Para configurar o MailerSend, siga os passos abaixo:

1. Acesse o site [MailerSend](https://mailersend.com/) e crie uma conta;
2. Após criar a conta, acesse o painel de controle e, no menu lateral esquerdo, clique em *Integrations*;
3. Em *MailerSend API -> API tokens*, clique em *Manage*;
4. Agora clique no botão *Generate New Token*;
5. No nome do token, digite *Loja Virtual DWA 2024* e clique em *Generate*;
6. Copie o token gerado e adicione no arquivo *.env* do projeto, conforme o exemplo abaixo:

```bash
MAILERSEND_TOKEN=tokencopiado
```

Pronto. Agora seu projeto está configurado para enviar e-mails através do MailerSend.