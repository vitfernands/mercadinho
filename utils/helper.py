def formata_float_str_moeda(valor: float) -> str:
    return f'R${valor:,.2f}'

valor = 1785.90

print(formata_float_str_moeda(valor))