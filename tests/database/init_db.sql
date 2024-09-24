------------------------------------------------
-- DDL Statements for table "USER"
------------------------------------------------
CREATE TABLE "USER" (
    "id" INTEGER PRIMARY KEY,
    "email" VARCHAR(128) NOT NULL,
    "password" VARCHAR(128) NOT NULL,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
