-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 23, 2022 at 01:54 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bmit_vat_service`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('9437805813a3');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `short_name` varchar(50) DEFAULT NULL,
  `email_address` varchar(100) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `invoice_logo` varchar(100) DEFAULT NULL,
  `bank_name` varchar(100) DEFAULT NULL,
  `ac_number` varchar(100) DEFAULT NULL,
  `branch` varchar(100) DEFAULT NULL,
  `business_nature` varchar(100) DEFAULT NULL,
  `business_economics` varchar(100) DEFAULT NULL,
  `vat_type` varchar(100) DEFAULT NULL,
  `bin_number` varchar(100) DEFAULT NULL,
  `tin_number` varchar(100) DEFAULT NULL,
  `currency` varchar(100) DEFAULT NULL,
  `person_name` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `person_phone_number` varchar(100) DEFAULT NULL,
  `nid` varchar(100) DEFAULT NULL,
  `person_email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`id`, `company_name`, `short_name`, `email_address`, `phone_number`, `country`, `address`, `invoice_logo`, `bank_name`, `ac_number`, `branch`, `business_nature`, `business_economics`, `vat_type`, `bin_number`, `tin_number`, `currency`, `person_name`, `designation`, `person_phone_number`, `nid`, `person_email`) VALUES
(1, 'BMIT Solutions Ltd.', 'BMIT', 'bmit@gmail.com', '01710336617', '18', 'Banani', '', 'DBBL', '3658214587', 'Banani', 'Supply (Trade), Service Render & Importer', 'Proprietorship ', '1', '6698745512355', '254784455122', '1', 'Rezaul Karim', 'Software Engineer', '01710336617', '19911927203000076', 'rk_rohan@hotmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `id` int(11) NOT NULL,
  `shortname` varchar(3) DEFAULT NULL,
  `country_name` varchar(150) DEFAULT NULL,
  `country_code` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`id`, `shortname`, `country_name`, `country_code`) VALUES
