'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''
from abc import ABC, abstractmethod

class ExamValidator(ABC):
    @abstractmethod
    def validate(self, exame):
        pass

class BloodTestValidator(ExamValidator):
    def validate(self, exame):
        # Implemente as condições específicas do exame de sangue
        if exame.parametros.get("hemoglobina") > 12:
            print("Exame sanguíneo aprovado!")
            return True
        else:
            print("Exame sanguíneo não aprovado.")
            return False

class XRayValidator(ExamValidator):
    def validate(self, exame):
        # Implemente as condições específicas do exame de raio-x
        if exame.parametros.get("imagem_clara"):
            print("Raio-X aprovado!")
            return True
        else:
            print("Raio-X não aprovado.")
            return False


class AprovaExame:
    def __init__(self):
        self.validators = {
            "sangue": BloodTestValidator(),
            "raio-x": XRayValidator(),
        }
        
    def aprovar_solicitacao_exame(self, exame):
        validator = self.validators.get(exame.tipo)
        if validator:
            return validator.validate(exame)
        else:
            print(f"Tipo de exame '{exame.tipo}' não suportado.")
            return False  
    
# Exemplo de uso:
class Exame:
    def __init__(self, tipo, parametros):
        self.tipo = tipo
        self.parametros = parametros

exame_sangue = Exame("sangue", {"hemoglobina": 13})
exame_raio_x = Exame("raio-x", {"imagem_clara": True})

aprovador = AprovaExame()

aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)
