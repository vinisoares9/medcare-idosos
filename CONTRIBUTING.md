# Como contribuir

Obrigado por querer contribuir com o **MedCare Idosos**!

## Fluxo de Trabalho

1. Faça um **fork** do repositório
2. Crie uma **branch de feature**:
```bash
   git checkout -b feature/nome-da-feature
```
3. Faça suas alterações e commit:
```bash
   git commit -m "feat: descrição da mudança"
```
4. Envie para o seu fork:
```bash
   git push origin feature/nome-da-feature
```
5. Abra um **Pull Request** para a branch `main`

## Antes de abrir o PR

- [ ] Os testes passam: `pytest`
- [ ] O lint não aponta erros: `flake8 --max-line-length=99 medcare/ tests/ main.py`
- [ ] O CHANGELOG foi atualizado