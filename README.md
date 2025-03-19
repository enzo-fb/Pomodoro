# Pomodoro

Este é um aplicativo simples de timer Pomodoro, implementado em Python. Ele permite que o usuário escolha entre o timer Pomodoro tradicional ou personalize os tempos para se adaptar às suas necessidades. A implementação utiliza o módulo `time` para controle de tempo e `colorama` para colorir a interface do terminal.

## Funcionalidades

- **Pomodoro Tradicional**: O timer segue o método Pomodoro tradicional com 25 minutos de foco seguidos de 5 minutos de descanso. Após 4 ciclos, há um descanso maior de 15 minutos.
- **Pomodoro Personalizado**: O usuário pode configurar os tempos de foco, descanso curto, descanso longo e o número de ciclos antes do descanso longo.
- **Interface Simples**: A interface de texto interativa permite a navegação pelo menu para escolher entre as opções e visualizar o tempo de forma clara e colorida.

## Como Usar

### Requisitos

1. Python3
2. Instalar Dependências <br>
Para instalar todas as dependências necessárias para o projeto, basta usar o arquivo `requirements.txt`:
   1. Clone este repositório ou baixe os arquivos do projeto.
   2. No terminal, navegue até o diretório do projeto e execute o comando abaixo para instalar as dependências:


```
pip install -r requirements.txt
```

### Instruções

1. Execute o script.
2. O menu principal será exibido:
   - **1**: Pomodoro Tradicional
   - **2**: Editar tempos do Pomodoro
   - **3**: Sair do programa

3. Se você escolher a opção **1**, o timer seguirá o ciclo tradicional de Pomodoro:
   - 25 minutos de foco
   - 5 minutos de descanso
   - Após 4 ciclos, será feito um descanso de 15 minutos.
   
   Após o descanso maior, você pode escolher reiniciar o ciclo ou voltar ao menu principal.

4. Se você escolher a opção **2**, você poderá editar os tempos:
   - Tempo de foco
   - Tempo de descanso curto
   - Tempo de descanso longo
   - Número de ciclos antes do descanso longo

5. Se você escolher **3**, o programa será encerrado.

### Exemplo de execução

```
---------- Welcome Pomodoro Time ----------
1 - Traditional Pomodoro
2 - Edit times
3 - Exit
```

### Exemplo de visualização do timer:

- Durante o tempo de foco:

```
---------- Focus Time ----------
Time: 25:00
```

- Durante o descanso:

```
---------- Rest Time ----------
Time: 5:00
```

## Como Funciona

### Função `pomodoro(tempo, descanso)`
Essa função gerencia o ciclo do Pomodoro. Ela aceita dois parâmetros:
- `tempo`: o tempo de foco ou descanso em minutos.
- `descanso`: um valor booleano que indica se o tempo é de descanso (`True`) ou foco (`False`).

A função exibe o tempo restante no formato `MM:SS` e atualiza a cada segundo. O terminal é limpo a cada iteração para uma experiência de usuário mais agradável.

### Função `main()`
Essa função exibe o menu principal e gerencia a lógica de navegação entre as opções:
- Inicia o timer Pomodoro tradicional ou personalizado.
- Permite editar os tempos do Pomodoro.
- Encerra o programa ao escolher a opção **3**.

## Contribuição

Sinta-se à vontade para contribuir para o projeto. Para isso, basta clonar o repositório e enviar um pull request com as suas melhorias.

---
