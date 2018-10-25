# notes

## Start Rails server

```
rails server
```

## Commands in the terminal

```
rails generate controller produtos

rake db:create

rails generate model produto nome:string descricao:text quantidade:integer preco:decimal

rake db:migrate

rails dbconsole

rails console

bundle install

rake routes

```

## Commands in rails console

```ruby
irb(main):001:0> bigbang = Produto.new
=> #<Produto id: nil, nome: nil, descricao: nil, quantidade: nil, preco: nil, created_at: nil, updated_at: nil>
irb(main):002:0> bigbang.nome = "Camiseta do BigBang Theory"
=> "Camiseta do BigBang Theory"
irb(main):003:0> bigbang.descricao = "Camiseta super bacana do BTT"
=> "Camiseta super bacana do BTT"
irb(main):004:0> bigbang.preco = 70.5
=> 70.5
irb(main):005:0> bigbang.quantidade = 10
=> 10
irb(main):006:0> bigbang
=> #<Produto id: nil, nome: "Camiseta do BigBang Theory", descricao: "Camiseta super bacana do BTT", quantidade: 10, preco: #<BigDecimal:57cd998,'0.705E2',18(36)>, created_at: nil, updated_at: nil>
irb(main):007:0> bigbang.save
   (1.0ms)  begin transaction
  SQL (1.0ms)  INSERT INTO "produtos" ("nome", "descricao", "quantidade", "preco", "created_at", "updated_at") VALUES (?, ?, ?, ?, ?, ?)  [["nome", "Camiseta do BigBang Theory"], ["descricao", "Camiseta super bacana do BTT"], ["quantidade", 10], ["preco", 70.5], ["created_at", "2018-09-21 17:50:29.899209"], ["updated_at", "2018-09-21 17:50:29.899209"]]
   (203.7ms)  commit transaction
=> true
irb(main):008:0> gastronomia = Produto.create nome: "Camiseta de gastronomia", desc<eate nome: "Camiseta de gastronomia", descricao: "Camiseta super bacana gourmet", quantidade : 8, preco: 37.66
   (0.0ms)  begin transaction
  SQL (2.0ms)  INSERT INTO "produtos" ("nome", "descricao", "quantidade", "preco", "created_at", "updated_at") VALUES (?, ?, ?, ?, ?, ?)  [["nome", "Camiseta de gastronomia"], ["descricao", "Camiseta super bacana gourmet"], ["quantidade", 8], ["preco", 37.66], ["created_at", "2018-09-21 17:53:08.180178"], ["updated_at", "2018-09-21 17:53:08.180178"]]
   (158.8ms)  commit transaction
=> #<Produto id: 2, nome: "Camiseta de gastronomia", descricao: "Camiseta super bacana gourmet", quantidade: 8, preco: #<BigDecimal:55d4348,'0.3766E2',18(36)>, created_at: "2018-09-21 17:53:08", updated_at: "2018-09-21 17:53:08">
irb(main):009:0> Produto.all
  Produto Load (0.0ms)  SELECT  "produtos".* FROM "produtos" LIMIT ?  [["LIMIT", 11]]
=> #<ActiveRecord::Relation [#<Produto id: 1, nome: "Camiseta do BigBang Theory", descricao: "Camiseta super bacana do BTT", quantidade: 10, preco: #<BigDecimal:3e43798,'0.705E2',18(36)>, created_at: "2018-09-21 17:50:29", updated_at: "2018-09-21 17:50:29">, #<Produto id: 2, nome: "Camiseta de gastronomia", descricao: "Camiseta super bacana gourmet", quantidade: 8, preco: #<BigDecimal:3e40b28,'0.3766E2',18(36)>, created_at: "2018-09-21 17:53:08", updated_at: "2018-09-21 17:53:08">]>
irb(main):010:0> Produto.all.size
   (1.0ms)  SELECT COUNT(*) FROM "produtos"
=> 3
irb(main):011:0>
```

## Others

@my_var -> the @ corresponds to an instance variable