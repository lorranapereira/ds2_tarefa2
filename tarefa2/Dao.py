
from conexao import ConDAO
class FuncDAO:
    def inserir(self,a):
        try:
            con = ConDAO().connect()
            cur = con.cursor()
            cur.execute('insert into "Funcionario" (nome, "idDepto") values (%s,%s)',[a.nome,a.idDepto])
            con.commit()
            con.close()
            return "Inserido com sucesso"
  
        except TypeError as e:
            return "Erro no valor inserido: {}".format(e) 
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao inserir: {}".format(e)

    def deletar(self,id):
        try: 
            con = ConDAO().connect()
            cur = con.cursor()
            id = int(id)
            cur.execute('delete from "Funcionario" where id = (%s)',[id])
            con.commit()
            con.close()
            return "Deletado com sucesso"
        except ValueError as e:
            return "Erro, valor inválido:{}".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e) 
        except BaseException as e:
            return "Erro ao deletar: {}".format(e)

    def alterar(self,a):
        try: 

            con = ConDAO().connect()
            cur = con.cursor()
            id = int(a.id)
            cur.execute('update "Funcionario" set nome = (%s), "idDepto"=(%s) where id = (%s)',[a.nome,a.idDepto,a.id])
            con.commit()
            con.close()
            return "Alterado com sucesso"
        except ValueError as e:
            return "Erro, valor inválido: {}".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao alterar: {}".format(e)

    def buscar(self,id):
        try: 

            con = ConDAO().connect()
            cur = con.cursor()
            id = int(id)
            cur.execute('select *from "Funcionario" where id = (%s)',[id])
            con.commit()
            linha = cur.fetchone()
            con.close()
            from funclass import Funcionario
            at = Funcionario(linha[0],linha[2],linha[1])
            return (at)
                      
        except ValueError as e:
            return "Erro, valor inválido: {} ".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao buscar: {} ".format(e)

    def listar(self):
        try: 

            con = ConDAO().connect()
            cur = con.cursor()
            cur.execute('select *from "Funcionario"')
            con.commit()
            lista = []
            from funclass import Funcionario
            for linha in cur.fetchall():
                at = Funcionario(linha[0],linha[2],linha[1])
                lista.append(at)
            con.close()
            return lista
                      
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao listar: {} ".format(e)
