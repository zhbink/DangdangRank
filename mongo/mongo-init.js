db.createUser(
        {
            user: "user",
            pwd: "MongoPassWd1",
            roles: [
                {
                    role: "readWrite",
                    db: "douBan"
                }
            ]
        }
);