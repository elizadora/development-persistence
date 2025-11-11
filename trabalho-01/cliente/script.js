
base_url = "http://127.0.0.1:8000"

const produtosLista = document.getElementById("produtos-lista");
const resultado = document.getElementById("resultado");

async function listarProdutos() {
    try {
        const resposta = await fetch(`${base_url}/produtos`);
        const dados = await resposta.json();
        exibirProdutos(dados);
        return dados;
    } catch (error) {
        console.error("Erro ao buscar produtos:", error);
        return [];
    }
}

// exibe os produtos na tela
function exibirProdutos(produtos) {
    produtosLista.innerHTML = "";

    produtos.forEach(produto => {
        const tr = document.createElement("tr");
        tr.classList.add("border-b");
        tr.innerHTML = `
            <td class="p-4">${produto.nome}</td>
            <td class="p-4">${produto.categoria}</td>
            <td class="p-4">R$ ${produto.preco.toFixed(2)}</td>
            <td>
                <button
                    class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 cursor-pointer"
                    onclick="apagarProduto(${produto.id})">
                    Apagar
                </button>
                <button class="bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600 cursor-pointer" onclick="obterProduto(${produto.id})">Editar</button>
            </td>
        `;
        produtosLista.appendChild(tr);
    }
    );
}

function salvarProduto() {
    if (document.getElementById("produto-id").value != "") {
        atualizarProduto();
    } else {
        adicionarProduto();
    }
}

async function adicionarProduto() {
    const nome = document.getElementById("nome-produto").value;
    const categoria = document.getElementById("categoria-produto").value;
    const preco = parseFloat(document.getElementById("preco-produto").value);

    const novoProduto = {
        nome: nome,
        categoria: categoria,
        preco: preco
    };

    try {
        const resposta = await fetch(`${base_url}/produtos`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(novoProduto)
        });
        if (resposta.ok) {
            alert("Produto adicionado com sucesso!");
            listarProdutos();
        }

        limparFormulario();

    } catch (error) {
        console.error("Erro ao adicionar produto:", error);
    }
}

async function apagarProduto(id) {
    try {
        let confirmacao = confirm("Tem certeza que deseja apagar o produto selecionado?");

        if (!confirmacao) {
            return;
        }

        const resposta = await fetch(`${base_url}/produtos/${id}`, {
            method: "DELETE"
        });


        if (resposta.ok) {
            alert("Produto apagado com sucesso!");
            listarProdutos();
        }

    } catch (error) {
        console.error("Erro ao apagar produto:", error);
    }
}

async function obterProduto(id) {
    try {
        const resposta = await fetch(`${base_url}/produtos/${id}`);
        const produto = await resposta.json();

        document.getElementById("nome-produto").value = produto.nome;
        document.getElementById("categoria-produto").value = produto.categoria;
        parseFloat(document.getElementById("preco-produto").value = produto.preco);
        document.getElementById("produto-id").value = produto.id;

    } catch (error) {
        console.error("Erro ao obter produto:", error);
    }

}

async function atualizarProduto() {
    try {
        const nome = document.getElementById("nome-produto").value;
        const categoria = document.getElementById("categoria-produto").value;
        const preco = parseFloat(document.getElementById("preco-produto").value);
        const id = document.getElementById("produto-id").value;

        produtoAtualizado = {
            nome: nome,
            categoria: categoria,
            preco: preco
        };

        resposta = await fetch(`${base_url}/produtos/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(produtoAtualizado)
        });

        if (resposta.ok) {
            alert("Produto editado com sucesso!");
            listarProdutos();
        }

        limparFormulario();


    } catch (error) {
        console.error("Erro ao editar produto:", error);
    }
}

function limparFormulario() {
    document.getElementById("nome-produto").value = "";
    document.getElementById("categoria-produto").value = "";
    document.getElementById("preco-produto").value = "";
    document.getElementById("produto-id").value = "";
}

async function maiorValor() {
    try {
        resposta = await fetch(`${base_url}/produtos/maior-valor`)
        dados = await resposta.json()
        resultado.innerHTML = `<h2 class="text-xl font-bold mb-4">Produto(s) de maior valor:</h2>`
        dados.forEach(produto => {
            const p = document.createElement("p");
            p.innerText = `Nome: ${produto.nome} - Preço: R$ ${produto.preco.toFixed(2)}`
            resultado.appendChild(p)
        })
    } catch (error) {
        console.error("Erro ao buscar produto(s) de maior valor:", error);

    }

}

async function menorValor() {
    try {
        resposta = await fetch(`${base_url}/produtos/menor-valor`)
        dados = await resposta.json()
        resultado.innerHTML = `<h2 class="text-xl font-bold mb-4">Produto(s) de menor valor:</h2>`
        dados.forEach(produto => {
            const p = document.createElement("p");
            p.innerText = `Nome: ${produto.nome} - Preço: R$ ${produto.preco.toFixed(2)}`
            resultado.appendChild(p)
        })

    } catch (error) {
        console.error("Erro ao buscar produto(s) de menor valor:", error);

    }
}

async function media() {
    try {
        resposta = await fetch(`${base_url}/produtos/media`)
        dados = await resposta.json()
        resultado.innerHTML = `<h2 class="text-xl font-bold mb-4">Média dos preços dos produtos:</h2>`
        const p = document.createElement("p");
        p.innerText = `R$ ${dados.media.toFixed(2)}`
        resultado.appendChild(p)


    } catch (error) {
        console.error("Erro ao buscar media:", error);

    }
}

async function acimaMedia() {
    try {
        resposta = await fetch(`${base_url}/produtos/acima-media`)
        dados = await resposta.json()
        resultado.innerHTML = `<h2 class="text-xl font-bold mb-4">Produto(s) acima da média:</h2>`
        dados.forEach(produto => {
            const p = document.createElement("p");
            p.innerText = `Nome: ${produto.nome} - Preço: R$ ${produto.preco.toFixed(2)}`
            resultado.appendChild(p)
        })

    } catch (error) {
        console.error("Erro ao buscar produto(s) acima da media:", error);

    }
}

function limparResultado() {
    resultado.innerHTML = "";
}

async function abaixoMedia() {
    try {
        resposta = await fetch(`${base_url}/produtos/abaixo-media`)
        dados = await resposta.json()
        resultado.innerHTML = `<h2 class="text-xl font-bold mb-4">Produto(s) abaixo da média:</h2>`
        dados.forEach(produto => {
            const p = document.createElement("p");
            p.innerText = `Nome: ${produto.nome} - Preço: R$ ${produto.preco.toFixed(2)}`
            resultado.appendChild(p)
        })


    } catch (error) {
        console.error("Erro ao buscar produto(s) abaixo da media:", error);

    }
}

listarProdutos()