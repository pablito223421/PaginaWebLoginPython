
CREATE DATABASE db_usuario;

CREATE TABLE  `db_usuario`.`usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombreusuario` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `contrasena` varchar(50) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

