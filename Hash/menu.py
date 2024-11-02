import exercicioPontoExtra

print('\nTabela hash com função hash resto da divisão, tratamento de colisão open adressing com pesquisa linear e encadeamento')

while True:
    print('\n1. Criar tabela (tamanho)\n2. Inserir valor (chave, valor)\n3. Remover valor (chave)\n4. Busca por chave (chave; retorna linha e valor)\n5. Printar tabela\n6. Deletar tabela')
    opt = int(input())
    match opt:
        case 1:
            try:
                size = int(input('Insira o tamanho da tabela: '))
                tabela = exercicioPontoExtra.Tabela(size)
            except ValueError:
                print('Você deve inserir um valor inteiro!')

        case 2:
            try:
                key = input('Insira a chave: ')
                value = input('Insira o valor: ')
                if not tabela._insert(key, value):
                    print('Tabela cheia!')
            except NameError:
                print('Você deve criar uma tabela antes!')
            except IndexError:
                print('Insira uma chave válida!')

        case 3:
            try:
                key = input('Insira a chave: ')
                if not tabela._remove(key):
                    print('Chave não encontrada!')
            except NameError:
                print('Você deve criar uma tabela antes!')

        case 4:
            try:
                key = input('Insira a chave: ')
                search = tabela._search(key)
                if search:
                    print(search)
                else:
                    print('Chave não encontrada!')
            except NameError:
                print('Você deve criar uma tabela antes!')

        case 5:
            try:
                print(tabela)
            except NameError:
                print('Você deve criar uma tabela antes!')

        case 6:
            try:
                tabela.__init__(size)
            except NameError:
                print('Você deve criar uma tabela antes!')
