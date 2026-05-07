"""Regras de negócio para cálculo de desconto."""


class DiscountError(ValueError):
    """Erro de validação para entradas inválidas no cálculo de desconto."""


def calculate_final_price(price: float, discount: float) -> float:
    """Aplica um desconto percentual sobre um preço e retorna o preço final.

    Args:
        price: Preço original. Deve ser maior que zero.
        discount: Porcentagem de desconto entre 0 e 100 (inclusive).

    Returns:
        O preço final após aplicar o desconto, arredondado para 2 casas decimais.

    Raises:
        DiscountError: quando ``price`` ou ``discount`` estão fora dos limites
            permitidos.
    """
    if price <= 0:
        raise DiscountError("price must be greater than zero")

    if discount < 0 or discount > 100:
        raise DiscountError("discount must be between 0 and 100")

    final_price = price - discount

    return round(final_price, 2)
