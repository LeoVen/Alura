Rails.application.routes.draw do

    post "/produtos" => "produtos#create"
    get "/produtos/new" => "produtos#new"

    # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
    root "produtos#index"
end
