# Curso de Python: aplicando a Orientação a Objetos
### Neste curso aprendi sobre alguns tópicos:
- #### Classes
Nada mais são do que a representação de um objeto na vida real por meio do código, por exemplo, temos um Carro que contém alguns atributos, como, cor, modelo, marca, tipo do combustível etc. Esse objeto, também possui métodos como acelerar, desacelerar etc.
- #### Construtor e instanciando objetos
Um construtor determina quais atributos são obrigatórios assim que seu objeto é instanciado, também é possível já definir um valor padrão para alguns desses atributos.
- #### Property e métodos de classe
Property é um decorador para transformar um método em uma propriedade de uma classe. Ele permite que um método seja acessado como uma tributo, sem a necessidade de chama-lo como uma função.
Métodos de classe servem para definir um método que opera na classe, e não em instâncias. Já os métodos estáticos utilizamos quando não precisamos receber a referência de um objeto especial (seja da classe ou de uma instância) e funciona como uma função comum, sem relação.
- #### Importando classe e composição
Quando criamos uma classe, é comum que ela fique separa de onde codamos nosso programa principal, sendo assim, para usa-la precisamos importar a mesma, para que seja possível acessar seus atributos e métodos. No Python a estrutura para importarmos uma classe é:\
------> from (nome da pasta e arquivo) import (nome da classe)\
Quando a importação é realizada e executamos o código principal, o python cria uma pasta com um arquivo pycache, isto é, uma versão compilada do código, assim quando o código for executado novamente, 
nosso projeto já tem salvo o arquivo compilado. Explicando de outra maneira, ele "cacheia" os dados do código, criando um arquivo .pyc escrito em bytecode. Desse modo o código é rodado um pouco mais rápido na segunda vez.
- #### Classe/Método abstrato
Significa que funcionará apenas como um modelo, para que suas instâncias implementem, isto é, cada classe derivada implementa como quiser o método. EX: tenho uma classe ItemCardapio, e duas classe Bebida e Prato que herdam a ItemCardapio. Quero implementar um método
que possibilite o usuário a dar desconto ao clientes e o estabelecimento nos informou que para Bebidas o desconto é de no máximo 8% e dos Pratos 5%. Sendo assim criamos um método abstrato na Classe "mãe" ItemCardapio chamado aplicar_desconto, ele será declarado da seguinte maneira:

              @abstractmethod
              def aplicar_desconto(self):
                pass

A implementação desse método será feita pelas classes que herdaram ItemCardapio, assim, implementaram de acordo com cada condição condizente ao tipo de item.
- #### Polimorfismo
O exemplo acima é considerado polimorfismo, pois o método se molda de forma diferente de acordo com as classes. Ele se adapta em diferentes lugares por meio do método abstrato criado na classes principal.
