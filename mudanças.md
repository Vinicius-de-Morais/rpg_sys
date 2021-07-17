# Mudanças que eu fiz no seu código e os motivos
**__Lembre-se__:
Eu pensei dessa forma, você pode achar outra solução!**
### Por que mudar o metodo de escolha das classes ???
    1. Facil manipulação:
        - Dicionarios e Funções são de facil construção, 
        porem é muito mais facil você dar uma manipulada em um dict do quer criar métodos
        para manipular atributos de uma classe.
    2. Facilitar sua contrução da classe em si:
        [OK, essa pode ser mais uma preferência minha.]  
        - Eu considero que minha função init deve "fazer todo o trabalho" ao ser criada, ou seja após ser criada
        o persona = Personagem(...) não deve ser necessário um método para set_classe() para
        "ativar" a classe. Meu ponto era : "Já que a classe já foi passada como parâmetro por que um método set_classe ??" 
---
### Por que mudar \_\_str\_\_ para um método mostrar_perfil() ???
    Essencialmente é a quase a mesma coisa. Porém, note como o código fica mais intuitivo, e mais bonito,
    e também é mais facil manutenção e leitura quando você tem um método que só de olhar o nome você já tem
    uma ideia de qual ação será executada.
---
### Por que excluir o arquivo de teste ???
    Quando quiser testar um método da sua classe, se for algo simples recomendo utilizar este formato que utilizo no final do arquivo. ( if __name__ == "__main__": )
    esta verificação faz meu código rodar se, e somente se, você estiver executando este arquivo diretamente. Ou seja, se ele for executado em outro modulo tudo que está dentro dessa verificação não vai ser executado. Utilizar este formato é bom para testes, melhor que utilizar um arquivo-teste.py.

# Author
| [<img src="https://avatars.githubusercontent.com/u/83929403?v=4" width=115><br><sub>@clcostaf</sub>](https://github.com/clcostaf) |
| :---: |