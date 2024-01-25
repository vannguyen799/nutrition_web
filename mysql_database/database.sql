CREATE TABLE Dish (
  id              int(10) NOT NULL AUTO_INCREMENT, 
  name            varchar(100) NOT NULL UNIQUE, 
  image           varchar(200) NOT NULL, 
  kcal            int(10) NOT NULL, 
  refuse_rate     int(11) NOT NULL, 
  description     text, 
  DishCategory_id int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE Dish_Nutrient (
  Dish_id     int(10) NOT NULL, 
  Nutrient_id int(10) NOT NULL, 
  value       real, 
  PRIMARY KEY (Dish_id, 
  Nutrient_id));
CREATE TABLE DishCategory (
  id              int(10) NOT NULL AUTO_INCREMENT, 
  name            varchar(100) NOT NULL UNIQUE, 
  description     text, 
  DishCategory_id int(10), 
  image           varchar(200), 
  PRIMARY KEY (id));
CREATE TABLE Food (
  id          int(10) NOT NULL AUTO_INCREMENT, 
  name        varchar(100) NOT NULL UNIQUE, 
  description text, 
  image       varchar(200), 
  PRIMARY KEY (id));
CREATE TABLE Food_Dish (
  Food_id int(10) NOT NULL, 
  Dish_id int(10) NOT NULL, 
  value   real NOT NULL, 
  count   int(10) DEFAULT 1 NOT NULL, 
  PRIMARY KEY (Food_id, 
  Dish_id));
CREATE TABLE Food_FoodCategory (
  Food_id         int(10) NOT NULL, 
  FoodCategory_id int(10) NOT NULL, 
  PRIMARY KEY (Food_id, 
  FoodCategory_id));
CREATE TABLE FoodArticle (
  id               int(10) NOT NULL AUTO_INCREMENT, 
  title            varchar(200) NOT NULL, 
  content          text NOT NULL, 
  image            varchar(200), 
  time_spend       int(11) NOT NULL, 
  created_date     timestamp default current_timestamp, 
  last_update_date timestamp default current_timestamp, 
  is_published     BOOL, 
  Food_id          int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE FoodArticleComment (
  FoodArticle_id int(10) NOT NULL, 
  id             int(11) NOT NULL AUTO_INCREMENT, 
  content        text NOT NULL, 
  rate           int(11),
  created_date   timestamp default current_timestamp,
  is_hidden      BOOL DEFAULT false,
  is_anonymous   BOOL DEFAULT false,
  User_id        int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE FoodCategory (
  id          int(10) NOT NULL AUTO_INCREMENT, 
  name        varchar(100) NOT NULL UNIQUE, 
  description text, 
  image       varchar(200), 
  PRIMARY KEY (id));
CREATE TABLE FoodMenu (
  id              int(10) NOT NULL AUTO_INCREMENT, 
  FoodMenuList_id int(10) NOT NULL, 
  for_date        datetime NULL, 
  PRIMARY KEY (id));
CREATE TABLE FoodMenu_Food (
  FoodMenu_id int(10) NOT NULL, 
  Food_id     int(10) NOT NULL, 
  PRIMARY KEY (FoodMenu_id, 
  Food_id));
CREATE TABLE FoodMenuList (
  id             int(10) NOT NULL AUTO_INCREMENT, 
  name           varchar(100) NOT NULL, 
  created_date   date NOT NULL, 
  PeopleGroup_id int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE Nutrient (
  id                  int(10) NOT NULL AUTO_INCREMENT, 
  name                varchar(100) NOT NULL UNIQUE, 
  unit                varchar(100) NOT NULL, 
  description         text, 
  NutrientCategory_id int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE NutrientCategory (
  id          int(10) NOT NULL AUTO_INCREMENT, 
  name        varchar(100) NOT NULL UNIQUE, 
  description text, 
  image       varchar(200), 
  PRIMARY KEY (id));
CREATE TABLE People (
  id             int(10) NOT NULL AUTO_INCREMENT, 
  name           varchar(100) NOT NULL, 
  height         real NOT NULL, 
  weight         real NOT NULL, 
  age            int(10) NOT NULL, 
  gender         BOOL NOT NULL, 
  relationship   varchar(100), 
  PeopleGroup_id int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE PeopleGroup (
  id      int(10) NOT NULL AUTO_INCREMENT, 
  name    varchar(100) NOT NULL, 
  User_id int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE Permission (
  id   int(10) NOT NULL AUTO_INCREMENT, 
  name varchar(100) NOT NULL UNIQUE, 
  PRIMARY KEY (id));
CREATE TABLE `User` (
  id            int(10) NOT NULL AUTO_INCREMENT, 
  username      varchar(50) NOT NULL UNIQUE, 
  password      varchar(100) NOT NULL, 
  email         varchar(100) NOT NULL UNIQUE, 
  phone_number  int(20) UNIQUE, 
  created_date  timestamp default current_timestamp, 
  is_locked     BOOL DEFAULT false NOT NULL, 
  is_active     BOOL DEFAULT false NOT NULL, 
  permission_id int(10) NOT NULL, 
  firstname     varchar(100) DEFAULT 'unknown', 
  lastname      varchar(100) DEFAULT 'unknown', 
  address       varchar(200) DEFAULT 'unknown', 
  PRIMARY KEY (id));
ALTER TABLE FoodArticleComment ADD CONSTRAINT FKFoodArticl958827 FOREIGN KEY (User_id) REFERENCES `User` (id);
ALTER TABLE FoodArticleComment ADD CONSTRAINT FKFoodArticl665158 FOREIGN KEY (FoodArticle_id) REFERENCES FoodArticle (id);
ALTER TABLE DishCategory ADD CONSTRAINT FKDishCatego774090 FOREIGN KEY (DishCategory_id) REFERENCES DishCategory (id);
ALTER TABLE FoodMenu_Food ADD CONSTRAINT FKFoodMenu_F471285 FOREIGN KEY (Food_id) REFERENCES Food (id);
ALTER TABLE FoodArticle ADD CONSTRAINT FKFoodArticl671543 FOREIGN KEY (Food_id) REFERENCES Food (id);
ALTER TABLE Food_FoodCategory ADD CONSTRAINT FKFood_FoodC728370 FOREIGN KEY (Food_id) REFERENCES Food (id);
ALTER TABLE Food_Dish ADD CONSTRAINT FKFood_Dish468166 FOREIGN KEY (Food_id) REFERENCES Food (id);
ALTER TABLE FoodMenuList ADD CONSTRAINT FKFoodMenuLi416209 FOREIGN KEY (PeopleGroup_id) REFERENCES PeopleGroup (id);
ALTER TABLE FoodMenu ADD CONSTRAINT FKFoodMenu843144 FOREIGN KEY (FoodMenuList_id) REFERENCES FoodMenuList (id);
ALTER TABLE FoodMenu_Food ADD CONSTRAINT FKFoodMenu_F216288 FOREIGN KEY (FoodMenu_id) REFERENCES FoodMenu (id);
ALTER TABLE PeopleGroup ADD CONSTRAINT FKPeopleGrou4243 FOREIGN KEY (User_id) REFERENCES `User` (id);
ALTER TABLE People ADD CONSTRAINT FKPeople246632 FOREIGN KEY (PeopleGroup_id) REFERENCES PeopleGroup (id);
ALTER TABLE Dish_Nutrient ADD CONSTRAINT FKDish_Nutri469155 FOREIGN KEY (Nutrient_id) REFERENCES Nutrient (id);
ALTER TABLE Dish_Nutrient ADD CONSTRAINT FKDish_Nutri15371 FOREIGN KEY (Dish_id) REFERENCES Dish (id);
ALTER TABLE Dish ADD CONSTRAINT FKDish238343 FOREIGN KEY (DishCategory_id) REFERENCES DishCategory (id);
ALTER TABLE Nutrient ADD CONSTRAINT FKNutrient740879 FOREIGN KEY (NutrientCategory_id) REFERENCES NutrientCategory (id);
ALTER TABLE Food_FoodCategory ADD CONSTRAINT FKFood_FoodC323066 FOREIGN KEY (FoodCategory_id) REFERENCES FoodCategory (id);
ALTER TABLE Food_Dish ADD CONSTRAINT FKFood_Dish568016 FOREIGN KEY (Dish_id) REFERENCES Dish (id);
ALTER TABLE `User` ADD CONSTRAINT FKUser642350 FOREIGN KEY (permission_id) REFERENCES Permission (id);
