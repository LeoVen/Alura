class ProdutosController < ApplicationController

	def index
		@todos_produtos = Produto.order(:nome).limit(2)
	end

end
