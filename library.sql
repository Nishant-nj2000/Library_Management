-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(400) NOT NULL,
  `num_pages` int NOT NULL,
  `authors` varchar(400) NOT NULL,
  `average_rating` float NOT NULL,
  `isbn` varchar(30) NOT NULL,
  `isbn13` bigint NOT NULL,
  `language_code` varchar(100) NOT NULL,
  `publication_date` date NOT NULL,
  `publisher` varchar(400) NOT NULL,
  `ratings_count` bigint NOT NULL,
  `text_reviews_count` bigint NOT NULL,
  `stock` bigint NOT NULL DEFAULT '1',
  `total_stock` bigint NOT NULL DEFAULT '1',
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=45086 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (8,'Harry Potter Boxed Set  Books 1-5 (Harry Potter  #1-5)',2690,'J.K. Rowling/Mary GrandPré',4.78,'0439682584',9780439682589,'eng','2004-09-13','Scholastic',41428,164,8,8),(1226,'Life of Pi',401,'Yann Martel',3.91,'0156030209',9780156030205,'en-US','2004-05-03','Mariner Books / Harvest Books',4318,668,7,7),(2002,'Harry Potter Schoolbooks Box Set: Two Classic Books from the Library of Hogwarts School of Witchcraft and Wizardry',240,'J.K. Rowling',4.4,'043932162X',9780439321624,'eng','2001-01-11','Arthur A. Levine',11515,139,2,2),(3921,'London is the Best City in America',256,'Laura Dave',3.45,'0670037567',9780670037568,'eng','2006-05-18','Viking Adult',2168,233,8,8),(4681,'Reversible Errors (Kindle County Legal Thriller #6)',553,'Scott Turow',3.83,'0446612626',9780446612623,'eng','2003-11-01','Warner Vision',5073,222,9,9),(5700,'The Adolescent',647,'Fyodor Dostoyevsky/Richard Pevear/Larissa Volokhonsky',3.94,'0375719008',9780375719004,'eng','2004-12-07','Vintage',3568,159,4,4),(8598,'Eats  Shoots & Leaves: Why  Commas Really Do Make a Difference!',32,'Lynne Truss/Bonnie Timmons',4.15,'0399244913',9780399244919,'eng','2006-07-25','G.P. Putnam\'s Sons Books for Young Readers',1371,205,5,5),(10765,'A Year in the Merde',276,'Stephen Clarke',3.54,'1582346178',9781582346175,'en-US','2006-05-02','Bloomsbury Publishing PLC',11429,979,3,3),(10964,'Outlander (Outlander  #1)',850,'Diana Gabaldon',4.23,'0440242940',9780440242949,'eng','2005-07-26','Dell Publishing Company',673350,34690,3,4),(10970,'Outlander',254,'Matt Keefe',3.85,'184416411X',9781844164110,'eng','2006-12-26','Games Workshop(uk)',54,5,5,5),(10971,'Hydra\'s Ring (Outlanders  #39)',348,'James Axler',3.88,'0373638523',9780373638529,'eng','2006-11-01','Gold Eagle',25,2,2,2),(10972,'Omega Path (Outlanders  #4)',352,'James Axler',3.87,'0373638175',9780373638178,'en-US','1998-01-23','Gold Eagle',80,2,2,2),(11434,'Forgiven (Firstborn  #2)',358,'Karen Kingsbury',4.41,'0842387447',9780842387446,'eng','2005-09-23','Tyndale House Publishers',9804,172,6,6),(12240,'The Play Soldier',328,'Chet Green',4.5,'159113644X',9781591136446,'eng','2011-05-22','Booklocker.com  Inc.',2,2,11,11),(12496,'The Sunset Limited',160,'Cormac McCarthy',3.96,'0307278360',9780307278364,'eng','2006-10-24','Vintage',6494,562,5,7),(12937,'See You Around  Sam! (Sam Krupnik  #3)',128,'Lois Lowry/Diane deGroat',3.71,'0440414008',9780440414001,'eng','1998-03-09','Yearling',244,15,5,5),(15930,'Wokini: A Lakota Journey to Happiness and Self-Understanding',175,'Billy Mills/Nicholas Sparks',3.57,'1561706604',9781561706600,'eng','2003-06-01','Hay House',253,21,7,9),(16842,'A Single Man',192,'Christopher Isherwood',4.1,'0816638624',9780816638628,'eng','2001-03-20','Univ Of Minnesota Press',17451,1029,10,10),(17946,'Seven Nights',121,'Jorge Luis Borges/Eliot Weinberger',4.33,'0811209059',9780811209052,'eng','1985-05-29','New Directions Publishing Corporation',1037,60,1,1),(18892,'The Forest House (Avalon  #2)',462,'Marion Zimmer Bradley/Diana L. Paxson',3.86,'0451454243',9780451454249,'eng','1995-04-01','Roc',15171,322,1,1),(19801,'Goodbye  Darkness: A Memoir of the Pacific War',401,'William Manchester',4.18,'0316501115',9780316501118,'eng','2002-04-12','Back Bay Books',4936,174,5,5),(22067,'The Last Quarry (Quarry #7)',201,'Max Allan Collins',3.93,'0843955937',9780843955934,'eng','2006-08-01','Hard Crime Case',673,68,17,17),(27243,'Dancing in the Flames: The Dark Goddess in the Transformation of Consciousness',256,'Marion Woodman/Elinor Dickson',4.24,'1570623139',9781570623134,'eng','1997-05-06','Shambhala',375,24,4,4),(27695,'Nine Coaches Waiting',342,'Mary  Stewart/Sandra Brown',4.03,'1556526180',9781556526183,'eng','2006-01-05','Chicago Review Press',10640,905,10,11),(28869,'Pégate un tiro para sobrevivir: un viaje personal por la América de los mitos',272,'Chuck Klosterman',3.81,'8439720033',9788439720034,'spa','2006-02-28','Literatura Random House',27,2,4,5),(30071,'The Walking Dead  Book One (The Walking Dead #1-12)',304,'Robert Kirkman/Tony Moore/Charlie Adlard/Cliff Rathburn',4.35,'1582406197',9781582406190,'eng','2010-10-05','Image Comics',34751,1346,8,8),(30097,'The Eternal Champion (Eternal Champion  #1)',484,'Michael Moorcock',3.95,'1565041917',9781565041912,'eng','1996-02-01','White Wolf Games Studio',2524,40,12,12),(31389,'Life Management for Busy Woman: Growth and Study Guide',166,'Elizabeth George',4.53,'0736910190',9780736910194,'en-GB','2002-07-01','Harvest House Publishers',14,1,4,4),(32358,'James Dean: The Mutant King: A Biography',384,'David Dalton',4.07,'155652398X',9781556523984,'eng','2001-09-01','Chicago Review Press',491,29,3,3),(32637,'Imajica: The Reconciliation',544,'Clive Barker',4.42,'0061094153',9780061094156,'eng','1995-05-10','HarperTorch',2583,30,1,1),(33609,'Katherine',500,'Anya Seton/Philippa Gregory',4.19,'155652532X',9781556525322,'eng','2004-05-01','Chicago Review Press',25552,1637,17,17),(33904,'Swimming Upstream: Collaborative Approaches to Watershed Management',344,'Paul A. Sabatier/Will Focht/Mark Lubell/Zev Trachtenberg/Arnold Vedlitz/Marty Matlock',3.21,'0262693194',9780262693196,'eng','2005-04-29','The MIT Press',13,1,4,5),(34307,'Aches & Pains',99,'Maeve Binchy/Wendy Shea',3.53,'0385335105',9780385335102,'en-US','2000-06-13','Delacorte Press',356,30,9,10),(35149,'Star Wars: The Approaching Storm',344,'Alan Dean Foster',3.51,'0345443004',9780345443007,'eng','2002-12-01','Del Rey Books',3947,100,3,3),(36252,'Avalon',440,'Anya Seton/Philippa Gregory',3.87,'1556526008',9781556526008,'en-US','2006-05-01','Chicago Review Press',2857,158,3,3),(36368,'Suddenly Daddy (Suddenly #1)',256,'Loree Lough',3.78,'0373870280',9780373870288,'eng','1998-04-24','Love Inspired',37,1,3,3),(39763,'The Mystical Poems of Rumi 1: First Selection  Poems 1-200',208,'Rumi/A.J. Arberry',4.28,'0226731510',9780226731513,'eng','1974-03-15','University Of Chicago Press',114,8,1,1),(41909,'Harry Potter ve Sırlar Odası (Harry Potter  #2)',403,'J.K. Rowling/Sevin Okyay',4.42,'3570211029',9783570211021,'tur','2001-10-01','Yapı Kredi Yayınları',1000,41,13,13),(42864,'Lead Like Jesus: Lessons from the Greatest Leadership Role Model of All Time',239,'Kenneth H. Blanchard/Phil Hodges',4.04,'0849918723',9780849918728,'en-US','2007-03-01','W Publishing Group',808,41,25,25),(44949,'Write Great Code: Volume 1: Understanding the Machine',456,'Randall Hyde',3.92,'1593270038',9781593270032,'eng','2004-11-08','No Starch Press',145,12,6,6),(45085,'Zen in Your Garden',128,'Jenny Hendy',3.6,'1841811106',9781841811109,'eng','2003-01-04','Godsfield Press Ltd',7,2,5,5);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `m_name` varchar(45) NOT NULL,
  `mobile` bigint NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `m_address` varchar(200) NOT NULL,
  `total_amount_paid` bigint NOT NULL DEFAULT '0',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (7,'Nishant Jain',9521681348,'nj27nishant@gmail.com','New Colony, Dungarpur (Raj.)\r\n',750),(8,'Ajay Nagar',7889456123,'Ajay.Nagar@gmail.com','New Post Office Navrangpura Ahmedabad',600),(9,'Mitesh Patil',7894561239,'mitesh.patil@gmail.com','Bapu Bazaar Udaipur',920),(10,'Jaydeep Singh',7895563215,'jaydeep.singh@gmail.com','Old Bus Stand Naranpura',450),(11,'Pritesh Jain',7894562587,'pritesh.jain@gmail.com','Sg Highway Ahmedabad',250);
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `t_id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `member_id` int NOT NULL,
  `issue_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `total_rent` bigint NOT NULL DEFAULT '0',
  `rent_paid` varchar(3) DEFAULT 'no',
  `outstanding_amount` bigint NOT NULL DEFAULT '0',
  PRIMARY KEY (`t_id`),
  KEY `book_id_idx` (`book_id`),
  KEY `member_id_idx` (`member_id`),
  CONSTRAINT `book_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `member_id` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (120,1226,7,'2021-06-07','2021-06-07',400,'no',200),(121,3921,7,'2021-06-07','2021-06-07',100,'yes',0),(122,4681,8,'2021-06-07','2021-06-07',600,'yes',0),(123,5700,8,'2021-06-07','2021-06-07',100,'no',100),(124,10765,9,'2021-06-07','2021-06-07',620,'yes',0),(125,11434,9,'2021-06-07','2021-06-07',420,'no',220),(126,12240,10,'2021-06-07','2021-06-07',350,'yes',0),(127,12496,10,'2021-06-07',NULL,0,'no',0),(128,30071,11,'2021-06-07','2021-06-07',250,'yes',0),(129,34307,11,'2021-06-07',NULL,0,'no',0),(130,15930,7,'2021-06-07','2021-06-07',650,'yes',0),(131,12496,9,'2021-06-07',NULL,0,'no',0),(132,22067,10,'2021-06-07','2021-06-08',100,'yes',0),(133,30097,9,'2021-06-07','2021-06-08',150,'yes',0),(134,15930,8,'2021-06-07',NULL,0,'no',0),(135,15930,7,'2021-06-07',NULL,0,'no',0),(136,34307,7,'2021-06-07','2021-06-07',460,'no',460),(137,33904,11,'2021-06-07',NULL,0,'no',0),(138,27695,8,'2021-06-08',NULL,0,'no',0),(139,8598,9,'2021-06-08','2021-06-08',150,'yes',0),(140,28869,9,'2021-06-08',NULL,0,'no',0),(141,10964,10,'2021-06-08',NULL,0,'no',0);
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-09 17:14:28
