function initializeJsonForm() {
    var form = document.querySelector('.json-form');

    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Impede o envio padrão do formulário

            var formData = new FormData(form);
            var jsonData = {};

            formData.forEach(function (value, key) {
                jsonData[key] = value;
            });

            fetch(form.action, {
                method: form.method,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            })
                .then(response => response.json())
                .then(data => {
                    if (data.detail) {
                        handleFormErrors(form, data.detail);
                    }
                    if (data.redirect) {
                        handleRedirectResponse(data.redirect);
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        });
    }
}

function handleFormErrors(form, errors) {
    // Primeiro, remove todas as classes de erro/validação anteriores    
    var fields = form.querySelectorAll('input, select, textarea');
    fields.forEach(field => {
        field.classList.remove('is-valid', 'is-invalid');
        var errorMessage = field.parentNode.querySelector('.error-message');
        if (errorMessage) {
            errorMessage.remove();
        }
    });

    // Crie um mapa de erros para facilitar a verificação
    var errorMap = {};
    errors.forEach(error => {
        if (Array.isArray(error.loc) && error.loc.length > 1) {
            var fieldName = error.loc[1];
            errorMap[fieldName] = error.msg.replace('Value error, ', '');
        }
    });

    // Adicione as classes apropriadas aos campos
    fields.forEach(field => {
        var fieldName = field.name;
        if (errorMap[fieldName]) {
            field.classList.add('is-invalid');
            // Adicione a mensagem de erro
            var errorMessage = document.createElement('div');
            errorMessage.classList.add('error-message');
            errorMessage.innerHTML = errorMap[fieldName];
            field.parentNode.insertBefore(errorMessage, field.nextSibling);
        } else {
            field.classList.add('is-valid');
        }
    });
}

function handleRedirectResponse(redirect) {
    if (redirect.url) {
        window.location.href = redirect.url;
    }
}

// Chama a função de inicialização quando a página é totalmente carregada
window.addEventListener('load', initializeJsonForm);
