
from __future__ import annotations


class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao: int):
        self._titulo = None
        self._ano_publicacao = None
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    # --- getters/setters com @property ---
    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("O título não pode ser vazio.")
        self._titulo = valor

    @property
    def ano_publicacao(self) -> int:
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("O ano de publicação deve ser um número positivo.")
        self._ano_publicacao = valor

    # Polimórfico: será sobrescrito nas filhas
    def apresentar_detalhes(self) -> str:
        return f"Título: {self.titulo} | Ano: {self.ano_publicacao}"



class Livro(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, autor: str, num_paginas: int):
        super().__init__(titulo, ano_publicacao)
        self._autor = None
        self._num_paginas = None
        self.autor = autor
        self.num_paginas = num_paginas

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("O autor não pode ser vazio.")
        self._autor = valor

    @property
    def num_paginas(self) -> int:
        return self._num_paginas

    @num_paginas.setter
    def num_paginas(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 50:
            print("Erro: número de páginas deve ser maior que 50.")
            return
        self._num_paginas = valor


    def apresentar_detalhes(self) -> str:
        return (f"[LIVRO] Título: {self.titulo} | Ano: {self.ano_publicacao} | "
                f"Autor: {self.autor} | Páginas: {self.num_paginas}")



class Revista(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, edicao: int, volume: int):
        super().__init__(titulo, ano_publicacao)
        self._edicao = None
        self._volume = None
        self.edicao = edicao
        self.volume = volume

    @property
    def edicao(self) -> int:
        return self._edicao

    @edicao.setter
    def edicao(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("A edição deve ser um número positivo.")
        self._edicao = valor

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("O volume deve ser um número positivo.")
        self._volume = valor


    def apresentar_detalhes(self) -> str:
        return (f"[REVISTA] Título: {self.titulo} | Ano: {self.ano_publicacao} | "
                f"Edição: {self.edicao} | Volume: {self.volume}")


# ===== Teste inicial =====
def demonstracao_inicial():
    print("=== Demonstração Automática ===")
    l1 = Livro("POO com Python", 2024, "Gustavo Guanabara", 120)
    r1 = Revista("Ciência Hoje", 2023, 7, 3)
    l2 = Livro("Algoritmos Descomplicados", 2022, "Cormen", 900)
    acervo = [l1, r1, l2]

    for item in acervo:
        print(item.apresentar_detalhes())



def menu():
    acervo = []

    def cadastrar_livro():
        print("\n=== Cadastrar Livro ===")
        titulo = input("Título: ").strip()
        ano = int(input("Ano de publicação: ").strip())
        autor = input("Autor: ").strip()
        num_pag = int(input("Número de páginas (>50): ").strip())
        livro = Livro(titulo, ano, autor, num_pag)
        if livro.num_paginas is None:
            print("Livro não cadastrado (número de páginas inválido).")
            return
        acervo.append(livro)
        print("✅ Livro cadastrado com sucesso!")

    def cadastrar_revista():
        print("\n=== Cadastrar Revista ===")
        titulo = input("Título: ").strip()
        ano = int(input("Ano de publicação: ").strip())
        edicao = int(input("Edição: ").strip())
        volume = int(input("Volume: ").strip())
        revista = Revista(titulo, ano, edicao, volume)
        acervo.append(revista)
        print("✅ Revista cadastrada com sucesso!")

    def listar_acervo():
        print("\n=== ACERVO CADASTRADO ===")
        if not acervo:
            print("Nenhum item cadastrado ainda.")
            return
        for idx, item in enumerate(acervo, start=1):
            print(f"{idx}. {item.apresentar_detalhes()}")

    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1 - Cadastrar Livro")
        print("2 - Cadastrar Revista")
        print("3 - Listar Acervo")
        print("0 - Sair")
        opc = input("Escolha: ").strip()

        if opc == "1":
            cadastrar_livro()
        elif opc == "2":
            cadastrar_revista()
        elif opc == "3":
            listar_acervo()
        elif opc == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    demonstracao_inicial()
    print("\nAgora você pode usar o menu para cadastrar seus itens!")
    menu()
