function add_carro(){
    container = document.getElementById('form-carro')

    html = "<div class='car-container'><br><div class='row car-row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro' > </div> <div class='col-md'> <input type='text' placeholder='marca' class='form-control' name='marca' > </div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa' ></div> <div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='ano'> </div> <div class='col-md d-flex justify-content-center align-items-center'> <span class='btn-rm-carros' onclick='remove_carro(this)'> excluir carro</span> </div> </div></div>"
    
    container.innerHTML += html
}

function remove_carro(element){
    element.closest('.car-container').remove();
}


function exibir_form(tipo){

    add_cliente = document.getElementById('add-cliente')
    att_cliente = document.getElementById('att-cliente')

    if(tipo == 1){
        att_cliente.style.display = 'none'
        add_cliente.style.display = 'block'
    }else if(tipo == 2){
        add_cliente.style.display = 'none'
        att_cliente.style.display = 'block'
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}   


function add_carro2(cliente_id) {
    var csrftoken = getCookie('csrftoken');
    var div_carros = document.getElementById('carros');
    div_carros.innerHTML += "<form action='/clientes/add_carro/' method='POST'>\
        <input type='hidden' name='csrfmiddlewaretoken' value='" + csrftoken + "'>\
        <input type='hidden' name='cliente_id' value='" + cliente_id + "'>\
        <div class='row'>\
            <div class='col-md'>\
                <input class='form-control' name='carro' type='text' placeholder='Carro'>\
            </div>\
            <div class='col-md'>\
                <input class='form-control' name='marca' type='text' placeholder='Marca'>\
            </div>\
            <div class='col-md'>\
                <input class='form-control' name='placa' type='text' placeholder='Placa'>\
            </div>\
            <div class='col-md'>\
                <input class='form-control' type='text' name='ano' placeholder='Ano'>\
            </div>\
            <div class='col-md'>\
                <input class='btn-salvar' type='submit'>\
            </div>\
        </div><br>"
}




function dados_cliente(){
    cliente = document.getElementById('cliente-select')
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/", {
        method: "POST",
        headers:{
            'X-CSRFToken': csrftoken,
        },
        body: data
    }).then( function (result){
        return result.json()
    }).then(function(data){
        
        document.getElementById('form-att-cliente').style.display = 'block'
        
        id = document.getElementById('id')
        id.value = data['cliente_id']
        
        nome = document.getElementById('nome')
        nome.value = data['cliente']['nome']
        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['cliente']['sobrenome']

        email = document.getElementById('email')
        email.value = data['cliente']['email']

        cpf = document.getElementById('cpf')
        cpf.value = data['cliente']['cpf']

        div_carros = document.getElementById('carros')
        var cliente_id = document.getElementById('cliente-select').value;
        div_carros.innerHTML = "<button class='btn-add-carros' onclick='add_carro2(" + cliente_id + ")'>Adicionar Carro</button>";
        for(i=0; i<data['carros'].length; i++){
            div_carros.innerHTML += "\<form action='/clientes/update_carro/" + data['carros'][i]['id'] +"' method='POST'>\
                <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control' name='carro' type='text' value='" + data['carros'][i]['fields']['carro'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' name='marca' type='text' value='" + data['carros'][i]['fields']['marca'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' name='placa' type='text' value='" + data['carros'][i]['fields']['placa'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='ano' value='" + data['carros'][i]['fields']['ano'] + "' >\
                        </div>\
                        <div class='col-md'>\
                            <input class='btn-salvar' type='submit'>\
                        </form>\
                        <a href='/clientes/excluir_carro/"+ data['carros'][i]['id'] +"' class='btn-excluir'>Delete</a>\
                    </div>\
                </div><br>"
        }

    })

}

function update_cliente(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value

    fetch("/clientes/update_cliente/" + id, {
        method: "POST",
        headers:{
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        if(data['status'] == 200){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterados com sucesso')
        }else{
            console.log('Erro ao alterar dados')
        }

    })

}