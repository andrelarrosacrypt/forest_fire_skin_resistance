# forest_fire_firefighters
Versão modificada de forest_fire_skin_resistance<br />
Original disponível em https://github.com/andrelarrosacrypt/forest_fire_skin_resistance

## Hipótese

Qaunto mais rápido o tempo de resposta dos bombeiros, menos o fogo irá se espelhar.

## Sumário

Modelo que simula a propagação de um incêndio em uma floresta. O esquema apresenta a dorma de grid of cells, cada célula pode ter ou não uma árvore. Cada árvore está não queimada (Fine), queimando (On Fire) ou queimada (Burned Out). O fogo se espalha de uma árvore que está em chamas (On Fire) para uma árvore que esteja intacta (Fine) somente se vencer a resistência da casaca da árvore intacta (número randômico maior ou igual ao valor de resistência (skin) ); as árvores que pegam fogo eventualmente são totalmente consumidas (On Fire -> Burned Out). O processo continua até todas as árvores em chamas (On Fire) se transformarem em totalmente queimadas (Burned Out).
A modificação consiste na adição de uma nova variável (Firefighters response time) que representa o tempo de resposta de uma equipe de bombeiros para combater o fogo. Quanto menor o tempo de resposta, menor a chance do fogo se espalhar. Definoms, então, o tempo de resposta dos bombeiros (número inteiro de 1 a 100) que, na prática, será o número de passos (steps) da simulação antes de se iniciar o combate ao fogo. Vamos considerar que os bombeiros, uma vez presentes, apagam o fogo imediatamente.

## Como rodar

No diretório forest_fire_firefighters, utilize o comando:<br />
    `$ mesa runserver`<br />
Abra o browser em http://127.0.0.1:8521/.<br />
Defina os valores das variáveis "Tree skin thickness", "Tree density" e "Firefighters response time", precione "Reset" e em seguida "Start".

## Arquivos CSV

O progrma gera dois arquivos .csv, "agent_var.csv" e "model_var.csv".<br />
"agent_var.csv" armazena o estado dos agentes (Fine, On Fire ou Burned Out) a cada iteração.<br />
"model_var.csv" armazena a porcentagem das árvores que sobreviveram e impediram o aumento da queimada porque sua resistência a protegeu.