(1, 'AF', 'Afghanistan', 93),
(2, 'AL', 'Albania', 355),
(3, 'DZ', 'Algeria', 213),
(4, 'AS', 'American Samoa', 1684),
(5, 'AD', 'Andorra', 376),
(6, 'AO', 'Angola', 244),
(7, 'AI', 'Anguilla', 1264),
(8, 'AQ', 'Antarctica', 0),
(9, 'AG', 'Antigua And Barbuda', 1268),
(10, 'AR', 'Argentina', 54),
(11, 'AM', 'Armenia', 374),
(12, 'AW', 'Aruba', 297),
(13, 'AU', 'Australia', 61),
(14, 'AT', 'Austria', 43),
(15, 'AZ', 'Azerbaijan', 994),
(16, 'BS', 'Bahamas The', 1242),
(17, 'BH', 'Bahrain', 973),
(18, 'BD', 'Bangladesh', 880),
(19, 'BB', 'Barbados', 1246),
(20, 'BY', 'Belarus', 375),
(21, 'BE', 'Belgium', 32),
(22, 'BZ', 'Belize', 501),
(23, 'BJ', 'Benin', 229),
(24, 'BM', 'Bermuda', 1441),
(25, 'BT', 'Bhutan', 975),
(26, 'BO', 'Bolivia', 591),
(27, 'BA', 'Bosnia and Herzegovina', 387),
(28, 'BW', 'Botswana', 267),
(29, 'BV', 'Bouvet Island', 0),
(30, 'BR', 'Brazil', 55),
(31, 'IO', 'British Indian Ocean Territory', 246),
(32, 'BN', 'Brunei', 673),
(33, 'BG', 'Bulgaria', 359),
(34, 'BF', 'Burkina Faso', 226),
(35, 'BI', 'Burundi', 257),
(36, 'KH', 'Cambodia', 855),
(37, 'CM', 'Cameroon', 237),
(38, 'CA', 'Canada', 1),
(39, 'CV', 'Cape Verde', 238),
(40, 'KY', 'Cayman Islands', 1345),
(41, 'CF', 'Central African Republic', 236),
(42, 'TD', 'Chad', 235),
(43, 'CL', 'Chile', 56),
(44, 'CN', 'China', 86),
(45, 'CX', 'Christmas Island', 61),
(46, 'CC', 'Cocos (Keeling) Islands', 672),
(47, 'CO', 'Colombia', 57),
(48, 'KM', 'Comoros', 269),
(49, 'CG', 'Congo', 242),
(50, 'CD', 'Congo The Democratic Republic Of The', 242),
(51, 'CK', 'Cook Islands', 682),
(52, 'CR', 'Costa Rica', 506),
(53, 'CI', 'Cote D\'Ivoire (Ivory Coast)', 225),
(54, 'HR', 'Croatia (Hrvatska)', 385),
(55, 'CU', 'Cuba', 53),
(56, 'CY', 'Cyprus', 357),
(57, 'CZ', 'Czech Republic', 420),
(58, 'DK', 'Denmark', 45),
(59, 'DJ', 'Djibouti', 253),
(60, 'DM', 'Dominica', 1767),
(61, 'DO', 'Dominican Republic', 1809),
(62, 'TP', 'East Timor', 670),
(63, 'EC', 'Ecuador', 593),
(64, 'EG', 'Egypt', 20),
(65, 'SV', 'El Salvador', 503),
(66, 'GQ', 'Equatorial Guinea', 240),
(67, 'ER', 'Eritrea', 291),
(68, 'EE', 'Estonia', 372),
(69, 'ET', 'Ethiopia', 251),
(70, 'XA', 'External Territories of Australia', 61),
(71, 'FK', 'Falkland Islands', 500),
(72, 'FO', 'Faroe Islands', 298),
(73, 'FJ', 'Fiji Islands', 679),
(74, 'FI', 'Finland', 358),
(75, 'FR', 'France', 33),
(76, 'GF', 'French Guiana', 594),
(77, 'PF', 'French Polynesia', 689),
(78, 'TF', 'French Southern Territories', 0),
(79, 'GA', 'Gabon', 241),
(80, 'GM', 'Gambia The', 220),
(81, 'GE', 'Georgia', 995),
(82, 'DE', 'Germany', 49),
(83, 'GH', 'Ghana', 233),
(84, 'GI', 'Gibraltar', 350),
(85, 'GR', 'Greece', 30),
(86, 'GL', 'Greenland', 299),
(87, 'GD', 'Grenada', 1473),
(88, 'GP', 'Guadeloupe', 590),
(89, 'GU', 'Guam', 1671),
(90, 'GT', 'Guatemala', 502),
(91, 'XU', 'Guernsey and Alderney', 44),
(92, 'GN', 'Guinea', 224),
(93, 'GW', 'Guinea-Bissau', 245),
(94, 'GY', 'Guyana', 592),
(95, 'HT', 'Haiti', 509),
(96, 'HM', 'Heard and McDonald Islands', 0),
(97, 'HN', 'Honduras', 504),
(98, 'HK', 'Hong Kong S.A.R.', 852),
(99, 'HU', 'Hungary', 36),
(100, 'IS', 'Iceland', 354),
(101, 'IN', 'India', 91),
(102, 'ID', 'Indonesia', 62),
(103, 'IR', 'Iran', 98),
(104, 'IQ', 'Iraq', 964),
(105, 'IE', 'Ireland', 353),
(106, 'IL', 'Israel', 972),
(107, 'IT', 'Italy', 39),
(108, 'JM', 'Jamaica', 1876),
(109, 'JP', 'Japan', 81),
(110, 'XJ', 'Jersey', 44),
(111, 'JO', 'Jordan', 962),
(112, 'KZ', 'Kazakhstan', 7),
(113, 'KE', 'Kenya', 254),
(114, 'KI', 'Kiribati', 686),
(115, 'KP', 'Korea North', 850),
(116, 'KR', 'Korea South', 82),
(117, 'KW', 'Kuwait', 965),
(118, 'KG', 'Kyrgyzstan', 996),
(119, 'LA', 'Laos', 856),
(120, 'LV', 'Latvia', 371),
(121, 'LB', 'Lebanon', 961),
(122, 'LS', 'Lesotho', 266),
(123, 'LR', 'Liberia', 231),
(124, 'LY', 'Libya', 218),
(125, 'LI', 'Liechtenstein', 423),
(126, 'LT', 'Lithuania', 370),
(127, 'LU', 'Luxembourg', 352),
(128, 'MO', 'Macau S.A.R.', 853),
(129, 'MK', 'Macedonia', 389),
(130, 'MG', 'Madagascar', 261),
(131, 'MW', 'Malawi', 265),
(132, 'MY', 'Malaysia', 60),
(133, 'MV', 'Maldives', 960),
(134, 'ML', 'Mali', 223),
(135, 'MT', 'Malta', 356),
(136, 'XM', 'Man (Isle of)', 44),
(137, 'MH', 'Marshall Islands', 692),
(138, 'MQ', 'Martinique', 596),
(139, 'MR', 'Mauritania', 222),
(140, 'MU', 'Mauritius', 230),
(141, 'YT', 'Mayotte', 269),
(142, 'MX', 'Mexico', 52),
(143, 'FM', 'Micronesia', 691),
(144, 'MD', 'Moldova', 373),
(145, 'MC', 'Monaco', 377),
(146, 'MN', 'Mongolia', 976),
(147, 'MS', 'Montserrat', 1664),
(148, 'MA', 'Morocco', 212),
(149, 'MZ', 'Mozambique', 258),
(150, 'MM', 'Myanmar', 95),
(151, 'NA', 'Namibia', 264),
(152, 'NR', 'Nauru', 674),
(153, 'NP', 'Nepal', 977),
(154, 'AN', 'Netherlands Antilles', 599),
(155, 'NL', 'Netherlands The', 31),
(156, 'NC', 'New Caledonia', 687),
(157, 'NZ', 'New Zealand', 64),
(158, 'NI', 'Nicaragua', 505),
(159, 'NE', 'Niger', 227),
(160, 'NG', 'Nigeria', 234),
(161, 'NU', 'Niue', 683),
(162, 'NF', 'Norfolk Island', 672),
(163, 'MP', 'Northern Mariana Islands', 1670),
(164, 'NO', 'Norway', 47),
(165, 'OM', 'Oman', 968),
(166, 'PK', 'Pakistan', 92),
(167, 'PW', 'Palau', 680),
(168, 'PS', 'Palestinian Territory Occupied', 970),
(169, 'PA', 'Panama', 507),
(170, 'PG', 'Papua new Guinea', 675),
(171, 'PY', 'Paraguay', 595),
(172, 'PE', 'Peru', 51),
(173, 'PH', 'Philippines', 63),
(174, 'PN', 'Pitcairn Island', 0),
(175, 'PL', 'Poland', 48),
(176, 'PT', 'Portugal', 351),
(177, 'PR', 'Puerto Rico', 1787),
(178, 'QA', 'Qatar', 974),
(179, 'RE', 'Reunion', 262),
(180, 'RO', 'Romania', 40),
(181, 'RU', 'Russia', 70),
(182, 'RW', 'Rwanda', 250),
(183, 'SH', 'Saint Helena', 290),
(184, 'KN', 'Saint Kitts And Nevis', 1869),
(185, 'LC', 'Saint Lucia', 1758),
(186, 'PM', 'Saint Pierre and Miquelon', 508),
(187, 'VC', 'Saint Vincent And The Grenadines', 1784),
(188, 'WS', 'Samoa', 684),
(189, 'SM', 'San Marino', 378),
(190, 'ST', 'Sao Tome and Principe', 239),
(191, 'SA', 'Saudi Arabia', 966),
(192, 'SN', 'Senegal', 221),
(193, 'RS', 'Serbia', 381),
(194, 'SC', 'Seychelles', 248),
(195, 'SL', 'Sierra Leone', 232),
(196, 'SG', 'Singapore', 65),
(197, 'SK', 'Slovakia', 421),
(198, 'SI', 'Slovenia', 386),
(199, 'XG', 'Smaller Territories of the UK', 44),
(200, 'SB', 'Solomon Islands', 677),
(201, 'SO', 'Somalia', 252),
(202, 'ZA', 'South Africa', 27),
(203, 'GS', 'South Georgia', 0),
(204, 'SS', 'South Sudan', 211),
(205, 'ES', 'Spain', 34),
(206, 'LK', 'Sri Lanka', 94),
(207, 'SD', 'Sudan', 249),
(208, 'SR', 'Suriname', 597),
(209, 'SJ', 'Svalbard And Jan Mayen Islands', 47),
(210, 'SZ', 'Swaziland', 268),
(211, 'SE', 'Sweden', 46),
(212, 'CH', 'Switzerland', 41),
(213, 'SY', 'Syria', 963),
(214, 'TW', 'Taiwan', 886),
(215, 'TJ', 'Tajikistan', 992),
(216, 'TZ', 'Tanzania', 255),
(217, 'TH', 'Thailand', 66),
(218, 'TG', 'Togo', 228),
(219, 'TK', 'Tokelau', 690),
(220, 'TO', 'Tonga', 676),
(221, 'TT', 'Trinidad And Tobago', 1868),
(222, 'TN', 'Tunisia', 216),
(223, 'TR', 'Turkey', 90),
(224, 'TM', 'Turkmenistan', 7370),
(225, 'TC', 'Turks And Caicos Islands', 1649),
(226, 'TV', 'Tuvalu', 688),
(227, 'UG', 'Uganda', 256),
(228, 'UA', 'Ukraine', 380),
(229, 'AE', 'United Arab Emirates', 971),
(230, 'GB', 'United Kingdom', 44),
(231, 'US', 'United States', 1),
(232, 'UM', 'United States Minor Outlying Islands', 1),
(233, 'UY', 'Uruguay', 598),
(234, 'UZ', 'Uzbekistan', 998),
(235, 'VU', 'Vanuatu', 678),
(236, 'VA', 'Vatican City State (Holy See)', 39),
(237, 'VE', 'Venezuela', 58),
(238, 'VN', 'Vietnam', 84),
(239, 'VG', 'Virgin Islands (British)', 1284),
(240, 'VI', 'Virgin Islands (US)', 1340),
(241, 'WF', 'Wallis And Futuna Islands', 681),
(242, 'EH', 'Western Sahara', 212),
(243, 'YE', 'Yemen', 967),
(244, 'YU', 'Yugoslavia', 38),
(245, 'ZM', 'Zambia', 260),
(246, 'ZW', 'Zimbabwe', 263);

