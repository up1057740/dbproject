INSERT INTO CLIENT(id,_name,_surname,phone_no) VALUES
('YD3YITTY','Tenia','Paulou',6983567721), /*1*/
('82UNTP38','Dionusis','Maurotsoukalos',6945608831),/*2*/
('VVVHSR5U','Makis', 'Kotsampasis',6988346742),/*3*/
('0A13JKBH','Ifigenia','Saslidou',6973498229),/*4*/
('MYBZ6K7K','Fotis',' Mastrapas',6934599825),/*5*/
('YPBYHSKM','Eva','Palaiologou',6983487246),/*6*/
('FBJBMZ05','Spyros','Deloglou',6945678245), /*7*/
('VCZK9PZK','Thomas','Voulinos',6942367885),/*8*/
('BCFOTSIO','Frida','Papaparaskeua',6975173410), /*9*/
('3Q71Z3IZ','Aris','Paurinos',6974506124),/*10*/
('6IO5XRW7','Fotis','Voulinos',6982398456),/*11*/
('DRK08TK7','Dalia', 'Hatzialeksandrou',6936577923),/*12*/
('3YN4MULL','Theopoula','Tzini',6983652779);/*13*/



insert into EQUIPMENT(equipment_code,equipment_type,price_per_day) values
('tnt1','tent','4.0'),
('tnt2','tent','4.0'),
('tnt3','tent','4.0'),
('tnt4','tent','4.0'),
('tnt5','tent','4.0'),
('tnt6','tent','4.0'),
('tnt7','tent','4.0'),
('tnt8','tent','4.0'),
('tnt9','tent','4.0'),
('tnt0','tent','4.0'),
('mat1','mattress','3.5'),
('mat2','mattress','3.5'),
('mat3','mattress','3.5'),
('mat4','mattress','3.5'),
('mat5','mattress','3.5'),
('mat6','mattress','3.5'),
('mat7','mattress','3.5'),
('mat8','mattress','3.5'),
('mat9','mattress','3.5'),
('mat0','mattress','3.5'),
('lan1','lantern','2.0'),
('lan2','lantern','2.0'),
('lan3','lantern','2.0'),
('lan4','lantern','2.0'),
('lan5','lantern','2.0'),
('lan6','lantern','2.0'),
('lan7','lantern','2.0'),
('lan8','lantern','2.0'),
('lan9','lantern','2.0'),
('lan0','lantern','2.0');


insert into SPOT(spot_code,spot_no,spot_type,cost_per_day,parking_code) values
('ec01','01','tent','4.0','ecx01'),/*1*/
('ec02','02','tent','4.0','ecx02'),/*2*/
('ec03','03','tent','4.0','ecx03'),/*3*/
('ec04','04','tent','4.0','ecx04'),/*4*/
('ec05','05','tent','4.0','ecx05'),/*5*/
('ec06','06','tent','4.0','ecx06'),/*6*/
('ec07','07','tent','4.0','ecx07'),/*7*/
('ec08','08','tent','4.0','ecx08'),/*8*/
('ec09','09','tent','4.0','ecx09'),/*9*/
('ec10','10','tent','4.0','ecx10'),/*10*/
('ec11','11','tent','4.0','ecx11'),/*11*/
('ec12','12','tent','4.0','ecx12'),/*12*/
('ec13','13','tent','4.0','ecx13'),/*13*/
('ec14','14','tent','4.0','ecx14'),/*14*/
('ec15','15','tent','4.0','ecx15'),/*15*/
('ec16','16','tent','4.0','ecx16'),/*16*/
('ec17','17','tent','4.0','ecx17'),/*17*/
('ec18','18','tent','4.0','ecx18'),/*18*/
('ec19','19','tent','4.0','ecx19'),/*19*/
('ec20','20','tent','4.0','ecx20'),/*20*/
('pr21','21','motorhouse','5.0','prx21'),/*21*/
('pr22','22','motorhouse','5.0','prx22'),/*22*/
('pr23','23','motorhouse','5.0','prx23'),/*23*/
('pr24','24','motorhouse','5.0','prx24'),/*24*/
('pr25','25','motorhouse','5.0','prx25'),/*25*/
('pr26','26','motorhouse','5.0','prx26'),/*26*/
('pr27','27','motorhouse','5.0','prx27'),/*27*/
('pr28','28','motorhouse','5.0','prx28'),/*28*/
('pr29','29','motorhouse','5.0','prx29'),/*29*/
('pr30','30','motorhouse','5.0','prx30'),/*30*/
('sp31','31','special provisions','3.0','spx31'),/*31*/
('sp32','32','special provisions','3.0','spx32'),/*32*/
('sp33','33','special provisions','3.0','spx33'),/*33*/
('sp34','34','special provisions','3.0','spx34'),/*34*/
('sp35','35','special provisions','3.0','spx35');/*35*/


