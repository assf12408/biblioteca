
function mostrarProdutos(lista) {
  container.innerHTML = '';
  lista.forEach(p => {
    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
      <img src="${p.imagem}" alt="${p.nome}">
      <h3>${p.nome}</h3>
      <p><strong>R$ ${p.preco.toFixed(2)}</strong></p>
      <p>${p.descricao}</p>
      <p><small>${p.marca} | ${p.cor} | Tam ${p.tamanho}</small></p>
      <p>⭐ ${p.avaliacao} | Estoque: ${p.estoque}</p>
      <button>Comprar</button>
    `;
    container.appendChild(card);
  });
}

mostrarProdutos(produtos);

// Filtro de busca
document.getElementById('search').addEventListener('input', (e) => {
  const termo = e.target.value.toLowerCase();
  const filtrados = produtos.filter(p => p.nome.toLowerCase().includes(termo));
  mostrarProdutos(filtrados);
});

 function irParaConsulta() {
        window.location.href = "/consultar/"; 
    }

 function irParaCadastro() {
        window.location.href = "/cadastrar/"; 
    }

    function irParaContato() {
        window.location.href = "/contato/"; 
    }

    function irParaHome() {
      window.location.href = "/";
    }
  function irParaListar() {
        window.location.href = "/listar/"; 
    }

    function irParaSobre() {
        window.location.href = "/sobre/"; 
    }