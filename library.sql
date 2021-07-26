-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: sql6.freesqldatabase.com    Database: sql6418281
-- ------------------------------------------------------
-- Server version	5.5.62-0ubuntu0.14.04.1

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
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(400) NOT NULL,
  `num_pages` int(11) NOT NULL,
  `authors` varchar(400) NOT NULL,
  `average_rating` float NOT NULL,
  `isbn` varchar(30) NOT NULL,
  `isbn13` bigint(20) NOT NULL,
  `language_code` varchar(100) NOT NULL,
  `publication_date` date NOT NULL,
  `publisher` varchar(400) NOT NULL,
  `ratings_count` bigint(20) NOT NULL,
  `text_reviews_count` bigint(20) NOT NULL,
  `stock` bigint(20) NOT NULL DEFAULT '1',
  `total_stock` bigint(20) NOT NULL DEFAULT '1',
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=45089 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (890,'Of Mice and Men',103,'John Steinbeck',3.87,'0142000671',9780142000670,'eng','2002-01-08','Penguin Books',1755253,25554,2,2),(1226,'Life of Pi',401,'Yann Martel',3.91,'0156030209',9780156030205,'en-US','2004-05-03','Mariner Books / Harvest Books',4318,668,22,23),(1320,'Gita on the Green',176,'Stephen J. Rosen/Steven Pressfield',3.78,'0826413013',9780826413017,'en-US','2002-05-30','Continuum',14,2,15,15),(1429,'The Fifth Mountain',256,'Paulo Coelho/Clifford E. Landers',3.62,'0060930136',9780060930134,'en-US','2000-04-26','HarperOne',1415,68,5,1),(2002,'Harry Potter Schoolbooks Box Set: Two Classic Books from the Library of Hogwarts School of Witchcraft and Wizardry',240,'J.K. Rowling',4.4,'043932162X',9780439321624,'eng','2001-01-11','Arthur A. Levine',11515,139,7,7),(2123,'The 36-Hour Day: A Family Guide to Caring for Persons with Alzheimer Disease  Related Dementing Illnesses  and Memory Loss in Later Life',624,'Nancy L. Mace/Peter V. Rabins',4.24,'0446618764',9780446618762,'eng','2006-11-01','Grand Central Life & Style',69,6,20,20),(2336,'Tandia',905,'Bryce Courtenay',4.05,'0140272925',9780140272925,'eng','1998-08-31','Penguin Books Australia Ltd.',8461,369,46,46),(2543,'Las intermitencias de la muerte',274,'José Saramago/Pilar del Río',4,'9587043642',9789587043648,'spa','2005-12-01','Alfaguara',2862,306,20,20),(2713,'The Portable Chaucer',611,'Geoffrey Chaucer/Theodore Morrison',3.86,'0140150811',9780140150810,'eng','1977-05-26','Penguin Books',70,8,50,50),(2912,'Escape from Fire Mountain (World of Adventure  #3)',80,'Gary Paulsen/Steve Chorney',3.67,'0440410258',9780440410256,'eng','1995-01-01','Yearling',114,17,20,20),(3690,'The Power and the Glory',222,'Graham Greene/John Updike',4,'0142437301',9780142437308,'eng','2003-02-25','Penguin Books',25490,1585,2,3),(3750,'Moonraker (James Bond  #3)',247,'Ian Fleming',3.74,'0142002062',9780142002063,'eng','2002-12-31','Penguin Books',15204,780,1,1),(3921,'London is the Best City in America',256,'Laura Dave',3.45,'0670037567',9780670037568,'eng','2006-05-18','Viking Adult',2168,233,8,8),(4681,'Reversible Errors (Kindle County Legal Thriller #6)',553,'Scott Turow',3.83,'0446612626',9780446612623,'eng','2003-11-01','Warner Vision',5073,222,8,9),(5700,'The Adolescent',647,'Fyodor Dostoyevsky/Richard Pevear/Larissa Volokhonsky',3.94,'0375719008',9780375719004,'eng','2004-12-07','Vintage',3568,159,4,4),(9742,'The Audacity of Hope: Thoughts on Reclaiming the American Dream',375,'Barack Obama',3.75,'0307237699',9780307237699,'eng','2006-10-17','Crown',127324,4496,20,20),(10765,'A Year in the Merde',276,'Stephen Clarke',3.54,'1582346178',9781582346175,'en-US','2006-05-02','Bloomsbury Publishing PLC',11429,979,10,10),(10964,'Outlander (Outlander  #1)',850,'Diana Gabaldon',4.23,'0440242940',9780440242949,'eng','2005-07-26','Dell Publishing Company',673350,34690,3,4),(10970,'Outlander',254,'Matt Keefe',3.85,'184416411X',9781844164110,'eng','2006-12-26','Games Workshop(uk)',54,5,24,25),(10971,'Hydra\'s Ring (Outlanders  #39)',348,'James Axler',3.88,'0373638523',9780373638529,'eng','2006-11-01','Gold Eagle',25,2,2,2),(10972,'Omega Path (Outlanders  #4)',352,'James Axler',3.87,'0373638175',9780373638178,'en-US','1998-01-23','Gold Eagle',80,2,3,5),(11434,'Forgiven (Firstborn  #2)',358,'Karen Kingsbury',4.41,'0842387447',9780842387446,'eng','2005-09-23','Tyndale House Publishers',9804,172,6,6),(11910,'Mr. Sammler\'s Planet',288,'Saul Bellow/Stanley Crouch',3.76,'0142437832',9780142437834,'eng','2004-01-06','Penguin Classics',2721,135,1,1),(12240,'The Play Soldier',328,'Chet Green',4.5,'159113644X',9781591136446,'eng','2011-05-22','Booklocker.com  Inc.',2,2,11,11),(12496,'The Sunset Limited',160,'Cormac McCarthy',3.96,'0307278360',9780307278364,'eng','2006-10-24','Vintage',6494,562,6,7),(12937,'See You Around  Sam! (Sam Krupnik  #3)',128,'Lois Lowry/Diane deGroat',3.71,'0440414008',9780440414001,'eng','1998-03-09','Yearling',244,15,5,5),(14257,'English Passengers',446,'Matthew Kneale',4.06,'038549744X',9780385497442,'eng','2001-01-16','Anchor',4863,409,30,30),(14258,'English Passengers',462,'Matthew Kneale',4.06,'0140285210',9780140285215,'en-GB','2001-04-26','Penguin',537,65,15,15),(15004,'First Love: A Gothic Tale',86,'Joyce Carol Oates/Barry Moser/Erhan Sunar',3.19,'088001508X',9780880015080,'eng','1997-08-21','Ecco',579,83,20,20),(15867,'Mugglenet.Com\'s What Will Happen in Harry Potter 7: Who Lives  Who Dies  Who Falls in Love and How Will the Adventure Finally End?',216,'Ben Schoen/Andy Gordon/Gretchen Stull/Emerson Spartz/Jamie Lawrence',4.23,'1569755833',9781569755839,'en-GB','2006-10-19','Ulysses Press',9023,112,5,5),(15877,'Ultimate Unofficial Guide to the Mysteries of Harry Potter: Analysis of Books 1-4',412,'Galadriel Waters/Astre Mithrandir',4.05,'0972393617',9780972393614,'en-US','2003-01-01','Wizarding World Press',2774,37,5,5),(15930,'Wokini: A Lakota Journey to Happiness and Self-Understanding',175,'Billy Mills/Nicholas Sparks',3.57,'1561706604',9781561706600,'eng','2003-06-01','Hay House',253,21,7,9),(16842,'A Single Man',192,'Christopher Isherwood',4.1,'0816638624',9780816638628,'eng','2001-03-20','Univ Of Minnesota Press',17451,1029,5,5),(18892,'The Forest House (Avalon  #2)',462,'Marion Zimmer Bradley/Diana L. Paxson',3.86,'0451454243',9780451454249,'eng','1995-04-01','Roc',15171,322,91,91),(19148,'The Divine Comedy  Vol. I: Inferno',432,'Dante Alighieri/Mark Musa',4,'0140444416',9780140444414,'eng','1984-11-28','Penguin Classics',305,19,1,1),(19155,'The Divine Comedy  Vol. 1: Inferno',432,'Dante Alighieri/Mark Musa',4,'0142437220',9780142437223,'eng','2003-02-27','Penguin Classics',2172,166,1,1),(19411,'The Portable Gibbon: The Decline and Fall of the Roman Empire',691,'Edward Gibbon/Dero A. Saunders/Charles Alexander Robinson Jr.',3.98,'0140150609',9780140150605,'eng','1977-06-30','Penguin Books',2,1,1,1),(19801,'Goodbye  Darkness: A Memoir of the Pacific War',401,'William Manchester',4.18,'0316501115',9780316501118,'eng','2002-04-12','Back Bay Books',4936,174,5,5),(21075,'Citizens: A Chronicle of the French Revolution',825,'Simon Schama',3.99,'0141017279',9780141017273,'en-GB','2004-08-05','Penguin',90,12,5,1),(22067,'The Last Quarry (Quarry #7)',201,'Max Allan Collins',3.93,'0843955937',9780843955934,'eng','2006-08-01','Hard Crime Case',673,68,17,17),(23929,'Selected Letters  1940-1956',656,'Jack Kerouac/Ann Charters',4.13,'0140234446',9780140234442,'eng','1996-03-01','Penguin (Non-Classics)',804,21,1,1),(25257,'Mein Urgroßvater  die Helden und ich',250,'James Krüss',4.3,'3551552711',9783551552716,'ger','2002-12-01','Carlsen',16,1,20,20),(26860,'Michael\'s Golden Rules',32,'Deloris Jordan/Roslyn M. Jordan/Michael Jordan/Kadir Nelson',3.93,'0689870167',9780689870163,'eng','2007-01-23','Simon  Schuster/Paula Wiseman Books',83,22,5,5),(27243,'Dancing in the Flames: The Dark Goddess in the Transformation of Consciousness',256,'Marion Woodman/Elinor Dickson',4.24,'1570623139',9781570623134,'eng','1997-05-06','Shambhala',375,24,4,4),(27695,'Nine Coaches Waiting',342,'Mary  Stewart/Sandra Brown',4.03,'1556526180',9781556526183,'eng','2006-01-05','Chicago Review Press',10640,905,12,14),(28869,'Pégate un tiro para sobrevivir: un viaje personal por la América de los mitos',272,'Chuck Klosterman',3.81,'8439720033',9788439720034,'spa','2006-02-28','Literatura Random House',27,2,25,25),(29289,'Lentil',64,'Robert McCloskey',4.13,'0140502874',9780140502879,'eng','1978-04-27','Puffin Books',4076,104,20,20),(29680,'The Coen Brothers: Interviews',208,'William Rodney Allen',3.82,'1578068894',9781578068890,'eng','2006-08-18','University Press of Mississippi',73,3,20,20),(30071,'The Walking Dead  Book One (The Walking Dead #1-12)',304,'Robert Kirkman/Tony Moore/Charlie Adlard/Cliff Rathburn',4.35,'1582406197',9781582406190,'eng','2010-10-05','Image Comics',34751,1346,8,8),(30097,'The Eternal Champion (Eternal Champion  #1)',484,'Michael Moorcock',3.95,'1565041917',9781565041912,'eng','1996-02-01','White Wolf Games Studio',2524,40,12,12),(30118,'A Light in the Attic',176,'Shel Silverstein',4.34,'0060513063',9780060513061,'eng','2002-10-07','Harpercollins Childrens Books',349247,2567,5,5),(30247,'A Stolen Season (Alex McKnight  #7)',304,'Steve Hamilton',3.96,'031235360X',9780312353605,'eng','2006-09-05','Minotaur Books',1889,137,22,22),(30659,'Meditations',303,'Marcus Aurelius/Martin Hammond/Albert Wittstock/Diskin Clay',4.23,'0140449337',9780140449334,'eng','2006-04-27','Penguin Books',76332,3206,1,1),(31389,'Life Management for Busy Woman: Growth and Study Guide',166,'Elizabeth George',4.53,'0736910190',9780736910194,'en-GB','2002-07-01','Harvest House Publishers',14,1,4,4),(31434,'The Poetry of Sylvia Plath',202,'Claire Brennan',4.25,'0231124279',9780231124270,'eng','2001-08-29','Columbia University Press',27,0,2,2),(31819,'Harry Potter and Philosophy: If Aristotle Ran Hogwarts',243,'David Baggett/Shawn E. Klein',4.48,'0812694554',9780812694550,'eng','2004-09-10','Open Court',11422,78,5,5),(32358,'James Dean: The Mutant King: A Biography',384,'David Dalton',4.07,'155652398X',9781556523984,'eng','2001-09-01','Chicago Review Press',491,29,3,3),(32637,'Imajica: The Reconciliation',544,'Clive Barker',4.42,'0061094153',9780061094156,'eng','1995-05-10','HarperTorch',2583,30,21,22),(32816,'The Canterbury Tales: Fifteen Tales and the General Prologue',600,'Geoffrey Chaucer/V.A. Kolve/Glending Olson',3.95,'0393925870',9780393925876,'enm','2005-08-01','W. W. Norton & Company',1149,41,20,20),(33008,'North Carolina Weekends',353,'Lynn Setzer',3.71,'0895872730',9780895872739,'en-US','2003-10-01','John F. Blair  Publisher',7,1,5,5),(33308,'There\'s No Toilet Paper . . . on the Road Less Traveled: The Best of Travel Humor and Misadventure',216,'Doug Lansky',3.38,'1932361278',9781932361278,'eng','2005-11-16','Travelers\' Tales',413,53,20,20),(33513,'The White Man\'s Burden: Why the West\'s Efforts to Aid the Rest Have Done So Much Ill and So Little Good',436,'William Easterly',3.83,'0143038826',9780143038825,'eng','2007-03-01','Penguin Books',4473,232,1,1),(33609,'Katherine',500,'Anya Seton/Philippa Gregory',4.19,'155652532X',9781556525322,'eng','2004-05-01','Chicago Review Press',25552,1637,10,2),(33928,'Full House: The Spread of Excellence from Plato to Darwin',256,'Stephen Jay Gould',3.96,'0609801406',9780609801406,'eng','1997-09-16','Three Rivers Press (CA)',1630,84,30,30),(34307,'Aches & Pains',99,'Maeve Binchy/Wendy Shea',3.53,'0385335105',9780385335102,'en-US','2000-06-13','Delacorte Press',356,30,9,10),(35149,'Star Wars: The Approaching Storm',344,'Alan Dean Foster',3.51,'0345443004',9780345443007,'eng','2002-12-01','Del Rey Books',3947,100,3,3),(36252,'Avalon',440,'Anya Seton/Philippa Gregory',3.87,'1556526008',9781556526008,'en-US','2006-05-01','Chicago Review Press',2857,158,20,20),(36368,'Suddenly Daddy (Suddenly #1)',256,'Loree Lough',3.78,'0373870280',9780373870288,'eng','1998-04-24','Love Inspired',37,1,3,3),(39763,'The Mystical Poems of Rumi 1: First Selection  Poems 1-200',208,'Rumi/A.J. Arberry',4.28,'0226731510',9780226731513,'eng','1974-03-15','University Of Chicago Press',114,8,3,3),(40395,'A Princess of Mars (Barsoom  #1)',186,'Edgar Rice Burroughs/John Seelye',3.81,'0143104888',9780143104889,'eng','2007-01-30','Penguin Books',38926,2355,10,1),(41304,'strangers from a different shore: a history of asian americans',640,'ronald takaki',4.13,'0316831301',9780316831307,'en-us','1998-09-23','back bay books',888,45,1,1),(41909,'Harry Potter ve Sırlar Odası (Harry Potter  #2)',403,'J.K. Rowling/Sevin Okyay',4.42,'3570211029',9783570211021,'tur','2001-10-01','Yapı Kredi Yayınları',1000,41,18,18),(42864,'Lead Like Jesus: Lessons from the Greatest Leadership Role Model of All Time',239,'Kenneth H. Blanchard/Phil Hodges',4.04,'0849918723',9780849918728,'en-US','2007-03-01','W Publishing Group',808,41,25,25),(44145,'The Bar on the Seine',160,'Georges Simenon/David Watson',3.69,'0143038311',9780143038313,'en-US','2006-12-26','Penguin Books',380,54,40,40),(44229,'The Silver Pigs (Marcus Didius Falco  #1)',241,'Lindsey Davis',3.94,'0345369076',9780345369079,'eng','1991-02-13','Fawcett Books',144,26,20,20),(44949,'Write Great Code: Volume 1: Understanding the Machine',456,'Randall Hyde',3.92,'1593270038',9781593270032,'eng','2004-11-08','No Starch Press',145,12,6,6),(45085,'Zen in Your Garden',128,'Jenny Hendy',3.6,'1841811106',9781841811109,'eng','2003-01-04','Godsfield Press Ltd',7,2,5,5);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `m_name` varchar(45) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `m_address` varchar(200) NOT NULL,
  `total_amount_paid` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (22,'Nishant Jain',9521681348,'nishant.nj2000@gmail.com','Jai Hind Nagar Street no. 6\r\nNear Subhash Park, New Colony\r\nDungarpur (Raj.)',1200),(25,'Nitesh Sharma',7854691234,'Nitesh.sharma2021@gmail.com','Maninagar Ahmedabad',350),(27,'Pritesh Jain',7845961237,'Pritesh.jain2021@gmail.com','Vijay Cross Road Ahmedabad',200),(29,'Faris Ansari',7778887778,'faris@ansari.com','India',200);
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `t_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `issue_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `total_rent` bigint(20) NOT NULL DEFAULT '0',
  `rent_paid` varchar(3) DEFAULT 'no',
  `outstanding_amount` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`t_id`),
  KEY `book_id_idx` (`book_id`),
  KEY `member_id_idx` (`member_id`),
  CONSTRAINT `book_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `member_id` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=164 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (149,1226,22,'2021-06-12','2021-06-12',150,'no',150),(150,4681,25,'2021-06-12','2021-06-12',160,'no',160),(151,10765,22,'2021-06-12','2021-06-12',350,'yes',0),(153,10972,25,'2021-06-12','2021-06-12',350,'yes',0),(154,12496,22,'2021-06-12','2021-06-12',450,'yes',0),(155,1226,27,'2021-06-12',NULL,0,'no',0),(156,44949,29,'2021-06-23','2021-06-23',200,'yes',0),(157,15867,27,'2021-07-11','2021-07-26',200,'yes',0),(159,3690,22,'2021-07-26',NULL,0,'no',0),(160,11910,22,'2021-07-26','2021-07-26',100,'0',20),(161,890,22,'2021-07-26','2021-07-26',400,'yes',0),(162,30659,27,'2021-07-26','2021-07-26',250,'no',250),(163,890,29,'2021-07-26',NULL,0,'no',0);
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

-- Dump completed on 2021-07-26 19:55:14
