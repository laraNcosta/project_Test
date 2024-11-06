Roteiro de Teste: Funcionalidade de Login
Objetivo:
    Validar o comportamento da funcionalidade de login com diferentes entradas de dados, garantindo que as mensagens corretas sejam exibidas de acordo com o cenário.

Cenários de Teste:
Cenário 1: Login com sucesso

Pré-condição: Usuário existe e possui as credenciais corretas.
    Entrada:
        E-mail: alan_nichols_717@growthmachine.com.br
        Senha: senha123

Passos:
    Acessar a página de login.
    Inserir e-mail e senha.
    Clicar no botão de login.

Resultado Esperado: 
    Página de Banco de atividades carregada com modelos criados visíveis.
    
Cenário 2: Login com e-mail e senha inválidos

Pré-condição: E-mail não registrado e senha inválida.
    Entrada:
        E-mail: wrong_email@growthmachine.com.br
        Senha: wrong_password

Passos:
    Acessar a página de login.
    Inserir e-mail e senha incorretos.
    Clicar no botão de login.
    
Resultado Esperado: 
    Exibição de mensagem de erro: "E-mail ou senha inválidos".

Cenário 3: Login com senha incorreta

Pré-condição: Usuário existe, mas senha incorreta.
    Entrada:
        E-mail: alan_nichols_717@growthmachine.com.br
        Senha: wrong_password

Passos:
    Acessar a página de login.
    Inserir e-mail válido e senha incorreta.
    Clicar no botão de login.
    
Resultado Esperado: 
    Exibição de mensagem de erro: "E-mail ou senha inválidos".

Cenário 4: Login com E-mail incorreto

Pré-condição: Usuário existe, mas senha incorreta.
    Entrada:
        E-mail: wrong_email@growthmachine.com.br
        Senha: senha123

Passos:
    Acessar a página de login.
    Inserir e-mail inválido e senha correta.
    Clicar no botão de login.
   
Resultado Esperado: 
    Exibição de mensagem de erro: "E-mail ou senha inválidos".

Cenário 5: Login com campos vazios

Pré-condição: Nenhuma.
    Entrada:
        E-mail: (campo vazio)
        Senha: (campo vazio)

Passos:
    Acessar a página de login.
    Deixar os campos de e-mail e senha em branco.
    Clicar no botão de login.
    
Resultado Esperado: 
    Exibição de mensagem de erro: "E-mail ou senha inválidos".

Cenário 5: Login com e-mail no formato inválido

Pré-condição: Usuário tenta inserir e-mail mal formatado.
        Entrada:
        E-mail: email_invalido@
        Senha: senha123

Passos:
    Acessar a página de login.
    Inserir um e-mail inválido e senha válida.
    Clicar no botão de login.
    
Resultado Esperado: 
    Exibição de mensagem de erro: "E-mail ou senha inválidos".

----------------------------------------------------------------------------------

Roteiro de Teste: Esqueci a Senha

Cenários de Teste:

Cenário 1: E-mail Válido

Objetivo: 
    Validar a funcionalidade de recuperação de senha seja executados corretamente.

Pré-condição: Usuário existe e possui as credenciais corretas.
    Entrada:
        E-mail: alan_nichols_717@growthmachine.com.br

Passos:
    Acessar a página de login.
    Clicar no link de Esqueceu a senha?.
    Na tela de recuperação de senha, inserir um e-mail válido (registrado no sistema)
    Verificar se o sistema exibe uma mensagem de sucesso, indicando que um e-mail foi enviado para recuperação de senha.

Resultado Esperado: 
    E-mail válido com mensagem de Sucesso.

Cenário 2: E-mail inválido

Pré-condição: E-mail não registrado.
    Entrada:
        E-mail: wrong_email@growthmachine.com.br

Passos:
    Acessar a página de login.
    Clicar no link de Esqueceu a senha?.
    Na tela de recuperação de senha, inserir um e-mail inválido (não registrado no sistema)
    Verificar se o sistema exibe uma mensagem de erro, indicando que o usuário não foi encontrado.

Resultado Esperado: 
    Indicação de erro ao indicar e-mail inválido, usuário incorreto.

Cenário 3: Campo de e-mail em branco

Pré-condição: Nenhuma.
    Entrada:
        E-mail: "  "

