# DangdangRank
 Scrapy爬虫：当当网图书销量排行数据

pip install -r requirement.txt


```
 docker exec -it mongodb mongo admin
db.auth("admin", "MongoPassWd1")
db.createUser({ user: "user1", pwd: "MongoPassWd1", roles: [{ role: "readWrite", db: "douBan" }, {role: "readWrite", db: "DjangoServer"}] })
```

```
mongodb://user1:MongoPassWd1@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false
```

scrapy crawl dangdang -a year=2020
