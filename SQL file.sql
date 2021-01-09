SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `CLIENT`;
DROP TABLE IF EXISTS `SPOT`;
DROP TABLE IF EXISTS `PAYMENT`;
DROP TABLE IF EXISTS `RESERVATION`;
DROP TABLE IF EXISTS `EQUIPMENT`;
DROP TABLE IF EXISTS `INCLUDES`;
DROP TABLE IF EXISTS `DOES`;
DROP TABLE IF EXISTS `PAYS`;
drop table if exists `CONNECTS`;
drop table if exists `RENTS`;
SET FOREIGN_KEY_CHECKS=1;


CREATE TABLE `DOES` (
	`cl_id` varchar(255) NOT NULL,
	`bk_code` varchar(255) NOT NULL,
	`booking_date` DATETIME NOT NULL,
	PRIMARY KEY (`cl_id`,`bk_code`)
)ENGINE = InnoDB;

CREATE TABLE `CLIENT` (
	`id` varchar(255) NOT NULL,
	`_name` varchar(255) NOT NULL,
	`_surname` varchar(255) NOT NULL,
	`phone_no` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
)ENGINE = InnoDB;

CREATE TABLE `PAYS` (
	`client_id` varchar(255) NOT NULL,
	`payment_code` INT(5) NOT NULL,
	`payment_date` DATETIME NOT NULL,
	PRIMARY KEY (`client_id`,`payment_code`)
)ENGINE = InnoDB;

CREATE TABLE `PAYMENT` (
	`p_code` INT(5) NOT NULL,
	`payment_method` ENUM ('CASH','CREDIT CARD','DEBIT CARD','PAYPAL') NOT NULL,
	PRIMARY KEY (`p_code`)
)ENGINE = InnoDB;

CREATE TABLE `INCLUDES` (
	`b_code` varchar(255) NOT NULL,
	`s_code` varchar(255) NOT NULL,
	PRIMARY KEY (`s_code`)
)ENGINE = InnoDB;

CREATE TABLE `RESERVATION` (
	`booking_code` varchar(255) NOT NULL,
	`no_of_campers` varchar(255) NOT NULL,
	`category` ENUM('family package','basic package','students package') NOT NULL,
	`arrival_date` DATE NOT NULL,
	`departure_date` DATE NOT NULL,
	`check_in` DATETIME DEFAULT NULL,
	`check_out` DATETIME DEFAULT NULL,
    `discount` float,
	PRIMARY KEY (`booking_code`)
)ENGINE = InnoDB; /*test*/

CREATE TABLE `SPOT` (
    `spot_code` varchar(255) NOT NULL,
	`spot_no` varchar(255) NOT NULL,
	`spot_type` enum('tent','motorhouse','special provisions') NOT NULL,
	`cost_per_day` FLOAT NOT NULL,
	`parking_code` varchar(255) NOT NULL,
	PRIMARY KEY (`spot_code`)
)ENGINE = InnoDB;

CREATE TABLE `EQUIPMENT` (
	`equipment_code` varchar(255) not null,
	`equipment_type` enum('tent','mattress','lantern') not null, 
	`price_per_day` float not null,
	PRIMARY KEY (`equipment_code`)
)ENGINE = InnoDB;

CREATE TABLE `CONNECTS` (
	`pm_code` INT(5) NOT NULL,
	`bkng_code` varchar(255) NOT NULL,
	PRIMARY KEY (`pm_code`,`bkng_code`)
)ENGINE = InnoDB;

CREATE TABLE `RENTS` (
	`bk_code` varchar(255) NOT NULL,
	`e_code` varchar(255) not null,
	PRIMARY KEY (`e_code`)
)ENGINE = InnoDB;

ALTER TABLE `DOES` ADD CONSTRAINT `DOES_fk0` FOREIGN KEY (`cl_id`) REFERENCES `CLIENT`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `DOES` ADD CONSTRAINT `DOES_fk1` FOREIGN KEY (`bk_code`) REFERENCES `RESERVATION`(`booking_code`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `PAYS` ADD CONSTRAINT `PAYS_fk0` FOREIGN KEY (`client_id`) REFERENCES `CLIENT`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `PAYS` ADD CONSTRAINT `PAYS_fk1` FOREIGN KEY (`payment_code`) REFERENCES `PAYMENT`(`p_code`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `INCLUDES` ADD CONSTRAINT `INCLUDES_fk0` FOREIGN KEY (`b_code`) REFERENCES `RESERVATION`(`booking_code`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `INCLUDES` ADD CONSTRAINT `INCLUDES_fk1` FOREIGN KEY (`s_code`) REFERENCES `SPOT`(`spot_code`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CONNECTS` ADD CONSTRAINT `CONNECTS_fk0` FOREIGN KEY (`pm_code`) REFERENCES `PAYMENT`(`p_code`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CONNECTS` ADD CONSTRAINT `CONNECTS_fk1` FOREIGN KEY (`bkng_code`) REFERENCES `RESERVATION`(`booking_code`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `RENTS` ADD CONSTRAINT `RENTS_fk0` FOREIGN KEY (`bk_code`) REFERENCES `RESERVATION`(`booking_code`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `RENTS` ADD CONSTRAINT `RENTS_fk1` FOREIGN KEY (`e_code`) REFERENCES `EQUIPMENT`(`equipment_code`) ON DELETE CASCADE ON UPDATE CASCADE;

