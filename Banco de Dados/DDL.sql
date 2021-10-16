CREATE TABLE `Cliente` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`nome` VARCHAR(50) NOT NULL,
	`cpf` INT(11) NOT NULL UNIQUE,
	`telefone` INT(11),
	PRIMARY KEY (`id`)
);

CREATE TABLE `Carro` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`placa` VARCHAR(255) NOT NULL UNIQUE,
	`marca` VARCHAR(50) NOT NULL,
	`modelo` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Aluguel` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`carro_id` INT NOT NULL,
	`cliente_id` INT NOT NULL,
	`data` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Aluguel` ADD CONSTRAINT `Aluguel_fk0` FOREIGN KEY (`carro_id`) REFERENCES `Carro`(`id`);

ALTER TABLE `Aluguel` ADD CONSTRAINT `Aluguel_fk1` FOREIGN KEY (`cliente_id`) REFERENCES `Cliente`(`id`);
