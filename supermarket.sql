-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 19, 2023 at 10:10 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `supermarket`
--

-- --------------------------------------------------------

--
-- Table structure for table `categorie`
--

CREATE TABLE `categorie` (
  `IDcategorie` int(11) NOT NULL,
  `Denumire` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categorie`
--

INSERT INTO `categorie` (`IDcategorie`, `Denumire`) VALUES
(1, 'Fructe'),
(2, 'Legume'),
(3, 'Racoritoare'),
(4, 'Apa'),
(5, 'Carne'),
(6, 'Lactate');

-- --------------------------------------------------------

--
-- Table structure for table `comandaprodus`
--

CREATE TABLE `comandaprodus` (
  `ID` int(11) NOT NULL,
  `IDcomanda` int(11) NOT NULL,
  `IDprodus` int(11) NOT NULL,
  `NrBucati` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comandaprodus`
--

INSERT INTO `comandaprodus` (`ID`, `IDcomanda`, `IDprodus`, `NrBucati`) VALUES
(1, 3, 4, 75),
(2, 1, 1, 80),
(3, 5, 3, 85),
(4, 4, 2, 65),
(5, 2, 4, 30),
(6, 3, 5, 50);

-- --------------------------------------------------------

--
-- Table structure for table `comenzi`
--

CREATE TABLE `comenzi` (
  `IDcomanda` int(11) NOT NULL,
  `Cod` varchar(32) DEFAULT NULL,
  `DataCerere` date NOT NULL,
  `DataPrimire` date NOT NULL,
  `Pret` float DEFAULT NULL,
  `IDfurnizor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comenzi`
--

INSERT INTO `comenzi` (`IDcomanda`, `Cod`, `DataCerere`, `DataPrimire`, `Pret`, `IDfurnizor`) VALUES
(1, '54kduo99', '2022-11-01', '2022-11-04', 300, 3),
(2, '87bnf56l', '2022-11-02', '2022-11-07', 250.5, 5),
(3, '09dfgh10o', '2022-11-07', '2022-11-10', 375.5, 1),
(4, '66nmbv88v', '2022-11-01', '2022-11-02', 400, 2),
(5, '12wert73v', '2022-11-04', '2022-11-09', 205.75, 3);

-- --------------------------------------------------------

--
-- Table structure for table `furnizori`
--

CREATE TABLE `furnizori` (
  `IDfurnizor` int(11) NOT NULL,
  `Nume` varchar(32) NOT NULL,
  `Prenume` varchar(32) NOT NULL,
  `Adresa` varchar(50) NOT NULL,
  `Localitate` varchar(15) NOT NULL,
  `Judet` varchar(15) NOT NULL,
  `Tara` varchar(15) NOT NULL,
  `Telefon` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `furnizori`
--

INSERT INTO `furnizori` (`IDfurnizor`, `Nume`, `Prenume`, `Adresa`, `Localitate`, `Judet`, `Tara`, `Telefon`) VALUES
(1, 'Gheorghe', 'Andrei', 'strada x, nr y', 'Bucuresti', 'Ilfov', 'Romania', '0723456964'),
(2, 'Vasile', 'Andreea', 'strada abc, nr 20', 'Galati', 'Galati', 'Romania', '0739558110'),
(3, 'Iordache', 'Adrian', 'strada thjm, bl. U3, ap.20', 'Zalau', 'Salaj', 'Romania', '0749665939'),
(4, 'Sandu', 'Vasile', 'strada dhjudnbf, nr 12', 'Crasna', 'Vaslui', 'Romania', '0784627578'),
(5, 'Aldea', 'Ioana', 'strada dbgduud, bl. C, ap.5', 'Focsani', 'Vrancea', 'Romania', '0793658461'),
(6, 'Ion', 'Stefan', 'strada a, nr b', 'Vaslui', 'Vaslui', 'Romania', '0724387340');

-- --------------------------------------------------------

--
-- Table structure for table `produse`
--

CREATE TABLE `produse` (
  `IDprodus` int(11) NOT NULL,
  `Denumire` varchar(32) NOT NULL,
  `IDcategorie` int(11) NOT NULL,
  `Cantitate` int(11) NOT NULL,
  `PretBucata` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `produse`
--

INSERT INTO `produse` (`IDprodus`, `Denumire`, `IDcategorie`, `Cantitate`, `PretBucata`) VALUES
(1, 'Coca-Cola 0.5L', 3, 50, 3.5),
(2, 'Lapte Napolact 1L', 6, 15, 7.55),
(3, 'Carne de Vita 600g', 5, 30, 22.99),
(4, 'Apa plata Bucovina 700ml', 4, 55, 2.79),
(5, 'Smantana 12%', 6, 25, 12.5),
(6, 'Fanta 0.5L', 3, 50, 3.5),
(7, 'Pepsi Max 0.5L', 3, 45, 3.25);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categorie`
--
ALTER TABLE `categorie`
  ADD PRIMARY KEY (`IDcategorie`);

--
-- Indexes for table `comandaprodus`
--
ALTER TABLE `comandaprodus`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `IDcomanda` (`IDcomanda`),
  ADD KEY `IDprodus` (`IDprodus`);

--
-- Indexes for table `comenzi`
--
ALTER TABLE `comenzi`
  ADD PRIMARY KEY (`IDcomanda`),
  ADD KEY `IDfurnizor` (`IDfurnizor`);

--
-- Indexes for table `furnizori`
--
ALTER TABLE `furnizori`
  ADD PRIMARY KEY (`IDfurnizor`);

--
-- Indexes for table `produse`
--
ALTER TABLE `produse`
  ADD PRIMARY KEY (`IDprodus`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comandaprodus`
--
ALTER TABLE `comandaprodus`
  ADD CONSTRAINT `comandaprodus_ibfk_1` FOREIGN KEY (`IDcomanda`) REFERENCES `comenzi` (`IDcomanda`),
  ADD CONSTRAINT `comandaprodus_ibfk_2` FOREIGN KEY (`IDprodus`) REFERENCES `produse` (`IDprodus`);

--
-- Constraints for table `comenzi`
--
ALTER TABLE `comenzi`
  ADD CONSTRAINT `comenzi_ibfk_1` FOREIGN KEY (`IDfurnizor`) REFERENCES `furnizori` (`IDfurnizor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
