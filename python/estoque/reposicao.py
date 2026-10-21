"""Lê um estoque CSV e gera um relatório de reposição. Apenas biblioteca padrão."""

import argparse
import csv
from pathlib import Path


def ler_estoque(caminho):
    """Valida todos os dados antes de criar qualquer relatório."""
    produtos = []
    with caminho.open(encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        colunas = {"produto", "quantidade", "estoque_minimo"}
        if not colunas.issubset(leitor.fieldnames or []):
            raise ValueError("CSV deve conter produto,quantidade,estoque_minimo.")
        for linha, registro in enumerate(leitor, start=2):
            nome = (registro.get("produto") or "").strip()
            if not nome:
                raise ValueError(f"Registro {linha}: produto sem nome.")
            try:
                quantidade = int(registro["quantidade"])
                minimo = int(registro["estoque_minimo"])
            except (ValueError, TypeError):
                raise ValueError(f"Registro {linha}: use quantidades inteiras.") from None
            if quantidade < 0 or minimo < 0:
                raise ValueError(f"Registro {linha}: quantidades não podem ser negativas.")
            produtos.append((nome, quantidade, minimo))
    return produtos


def gerar_relatorio(produtos, destino):
    # Uma lista guarda os produtos abaixo do mínimo; igualdade não exige reposição.
    pendentes = []
    for nome, quantidade, minimo in produtos:
        if quantidade < minimo:
            pendentes.append((nome, quantidade, minimo, minimo - quantidade))

    # O modo 'x' impede sobrescrever um arquivo existente, inclusive o de entrada.
    with destino.open("x", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["produto", "quantidade", "estoque_minimo", "repor"])
        escritor.writerows(pendentes)
    return len(pendentes)


def main():
    pasta = Path(__file__).resolve().parent
    argumentos = argparse.ArgumentParser(description=__doc__)
    argumentos.add_argument("--entrada", type=Path, default=pasta / "estoque_exemplo.csv")
    argumentos.add_argument("--saida", type=Path, default=pasta / "reposicao.csv")
    opcoes = argumentos.parse_args()
    try:
        produtos = ler_estoque(opcoes.entrada)
        total = gerar_relatorio(produtos, opcoes.saida)
    except (OSError, ValueError, csv.Error) as erro:
        argumentos.exit(1, f"Não foi possível gerar o relatório: {erro}\n")
    print(f"Produtos que precisam de reposição: {total}")
    print(f"Relatório salvo em: {opcoes.saida}")


if __name__ == "__main__":
    main()
