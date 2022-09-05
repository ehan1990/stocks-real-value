db-up:
	docker run --name db -p 27017:27017 -v persistence:/data/db -d mongo mongod

db-ssh:
	docker exec -it db bash

apple:
	@curl -s localhost:8080/stocks/aapl

# TICKER=aapl make stock
stock:
	@curl -s localhost:8080/stocks/${TICKER}

health:
	@curl -s localhost:8080/healthcheck | jq