insert into RESERVATION(booking_code,no_of_campers,category,arrival_date,departure_date,check_in,check_out,discount) values
('ALPHA00','2','basic package','2021-05-20','2021-05-23','2021-05-20 10:10:10','2021-05-23 16:03:45','30.0'),/*--tesseris meres, duo atoma economy, maios 20-23*/ 
('ALPHA01','4','family package','2021-08-15','2021-08-19','2021-08-15 11:10:30','2021-08-19 13:47:00',null),/*pente meres, duo enhlikoi duo paidia premium, augoustos 15-19*/
('ALPHA03','3','family package','2021-08-14','2021-08-18','2021-08-14 15:28:23','2021-08-18 15:47:20',null),/*--pente meres, duo enhlikoi economy, ena amea, augoustos 14-18*/
('ALPHA04','7','students package','2021-08-10','2021-08-19','2021-08-10 09:39:10','2021-08-19 20:09:10','40.0'),/*--10 meres, 7 foithtes economy , augoustos 10-19*/
('ALPHA05','4','students package','2021-07-25','2021-07-28','2021-07-25 12:34:20','2021-07-28 17:15:22','40.0'),/*--4meres tesseris foithtes economy, ioulios 25-28*/
('ALPHA06','2','basic package','2021-08-02','2021-08-08','2021-08-02 17:33:29','2021-08-08 10:10:45',null),/*--5 meres, 2 enhliki premium, augoustos 2-8*/
('ALPHA07','6','students package','2021-08-10','2021-08-15','2021-08-10 10:25:22','2021-08-15 19:33:28','40.0'),/*--6 meres, 6 foithtes economy, augoustos 10-15*/
('ALPHA08','4','family package','2021-08-10','2021-08-16','2021-08-10 12:09:08','2021-08-10 15:06:22','35.0'),/*7 meres, 2 gon 2 paidia, augoustos 10-16*/
('ALPHA09','2','students package','2021-07-12','2021-07-15','2021-07-12 16:17:09','2021-07-15 18:09:22',null),/*4 meres, duo foithtes, 12-15 iouliou*/
('ALPHA10','5','students package','2021-07-20','2021-07-25','2021-07-20 10:10:22','2021-07-25 10:55:20','40.0'),/*6 meres, 5 foith, 20-25 iouliou*/
('BETA00','7','basic package','2021-08-10','2021-08-17','2021-08-10 10:12:21','2021-08-17 17:06:30','30.0'),/*8 meres, 7 dudes, 10-17 augoustos*/
('BETA01','6','students package','2021-08-21','2021-08-27','2021-08-21 17:00:21','2021-08-27 13:12:00','40.0'),/*7 meres, 6 atoma, 21-27 aug*/
('BETA02','4','students package','2021-08-01','2021-08-05','2021-08-01 10:10:10','2021-08-05 17:05:09','40.0'); /*theopoula foithtiko me tesseris grande, 5 meres apo 1-5 aug*/