-- --------------------------------------------------------

--
-- Table structure for table `credit_note`
--

CREATE TABLE `credit_note` (
  `id` int(11) NOT NULL,
  `credit_note_no` varchar(100) DEFAULT NULL,
  `credit_note_type` int(11) DEFAULT NULL,
  `cn_issue_date` date DEFAULT NULL,
  `sales_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `vehicle_info` varchar(100) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `total_vat` decimal(10,2) DEFAULT NULL,
  `total_sd` decimal(10,2) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `credit_note_line`
--

CREATE TABLE `credit_note_line` (
  `id` int(11) NOT NULL,
  `credit_note_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `rate` decimal(10,2) DEFAULT NULL,
  `s_amount` decimal(10,2) DEFAULT NULL,
  `s_vat_percent` decimal(10,2) DEFAULT NULL,
  `s_vat_amount` decimal(10,2) DEFAULT NULL,
  `s_sd` decimal(10,2) DEFAULT NULL,
  `return_qty` int(11) DEFAULT NULL,
  `return_amount` decimal(10,2) DEFAULT NULL,
  `return_vat` decimal(10,2) DEFAULT NULL,
  `return_sd` decimal(10,2) DEFAULT NULL,
  `entry_date` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `email_address` varchar(100) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `country_id` varchar(100) DEFAULT NULL,
  `customer_type` varchar(100) DEFAULT NULL,
  `customer_address` varchar(100) DEFAULT NULL,
  `shipping_address` varchar(100) DEFAULT NULL,
  `shipping_country` varchar(100) DEFAULT NULL,
  `customer_bin` varchar(100) DEFAULT NULL,
  `customer_tin` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `customer_name`, `email_address`, `phone_number`, `country_id`, `customer_type`, `customer_address`, `shipping_address`, `shipping_country`, `customer_bin`, `customer_tin`) VALUES
