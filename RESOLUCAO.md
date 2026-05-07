# Resolução — Teste Técnico Desenvolvedor Júnior

> ⚠️ **Este arquivo é para uso interno do avaliador. Não deve ser entregue ao candidato.**

---

## Onde está o bug

Arquivo: `backend/app/discount.py`, função `calculate_final_price`.

### Código com bug

```python
final_price = price - discount
```

Essa linha subtrai o **valor bruto** do desconto do preço, em vez de calcular o **percentual** sobre o preço. Isso significa que para `price=100` e `discount=10`, o resultado acidental é `90` — que é o valor correto — mas por razões erradas. Para `price=200` e `discount=25`, o resultado seria `175` em vez de `150`.

---

## Correção

Substituir a linha pelo cálculo percentual correto:

```python
final_price = price * (1 - discount / 100)
```

### Função corrigida completa

```python
def calculate_final_price(price: float, discount: float) -> float:
    if price <= 0:
        raise DiscountError("price must be greater than zero")

    if discount < 0 or discount > 100:
        raise DiscountError("discount must be between 0 and 100")

    final_price = price * (1 - discount / 100)

    return round(final_price, 2)
```

---

## Por que o caso `(100, 10)` passava mesmo com o bug

`100 - 10 = 90` e `100 * (1 - 10/100) = 90`.

Os dois cálculos coincidem quando `price - discount == price * (1 - discount/100)`, o que simplifica para `discount == price * discount / 100`, ou seja, `100 == price`. Só funciona quando o preço é exatamente 100.

Esse é o ponto mais sutil da prova: o candidato que testar apenas com preço 100 vai achar que está tudo certo.

---

## Testes que falham antes da correção

| Teste | Entrada | Resultado errado | Resultado esperado |
|---|---|---|---|
| `test_applies_twenty_five_percent_discount` | price=200, discount=25 | 175.0 | 150.0 |
| `test_full_discount_returns_zero` | price=50, discount=100 | -50.0 | 0.0 |
| `test_keeps_two_decimal_places` | price=19.99, discount=15 | 4.99 | 16.99 |
| `test_request_with_decimal_values` (HTTP) | price=250, discount=20 | 230.0 | 200.0 |

---

## Resultado esperado após a correção

```
pytest backend/
```

```
14 passed in 0.XX s
```

---

## O que avaliar na entrega do candidato

- **Identificou corretamente o bug?** A descrição dele deve mencionar o cálculo percentual errado, não apenas "a fórmula estava errada".
- **Fez a menor mudança possível?** A correção ideal é apenas uma linha. Reescritas desnecessárias são sinal de insegurança.
- **Não alterou os testes?** Os testes estão corretos. Qualquer alteração neles deve ser justificada.
- **Frontend continua funcionando?** Após a correção do backend, o frontend deve exibir os valores certos sem nenhuma mudança.
- **Entendeu o caso do preço 100?** Candidatos mais atentos vão notar e comentar a coincidência.