INSERT INTO PAYMENT(p_code,payment_method) values
('15001','CREDIT CARD'), /*1*/
('15002','CASH'), /*2*/
('15003','CREDIT CARD'), /*3*/
('15004','CREDIT CARD'), /*4*/ 
('15005','CASH'), /*5*/
('15006','CASH'), /*6*/
('15007','CREDIT CARD'), /*7*/
('15008','DEBIT CARD'),/*8*/
('15009','CASH'),/*9*/
('15010','CREDIT CARD'),/*10*/
('15011','CASH'),/*11*/
('15012','CASH'),/*12*/
('15013','CREDIT CARD');


INSERT INTO DOES(cl_id,bk_code,booking_date) VALUES
('YD3YITTY','ALPHA00','2021-02-26 10:25:43'),/*1*/
('82UNTP38','ALPHA01','2021-03-01 14:19:20'),/*2*/
('VVVHSR5U','ALPHA03','2021-03-10 15:09:58'),/*3*/
('0A13JKBH','ALPHA04','2021-03-15 18:45:10'),/*4*/
('MYBZ6K7K','ALPHA05','2021-03-16 20:09:22'),/*5*/
('YPBYHSKM','ALPHA06','2021-03-16 20:19:19'),/*6*/
('FBJBMZ05','ALPHA07','2021-03-17 11:00:32'),/*7*/
('VCZK9PZK','ALPHA08','2021-03-17 14:07:21'),/*8*/
('BCFOTSIO','ALPHA09','2021-03-17 16:09:59'),/*9*/
('3Q71Z3IZ','ALPHA10','2021-03-18 19:34:26'),/*10*/
('6IO5XRW7','BETA00','2021-03-19 10:58:06'),/*11*/
('DRK08TK7','BETA01','2021-03-19 12:32:45'),/*12*/
('3YN4MULL','BETA02','2021-03-19 13:42:12');/*13*/



INSERT INTO INCLUDES(b_code,s_code) VALUES
('ALPHA00','ec01'),/*--tesseris meres, duo atoma economy, maios 20-23*/ 
('ALPHA01','ec02'),/*pente meres, duo enhlikoi duo paidia premium, augoustos 15-19*/
('ALPHA03','sp32'),/*--pente meres, duo enhlikoi economy, ena amea, augoustos 14-18*/
('ALPHA04','ec03'),
('ALPHA04','ec04'),/*--10 meres, 7 foithtes economy , augoustos 10-19*//*null*/
('ALPHA05','ec05'),
('ALPHA05','ec06'),/*--4meres tesseris foithtes economy, ioulios 25-28!!!!!!!!!!!!!!!!!!!!!!!!!*/
('ALPHA06','pr22'),/*--5 meres, 2 enhliki premium, augoustos 2-8*/
('ALPHA07','ec07'),
('ALPHA07','ec08'),
('ALPHA07','ec09'),/*--6 meres, 6 foithtes economy, augoustos 10-15*/
('ALPHA08','ec10'),
('ALPHA08','ec11'),/*7 meres, 2 gon 2 paidia, augoustos 10-16*/
('ALPHA09','pr29'),/*4 meres, duo foithtes, 12-15 iouliou!!!!!!!!!!!!!!!!!!!!!!!!!!*/
('ALPHA10','ec12'),
('ALPHA10','ec13'),/*6 meres, 5 foith, 20-25 iouliou!!!!!!!!*/
('BETA00','ec14'),
('BETA00','ec15'),
('BETA00','ec16'),
('BETA00','ec17'),/*8 meres, 7 dudes, 10-17 augoustos*/
('BETA01','ec18'),
('BETA01','ec19'),/*7 meres, 6 atoma, 21-27 aug*/
('BETA02','ec20');

