class Funcionario:
    def __init__(self,nome,salario,matricula):
        # construtor da classe funcionário
        self.__nome=nome
        self.__salario=salario
        self.__matricula=matricula

    # Funções getter e setter dos atributos do funcionário abaixo
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,novo_nome):
        self.__nome=novo_nome

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self,novo_salario):
        if novo_salario<=0:
            raise ValueError('O valor não pode ser negativo ou nulo')
        else:
            self.__salario=novo_salario
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,nova_matricula):
        self.__matricula=nova_matricula

    def __str__(self):
        return f''' 
        ---> FUNCIONÁRIO <---
            Nome --> {self.__nome};
            salário--> R$ {self.__salario:.2f};
            matrícula--> {self.__matricula}.
'''
class Gerente(Funcionario):
    # construtor da classe gerente
    def __init__(self, nome, salario, matricula,setor):
        super().__init__(nome, salario, matricula)
        self.__setor=setor
     # Funções getter e setter dos atributos do funcionário abaixo
    @property
    def setor(self):
        return self.__setor
        
    @setor.setter
    def setor(self,novo_setor):
        self.__setor=novo_setor

    def __str__(self):
        return f''' 
        ---> GERENTE <---
            Nome --> {self.nome};
            salário--> R$ {self.salario:.2f};
            matrícula--> {self.matricula};
            setor --> {self.__setor}
    '''

class Departamento:

    def __init__(self,nome_departamento):
        self.nome_departamento=nome_departamento
        self.funcionarios=[]

    def adicionar_funcionario(self,funcionario):
        self.funcionarios.append(funcionario)
    def contar_funcionarios(self):
        return len(self.funcionarios)
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)
