
## Running postgresql image

Deploy container with db instance
```bash
docker compose up -d
```
Execute bash of the db container
```bash
docker exec -it db bash
```
Execute postgresql CLI
```bash
psql -h localhost -U postgres
```
