## The Doge Project

每次马斯克在推特上写关于区块链，比特币，或者狗狗币的时候，通过 Kraken 或者类似的API来买狗狗币

### 目前状态

在等推特批准我们的推特程序员账号。用了账号我们就能调用推特API

### 用的编程语言是什么？

什么语言都可以。目前选了 python 因为好写

### 程序在哪里跑？

任何 kubernetes cluster 都可以

### 创造本地 kubernetes cluster
```
make install-kubectl
make install-kube-container
make create-cluster
```

### 本地运行 cron docker 镜像
```
make build
make run
```

### 部署到本地 kubernetes cluster
```
make deploy
```