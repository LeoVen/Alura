class ProdutosController < ApplicationController

	def index
		@todos_produtos = Produto.order(:nome)
	end

	def create
        valores = params.require(:produto).permit :nome, :preco, :descricao, :quantidade
        produto = Produto.create valores
	end

end
