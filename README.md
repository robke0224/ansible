# Container + Ansible demo

Trumpas setupas, skirtas laboratoriniui: sukuria web konteinerį (Flask + SQLite), ir Ansible controller konteinerį.

Paleidimas:

```bash
# statyti ir paleisti konteinerius
docker compose up --build -d

# atidaryti http://localhost:8000 ir pridėti komentarų

# paleisti Ansible playbook, kuris paleis valymo skriptą bendrame workspace
docker compose run --rm ansible ansible-playbook /workspace/ansible/remove_profanity.yml -i /workspace/ansible/inventory.ini
```

Ką dar galima daryti:
- redaguoti `webapp/profanities.txt` ir pridėti žodžius, kuriuos norite pašalinti
- peržiūrėti likusius komentarus puslapyje
