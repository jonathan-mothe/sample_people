# Desafio
Usando a API de modelos do Django, elabore queries para atender as seguintes operações

1. Uma lisa das n pessoas mais jovens, ordenadas ascendentemente

```
    p = People.objects.order_by('-data_nasc')[:3]
    p.idade
```

2. Uma lista das n pessoas mais velhas ordenadas ascendentemente

```
    p = People.objects.order_by('data_nasc')[:3]
    p.idade
```

3. Qual a quantidade de pessoas do sexo feminino?

```
    p = People.objects.filter(sexo='F')
    p.count()
```

4. Qual a quantidade de pessoas do sexo masculino?

```
    p = People.objects.filter(sexo='M')
    p.count()
```

5. Escreva uma método "to_json", que retorne os dados de uma pessoa em formato json

```
    def to_json(p):

        dictionary = {}
        dictionary['nome'] = p.nome
        dictionary['cpf'] = p.cpf
        dictionary['rg'] = p.rg
        dictionary['data_nasc'] = p.data_nasc
        dictionary['sexo'] = p.sexo
        dictionary['mae'] = p.mae
        dictionary['pai'] = p.pai
        dictionary['celular'] = p.celular
        dictionary['altura'] = p.altura
        dictionary['peso'] = p.peso
        dictionary['tipo_sanguineo'] = p.tipo_sanguineo

        return dictionary
```

6. Listar os nomes de todas as pessoas no dataset em ordem alfabética

```
    p = People.objects.order_by('nome')
```

7. Implemente uma função para buscar pessoas por nome, ou parte do nome (Case insensitive)

```
    def search_people(self, nome):
        return self.model.objects.filter(nome__icontains=nome)
```