Passos:
    Acessar a página de login.
    Clicar no link de Esqueceu a senha?.
    Na tela de recuperação de senha, deixar campo em branco.
    Verificar se o sistema exibe uma mensagem de erro, indicando que o usuário não foi encontrado.

Resultado Esperado: 
    Indicação de erro ao deixar campo em branco, usuário incorreto.

----------------------------------------------------------------------------------

Roteiro de Teste: Funcionalidades de Visualização, Pesquisa, Filtro, Edição e Exclusão do Banco de Atividades

Caso de Teste 1: Acesso à Tela de Banco de Atividades

Objetivo: 
    Verificar se o usuário consegue acessar a tela de Banco de Atividades após realizar login.

Cenário De Teste:
Cenário 1: Exibição de Banco de Atividade

Pré-condições: O usuário deve ter uma conta registrada e credenciais válidas.
    Passos:
        Realizar login no sistema com credenciais válidas.
        Verificar se a tela principal de Banco de Atividades é exibida.

        Resultado Esperado: A tela de Banco de Atividades é carregada com sucesso.
        Critério de Aprovação: Acesso bem-sucedido e visualização dos modelos existentes.

Cenário 2: Pesquisa por WhatsApp

Objetivo:
    Validar se a pesquisa pelo termo "WhatsApp" exibe o resultado esperado.

Pré-condição:
O sistema possui o termo "WhatsApp" registrado.
    Entrada:
        Termo de busca: "WhatsApp"

Passos:
    Acessar o campo de busca.
    Inserir o termo "WhatsApp".
    Acionar a funcionalidade de busca.
    Verificar se o sistema exibe o texto "WhatsApp" na área de resultados.
    
Resultado Esperado:
    O sistema exibe o termo "WhatsApp" na área de resultados.

Cenário 3: Pesquisa por LinkedIn

Objetivo:
    Validar se a pesquisa pelo termo "LinkedIn" exibe o resultado esperado.

Pré-condição:
    O sistema possui o termo "LinkedIn" registrado.
        Entrada:
            Termo de busca: "LinkedIn"

Passos:

    Acessar o campo de busca.
    Inserir o termo "LinkedIn".
    Acionar a funcionalidade de busca.
    Verificar se o sistema exibe o texto "LinkedIn" na área de resultados.

Resultado Esperado:
    O sistema exibe o termo "LinkedIn" na área de resultados.

Cenário 4: Editar e Salvar Descrição de WhatsApp

Objetivo:
    Validar se o sistema permite editar e salvar a descrição de um item.

Pré-condição:
    O item "WhatsApp" está registrado no sistema.
        Entrada:
            Descrição nova: "Caso_Teste_WhatsApp teste 2"

Passos:

    Realizar a busca pelo termo "WhatsApp".
    Selecionar a opção de edição do item "WhatsApp".
    Confirmar a exibição do rótulo "Nome do Modelo de Atividade*".
    Alterar a descrição para "Caso_Teste_WhatsApp teste 2".
    Salvar as alterações.

Resultado Esperado:
    A nova descrição "Caso_Teste_WhatsApp teste 2" aparece no item atualizado.

Cenário 5: Editar e Cancelar Descrição de WhatsApp

Objetivo:
    Validar que o cancelamento da edição mantém a descrição original do item.

Pré-condição:
    O item "WhatsApp" está registrado no sistema.
        Entrada:
            Descrição nova: "Caso_Teste_WhatsApp teste 2"

Passos:

    Realizar a busca pelo termo "WhatsApp".
    Selecionar a opção de edição do item "WhatsApp".
    Confirmar a exibição do rótulo "Nome do Modelo de Atividade*".
    Alterar a descrição para "Caso_Teste_WhatsApp teste 2".
    Cancelar a operação de edição.

Resultado Esperado:
    A descrição original do item "WhatsApp" permanece inalterada.

Cenário 6: Duplicar, Pesquisar e Excluir LinkedIn

Objetivo:
    Validar a duplicação e exclusão de um item.

Pré-condição:
    O item "LinkedIn" está registrado no sistema.
        Entrada:
        Item: "LinkedIn"

Passos:

    Realizar a busca pelo termo "LinkedIn".
    Selecionar a opção de duplicação do item "LinkedIn".
    Verificar se o item aparece duplicado.
    Excluir o item duplicado.

Resultado Esperado:
    O item duplicado é removido e o item original "LinkedIn" permanece no sistema.
