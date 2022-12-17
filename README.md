# Index
- [Comentários](#comentários)
- [Operadores](#operadores)
- [Identificadores](#identificadores)
- [Tipos de Dados](#tipos-de-dados)
- [Coleções de Dados](#coleção-de-dados)
- [Conversão de dados](#type-casting)
- [Condicionais](#condicionais)
- [Laços de Repetição](#loops)
- [Funções](#functions)
- [Métodos](#métodos-python)

# Introdução
Idealizada e desenvolvida por Guido Van Rossum, matemático holandês, no início dos anos 90, o Python foi criado com o objetivo de otimizar a leitura de códigos e estimular a produtividade de quem os cria, seja este um programador ou qualquer outro profissional - ou seja, focado na resolução de problemas.
O grande trunfo do Python é a sua syntax simples e aliado ao fato de ser multiplataforma, sendo útil em diferentes contextos. Desde automações, desenvolvimento web, machine learning, IA, big data, análise e ciência de dados.
Quando queremos escrever um programa, nós utilizamos um editor de texto para
escrever as instruções em Python em um arquivo, isto é chamado de um script.
Por convenção, scripts em Python possuem nomes que terminam com .py.

**Termos comuns no desenvolvimento de sistemas**
**entrada (input)**
Obter dados do “mundo externo”. Isso pode ser ler dados de
um arquivo, ou até de algum tipo de sensor como um microfone ou GPS. Nos
nossos programas iniciais, nossa entrada virá do usuário digitando dados em
seu teclado.

**saída (output)**
Mostrar resultados de um programa numa tela, ou guardá-los
em um arquivo, ou talvez gravá-los em um dispositivo como um alto falante,
para que ele toque música ou fale algum texto.
execução sequencial Realizar instruções uma após a outra na ordem na qual
são encontradas no script.

**execução condicional**
Checar certas condições para que uma certa sequência de
instruções seja executada ou ignorada. execução repetitiva:] Realizar algum
conjunto de instruções repetidamente, geralmente com alguma variação.

**reuso**
Escrever um conjunto de instruções atribuindo um nome a ele para que
estas instruções sejam reutilizadas quando necessárias durante o programa.
Neste curso o Python será usado na IDE Spyder integrada ao Anaconda Navigator, lá haverá integração ao ambiente de dados com Jupyter Notebook, Pandas, etc. O objetivo do uso destas ferramentas é transformar informações dentro de um contexto, em dados utilizaveis.

# Comentários
No Python existem consensos do uso de comentários nos códigos
```python
# Comentário de linha única

# Coméntario de linha extensa
# Que recebe uma descrição um pouco maior

# Comentário de bloco que intercala blocos de códigos
user_name = "Nome"
user_age = 18
# Acompanhado de descrições para cada bloco de forma especifica
car_year = 2010
car_type = "SUV"

"""
	Comentário de várias linhas delcarado com 3 aspas duplas
	na abertura e no fechamento do comentário
"""
```
Assim como toda linguagem de programação, Python tem caracteres e palavras reservadas. Visto que o sinal de ‘#’ é reservado para comentários, existem várias palavras que terão o mesmo comportamento com usabilidades diferentes.

[VOLTAR AO TOPO](#index)

# Operadores
## Operadores aritméticos
| Operador | Significado | Exemplo | Resultado |
| --- | --- | --- | --- |
| + | Adição | a = 3 + 2 | a = 5 |
| - | Subtração | b = 7 - a | b = 2 |
| * | Multiplicação | c = a * b | c = 10 |
| / | Divisão | d = 10/3 | d = 3.33 |
| // | Quociente | e = 10//3 | e = 3 |
| % | Resto | f = 10%3 | f = 1 |
| ** | Exponenciação | g = 2 ** 3 | g = 8 |
| ** | Radiciação (Raiz Quadrada) | h = 16 ** (1/2) | h = 4.0 |
| ** | Radiciação (Raiz Quadrada) | h2 = 16 ** (0.5) | h2 = 4.0 |
| ** | Raiz Cúbica | h3 = raiz ** (1/3) | h3 = 2.5 |

### Ordem de Precedência
São as sequências de importância numa operação matemática, ou seja, aquela operação que será feita primeiro.

1. Parênteses
2. Potenciação
3. Multiplicação e Divisão
4. Soma e subtração

**EXERCICIO**
Operação1:  2 + 3 * 4 \ 5 - 6
Resultado antes da conversão = -1.599

```python
# Conversão para Python
(2 + 3) * 4 / (5 - 6)
```
**Resultado -20.0**

**Operação2:** Encontrar a raiz quadrada de 2+3²/4
2 - 3 = -1;
-1² = 1
1 / 4 = 0.25
V0.25 = 0.5
R: 0.5

```python
((2-3)**2/4)**(0.5)
```
Resultado 0.5

Mais em [Type Coversion](#type-coversion)

## **Operadores de atribuição do Python**
| Operador | Exemplo | Significado |
| --- | --- | --- |
| = | a = 5 | Atribuição simples |
| += | a += 2 | a = a + 2 |
| -= | a -= 2 | a = a - 2 |
| *= | a *= 2 | a = a * 2 |
| /= | a /= 2 | a = a / 2 |
| //= | a //= 2 | a = a // 2 |
| %= | a %= 2 | a = a % 2 |
| **= | a **= 2 | a = a ** 2 |

## **Operadores relacionais (operadores de comparação)**
| Operador | Significado | Exemplo |
| --- | --- | --- |
| == | Igualdade | a == b |
| != | DesiIgualdade | a != b |
| > | Maior que | a > b |
| < | Menor que | a < b |
| >= | Maior ou igual | a >= b |
| <= | Menor ou igual | a <= b |
|  |  |  |

## **Operadores lógicos (conectivos lógicos)**
| Operador | Significado | Exemplo |
| --- | --- | --- |
| and | E lógico | a == b and b == c |
| or | OU lógico | a == b or b == c |
| ^ | OU exclusivo (XOR) | a == b ^ b == c |
| not | Negação (inverte o resultado lógico) | not(a == b and b == c) |

## **Operadores de identidade**
| Operador | Significado | Exemplo |
| --- | --- | --- |
| is | Verifica se duas referências apontam para o mesmo objeto | a is b |
| is not | Verifica se duas referências apontam para diferentes objetos | a is not b |

[VOLTAR AO TOPO](#index)

# Identificadores
No Python esse é o nome dado para a declaração de Variáveis, Constantes e funções. O identificador deve começar com underscore ou uma letra, o sistema não é capaz de ler identificadores que iniciam com números.

BOA PRÁTICA
A recomendação para declarar um identificador, é fazer o uso de todas as letras minúsculas e caso seja preciso escrever mais de uma palavra, usar o underscore. Ex:

client_id
_*client*_id

Visto que, variáveis não recebem acentuação, caracteres especiais,  espaços e nem podem iniciar com números
Sendo assim, para declarar uma variável é necessário um identificador e uma expressão. A expressão poder ser um operador aritmético, uma função ou um tipo de dado.

**PALAVRAS RESERVADAS**
São palavras que não podem ser atribuídas a nenhuma variável pois o sistema já entende que elas tem uma função atribuída, como: def, if, else, import, from, del, global, not, with, as, yield, assert, pass, break, except, raise, class, finally, is, continue, try, nonlocal, entre outras.

### Identificado valores
Existem dois métodos que nos retornam o tipo de dado que aquela variável armazenou, os métodos são: 

type( ) - retorna qual é o tipo da dado
isinstance( ) - recebe o dado e o um tipo, e retorna verdadeiro caso sejam valores condizentes ou falso caso os valores não tenham relação com o tipo. ex:

```python
isstance(5, int) # true
isstance(5, str) # false
isstance('5', int) # false
isstance('5', str) # true
```
Classes e instâncias, basicamente são tudo aquilo que delcradaos. Sendo objetos as classes, e valores as instâncias. Exemplo: váriavel é uma classe, e seu valor uma instância.

imprimindo valores:
print(nome_variável)

[VOLTAR AO TOPO](#index)

# Tipos de dados
Os tipos de dados suportados pelo Python são divididos entre Dados Simples e Dados de Estruturas, os Simples são considerados os dados de informações únicas, como: Inteiro, Real, Boolean e String; pois cada informação será atribuída a um valor. Enquanto os de Estrutura são conjuntos de dados - como Arrays em JS - que irão receber vários valores diferentes, sendo essas estruturas o list, tuple, range, dict.

## Dados Simples
### Tipo inteiro - int
São informações numéricas inteiras, ou seja, números que não são quebrados.
- Ano de fabricação
- Quantidade de portas
- Assentos
- Comprimento e largura - com medidas contínuas, por exemplo milímetros

### Tipo Real\Flutuante - float
Informações numéricas quebradas, não inteiras - ex: 0,5
- Velocidade max
- Autonomia de gasolina
- Preço

### Tipo String - str
Informações que são textos
- Descrição
- Marca
- Modelo
- Cor
- Tipo de combustível

### Tipo boolean\lógico - bool
Informações de Sim ou não, no caso true ou false
- Possui ABS?
- Possui Seguro?
- Cliente tem CNH?

### Dados em String
Mesmo que valores como CPF/RG, data de nascimento, número de telefone; sejam números, eles entram como tipo de dado string, pois seu formato não é inteiro tem nem decimal, aliado ao fato de que podem receber caracteres especiais na sua formatação. Portanto não podem ser considerados com valores numéricos, e sim strings.

Tipo de dado esse que tem uma grande game de manipulações
Como dito antes, strings são valores de texto que podem ser declarados com aspas duplas ou aspas simples, ambas fazem a mesma função, o que vai depender do seu uso é que as vezes haverão textos que contém palavras que também usam aspas - principalmente na lingua inglesa - e por conta disso deve haver um consenso de declaração para não confundir o sistema.
```python
'Eu sou um professor' # String com aspas simples
"I'm a teacher" # String dupla agrupando uma frase que contém aspas simples
```
Um comportamento interessante, é que as strings recebem um identificador para cada caractere dentro dela, um index - que também são atribuídos as coleções de dados - sendo qualquer caractere mesmo, até a barra de espaço, que do inglês é blackspace, ou seja espaço vazio mas que precisa ser inserido e reconhecido ali para dividir as palavras.

```python
frase = 'Eu sou um professor'
print(len(frase))

s = "Python"
# Acessando cada caractere armazenado no string s
print(s[0]) # P
print(s[1]) # y
print(s[2]) # t
print(s[3]) # h
print(s[4]) # o
print(s[5]) # n
```
A importância de entender sobre index é que o Python não nos limita a acessar apenas um elemento, mas definir o retorno de uma quantidade de caracteres baseado nos seus indices.

Slicing:
- `variavel[inicial:final]` => Acessa os caracteres armazenados entre os índices *ind_inicial* e *ind_final-1*
- `variavel[inicial:final:inc]` => Acessa os caracteres armazenados entre os índices *inicial* e *ind_final-1* com incremento *inc - pulando a cada inc números*

```python
frase = 'Eu sou um professor'

print(frase[10:19])
# retornando assim apenas a palavra "professor", baseado no seu index

print(frase[10:19:2])
# Usando slicing com incremento para pular caracteres, o output é 'poesr'

```
Esse método também pode receber espaços em branco, sendo: variavel[ :10 ] indica que irá do inicio ao index 10, e o inverso significa do indice 10 até o indice final.
Toda palavra também recebe valores de index negativo, sendo o primeiro o -1 e vai até o valor fina, do length.

TABELA DE OPERADORES APLICADOS A STRING
| Operador | Significado | Exemplo |
| --- | --- | --- |
| s[ind] | Acesso a uma posição | s[0] |
| s[i:f] | Acesso a uma faixa de posições | s[1:3] |
| s[i:f:inc] | Acesso a uma faixa de posições com incremento | s[0:15:3] |
| s1 + s2 | Concatenação de strings | novastr = s1 + s2 |
| s*n | Retorna um string contendo n repetições de s | s = 'ABC'*10 |
| s1 in s2 | Retorna True se o substring s1 está contido em s2 | 'ABC' in 'ABCDEFGH' |
| s1 not in s2 | Retorna True se o substring s1 não está contido em s2 | 'XYZ' not in 'ABCDEFGH' |

## Métodos String
| Método | Descrição | Exemplo |
| --- | --- | --- |
| capitalize() | Retorna uma cópia da string com primeiro caractere maiúsculo e os caracteres restantes em minúsculo | s.capitalize() |
| casefold() | Retorna uma cópia da string convertido para letras minúsculas | s.casefold() |
| center() | Retorna uma cópia da string centralizada e preenchida com o caractere especificado (default = espaço em branco) | s.center(20) |
| center() | Retorna uma cópia da string centralizada e preenchida com o caractere especificado (default = espaço em branco) | s.center(20, '*') |
| count() | Retorna o número de ocorrências de um determinado substring | s.count('abc') |
| encode() | Retorna uma cópia da string utilizando um determinando encoding (default = UTF-8) | s.encode() |
| endswith() | Retorna True se uma string terminar com o sufixo especificado | s.endswith("python") |
| expandtabs() | Retorna uma cópia da string no qual os caracteres de tabulação \t são substituídos por caracteres de espaço em branco | s.expandtabs(3) |
| find() | Retorna o índice da primeira ocorrência da substring. Se não encontrado, retorna -1 | s.find('python') |
| format() | Formata a string de entrada em uma string de saída | "{} é {}".format("Python", "demais!") |
| index() | Retorna o índice da primeira ocorrência de uma substring dentro da string. Se a substring não for encontrada, levanta uma exceção | s.index('python') |
| isalnum() | Retorna True se todos os caracteres na string forem alfanuméricos (letras ou números) | s.isalnum() |
| isalpha() | Retorna True se a string tiver apenas letras | s.isalpha() |
| isascii() | Retorna True se todos os caracteres na string forem ASCII | s.isascii() |
| isdecimal() | Retorna True se todos os caracteres na string forem decimais (0 a 9) | s.isdecimal() |
| isdigit() | Retorna True se todos os caracteres na string forem dígitos (ex: 3²) | s.isdigit() |
| isidentifier() | Retorna True se a string for um identificador válido em Python | s.isidentifier() |
| islower() | Retorna True se todos as letras da string forem letras minúsculas | s.islower() |
| isnumeric() | Retorna True se todos os caracteres na string forem numéricos (ex: ½) | s.isnumeric() |
| isprintable() | Retorna True se todos os caracteres da string podem ser impressos | s.isprintable() |
| isspace() | Retorna True se houverem apenas espaços em branco na string | s.isspace() |
| istitle() | Retorna True se a string estiver em formato de título, ou seja, se cada palavra da string começa com letra maiúscula e tem o restante das letras minúsculas | s.istitle() |
| isupper() | Retorna True se todos as letras do string forem letras maiúsculas | s.isupper() |
| ljust() | Retorna uma cópia da string justificada à esquerda | s.ljust(20) |
| lower() | Retorna uma cópia da string com as letras maiúsculas convertidas em minúsculas | s.lower() |
| lstrip() | Retorna uma cópia da string com os caracteres passados por parâmetro removidos do início da string | s.lstrip(' *@') |
| partition() | Divide a string e retorna uma tupla contendo a parte antes do separador (primeira ocorrência), a string de argumento (separador) e a parte após o separador | s.partition('@') |
| replace() | Retorna uma cópia da string onde todas as ocorrências de uma substring são substituídas por outra | s.partition('@',' at ') |
| rfind() | Retorna o índice da última ocorrência da substring. Se não encontrado, retorna -1 | s.rfind('python') |
| rindex() | Retorna o índice da última ocorrência da substring dentro da string. Se a substring não for encontrada, levanta uma exceção | s.rindex('python') |
| rjust() | Retorna uma cópia da string justificada à direita | s.rjust(20) |
| rpartition() | Divide a string e retorna uma tupla contendo a parte antes do separador (última ocorrência), a string de argumento (separador) e a parte após o separador | s.rpartition('@') |
| rsplit() | Divide a string à partir da direita (última posição), usando um separador passado por parâmetro, e retorna uma lista de strings | s.rsplit(';') |
| rstrip() | Retorna uma cópia da string com os caracteres passados por parâmetro removidos do final da string | s.rstrip('!?.') |
| split() | Divide a string à partir da esquerda (primeira posição), usando um separador passado por parâmetro, e retorna uma lista de strings | s.split(';') |
| splitlines() | Divide e retorna as linhas contidas em uma string | s.splitlines() |
| starstwith() | Retorna True se uma string começar com o prefixo especificado | s.starstwith("Python") |
| strip() | Retorna uma cópia da string com os caracteres passados por parâmetro removidos do início e do final da string | s.strip(' *@') |
| swapcase() | Retorna uma cópia da string com letras minúsculas convertidas em maiúsculas e vice-versa | s.swapcase() |
| title() | Retorna uma cópia da string com a primeira letra de cada palavra convertida para maiúscula | s.title() |
| upper() | Retorna uma cópia da string com as letras minúsculas convertidas em maiúsculas | s.upper() |
| zfill() | Retorna uma cópia da string preenchida com 0s (zeros) à esquerda | s.zfill(8) |

[VOLTAR AO TOPO](#index)

# Coleção de dados
## Listas
São agrupamentos de dados - como vetores em Java ou Arrays em Javascript - cada valor dentro dele recebe um index, começando pelo número zero. Ou seja o número do index não é o exato mesmo valor da quantidade de tens dentro dele. Ex

lista = [ a, b, c, d, e, f, g, h ] | Temos 8 valores

index [ 0, 1, 2, 4, 5, 6, 7 ] | Index terminando no número 7

O Python permite o acesso aos valores da lista de duas formas: através do número do index ou número final - número desejado, ex: 

index 2 = c
n-6 = c

A indexação no Python também pode ser acessada de forma crescente ou decrescente.

## Declaração - Listas
Existe duas maneiras de criar listas
- lista = list( ) - Função que cria uma lista vazia
- lista = [ ] - criar uma lista a partir de um colchete vazio ou inserindo qualquer tipo de dado
- lista_aninhada = [ [1, 2 ,3], [4, 5, 6] ] - Semelhante a objetos de arrays em javascript

Para acessar os dados dentro de cada lista é usado o identificador seguido do colchetes indicando o index desejado.
Em caso de linha aninhada, cada conjunto de dados recebe um index único e são acessados através do index geral daquela lista.
```python
lista = ["a", "b", "c", "d", "e", "f" ]
lista[3]

lista_aninhada = [["a", "b", "c"], ["d", "e", "f"]]
lista_aninhada[1][0]

# output = d
```

**Atribuindo novos valores para index já existentes**
```python
lista = [77, 2, 80, 4, 15, 30, 12, 90, 99]
lista[8] = 100
lista[1] = lista[1] + lista[3]

# output [77, 6, 80, 15, 30, 12, 90, 100]
```

### Métodos de List
| Método | Descrição | Exemplo |
| --- | --- | --- |
| append | Adiciona um elemento no final da lista | lista.append(5) |
| clear | Apaga todos os elementos de uma lista | lista.clear() |
| copy | Retorna uma cópia dos elementos da lista | copia = lista.copy() |
| count | Retorna a quantidade de ocorrências de um elemento na lista | qt = lista.count(5) |
| extend | Adiciona os elementos de outra lista passada por parâmetro | lista.extend(outra_lista) |
| index | Retorna o índice do elemento passado por parâmetro (primeira posição) | pos5 = lista.index(5) |
| insert | Adiciona um elemento em uma posição passada por parâmetro (adiciona no final caso a posição não exista) | lista.insert(3, "João") |
| pop | Remove o elemento na posição passada por parâmetro (provoca um erro caso a posição não exista) | elemento = lista.pop(3) |
| remove | Remove o elemento passado por parâmetro (provoca um erro caso o elemento não exista) | lista.remove(5) |
| reverse | Inverte a ordem dos elementos de uma lista | lista.reverse() |
| sort | Ordena os objetos de uma lista | lista.sort() |
|  |  | lista.sort(reverse=True) |

## Tuple
Tem a mesma estrutura de uma Lista, porém é do tipo constate, ou seja, quando o conteúdo da tupla é definido naada pode ser alterado, inserido e nem removido.
**************************************DECLARAÇÃO DA TUPLA**************************************
Assim como as listas, as tuplas podem receber qualquer tipo de dado dentro dele, até mesmo listas e outras tuplas.
Importante lembrar que apesar da syntax da tuple ser diferente da List - ( ) para Tuple e [ ] para list - os index são acessados da mesma forma, através do colchetes.

```python
# criando tuplas vazias
tupla_default = ()
tupla_function = tuple()

# tuplas com todo tipo de dado dentro
tupla_any_data = (1, "alpha", true, 1.5)
tupla_tupla = (1, 2, 3, (4, 5, 6))
tupla_list = (1, 2, 3, [4, 5, 6])
```
*As listas dentro de tuplas tem seu comportamento padrão, possibilitando fazer alterações dentro dessa coleção*

### Métodos 
****************COUNT( ) -**************** Retorna a quantidade de observações feitas desse elemento dentro da tupla

**********************INDEX( ) -********************** Retorna a posição de index do elemento requisitado { se houver mais de um, ele retorna o primeiro, assim como em list }.

## Dicionário
Lembram os um array de objetos - ou JSON -  onde cada campo recebe um nome para cada valor, esse é um comportamento importante já que em Dicionários não recebem index.
```python
# Declaração Dicionarios vazios
dicionario = {}
dicionario_function = dict()

# Estrutura de dicionário
email_clients = {
	"Cliente1" : "cliente1@gmail.com",
	"Cliente2" : "cliente2@gmail.com",
	"Cliente3" : "cliente3@gmail.com",
}
email = email_clients['Client2']
email

# Dicionário com outro dicionário
dic_notas_alunos_dicionario = {
	"João": {"nota1": 30, "nota2": 12, "nota3": 21},
	"Maria": {"nota1": 20, "nota2": 30, "nota3": 29},
	"José": {"nota1": 20, "nota2": 23, "nota3": 19},
}

dic_notas_alunos_dicionario

# Dicionario com listas
dic_notas_alunos = {
	"João":[30, 12, 21],
	"Maria": [20, 30, 29],
	"José": [20, 23, 19]
}
dic_notas_alunos["João"] # Para acessar o valor pela chave
nome_aluno = "Maria"
print("As notas de "+nome_aluno+" foram: "+str(dic_notas_alunos[nome_aluno])+".")
# variável que será responsável por fazer a busca da chave
# usando método string, pois caso contrário não é possível contatenar
# os valores dos chamados do dicionário

# dicionário com outros dicionários dentro
dic_notas_alunos2 = {
	"João": {"nota1": 30, "nota2": 12, "nota3": 21},
	"Maria": {"nota1": 20, "nota2": 30, "nota3": 29},
	"José": {"nota1": 20, "nota2": 23, "nota3": 19},
}

dic_notas_alunos2
```

******ALTERANDO DADOS DE UM DICIONÁRIO******
```python
dic_notas_alunos = {
	"João": {"nota1": 30, "nota2": 12, "nota3": 21},
	"Maria": {"nota1": 20, "nota2": 30, "nota3": 29},
	"José": {"nota1": 20, "nota2": 23, "nota3": 19},
}
# Para alterar todos os valores deve-se passar um novo objeto inteiro
dic_notas_alunos['Maria'] = {"nota1": 20, "nota2": 30, "nota3": 30}

# Para alterar um único valor, é preciso especificar pela chave individual
dic_notas_alunos["José"]["nota3"] = 25
```

## Métodos - Dicionário
| Método | Descrição | Exemplo |
| --- | --- | --- |
| clear | Apaga todos os elementos de um dicionário | dic.clear() |
| copy | Retorna uma cópia dos elementos de um dicionário | dic_copia = dic.copy() |
| fromkeys | Retorna um dicionário a partir de uma sequência de chaves | exemplo = dic.fromkeys({"k1", "k4", "k5"}) |
| get | Retorna o valor associado a uma chave | dic.get("k1") |
|  |  | dic.get("k1", 0) |
| items | Retorna uma visão dos pares chave/valor de um dicionário | dic.items() |
| keys | Retorna uma visão das chaves de um dicionário | dic.keys() |
| pop | Remove e retorna o elemento associado à chave passada por parâmetro (provoca erro se a chave não existir) | dic.pop(2) |
| popitem | Remove e retorna o último elemento adicionado ao dicionário | dic.popitem() |
| setdefault | Retorna o valor associado a uma chave (se a chave existir). Caso não exista, insere a chave com o valor (opcional) no dicionário | dic.setdefault(2, "dois") |
| update | Adiciona ao dicionário os pares de chave/valor de outro dicionário passado por parâmetro | dic.update(dic2) |
| values | Retorna uma visão dos valores de um dicionário | dic.values |

## Conjuntos\Set
São coleções que recebem apenas elementos únicos, e armazena os elementos sem ordem específica e não recebe index nem key.
Esse comportamento de valores únicos são em função dos métodos de teoria de conjuntos, onde pode ser feito a união, interseção ou a diferença entre dois conjuntos.
```python
# Essa é a única maneira de se declarar um conjunto
# visto que os valores serão agrupados entre chaves '{ }'
# e esse caractere já é utilizado também pelos dicionários
conj = set()
conj = {1, 2, 3, 4, 5, 6, 7,}
for elem in conj:
	print(elem)
```
*Visto que, como em conjuntos não existem index nem key values, é necessário acessar os seus elementos através de uma função de loop*

### Métodos
| Método | Descrição | Exemplo |
| --- | --- | --- |
| add | Adiciona um elemento ao conjunto | conj1.add(5) |
| clear | Apaga todos os elementos de um conjunto | conj1.clear() |
| copy | Retorna uma cópia dos elementos de um conjunto | conj_copia = conj1.copy() |
| difference | Retorna o conjunto de elementos de conj1 que não pertencem a conj2 | conj1.difference(conj2) |
| intersection | Retorna o conjunto de elementos presentes tanto em conj1 quanto em conj2 | conj1.intersection(conj2) |
| isdisjoint | Retorna True se conj1 e conj2 forem disjuntos (ou seja, não possuem elementos em comum) | conj1.isdisjoint(conj2) |
| issubset | Retorna True se conj1 for um subconjunto de conj2 (conj1 está contido em conj2) | conj1.issubset(conj2) |
| issuperset | Retorna True se conj1 for um superconjunto de conj2 (conj1 contém conj2) | conj1.issuperset(conj2) |
| remove e discard | Removem um elemento do conjunto | conj1.remove(5) ou conj1.discard(5) |
| symmetric_difference | Retorna o conjunto de elementos que não são comuns aos dois conjuntos (o contrário da interseção) | conj1.symmetric_difference(conj2) |
| union | Retorna a união entre 2 conjuntos | conj1.union(conj2) |

Atenção
 remove( ) e discard( ) tem funções semelhantes, porém com comportamentos diferentes. Ambos removem elementos, porém ao tentar remover um elemento inexistente o remove( ) retorna um erro, enquanto o discard( ) não

CONVERTENDO CONJUNTO PARA LISTA
```python

lista = [1, 2, 4, 3, 2, 1, 5, 2, 3, 1, 6, 3, 4, 2]
conjunto = set(list)
conjunto
# output esperado: {1, 2, 3, 4, 5, 6}
```

### Funções compartilhadas entre coleções
| Função | Descrição | Exemplo |
| --- | --- | --- |
| len | Retorna a quantidade de elementos de uma lista | print(len(lista)) |
| max | Retorna o maior elemento de uma lista | maior = max(lista) |
| min | Retorna o menor elemento de uma lista | menor = min(lista) |
| sum | Retorna o somatório dos elementos de uma lista | soma = sum(lista) |

### Impressão de dados
Para retornar dados visualizáveis, é usada a função print( ) que pode receber textos, números e variáveis. E para uso mais avançado a concatenação de tipos de valores ou uso do formato em string literal. ex:
```python
nome = 'João'
idade = 18
print(nome) # retorna o valor dentro da variável
print('Nome: '+nome) # concatena a string + valor de uma variável
print('Seu nome é {} e ele tem {} anos de idade'.format(nome, idade)) # cacatenação literal
print(f'Seu nome é {nome} e ele tem {idade} anos de idade') # shorthand com concatenação literal
```

[VOLTAR AO TOPO](#index)

# Type Casting
É possível converter o tipo de dado a partir de métodos TypeCasting

## Dados
string = srt(true) - retorna um texto “true”
real = float(”3”) - retorna 3.0
inteiro = int(”2019”) - retorna a string para um valor numérico
boolean = bool( “false”) - retorna valor true, visto que qualquer tipo de dado que não for 0 é considerado true 

## Coleções
Em LIST são feitas as novas atribuições
lista[index] = novo valor
Em TUPLE não são permitidas alterações, **Em casos de necessidade de alteração ou não alteração de coleções, podemos fazer a conversão de tuplas em lista pela função list( ), e de lista para tupla com tuple( ).**
Em DICT, é acessado através do valor, já que não há index
dict[”key”] = novo valor

## Convertendo equações em expressões
******CÁLCULO DE ÁREA E PERIMETRO******
area = base x altura
perímetro = 2 x (base + altura)
```python
base = 7
altura = 8

area = base * altura
perimetro = 2 * (base + altura)

print(f'O valor da área é: {area}')
print(f'O valor do perímetro é: {perimetro}')
```

CÁLCULO DE ÁREA E COMPRIMENTO DA CIRCUNFERÊNCIA

área = pi X raio²
comprimento = 2 x pi * raio
```python
pi = 3.14159
raio = 2

area = pi * (raio**2)
comprimento = 2 * (pi * raio)

print(f'O valor da área é: {area}, e valor do comprimento é: {comprimento}')
```

CÁLCULO DA DISTÂNCIA EUCLIDIANA ENTRE 2 PONTOS CARTESIANO

distância = V_ ( X1 - X2)² + (Y1 - Y2)²
```python
x1 = 3
x2 = 5
y1 = 4
y2 = 6

dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
```

CÁLCULO DO DELTA E DAS RAÍZES DE UMA EQUAÇÃO DE SEGUNDO GRAU

delta = b² - 4ac
```python
a = 1
b = -5
c = 6

delta = (b**2) - 4*a*c
x1 = (-b+delta**(0.5)) / (2*a)
x2 = (-b-delta**(0.5)) / (2*a)
```

CALCULO  DO SETOR CIRCULAR - Fatia de pizza

Setor = Angulo . PI . Raio² | 360
```python
a = 45
r = 15
pi = 3.14159

S = (a * pi * (r**2)) / 360

print(S)
```

[VOLTAR AO TOPO](#index)

# Condicionais
São declarações de condições para enviar comandos ao sistema para que execute certa função apenas em contextos específicos.
A syntax das condicionais são baseadas em identação, lendo os blocos de código que não estão juntos a linha inicial. ex:
```python
x = 9
y = 15

if x > y:
    print(f'o valor de x é {x}, portanto é maior')
elif x == y:
    print(f'o valor de x e de y são iguais')
else :
    print(f'o valor de y é {y}, portanto é maior')
```

[VOLTAR AO TOPO](#index)

# Loops
## While
O while é o comando utilizado para programar repetições no Python baseadas na avaliação de uma condição. Enquanto a condição for verdadeira, o bloco de comandos interno ao while é repetido. Quando a condição se torna falsa, o bloco de comandos deixa de repetir.
while (cond):
    bloco de comandos
```python
# Contador 1
count = 0
while (count < 11):
    print(f'{count}')
    count = count + 1

# Contador 2
soma = 0
loop = 0
den = 0
termo = 1
while (termo > 0.0001):
    loop += 1
    den = loop ** 2
    termo = 1 / den
    soma += termo
    print(f"{loop}o termo {1}/{den} = {termo}")    
    
print(soma)
```

## For
A repetição FOR é feita baseada em um objeto, como uma coleção de dados, que ele irá receber uma variável baseada em cada posição referente a length.
```python
lista = [1, 19, 17, 5, 2]
for num in lista:
	print(num)
```
*percebe-se que ao terminar o loop, a variável num mantém o valor da última posição*

Função range( ) + For:
Com essa condição é possível atribuir certas condições ao loop For
```python
# contador até 9 - visto que o loop para antes de chegar no número final
for i in range(10):
	print(i)

# contador 9 invertido - também poderia ser feito com reverse()
# nesse caso a função recebe range(valorInicial, valorFinal, loopStep)
# sendo o último o valor alterado a cada repetição
for i in range(9, -1, -1):
	print(i)

# contador crescente com steps definidos para a multiplicos de 9
for i in range(0, 91, 9):
    print(i)
```

## Comprehensions
Para criação de coleções de dados de maneira mais prática
```python
# List escrita manualmente
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista

# Usando métodos list() e range()
lista1 = list(range(1, 21))
lista1

# Comprehensions - para adicionar elementos com determinadas condições
# Nesse caso retornando valores até 50, mas apenas os numeros pares
lista2  = [num for num in range (1,51) if num % 2 == 0]
lista2
```

[VOLTAR AO TOPO](#index)

# Functions
São blocos de código que armazenam determinadas ações, para serem executadas quando chamadas. Syntax, de uma função que recebe e imprime valores por argumento.
```python
def func(a):
	"""
	Esta área se chama documentation string, são os comentários para funções.
	Aqui é póssivel deixar descrições sobre a utilidade daquela função, que pode
	ser lida por outras pessoas e até pelo Jypter Notebook
	"""
	print(a)

func(1)
```

FUNÇÕES LAMBDAS - Funções anônimas
Apesar de sua escrita não ser declarada com nenhum nome, para reutilizar as funções lambdas o ideal é atribuir a uma variável para acessar o seu valor.
```python
# Synax default
def petencia1(num, pot):
	result = num ** pot
	return result

a = potencia(3, 5)
print(a)

# função ternária
def potencia1(num, pot):
	return num ** pot

b = potencia1(2, 5)
print(b)

# variavel recebendo função lambda e passando os argumentos na chamada
lambda_func = lambda num, pot: num ** pot
print(lambda_func(4, 5)
```

[VOLTAR AO TOPO](#index)

# Métodos Python
São funções do próprio sistema

## Map( )
Aplica uma função, para cada item de uma coleção de dados. Ou seja, assim como loop for, que percorre uma quantidade de dados e a cada repetição executa uma ação, o map( ) faz o mesmo, mas com uma syntax mais direta.
Código manual - criando e inserindo numa nova lista os valores atualizados pelo loop do for
```python
# FOR
valores = [1000, 1500, 1250, 2599]
def adicionar_imposto(valor):
	return valor * 1.1

valor_atualizado = []
for valor in valores:
    valor_atualizado.append(adicionar_imposto(valor))

print(valor_atualizado)
```

Código com map( ) - esse método recebe list( ) pois o map retorna um objeto e essa função o converte para lista, e então map(função que será executada, estrutura de base para a função executar baseada em seus elementos)
```python
valores = [1000, 1500, 1250, 2599]
def adicionar_imposto(valor):
	return valor * 1.1

valor_com_imposto = list(map(adicionar_imposto, valores))

print(valor_com_imposto)
```
*importante não esquecer de passar um parâmetro na declaração da função*

## Reduce( )
Executa uma função para cada valor da estrutura de dados, contando cada repetição de dois em dois, já que ele estará somando 2 valores de cada vez até gerar uma valor final; Recebe uma função e o iterável - variavel para receber o valor final
Percebe-se que reduce era uma função nativa do Python, e hoje já não é mais, então é necessário fazer o import.
```python
from functools import reduce
numeros = list(range(0, 11))

def soma(n1, n2):
    return n1 + n2

result = reduce(soma, numeros)
print(result)
```

## Filter( )
**Aplica um filtro na estrutura de dados, retornando apenas os elementos que passaram por esse filtro. Recebe uma função para impor condições, e a variável iterável.**
```python
numeros = list(range(0, 11))
 
def impar(num):
    if num % 2 != 0:
        return True
    else:
        return False

result = list(filter(impar, numeros))
print(result)
```
*Percebe-se que assim como o método Map( ), ele retorna um objeto que precisa ser convertido em estrutura de dados.*

## Zip( )
Faz a combinação de estruturas, combinado cada valor baseado na sua posição e cria uma tupla contendo uma lista para cada loop executado.
```python
nomes = ["Raul", "Bia", "José"]
idades = [32, 25, 28]
cidades = ["Campinas", "BHte", "João Pessoa"]
dados = list(zip(nomes, idades, cidades))

print(dados)

# output: [('Raul', 32, 'Campinas'), ('Bia', 25, 'BHte'), ('José', 28, 'João Pessoa')]
```

[VOLTAR AO TOPO](#index)