insert into CONNECTS (pm_code,bkng_code) values 
('15001','ALPHA00'), /*--tesseris meres, duo atoma economy, maios 20-23*/
('15002','ALPHA01'), /*pente meres, duo enhlikoi duo paidia premium, augoustos 15-19*/
('15003','ALPHA03'), /*--pente meres, duo enhlikoi economy, ena amea, augoustos 14-18*/
('15004','ALPHA04'), /*--10 meres, 7 foithtes economy , augoustos 10-19*/ 
('15005','ALPHA05'), /*--4meres tesseris foithtes economy, ioulios 25-28*/
('15006','ALPHA06'), /*--5 meres, 2 enhliki premium, augoustos 2-8*/
('15007','ALPHA07'), /*--6 meres, 6 foithtes economy, augoustos 10-15*/
('15008','ALPHA08'),
('15009','ALPHA09'),
('15010','ALPHA10'),
('15011','BETA00'),
('15012','BETA01'),
('15013','BETA02');


INSERT INTO PAYS (client_id,payment_code,payment_date) VALUES
('YD3YITTY','15001','2021-05-20 10:10:10'),/*1*/
('82UNTP38','15002','2021-08-15 11:10:30'),/*2*/
('VVVHSR5U','15003','2021-08-14 15:28:23'),/*3*/
('0A13JKBH','15004','2021-08-10 09:39:10'),/*4*/
('MYBZ6K7K','15005','2021-07-25 12:34:20'),/*5*/
('YPBYHSKM','15006','2021-08-02 17:33:29'),/*6*/
('FBJBMZ05','15007','2021-08-10 10:25:22'),/*7*/
('VCZK9PZK','15008','2021-08-10 12:09:08'),/*8*/
('BCFOTSIO','15009','2021-07-12 16:17:09'),/*9*/
('3Q71Z3IZ','15010','2021-07-20 10:10:22'),/*10*/
('6IO5XRW7','15011','2021-08-10 10:12:21'),/*11*/
('DRK08TK7','15012','2021-08-21 17:00:21'),/*12*/
('3YN4MULL','15013','2021-08-01 10:10:10');/*13*/


insert into RENTS(bk_code,e_code) values
('ALPHA00','lan8'),/*--tesseris meres, duo atoma economy, maios 20-23*/ 
('ALPHA01','tnt1'),/*pente meres, duo enhlikoi duo paidia premium, augoustos 15-19*/
('ALPHA03','mat0'),/*--pente meres, duo enhlikoi economy, ena amea, augoustos 14-18*/
('ALPHA04','lan7'),
('ALPHA04','lan1'),/*--10 meres, 7 foithtes economy , augoustos 10-19*//*null*/
('ALPHA05','tnt3'),
('ALPHA05','tnt4'),/*--4meres tesseris foithtes economy, ioulios 25-28!!!!!!!!!!!!!!!!!!!!!!!!!*/
('ALPHA06','lan2'),/*--5 meres, 2 enhliki premium, augoustos 2-8*/
('ALPHA07','mat1'),
('ALPHA07','tnt5'),
('ALPHA07','tnt6'),/*--6 meres, 6 foithtes economy, augoustos 10-15*/
('ALPHA08','mat2'),
('ALPHA08','mat3'),/*7 meres, 2 gon 2 paidia, augoustos 10-16*/
('ALPHA09','lan3'),/*4 meres, duo foithtes, 12-15 iouliou!!!!!!!!!!!!!!!!!!!!!!!!!!*/
('ALPHA10','lan4'),
('ALPHA10','lan5'),/*6 meres, 5 foith, 20-25 iouliou!!!!!!!!*/
('BETA00','tnt7'),
('BETA00','tnt8'),
('BETA00','mat4'),
('BETA00','mat5'),/*8 meres, 7 dudes, 10-17 augoustos*/
('BETA01','tnt9'),
('BETA01','tnt0'),/*7 meres, 6 atoma, 21-27 aug*/
('BETA02','mat6'),
('BETA02','lan6'); 
