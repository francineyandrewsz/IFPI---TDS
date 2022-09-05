const jogoAdvinha = {
  semente: 100,
  palpites: 0,
  numeroSorteado : function geraValorAleatorio() {
    return Math.round(Math.random() * this.semente);
  }
}

const btnVerifica = document.getElementById('btnVerifica');
const entregar = document.getElementById('entregar');
const palpites = document.getElementById('palpites');
const chute = document.getElementById('chute');

let numeroSorteado = jogoAdvinha.numeroSorteado();

function atualizarPalpites(palpites, valor) {
  if (valor > 1) {
    palpites.innerHTML = 'Palpites : <span style="color: blue">' + valor + '</span>';
  } else {
    palpites.innerHTML = 'Palpites : <span style="color: blue">' + valor + '</span>';
  }
}

function reiniciar() {
  btnVerifica.innerText = 'Verificar';
  palpites.innerHTML = 'Palpites : 0';
  chute.disabled = false;
  chute.value = '';
  jogoAdvinha.palpites = 0
  numeroSorteado = jogoAdvinha.numeroSorteado();
  btnVerifica.removeEventListener('click', reiniciar);
}

const formAdvinha = document.getElementById('form');
formAdvinha.addEventListener('submit', function(event) {
  event.preventDefault();

  if (!!chute.value == false) {
    entregar.innerHTML = '<span style="color:#FF3D00">Digite algum valor</span>';
    return;
  }

  atualizarPalpites(palpites, ++jogoAdvinha.palpites);

  if (numeroSorteado == chute.value) {
    entregar.innerHTML = '<span style="color:#00C853">Parabéns, você acertou!</span>';
    chute.disabled = true
    btnVerifica.innerText = "Tentar novamente?";
    btnVerifica.addEventListener('click', reiniciar);
  } else if (numeroSorteado > chute.value) {
    entregar.innerText = 'O número sorteado é maior';
  } else if (numeroSorteado < chute.value) {
    entregar.innerText = 'O número sorteado é menor';
  }
});