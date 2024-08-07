function mascararTelefone(input) {
    var valor = input.value;
    valor = valor.replace(/\D/g, "");
    if (valor.length > 11) valor = valor.substr(0, 11);
    valor = valor.replace(/^(\d{2})(\d)/g, "($1) $2");
    valor = valor.replace(/(\d)(\d{4})$/, "$1-$2");
    input.value = valor;
}

function mascararCPF(input) {
    var valor = input.value;
    valor = valor.replace(/\D/g, "");
    if (valor.length > 11) valor = valor.substr(0, 11);
    valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
    valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
    valor = valor.replace(/(\d{3})(\d{2})$/, "$1-$2");
    input.value = valor;
}

function mascararCNPJ(input) {
    var valor = input.value;
    valor = valor.replace(/\D/g, "");
    if (valor.length > 14) valor = valor.substr(0, 14);
    valor = valor.replace(/^(\d{2})(\d)/, "$1.$2");
    valor = valor.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3");
    valor = valor.replace(/\.(\d{3})(\d)/, ".$1/$2");
    valor = valor.replace(/(\d{4})(\d)/, "$1-$2");
    input.value = valor;
}

function mascararCEP(input) {
    var valor = input.value;
    valor = valor.replace(/\D/g, "");
    if (valor.length > 8) valor = valor.substr(0, 8);
    valor = valor.replace(/(\d{5})(\d)/, "$1-$2");
    input.value = valor;
}

function mascararCartao(input) {
    var valor = input.value;
    valor = valor.replace(/\D/g, "");
    if (valor.length > 16) valor = valor.substr(0, 16);
    valor = valor.replace(/(\d{4})(\d)/, "$1 $2");
    valor = valor.replace(/(\d{4}) (\d{4})(\d)/, "$1 $2 $3");
    valor = valor.replace(/(\d{4}) (\d{4}) (\d{4})(\d)/, "$1 $2 $3 $4");
    input.value = valor;
}

function mascararMesAno(input) {
    var valor = input.value;
    valor = valor.replace(/\D/g, "");
    if (valor.length > 4) valor = valor.substr(0, 4);
    valor = valor.replace(/(\d{2})(\d)/, "$1/$2");
    input.value = valor;
}

function aplicarMascaras() {
    const inputs = document.querySelectorAll('input[data-mask]');
    inputs.forEach(input => {
        const maskType = input.getAttribute('data-mask');
        input.addEventListener('input', () => {
            switch (maskType) {
                case 'telefone':
                    mascararTelefone(input);
                    break;
                case 'cpf':
                    mascararCPF(input);
                    break;
                case 'cnpj':
                    mascararCNPJ(input);
                    break;
                case 'cep':
                    mascararCEP(input);
                    break;
                case 'cartao':
                    mascararCartao(input);
                    break;
                case 'mes_ano':
                    mascararMesAno(input);
                    break;
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', aplicarMascaras);