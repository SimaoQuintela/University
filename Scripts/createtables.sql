-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dorlux
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dorlux
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dorlux` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema sakila
-- -----------------------------------------------------
USE `dorlux` ;

-- -----------------------------------------------------
-- Table `dorlux`.`Contact`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Contact` (
  `idContact` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `phone` INT NOT NULL,
  PRIMARY KEY (`idContact`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Client` (
  `idClient` INT NOT NULL,
  `VAT` INT NULL,
  `contact` INT NOT NULL,
  PRIMARY KEY (`idClient`),
  INDEX `fk_Client_Contact1_idx` (`contact` ASC) VISIBLE,
  CONSTRAINT `fk_Client_Contact1`
    FOREIGN KEY (`contact`)
    REFERENCES `dorlux`.`Contact` (`idContact`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Employee` (
  `idEmployee` INT NOT NULL,
  `manager` INT NOT NULL,
  `salary` DECIMAL(10) NULL,
  `contact` INT NOT NULL,
  PRIMARY KEY (`idEmployee`),
  INDEX `fk_Employee_Contact1_idx` (`contact` ASC) VISIBLE,
  INDEX `fk_Employee_Employee1_idx` (`manager` ASC, `contact` ASC) VISIBLE,
  CONSTRAINT `fk_Employee_Employee1`
    FOREIGN KEY (`manager` , `contact`)
    REFERENCES `dorlux`.`Employee` (`idEmployee` , `idEmployee`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employee_Contact1`
    FOREIGN KEY (`contact`)
    REFERENCES `dorlux`.`Contact` (`idContact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Order` (
  `idOrder` INT NOT NULL,
  `status` VARCHAR(200) NOT NULL,
  `shippingPrice` DECIMAL(6,2) NULL,
  `orderDate` TIMESTAMP NOT NULL,
  `upDate` TIMESTAMP NOT NULL,
  `Employee` INT NOT NULL,
  `Client_idClient` INT NOT NULL,
  PRIMARY KEY (`idOrder`),
  INDEX `fk_Order_Employee1_idx` (`Employee` ASC) VISIBLE,
  INDEX `fk_Order_Client1_idx` (`Client_idClient` ASC) VISIBLE,
  CONSTRAINT `fk_Order_Employee1`
    FOREIGN KEY (`Employee`)
    REFERENCES `dorlux`.`Employee` (`idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Client1`
    FOREIGN KEY (`Client_idClient`)
    REFERENCES `dorlux`.`Client` (`idClient`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Category` (
  `idCategory` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `descripton` VARCHAR(255) NULL,
  `tax` DECIMAL(6,2) NOT NULL,
  PRIMARY KEY (`idCategory`));


-- -----------------------------------------------------
-- Table `dorlux`.`Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Item` (
  `idItem` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NULL,
  `stockNr` INT NOT NULL,
  `priceBuy` DECIMAL(6,2) NOT NULL,
  `priceSell` DECIMAL(6,2) NOT NULL,
  `category` INT NOT NULL,
  PRIMARY KEY (`idItem`, `category`),
  INDEX `fk_Item_category1_idx` (`category` ASC) VISIBLE,
  CONSTRAINT `fk_Item_category1`
    FOREIGN KEY (`category`)
    REFERENCES `dorlux`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Suplier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Suplier` (
  `VAT` INT NOT NULL,
  `contact` INT NOT NULL,
  PRIMARY KEY (`VAT`),
  INDEX `fk_Suplier_Contact1_idx` (`contact` ASC) VISIBLE,
  CONSTRAINT `fk_Suplier_Contact1`
    FOREIGN KEY (`contact`)
    REFERENCES `dorlux`.`Contact` (`idContact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Suplier_provide_Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Suplier_provide_Item` (
  `Item_idItem` INT NOT NULL,
  `Suplier_VAT` INT NOT NULL,
  PRIMARY KEY (`Item_idItem`, `Suplier_VAT`),
  INDEX `fk_Item_has_Suplier_Suplier1_idx` (`Suplier_VAT` ASC) VISIBLE,
  INDEX `fk_Item_has_Suplier_Item1_idx` (`Item_idItem` ASC) VISIBLE,
  CONSTRAINT `fk_Item_has_Suplier_Item1`
    FOREIGN KEY (`Item_idItem`)
    REFERENCES `dorlux`.`Item` (`idItem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Item_has_Suplier_Suplier1`
    FOREIGN KEY (`Suplier_VAT`)
    REFERENCES `dorlux`.`Suplier` (`VAT`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Address` (
  `idAdress` INT NOT NULL,
  `street` VARCHAR(255) NOT NULL,
  `zipCode` VARCHAR(10) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAdress`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Client_has_Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Client_has_Address` (
  `Client_idClient` INT NOT NULL,
  `Address_idAdress` INT NOT NULL,
  PRIMARY KEY (`Client_idClient`, `Address_idAdress`),
  INDEX `fk_Client_has_Address_Address1_idx` (`Address_idAdress` ASC) VISIBLE,
  INDEX `fk_Client_has_Address_Client1_idx` (`Client_idClient` ASC) VISIBLE,
  CONSTRAINT `fk_Client_has_Address_Client1`
    FOREIGN KEY (`Client_idClient`)
    REFERENCES `dorlux`.`Client` (`idClient`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Client_has_Address_Address1`
    FOREIGN KEY (`Address_idAdress`)
    REFERENCES `dorlux`.`Address` (`idAdress`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dorlux`.`Order_has_Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dorlux`.`Order_has_Item` (
  `Order_idOrder` INT NOT NULL,
  `Item_idItem` INT NOT NULL,
  `amount` INT NOT NULL,
  PRIMARY KEY (`Order_idOrder`, `Item_idItem`),
  INDEX `fk_Order_has_Item_Item1_idx` (`Item_idItem` ASC) VISIBLE,
  INDEX `fk_Order_has_Item_Order1_idx` (`Order_idOrder` ASC) VISIBLE,
  CONSTRAINT `fk_Order_has_Item_Order1`
    FOREIGN KEY (`Order_idOrder`)
    REFERENCES `dorlux`.`Order` (`idOrder`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_has_Item_Item1`
    FOREIGN KEY (`Item_idItem`)
    REFERENCES `dorlux`.`Item` (`idItem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
