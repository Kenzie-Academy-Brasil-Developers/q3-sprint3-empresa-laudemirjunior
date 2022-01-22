class Funcionario:
    
    funcao = "Funcionario"
    
    def __init__(self, nome, sobrenome, cpf, salario = 3000):
        self.nome = nome.strip().capitalize()
        self.sobrenome = " ".join(sobrenome.title().split())
        self.cpf = cpf
        self.salario = salario
        self.nome_completo = (self.nome + ' ' + self.sobrenome).title()
        
    def __str__(self):
        return f'<{self.funcao}: {self.nome_completo}>'

    def __repr__(self):
        return f'<{self.funcao}: {self.nome_completo}>'
        
class Empresa():
    
    funcao = "Empresa"
    
    def __init__(self, nome, cnpj):
        self.nome = " ".join(nome.strip().split()).title()
        self.cnpj = str(cnpj)
        self.contratados = []
        
    def __str__(self):
        return f'<{self.funcao}: {self.nome}>'

    def __repr__(self):
        return f'<{self.funcao}: {self.nome}>'
    
    def contratar_funcionario(self, funcionario):
        nome_email = ".".join(funcionario.nome_completo.lower().split())
        dominio_email = "".join(self.nome.lower().split())
        funcionario.email = f"{nome_email}@{dominio_email}.com"
        
        if funcionario in self.contratados:
            return "Funcionário com esse CPF já foi contratado."
        
        self.contratados.append(funcionario)
        return "Funcionário contratado!"
        
    @staticmethod
    def adicionar_funcionario_para_gerente(gerente, funcionario):
        if not type(gerente) is Gerente or not type(funcionario) is Funcionario:
            return False
        
        if funcionario in gerente.funcionarios:
            return 'Funcionario já está na lista de funcionarios desse gerente.'
        
        gerente.funcionarios.append(funcionario)
        return 'Funcionário adicionado à lista do gerente!'
    
    def demissao(self, funcionario):
        self.contratados.remove(funcionario)
        if type(funcionario) is Gerente:
            return "Gerente demitido!"

        for contratado in self.contratados:
            if contratado.funcao == "Gerente":
                if funcionario in contratado.funcionarios:
                    contratado.funcionarios.remove(funcionario)
        return "Funcionário demitido!"
        
        
    @staticmethod
    def promocao(empresa, funcionario):
        if not type(funcionario) is Funcionario or funcionario not in empresa.contratados:
            return False
        
        empresa.contratados.remove(funcionario)
        funcionario = Gerente(funcionario.nome, funcionario.sobrenome, funcionario.cpf)
        empresa.contratar_funcionario(funcionario)
        return True

class Gerente(Funcionario):

    funcao = "Gerente"
    
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf, 8000)
        self.funcionarios = []
        
    def __str__(self):
        return f'<{self.funcao}: {self.nome_completo}>'

    def __repr__(self):
        return f'<{self.funcao}: {self.nome_completo}>'
    
    def aumento_salarial(self, funcionario, empresa):
        if not type(funcionario) is Funcionario or funcionario not in self.funcionarios:
            return False
        aumento = int(funcionario.salario + (funcionario.salario / 10))
        
        if aumento > 8000:
            empresa.promocao(empresa, funcionario)
            
        else:
            funcionario.salario = aumento
            
        return True
