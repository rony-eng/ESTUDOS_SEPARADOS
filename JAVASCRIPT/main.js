const idade = prompt('Insira sua idade')
const nome = 'Rony'
// if (idade >= 18) // esta seria a forma normal e simples de fazer uma condição
//     alert('Maior de idade')
// else
//     alert('Menor de idade')

// agora com o operador ternario ficaria menor e  simples também
idade >= 18 ? alert('Maior de idade') : alert('Menor de idade') // substituindo o if e else

const message = 'Olá meu nome é ${nome}'