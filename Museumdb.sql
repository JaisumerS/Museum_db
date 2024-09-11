Drop Database If Exists Museumdb;
Create Database Museumdb;
Use Museumdb;

Create Table Art_Object
(ID_No				Int(5)		Not Null,
Title				Varchar(50)	Not Null,
Descript			Varchar(80)	Not Null,
Yearcr				Varchar(10)	Not Null,
Epoch				Varchar(30)	Not Null,
Culture_of_origin	Varchar(15)	Not Null,
Collection_name		Varchar(70) Not Null,
Artist_name			Varchar(30),
Exhibition_name		Varchar(70),

Constraint	ARTID	Primary Key(ID_No)
);

Create Table Exhibition
(Ename		Varchar(70) Not Null,
End_date	Varchar(10)	Not Null,
Start_date	Varchar(10)	Not Null,

Constraint EN	Primary Key(Ename)
);

Create Table Artist
(Aname				Varchar(30)	Not Null,
Obj_ID				Int(5)		Not Null,
Adescription		Varchar(50)	Not Null,
Country_of_origin	Varchar(20)	Not Null,
Epoch				Varchar(50)	Not Null,
main_style			Varchar(20) Not Null,
Date_died			Varchar(10),
Date_born			Varchar(10),

Constraint	AP	Primary Key(Aname, Obj_ID),
Constraint	AID	Foreign Key(Obj_ID)	References Art_Object(ID_No)
);

Create Table Painting
(ID_no		Int(5)		Not Null,
Paint_Type	Varchar(20)	Not Null,
Style		Varchar(20)	Not Null,
Drawn_on	Varchar(20)	Not Null,

Constraint PID	Primary Key(ID_no),
Constraint PIDF	Foreign Key(ID_no) References Art_Object(ID_No) On Delete cascade On Update cascade
);

Create Table Statue
(ID_no		Int(5)		Not Null,
Style		Varchar(20)	Not Null,
Weight_lb	Int			Not Null,
Height_cm	Int			Not Null,
Material	Varchar(20)	Not Null,

Constraint STID		Primary Key(ID_No),
Constraint STIDF	Foreign Key(ID_no) References Art_Object(ID_No) On Delete cascade On Update cascade
);

Create Table Sculpture
(ID_no		Int(5)		Not Null,
Style		Varchar(20)	Not Null,
Weight_lb	Int			Not Null,
Height_cm	Int			Not Null,
Material	Varchar(25)	Not Null,

Constraint SCID		Primary Key(ID_No),
Constraint SCIDF	Foreign Key(ID_no) References Art_Object(ID_No) On Delete cascade On Update cascade
);

Create Table Other
(ID_no	Int(5)		Not Null,
Otype	Varchar(15)	Not Null,
Style	Varchar(30)	Not Null,

Constraint OID	Primary Key(ID_no),
Constraint OIDF	Foreign Key(ID_no) References Art_Object(Id_No) On Delete cascade On Update cascade
);

Create Table Collections
(Collection_name		Varchar(70)	Not Null	DEFAULT 'missing',
Ctype					Varchar(20)	Not Null,
Cdesc					Varchar(80)	Not Null,
Address					Varchar(30)	Not Null,
Phone					Int(15)		Not Null,
Current_Contact_Person	Varchar(30)	Not Null,

Constraint CN	Primary Key(Collection_name)
);

Create Table Permanent_Collection
(Collection_name		Varchar(70)	Not Null,
Pstatus					Varchar(10)	Not Null,
Cost					Int			Not Null,
Date_acquired			Varchar(10)	Not Null,

Constraint CNP	Primary Key(Collection_name),
Constraint CNPFK Foreign Key(Collection_name) References Collections(Collection_name)
);

Create Table Borrowed_Collection
(Collection_name		Varchar(70)	Not Null,
Borrowed_from			Varchar(20)	Not Null,
Date_borrowed			Varchar(10)	Not Null,
Date_returned			Varchar(10)	Not Null,

Constraint CNB	Primary Key(Collection_name),
Constraint CNBFK Foreign Key(Collection_name) References Collections(Collection_name)
);
    
