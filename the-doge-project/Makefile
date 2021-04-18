
build:
	docker-compose build

create-cluster:
	./kube-cluster-setup/create-cluster.sh

delete-cluster:
	kind delete cluster

deploy:
	kubectl apply -f deployment/cron-deployment.yaml

install-kube-container:
	curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.10.0/kind-linux-amd64
	chmod +x ./kind
	mv ./kind /usr/local/bin

install-kubectl:
	curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
	mv kubectl /usr/local/bin

run:
	docker-compose run doge-job