(1, 'Test Customer 1', 'testcustomer1@gmail.com', '+8801850145577', '18', '1', 'Nikunju', 'Nikunju', '18', '25414132554122', '78546745675467');

-- --------------------------------------------------------

--
-- Table structure for table `debit_note`
--

CREATE TABLE `debit_note` (
  `id` int(11) NOT NULL,
  `debit_note_no` varchar(100) DEFAULT NULL,
  `debit_note_type` int(11) DEFAULT NULL,
  `dn_issue_date` date DEFAULT NULL,
  `purchase_id` int(11) DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `vehicle_info` varchar(100) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `total_vat` decimal(10,2) DEFAULT NULL,
  `total_sd` decimal(10,2) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `debit_note_line`
--

CREATE TABLE `debit_note_line` (
  `id` int(11) NOT NULL,
  `debit_note_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `rate` decimal(10,2) DEFAULT NULL,
  `p_amount` decimal(10,2) DEFAULT NULL,
  `p_vat_percent` decimal(10,2) DEFAULT NULL,
  `p_vat_amount` decimal(10,2) DEFAULT NULL,
  `p_sd` decimal(10,2) DEFAULT NULL,
  `return_qty` int(11) DEFAULT NULL,
  `return_amount` decimal(10,2) DEFAULT NULL,
  `return_vat` decimal(10,2) DEFAULT NULL,
  `return_sd` decimal(10,2) DEFAULT NULL,
  `entry_date` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE `groups` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `restrictions` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `hs_code`
--

CREATE TABLE `hs_code` (
  `id` int(11) NOT NULL,
  `heading` varchar(100) DEFAULT NULL,
  `hs_code` varchar(100) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `cd` decimal(10,2) DEFAULT NULL,
  `sd` decimal(10,2) DEFAULT NULL,
  `vat` decimal(10,2) DEFAULT NULL,
  `ait` decimal(10,2) DEFAULT NULL,
  `rd` decimal(10,2) DEFAULT NULL,
  `at` decimal(10,2) DEFAULT NULL,
  `tti` decimal(10,2) DEFAULT NULL,
  `schedule` varchar(255) DEFAULT NULL,
  `vat_type` tinyint(4) DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `year_start` date DEFAULT NULL,
  `year_end` date DEFAULT NULL,
  `calculate_year` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `issue_vds`
--

CREATE TABLE `issue_vds` (
  `id` int(11) NOT NULL,
  `vds_no` varchar(100) DEFAULT NULL,
  `vds_type` int(11) DEFAULT NULL,
  `entry_date` date DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `total_vat` decimal(10,2) DEFAULT NULL,
  `total_vds` decimal(10,2) DEFAULT NULL,
  `total_payment` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `issue_vds_line`
--

CREATE TABLE `issue_vds_line` (
  `id` int(11) NOT NULL,
  `vds_id` int(11) DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `invoice_no` varchar(100) DEFAULT NULL,
  `inv_amount` decimal(10,2) DEFAULT NULL,
  `inv_date` date DEFAULT NULL,
  `vat_amount` decimal(10,2) DEFAULT NULL,
  `vds_amount` decimal(10,2) DEFAULT NULL,
  `payment_amount` decimal(10,2) DEFAULT NULL,
  `branch_name` varchar(50) DEFAULT NULL,
  `bank_name` varchar(50) DEFAULT NULL,
  `account_code` varchar(50) DEFAULT NULL,
  `deposit_serial` varchar(50) DEFAULT NULL,
  `deposit_date` date DEFAULT NULL,
  `entry_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `item_type` varchar(100) DEFAULT NULL,
  `hs_code` varchar(100) DEFAULT NULL,
  `hs_code_id` varchar(100) DEFAULT NULL,
  `calculate_year` varchar(100) DEFAULT NULL,
  `unit_id` varchar(100) DEFAULT NULL,
  `stock_status` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `opening_balance`
--

CREATE TABLE `opening_balance` (
  `id` int(11) NOT NULL,
  `opening_vat` decimal(10,2) DEFAULT NULL,
  `opening_sd` decimal(10,2) DEFAULT NULL,
  `closing_date` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `payable_mushak`
--

CREATE TABLE `payable_mushak` (
  `id` int(11) NOT NULL,
  `pay_type` int(11) DEFAULT NULL,
  `pay_date` date DEFAULT NULL,
  `pay_amount` decimal(10,2) DEFAULT NULL,
  `business_type` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `payable_voucher`
--

CREATE TABLE `payable_voucher` (
  `id` int(11) NOT NULL,
  `payable_desc` varchar(100) DEFAULT NULL,
  `chalan_no` varchar(100) DEFAULT NULL,
  `payable_amount` decimal(10,2) DEFAULT NULL,
  `vat_amount` decimal(10,2) DEFAULT NULL,
  `chalan_date` date DEFAULT NULL,
  `execute_date` date DEFAULT NULL,
  `business_type` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `id` int(11) NOT NULL,
  `p_invoice_no` varchar(100) DEFAULT NULL,
  `purchase_type` int(11) DEFAULT NULL,
  `lc_date` date DEFAULT NULL,
  `lc_no` varchar(100) DEFAULT NULL,
  `challan_date` date DEFAULT NULL,
  `total_vds` decimal(10,2) DEFAULT NULL,
  `grand_total` decimal(10,2) DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `total_tax` decimal(10,2) DEFAULT NULL,
  `vendor_invoice` varchar(255) DEFAULT NULL,
  `custom_house` varchar(255) DEFAULT NULL,
  `country_origin` varchar(255) DEFAULT NULL,
  `boe_item_no` int(11) DEFAULT NULL,
  `data_source` varchar(155) DEFAULT NULL,
  `cpc_code_id` varchar(255) DEFAULT NULL,
  `entry_date` datetime DEFAULT NULL,
  `notes` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `purchase_line`
--

CREATE TABLE `purchase_line` (
  `id` int(11) NOT NULL,
  `item_id` int(11) DEFAULT NULL,
  `hs_code_id` int(11) DEFAULT NULL,
  `purchase_id` int(11) DEFAULT NULL,
  `qty` float DEFAULT NULL,
  `rate` double DEFAULT NULL,
  `rate_value` double DEFAULT NULL,
  `vatable_value` double DEFAULT NULL,
  `vat_percent` double DEFAULT NULL,
  `vat_amount` double DEFAULT NULL,
  `cd_percent` double DEFAULT NULL,
  `cd_amount` double DEFAULT NULL,
  `sd_percent` double DEFAULT NULL,
  `sd_amount` double DEFAULT NULL,
  `rd_percent` double DEFAULT NULL,
  `rd_amount` double DEFAULT NULL,
  `at_amount` double DEFAULT NULL,
  `ait_amount` double DEFAULT NULL,
  `tti_percent` double DEFAULT NULL,
  `tti_amount` double DEFAULT NULL,
  `vat_type` varchar(100) DEFAULT NULL,
  `vds` varchar(100) DEFAULT NULL,
  `rebate` varchar(100) DEFAULT NULL,
  `purchase_date` date DEFAULT NULL,
  `entry_date` datetime DEFAULT NULL,
  `sub_total` double DEFAULT NULL,
  `grand_total` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `receivable_voucher`
--

CREATE TABLE `receivable_voucher` (
  `id` int(11) NOT NULL,
  `receivable_desc` varchar(100) DEFAULT NULL,
  `chalan_no` varchar(100) DEFAULT NULL,
  `receivable_amount` decimal(10,2) DEFAULT NULL,
  `vat_amount` decimal(10,2) DEFAULT NULL,
  `chalan_date` date DEFAULT NULL,
  `execute_date` date DEFAULT NULL,
  `business_type` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `receive_vds`
--

CREATE TABLE `receive_vds` (
  `id` int(11) NOT NULL,
  `vds_no` varchar(100) DEFAULT NULL,
  `vds_type` int(11) DEFAULT NULL,
  `entry_date` date DEFAULT NULL,
  `vds_certificate_no` varchar(100) DEFAULT NULL,
  `receive_date` date DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `total_vat` decimal(10,2) DEFAULT NULL,
  `total_vds` decimal(10,2) DEFAULT NULL,
  `total_receive` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `receive_vds_line`
--

CREATE TABLE `receive_vds_line` (
  `id` int(11) NOT NULL,
  `vds_id` int(11) DEFAULT NULL,
  `invoice_no` varchar(100) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `inv_amount` double DEFAULT NULL,
  `inv_date` date DEFAULT NULL,
  `vat_amount` double DEFAULT NULL,
  `vds_amount` double DEFAULT NULL,
  `receive_amount` double DEFAULT NULL,
  `branch_name` varchar(50) DEFAULT NULL,
  `bank_name` varchar(50) DEFAULT NULL,
  `account_code` varchar(50) DEFAULT NULL,
  `deposit_serial` varchar(50) DEFAULT NULL,
  `deposit_date` date DEFAULT NULL,
  `entry_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `allowances` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `sale_center_id` int(11) DEFAULT NULL,
  `sales_transfer_id` int(11) DEFAULT NULL,
  `sale_date` date DEFAULT NULL,
  `sales_invoice` varchar(100) DEFAULT NULL,
  `vehicle_info` varchar(100) DEFAULT NULL,
  `destination` varchar(100) DEFAULT NULL,
  `sales_challan` varchar(100) DEFAULT NULL,
  `entry_date` datetime DEFAULT NULL,
  `sales_type` int(11) DEFAULT NULL,
  `trans_type` int(11) DEFAULT NULL,
  `total_discount` decimal(10,2) DEFAULT NULL,
  `total_sd` decimal(10,2) DEFAULT NULL,
  `total_vat` decimal(10,2) DEFAULT NULL,
  `grand_total` decimal(10,2) DEFAULT NULL,
  `notes` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sales_line`
--

CREATE TABLE `sales_line` (
  `id` int(11) NOT NULL,
  `item_id` int(11) DEFAULT NULL,
  `hs_code_id` int(11) DEFAULT NULL,
  `sales_id` int(11) DEFAULT NULL,
  `qty` float DEFAULT NULL,
  `rate` double DEFAULT NULL,
  `rate_value` double DEFAULT NULL,
  `discount_percent` double DEFAULT NULL,
  `discount_amount` double DEFAULT NULL,
  `value_after_discount` double DEFAULT NULL,
  `sd_percent` double DEFAULT NULL,
  `sd_amount` double DEFAULT NULL,
  `vatable_value` double DEFAULT NULL,
  `vat_type` varchar(100) DEFAULT NULL,
  `vat_percent` double DEFAULT NULL,
  `vat_amount` double DEFAULT NULL,
  `vds` varchar(100) DEFAULT NULL,
  `sales_date` date DEFAULT NULL,
  `sub_total` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `id` int(11) NOT NULL,
  `supplier_name` varchar(100) DEFAULT NULL,
  `email_address` varchar(100) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `country_id` varchar(100) DEFAULT NULL,
  `supplier_type` varchar(100) DEFAULT NULL,
  `supplier_address` varchar(100) DEFAULT NULL,
  `supplier_bin` varchar(100) DEFAULT NULL,
  `supplier_tin` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `treasury_chalan`
--

CREATE TABLE `treasury_chalan` (
  `id` int(11) NOT NULL,
  `t_chalan_no` varchar(100) DEFAULT NULL,
  `t_bank` varchar(100) DEFAULT NULL,
  `t_branch` varchar(100) DEFAULT NULL,
  `t_account_code` varchar(100) DEFAULT NULL,
  `t_amount` decimal(10,2) DEFAULT NULL,
  `t_date` date DEFAULT NULL,
  `execute_date` date DEFAULT NULL,
  `t_type` int(11) DEFAULT NULL,
  `business_type` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `units`
--

CREATE TABLE `units` (
  `id` int(11) NOT NULL,
  `unit_name` varchar(100) DEFAULT NULL,
  `short_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `units`
--

INSERT INTO `units` (`id`, `unit_name`, `short_name`) VALUES
(1, 'Kilogram', 'KG'),
(2, 'Millimeter ', 'MM'),
(3, 'Service', 'Service'),
(4, 'Box', 'Box'),
(5, 'Pieces', 'Pcs'),
(6, 'test1', 'test1'),
(7, 'test1', 'test1'),
(8, 'test2', 'test2'),
(9, 'Gross', 'Gross');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `first_name` varchar(500) DEFAULT NULL,
  `last_name` varchar(500) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `first_name`, `last_name`, `email`, `password`) VALUES
(1, 'RK', NULL, NULL, 'rk_rohan@hotmail.com', '$2b$12$wfS6W8oxIgPilLCeNAhm7uX9AQMIwHijIKixEXNXweOwfzzTSPt0K');

-- --------------------------------------------------------

--
-- Table structure for table `user_group`
--

CREATE TABLE `user_group` (
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user_role`
--

CREATE TABLE `user_role` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `credit_note`
--
ALTER TABLE `credit_note`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `credit_note_line`
--
ALTER TABLE `credit_note_line`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debit_note`
--
ALTER TABLE `debit_note`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `debit_note_line`
--
ALTER TABLE `debit_note_line`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `hs_code`
--
ALTER TABLE `hs_code`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `issue_vds`
--
ALTER TABLE `issue_vds`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `issue_vds_line`
--
ALTER TABLE `issue_vds_line`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `opening_balance`
--
ALTER TABLE `opening_balance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payable_mushak`
--
ALTER TABLE `payable_mushak`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payable_voucher`
--
ALTER TABLE `payable_voucher`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchase_line`
--
ALTER TABLE `purchase_line`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `receivable_voucher`
--
ALTER TABLE `receivable_voucher`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `receive_vds`
--
ALTER TABLE `receive_vds`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `receive_vds_line`
--
ALTER TABLE `receive_vds_line`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales_line`
--
ALTER TABLE `sales_line`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `treasury_chalan`
--
ALTER TABLE `treasury_chalan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `units`
--
ALTER TABLE `units`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_users_username` (`username`),
  ADD UNIQUE KEY `ix_users_email` (`email`);

--
-- Indexes for table `user_group`
--
ALTER TABLE `user_group`
  ADD KEY `group_id` (`group_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `user_role`
--
ALTER TABLE `user_role`
  ADD KEY `role_id` (`role_id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `countries`
--
ALTER TABLE `countries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=247;

--
-- AUTO_INCREMENT for table `credit_note`
--
ALTER TABLE `credit_note`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `credit_note_line`
--
ALTER TABLE `credit_note_line`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `debit_note`
--
ALTER TABLE `debit_note`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `debit_note_line`
--
ALTER TABLE `debit_note_line`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `groups`
--
ALTER TABLE `groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hs_code`
--
ALTER TABLE `hs_code`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `issue_vds`
--
ALTER TABLE `issue_vds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `issue_vds_line`
--
ALTER TABLE `issue_vds_line`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `opening_balance`
--
ALTER TABLE `opening_balance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payable_mushak`
--
ALTER TABLE `payable_mushak`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payable_voucher`
--
ALTER TABLE `payable_voucher`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `purchase`
--
ALTER TABLE `purchase`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `purchase_line`
--
ALTER TABLE `purchase_line`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `receivable_voucher`
--
ALTER TABLE `receivable_voucher`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `receive_vds`
--
ALTER TABLE `receive_vds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `receive_vds_line`
--
ALTER TABLE `receive_vds_line`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sales_line`
--
ALTER TABLE `sales_line`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `treasury_chalan`
--
ALTER TABLE `treasury_chalan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `units`
--
ALTER TABLE `units`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `user_group`
--
ALTER TABLE `user_group`
  ADD CONSTRAINT `user_group_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`),
  ADD CONSTRAINT `user_group_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `user_role`
--
ALTER TABLE `user_role`
  ADD CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
