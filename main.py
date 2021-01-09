"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    import math
    n=input('Digite um ano qualquer: ')
    n=int(n)
    if (n%4==0 and n%100!=0) or (n%400==0):
      print(f'O ano {n} é bissexto.')
    else:
      print(f'O ano {n} não é bissexto.')
    # TODO


if __name__ == '__main__':
    main()
