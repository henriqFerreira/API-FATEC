const content2 = document.getElementById("content-2");
const arquivo2 = '../static/json/vagas-gerais.json';

    fetch(arquivo2)
        .then(resposta => {
            return resposta.json();
        })
        .then(jsondata => {
            
            vagas = jsondata.filter(i => {
                var id = i.id;
                var categoria = i.categoria;
                var titulo = i.titulo;
                var salario = i.salario;
                var empresa = i.empresa;
                var nivel = i.nivel;
                var descricao = i.descricao;
                var localizacao = i.localizacao;

                content2.innerHTML += `
                    <div class="vaga">
                        <img src="../static/images/icone.svg">
                        <div class="vaga-content2" id="${id}" onclick="getData(this.id)">
                            <h3>
                                <a>${titulo}</a>
                                <span class="nivel">${nivel}</span>
                            </h3>
                            <span class="empresa">${empresa} |</span>
                            <span class="local">${localizacao}</span>
                            <p class="descricao">${descricao}</p>
                        </div>
                    </div>
                `;
            });
        });

function getData(elementId) {
    fetch(arquivo2)
        .then(resposta => {
            return resposta.json()
        })
        .then(jsondata => {
            var vaga = jsondata.filter(i => {
                var id = i.id;
                if (id == elementId) {
                    var categoria = i.categoria;
                    var titulo = i.titulo;
                    var salario = i.salario;
                    var empresa = i.empresa;
                    var nivel = i.nivel;
                    var descricao = i.descricao;
                    var localizacao = i.localizacao;

                    var sessionCategoria = sessionStorage.setItem("categoria", categoria);
                    window.location.href = "vaga.html";
                }
            })
        })
}