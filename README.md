# trabfabricio_aula03_06

![image](https://user-images.githubusercontent.com/125207561/227806419-e7b414db-a97d-4a29-a3a3-4f82564f32e1.png)



ENGENHARIA DE SOFTWARE – 5º Período

Disciplina: Banco de Dados Não Relacionais

Prof.: Fabricio Dias
-----------------------
MARICÁ - RJ
2024
-----------------------
Requisitos da Aplicação:

Modelos (Models):

Usuário: Utilize o modelo de usuário padrão do Django.

Evento:

Título (CharField)

Descrição (TextField)

Data e Hora de Início (DateTimeField)

Data e Hora de Término (DateTimeField)

Local (CharField)

Criador (ForeignKey para o usuário)

Views:

Página Inicial: Lista de eventos futuros, ordenados pela data de início.

Detalhe do Evento: Exibe informações detalhadas sobre um evento específico.

Criação de Evento: Formulário para criar um novo evento (apenas para usuários autenticados).

Edição de Evento: Formulário para editar um evento existente (apenas para o criador do evento).

Exclusão de Evento: Permitir a exclusão de um evento (apenas para o criador do evento).

Templates:

Utilizar o sistema de templates do Django para renderizar as páginas.

Criar templates para cada uma das views descritas acima.

Usar a herança de templates para uma base.html que contenha o layout comum.

Formulários:

Utilizar forms.ModelForm para criar formulários baseados nos modelos.

Implementar validação personalizada nos formulários (ex: verificar se a data de término é posterior à data de início).