Insert Into Exhibition Value
	('The Tudors: Art and Majesty in Renaissance England','01-08-2023','10-10-2022'),
    ('Cubism and the Trompe l\'Oeil Tradition','01-22-2023','10-20-2022'),
    ('Hear Me Now: The Black Potters of Old Edgefield, South Carolina','02-05-2023','09-09-2022'),
    ('Cosmic Buddhas in the Himalayas','12-10-2017','06-24-2017');
    
Insert Into Art_Object Value
	(11111,'Portrait Bust of John Fisher','Bishop of Rochester and confessor to Henry VIII\'s first queen','1510–15','Renaissance','British','The Met Collection','Pietro Torrigiano','The Tudors: Art and Majesty in Renaissance England'),
    (22222,'The Absinthe Glass','The relationship between the real spoon and the modeled glass','1914','Renaissance','Italian','Leonard A. Lauder Cubist Collection','Pablo Picasso','Cubism and the Trompe l\'Oeil Tradition'),
    (33333,'Still Life—Violin and Music','Flat but reveals depth and tension between illusion and reality', '1888', 'American Trompe', 'American','Collection of C. Philip and Corbett Toussaint', 'William Michael Harnett', 'Cubism and the Trompe l\'Oeil Tradition'),
    (44444,'Trompe l\'Oeil Still Life', 'An object that seemingly crosses over into the viewer\'s space', '1658', 'Dutch Golden Age', 'Dutch', 'The Art Institute of Chicago', 'Adriaen van der Spelt', 'Cubism and the Trompe l\'Oeil Tradition'),
    (55555,'Tray','delicately executed cast shadows make the paper appear to lift','1760','Industrial Revolution','French','Musée National de Céramique',Null,'Cubism and the Trompe l\'Oeil Tradition'),
    (66666,'Fragment', 'personal expression, contributing to the historical', '1866', 'Reconstruction era', 'American', 'Collection of C. Philip and Corbett Toussaint', 'David Drake', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
    (77777,'Power figure', 'Nkisi Nkondi, are sacred objects infused with spiritual energy.', '1850', 'Renaissance', 'Kongo', 'University of Michigan Museum of Art', Null,'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
    (88888,'Armor Garniture of George Clifford', 'This armor features the Tudor rose and Elizabeth\'s cipher', '1586', 'Elizabethan period', 'Greenwich', 'Munsey Fund', 'Jacob Halder', 'The Tudors: Art and Majesty in Renaissance England'),
    (99999,'Floor Mosaic of Ktisis','Ktisis, a figure personifying the act of generous donation','500-550','Migration Period','African','Harris Brisbane Dick Fund',Null,'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
    (00000,'Shield of Henry II',' Shield of Henry II of France (reigned 1547–59)','1555','Renaissance','French','Harris Brisbane Dick Fund',Null,'The Tudors: Art and Majesty in Renaissance England'),
    (01111,'Gondola prow','The arms are of the Dolfini family of Venice','1700-1799','Renaissance','Italian','Harris Brisbane Dick Fund',Null,Null),
    (02222,'Crowned Buddha','Evokes the special form of Buddha as a cakravartin','800-899','Pala Period','Indian','University of Michigan Museum of Art',Null,'Cosmic Buddhas in the Himalayas'),
    (03333,'Seated Buddha','Earliest iconic representations of Shakyamuni','150','Pala Period','Indian','University of Michigan Museum of Art',Null,'Cosmic Buddhas in the Himalayas'),
    (04444,'Door Guardian (Dvarapala)','Significance as a protective deity','300-399','Pala-Sena Period','Pakistan','University of Michigan Museum of Art',Null,'Cosmic Buddhas in the Himalayas');
    
Insert Into Sculpture Value
	(11111,'Historical Figure',62,66,'Polychrome terracotta'),
    (22222,'Realism',20,23,'Perforated Tin'),
    (02222,'Cultural Beings',17,52,'Brass'),
    (03333,'Cultural Beings',6,17,'Bronze'),
    (04444,'Cultural Beings',30,46,'Stucco');
    
Insert Into Painting Value
	(33333,'Oil','realism','canvas'),
    (44444,'Oil','realism','panel');

Insert Into Other Value
	(55555,'Ceramics','Tin-glazed earthenware'),
    (66666,'Pot fragment','Alkaline-glazed stoneware'),
    (99999,'Floor fragment','Mosaic'),
    (00000,'Shield','Metalwork'),
    (01111,'Prow','Metalwork');
    
Insert Into Statue Value
	(77777,'Culture History',40,104,'Wood/Iron/Nails'),
	(88888,'Armour for Men',60,177,'Steel/gold');
    
Insert Into Artist Value
	('Pietro Torrigiano', 11111, 'Notable sculptor in Renaissance art history', 'Italy', 'Renaissance', 'Sculptures','08-29-1528','11-24-1472'),
    ('Pablo Picasso', 22222, 'Seminal figure in the development of Cubism', 'Spain', 'Modern and Contemporary art','Paintings','04-08-1973', '10-25-1881'),
    ('William Michael Harnett', 33333,'Prominent American still-life painter','Ireland','Realism','Paintings','10-29-1892','08-10-1848'),
    ('Adriaen van der Spelt', 44444,'Dutch Golden Age painter','Netherlands','Baroque','Paintings','1673','1630'),
    ('David Drake', 66666,'African American Potter','USA','Post-Civil War Period','Pottery',Null,Null),
    ('Jacob Halder', 88888,'Danish/Baroque painter','Denamrk','Baroque','Paintings',Null, Null);
    
Insert Into Collections Value
	('The Met Collection','museum','spans over 5,000 years of art from various cultures and time periods', 'New York City',2125357710,'Daniel H. Weiss'),
    ('Leonard A. Lauder Cubist Collection','personal', 'exceptional representation of Cubism', 'New York City', 1574969124,'Metropolitan Museum of Art'),
    ('The Art Institute of Chicago','museum', 'housing significant collections spanning various cultures and time periods', 'Chicago', 1235548371, 'Olivia Taylor'),
    ('Musée National de Céramique','ceramics', 'collection of exquisite ceramics and porcelains', 'France', 1699973794, 'Mia Touse'),
    ('Collection of C. Philip and Corbett Toussaint','pottery', 'craftsmanship across various styles and historical periods', 'France', 0719578270, 'Emily Toussaint'),
    ('Munsey Fund','Ancient Sculptures', 'supporting various cultural and educational endeavours', 'Greece', 0719560070, 'Noah Davis'),
    ('Catharine Lorillard Wolfe Collection','sculptures', 'art collector and philanthropist', 'France', 1759612497, 'Ethan Wolfe'),
    ('Harris Brisbane Dick Fund','paintings', 'supports various cultural and educational initiatives', 'New York City', 1923374979, 'Ryan Brisbane'),
    ('University of Michigan Museum of Art','African Art', 'African art remains an important and lasting collection', 'Michigan',0910067983, 'Benjamin Wilson');
    
Insert Into Permanent_Collection Value
	('The Met Collection','on display',850000,'1870'),
    ('Leonard A. Lauder Cubist Collection', ' is stored', 56890, '1907'),
    ('The Art Institute of Chicago', 'on display', 75678, '1879'),
    ('Musee National de Ceramique', 'is stored', 69389, '1824'),
    ('Collection of C. Philip and Corbett Toussaint', 'on loan', 32897, '1845'),
    ('Munsey Fund', 'on loan', 250950 , '1930'),
    ('Catharine Lorillard Wolfe Collection', 'on display', 487610 , '1963');

Insert Into Borrowed_Collection Value
	('Harris Brisbane Dick Fund', 'Harry Brisbane', '1855', '1916'),
    ('University of Michigan Museum of Art', 'Helmut Stern', '2005', '2022');

Alter Table Art_Object
	Add Constraint	ARTCNP	Foreign Key(Collection_name) References Collections(Collection_name) On Delete Set Default On Update cascade,
	Add Constraint	ARTN	Foreign Key(Artist_name)	 References Artist(Aname) On Delete Set Null On Update cascade,
	Add Constraint	ARTEX	Foreign Key(Exhibition_name) References Exhibition(Ename) On Delete Set Null On Update cascade;
