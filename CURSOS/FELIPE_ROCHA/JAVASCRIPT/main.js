const nomes = ['Felipe', 'João', 'Julia', 'Matheus', 'Carlos'];

nomes.push('Pedro'); // coloca no final da lista
nomes.unshift('Fernanda'); // coloca no começo da lista
nomes.pop(); // remove o ultimo valor de uma lista
nomes[3] = 'Rony'; // substitui o valor na lista
console.log(nomes.indexOf('Rony')) // ira mostrar a posição desse elemento na lista

const sortedNames = nomes.sort();

console.log(nomes);
console.log(sortedNames);