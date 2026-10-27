// Função para listar os clientes do banco
async function listarClientes() {
    try {
        const resposta = await fetch('/api/clientes/');
        const clientes = await resposta.json();
        
        const tabela = document.getElementById('lista-clientes');
        tabela.innerHTML = ''; // Limpa a tabela antes de preencher

        if (clientes.length === 0) {
            tabela.innerHTML = '<tr><td colspan="3" style="text-align:center;">Nenhum cliente cadastrado.</td></tr>';
            return;
        }

        clientes.forEach(cliente => {
            const novaLinha = tabela.insertRow();
            novaLinha.innerHTML = `
                <td>${cliente.nome}</td>
                <td>${cliente.telefone || '-'}</td>
                <td>${cliente.endereco || '-'}</td>
            `;
        });
    } catch (erro) {
        console.error('Erro ao listar:', erro);
    }
}

// Função para cadastrar o cliente no banco
async function adicionarCliente() {
    const nome = document.getElementById('nome').value;
    const telefone = document.getElementById('telefone').value;
    const endereco = document.getElementById('endereco').value;

    if(nome === '' || telefone === '' || endereco === '') {
        alert('Por favor, preencha todos os dados do cliente!');
        return;
    }

    const dados = {
        nome: nome,
        telefone: telefone,
        endereco: endereco
    };

    try {
        const resposta = await fetch('/api/clientes/criar/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });

        if (resposta.ok) {
            alert('Cliente gravado com sucesso!');
            // Limpa os campos do formulário
            document.getElementById('nome').value = '';
            document.getElementById('telefone').value = '';
            document.getElementById('endereco').value = '';
            
            // Recarrega a tabela para mostrar o cliente novo
            listarClientes();
        } else {
            alert('Erro ao gravar cliente.');
        }
    } catch (erro) {
        console.error('Erro:', erro);
        alert('Erro ao conectar com o servidor.');
    }
}

// Quando a página carregar, já busca a lista
document.addEventListener('DOMContentLoaded', listarClientes);