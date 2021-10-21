use locadora;

SELECT * FROM cliente;

-- carro pré cadastrado
INSERT INTO `locadora`.`carro` (
	`placa`,
	`marca`,
	`modelo`
) VALUES (
	"FNN-334",
	"Nissan",
	"Kicks"
);

-- id = SELECT id from cliente where nome="Matheus";

-- registrando aluguel
INSERT INTO `locadora`.`aluguel` (
	`carro_id`,
	`cliente_id`,
	`data`
) VALUES (
	1, -- {carro_id}
	-- (SELECT id from cliente where nome={nome}),
    -- {id},
    (SELECT id from cliente where nome="Matheus"),
	CURRENT_DATE()
);

select * from aluguel;

-- atualiza o status do carro para reservado
UPDATE `locadora`.`carro` SET
	`status` = 'reservado'
WHERE `id` = 1;

-- Relatório
select placa, `status` from carro;
delete from aluguel
where id = 1
-- and `status` = 'reservado'
;

-- Como pego o nome do cliente que reservou o carro?
SELECT nome, placa, `status`
FROM aluguel
LEFT JOIN carro ON carro.id = aluguel.carro_id
LEFT JOIN cliente ON cliente.id = aluguel.cliente_id
;