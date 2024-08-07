# Integração da Loja Virtual com o Mercado Pago

## Introdução

O Mercado Pago é uma plataforma de pagamentos que permite que você receba pagamentos de seus clientes de forma simples e segura. Com o Mercado Pago você pode receber pagamentos com cartão de crédito, boleto bancário, transferência bancária, saldo em conta Mercado Pago e outros meios de pagamento.

## Passos para Criação da Aplicação para Testes

* [Criar conta](https://www.mercadopago.com.br/) no Mercado Pago;
* [Entrar na área do desenvolvedor](https://www.mercadopago.com.br/developers/panel/app/) do Mercado Pago;
* [Criar usuários de teste](https://www.mercadopago.com.br/developers/pt/guides/online-payments/checkout-pro/test-integration/), sendo um "Vendedor" e um "Comprador";
* [Logar como vendedor](https://www.mercadopago.com.br) em uma nova janela anônima do navegador;
* [Entrar](https://www.mercadopago.com.br/developers/panel/app) no painel do desenvolvedor e criar uma aplicação;
    * Nome: `Loja Virtual`;
    * Tipo: `Pagamentos Online`;
    * Plataforma de e-commerce: `Não`;
    * Qual produto você vai usar?: `Checkout Pro`;
* Clicar na aplicação para ver os detalhes;
* Criar credenciais de teste e copiar Public Key e Access Token para um arquivo .env;

## Configuração da Aplicação para Efetuar uma Compra de Teste

* [Credenciais de Teste](https://www.mercadopago.com.br/developers/panel/app/7370094917462170/credentials/sandbox)

* [Cartões de Teste](https://www.mercadopago.com.br/developers/panel/app/7370094917462170/test-cards)

* [Usuários de Teste](https://www.mercadopago.com.br/developers/panel/app/7370094917462170/test-users)

* [Criar Preferência](https://www.mercadopago.com.br/developers/pt/reference/preferences/_checkout_preferences/post)