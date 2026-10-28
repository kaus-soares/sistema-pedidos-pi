async function listarProdutos() {
    try {
        const resposta = await fetch('/api/produtos/');
        const produtos = await resposta.json();
        
        const tabela = document.getElementById('lista-produtos');
        tabela.innerHTML = ''; // Limpa a tabela antes de preencher

        if (produtos.length === 0) {
            tabela.innerHTML = '<tr><td colspan="3" style="text-align:center;">Nenhum produto cadastrado.</td></tr>';
            return;
        }

        produtos.forEach(produto => {
            const novaLinha = tabela.insertRow();
            novaLinha.innerHTML = `
                <td>${produto.nome}</td>
                <td>${produto.preco || '-'}</td>
                <td>${produto.estoque || '-'}</td>
            `;
        });
    } catch (erro) {
        console.error('Erro ao listar:', erro);
    }
}

// Função para cadastrar o produto no banco
async function adicionarProduto() {
    const nome = document.getElementById('nome').value;
    const preco = document.getElementById('preco').value;
    const estoque = document.getElementById('estoque').value;

    if(nome === '' || preco === '' || estoque === '') {
        alert('Por favor, preencha todos os dados do produto!');
        return;
    }

    const dados = {
        nome: nome,
        preco: preco,
        estoque: estoque
    };

    try {
        const resposta = await fetch('/api/produtos/criar/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });

        if (resposta.ok) {
            alert('Produto gravado com sucesso!');
            // Limpa os campos do formulário
            document.getElementById('nome').value = '';
            document.getElementById('preco').value = '';
            document.getElementById('estoque').value = '';
            
            // Recarrega a tabela para mostrar o produto novo
            listarprodutos();
        } else {
            alert('Erro ao gravar produto.');
        }
    } catch (erro) {
        console.error('Erro:', erro);
        alert('Erro ao conectar com o servidor.');
    }
}

// Quando a página carregar, já busca a lista
document.addEventListener('DOMContentLoaded', listarProdutos);