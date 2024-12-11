

# Python_simple_crud_api

Como foi descrito na descrição do projeto, o mesmo foi criado para servir como trabalho final da máteria regida pelo docente Adriano Ferraz.
Essa api é baseada nos conceitos base da Trasnfêrencia de Estado Representacional ou REST, usando os 4 métodos principais do protocolo HTTP, GET,POST,PUT/UPDATE e DELETE.



## Documentação da API

#### get_products_list(request)

Recebe a requisição e retorna uma lista de produtos dentro do banco de dados.

```http
  GET /api/products
```


#### get_single_product(request,pk)

Recebe a requisição junto com o id desejado e retorna um único produto que contenha esse id, caso contrário retorna um erro legível ao usuário e mostra detalhes técnicos do erro no terminal.

```http
  GET /api/products/<pk>
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `pk`      | `int` | **Obrigatório**. O ID do produto que você quer visualizar |

#### post_product(request)

Recebe uma requisição em forma de JSON, verifica se o mesmo é valido e adiciona no banco de dados, caso o mesmo não seja válido retorna um erro légivel ao usuário e mostra detalhes técnicos do erro no terminal.

```http
    POST /api/products/create
```

#### get_and_update_product(request,pk)

Recebe uma requisição em forma de JSON,mas primeiro verifica se o produto existe dentro do banco de dados, se não existir retorna um erro légivel mas não manda detalhes técnicos de um erro dentro do terminal. Caso o produto exista o mesmo vai ser serializado e atualizado,caso ocorra um erro, vai retornar um erro légivel ao usuário e mostra detalhes técnicos do erro no terminal. 

```http
  PUT /api/products/update/<pk>
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `pk`      | `int` | **Obrigatório**. O ID do produto que você quer modificar |

#### delete_product(request,pk)

Recebe uma requisição,verifica se o Id de nome pk enviado é um produto existente dentro do banco de dados, caso não seja envia um erro légivel. Caso o mesmo seja um produto existente, o produto é apagado e é enviado uma mensagem de sucesso.

```http
  DELETE /api/products/delete/<pk>
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `pk`      | `int` | **Obrigatório**. O ID do produto que você quer apagar. |




