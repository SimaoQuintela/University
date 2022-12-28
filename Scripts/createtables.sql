-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema TPBD
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema TPBD
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `TPBD` DEFAULT CHARACTER SET utf8 ;


-- -----------------------------------------------------
-- Table `TPBD`.`Contact`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Contact` (
  `idContact` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `phone` INT NOT NULL,
  PRIMARY KEY (`idContact`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`Client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Client` (
  `idClient` INT NOT NULL,
  `VAT` INT NULL,
  `contact` INT NOT NULL,
  PRIMARY KEY (`idClient`, `contact`),
  INDEX `fk_Client_Contact1_idx` (`contact` ASC) VISIBLE,
  CONSTRAINT `fk_Client_Contact1`
    FOREIGN KEY (`contact`)
    REFERENCES `TPBD`.`Contact` (`idContact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Employee` (
  `idEmployee` INT NOT NULL,
  `manager` INT NOT NULL,
  `salary` DECIMAL(10) NULL,
  `contact` INT NOT NULL,
  PRIMARY KEY (`idEmployee`, `contact`),
  INDEX `fk_Employee_Employee1_idx` (`manager` ASC) VISIBLE,
  INDEX `fk_Employee_Contact1_idx` (`contact` ASC) VISIBLE,
  CONSTRAINT `fk_Employee_Employee1`
    FOREIGN KEY (`manager`)
    REFERENCES `TPBD`.`Employee` (`idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employee_Contact1`
    FOREIGN KEY (`contact`)
    REFERENCES `TPBD`.`Contact` (`idContact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Order` (
  `idOrder` INT NOT NULL,
  `status` VARCHAR(200) NOT NULL,
  `shippingPrice` DECIMAL(6,2) NULL,
  `orderDate` TIMESTAMP NOT NULL,
  `upDate` TIMESTAMP NOT NULL,
  `Employee` INT NOT NULL,
  `Employee_contact` INT NOT NULL,
  `Client_idClient` INT NOT NULL,
  `Client_contact` INT NOT NULL,
  PRIMARY KEY (`idOrder`, `Client_idClient`, `Client_contact`),
  INDEX `fk_Order_Employee1_idx` (`Employee` ASC, `Employee_contact` ASC) VISIBLE,
  INDEX `fk_Order_Client1_idx` (`Client_idClient` ASC, `Client_contact` ASC) VISIBLE,
  CONSTRAINT `fk_Order_Employee1`
    FOREIGN KEY (`Employee` , `Employee_contact`)
    REFERENCES `TPBD`.`Employee` (`idEmployee` , `contact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Client1`
    FOREIGN KEY (`Client_idClient` , `Client_contact`)
    REFERENCES `TPBD`.`Client` (`idClient` , `contact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`category` (
  `idCategory` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `descripton` VARCHAR(45) NULL,
  `tax` DECIMAL(6,2) NOT NULL,
  PRIMARY KEY (`idCategory`));


-- -----------------------------------------------------
-- Table `TPBD`.`Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Item` (
  `idItem` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `desc` VARCHAR(45) NULL,
  `stockNr` INT NOT NULL,
  `priceBuy` DECIMAL(6,2) NOT NULL,
  `priceSell` DECIMAL(6,2) NOT NULL,
  `category` INT NOT NULL,
  PRIMARY KEY (`idItem`, `category`),
  INDEX `fk_Item_category1_idx` (`category` ASC) VISIBLE,
  CONSTRAINT `fk_Item_category1`
    FOREIGN KEY (`category`)
    REFERENCES `TPBD`.`category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`Suplier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Suplier` (
  `VAT` INT NOT NULL,
  `contact` INT NOT NULL,
  PRIMARY KEY (`VAT`, `contact`),
  INDEX `fk_Suplier_Contact1_idx` (`contact` ASC) VISIBLE,
  CONSTRAINT `fk_Suplier_Contact1`
    FOREIGN KEY (`contact`)
    REFERENCES `TPBD`.`Contact` (`idContact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`Suplier_provide_Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Suplier_provide_Item` (
  `Item_idItem` INT NOT NULL,
  `Suplier_VAT` INT NOT NULL,
  `Suplier_contact` INT NOT NULL,
  PRIMARY KEY (`Item_idItem`, `Suplier_VAT`, `Suplier_contact`),
  INDEX `fk_Item_has_Suplier_Suplier1_idx` (`Suplier_VAT` ASC, `Suplier_contact` ASC) VISIBLE,
  INDEX `fk_Item_has_Suplier_Item1_idx` (`Item_idItem` ASC) VISIBLE,
  CONSTRAINT `fk_Item_has_Suplier_Item1`
    FOREIGN KEY (`Item_idItem`)
    REFERENCES `TPBD`.`Item` (`idItem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Item_has_Suplier_Suplier1`
    FOREIGN KEY (`Suplier_VAT` , `Suplier_contact`)
    REFERENCES `TPBD`.`Suplier` (`VAT` , `contact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Address` (
  `idAdress` INT NOT NULL,
  `street` VARCHAR(255) NOT NULL,
  `zipCode` VARCHAR(10) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAdress`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`Client_has_Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Client_has_Address` (
  `Client_idClient` INT NOT NULL,
  `Client_contact` INT NOT NULL,
  `Address_idAdress` INT NOT NULL,
  PRIMARY KEY (`Client_idClient`, `Client_contact`, `Address_idAdress`),
  INDEX `fk_Client_has_Address_Address1_idx` (`Address_idAdress` ASC) VISIBLE,
  INDEX `fk_Client_has_Address_Client1_idx` (`Client_idClient` ASC, `Client_contact` ASC) VISIBLE,
  CONSTRAINT `fk_Client_has_Address_Client1`
    FOREIGN KEY (`Client_idClient` , `Client_contact`)
    REFERENCES `TPBD`.`Client` (`idClient` , `contact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Client_has_Address_Address1`
    FOREIGN KEY (`Address_idAdress`)
    REFERENCES `TPBD`.`Address` (`idAdress`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TPBD`.`Order_has_Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TPBD`.`Order_has_Item` (
  `Order_idOrder` INT NOT NULL,
  `Order_Client_idClient` INT NOT NULL,
  `Order_Client_contact` INT NOT NULL,
  `Item_idItem` INT NOT NULL,
  `Item_category` INT NOT NULL,
  `amount` INT NOT NULL,
  PRIMARY KEY (`Order_idOrder`, `Order_Client_idClient`, `Order_Client_contact`, `Item_idItem`, `Item_category`),
  INDEX `fk_Order_has_Item_Item1_idx` (`Item_idItem` ASC, `Item_category` ASC) VISIBLE,
  INDEX `fk_Order_has_Item_Order1_idx` (`Order_idOrder` ASC, `Order_Client_idClient` ASC, `Order_Client_contact` ASC) VISIBLE,
  CONSTRAINT `fk_Order_has_Item_Order1`
    FOREIGN KEY (`Order_idOrder` , `Order_Client_idClient` , `Order_Client_contact`)
    REFERENCES `TPBD`.`Order` (`idOrder` , `Client_idClient` , `Client_contact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_has_Item_Item1`
    FOREIGN KEY (`Item_idItem` , `Item_category`)
    REFERENCES `TPBD`.`Item` (`idItem` , `category`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;