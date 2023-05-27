-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 27 2023 г., 10:55
-- Версия сервера: 8.0.30
-- Версия PHP: 8.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `database`
--

-- --------------------------------------------------------

--
-- Структура таблицы `cultures`
--

CREATE TABLE `cultures` (
  `id_culture` int NOT NULL,
  `name` varchar(40) COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `cultures`
--

INSERT INTO `cultures` (`id_culture`, `name`) VALUES
(1, 'Кукуруза на зерно'),
(2, 'Оз. пшеница по не пар. предшеств.'),
(3, 'Оз. пшеница по пару'),
(4, 'Подсолнечник'),
(6, 'Яр. ячмень');

-- --------------------------------------------------------

--
-- Структура таблицы `data`
--

CREATE TABLE `data` (
  `id` int NOT NULL,
  `id_culture` int NOT NULL,
  `id_fertilizer` int NOT NULL,
  `ratio` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `data`
--

INSERT INTO `data` (`id`, `id_culture`, `id_fertilizer`, `ratio`) VALUES
(1, 1, 1, 2.1),
(2, 1, 2, 1.6),
(3, 1, 3, 1.2),
(4, 2, 1, 2.6),
(5, 2, 2, 2.5),
(6, 2, 3, 1.3),
(7, 3, 1, 1.5),
(8, 3, 2, 2.4),
(9, 3, 3, 1.3),
(10, 4, 1, 2.1),
(11, 4, 2, 2.6),
(12, 4, 3, 1.3),
(16, 6, 1, 2.4),
(17, 6, 2, 2.3),
(18, 6, 3, 1.2);

-- --------------------------------------------------------

--
-- Структура таблицы `fertilizers`
--

CREATE TABLE `fertilizers` (
  `id_fertilizer` int NOT NULL,
  `name` varchar(30) COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `fertilizers`
--

INSERT INTO `fertilizers` (`id_fertilizer`, `name`) VALUES
(1, 'Азотные'),
(2, 'Фосфорные'),
(3, 'Калийные');

-- --------------------------------------------------------

--
-- Структура таблицы `phoshor_coefficient`
--

CREATE TABLE `phoshor_coefficient` (
  `id` int NOT NULL,
  `id_culture` int NOT NULL,
  `level` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8_general_ci NOT NULL,
  `coefficient` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `phoshor_coefficient`
--

INSERT INTO `phoshor_coefficient` (`id`, `id_culture`, `level`, `coefficient`) VALUES
(1, 1, '10 и менее (Очень низкое)', 1.2),
(2, 1, '11-15 (Низкое)', 1.1),
(3, 1, '16-30 (Среднее)', 1),
(4, 1, '31-45 (Повышенное)', 0.5),
(5, 1, '46-60 (Высокое)', 0.2),
(6, 1, '60 и более (Очень высокое)', 0.2),
(7, 4, '10 и менее (Очень низкое)', 1.2),
(8, 4, '11-15 (Низкое)', 1.1),
(9, 4, '16-30 (Среднее)', 1),
(10, 4, '31-45 (Повышенное)', 0.5),
(11, 4, '46-60 (Высокое)', 0.2),
(12, 4, '60 и более (Очень высокое)', 0.2),
(13, 6, '10 и менее (Очень низкое)', 1.2),
(14, 6, '11-15 (Низкое)', 1.1),
(15, 6, '16-30 (Среднее)', 1),
(16, 6, '31-45 (Повышенное)', 0.5),
(17, 6, '46-60 (Высокое)', 0.2),
(18, 6, '60 и более (Очень высокое)', 0.2),
(19, 3, '10 и менее (Очень низкое)', 1.4),
(20, 3, '11-15 (Низкое)', 1.3),
(21, 3, '16-30 (Среднее)', 1),
(22, 3, '31-45 (Повышенное)', 0.7),
(23, 3, '46-60 (Высокое)', 0.3),
(24, 3, '60 и более (Очень высокое)', 0.2),
(25, 2, '10 и менее (Очень низкое)', 1.4),
(26, 2, '11-15 (Низкое)', 1.3),
(27, 2, '16-30 (Среднее)', 1),
(28, 2, '31-45 (Повышенное)', 0.7),
(29, 2, '46-60 (Высокое)', 0.3),
(30, 2, '60 и более (Очень высокое)', 0.2);

-- --------------------------------------------------------

--
-- Структура таблицы `potassium_coefficient`
--

CREATE TABLE `potassium_coefficient` (
  `id` int NOT NULL,
  `id_culture` int NOT NULL,
  `level` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8_general_ci NOT NULL,
  `coefficient` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `potassium_coefficient`
--

INSERT INTO `potassium_coefficient` (`id`, `id_culture`, `level`, `coefficient`) VALUES
(1, 1, '100 и менее (Очень низкое)', 1),
(2, 1, '101-200 (Низкое)', 1),
(3, 1, '201-300 (Среднее)', 1),
(4, 1, '301-500 (Повышенное)', 0.3),
(5, 1, '501-700 (Высокое)', 0),
(6, 1, '700 и более (Очень высокое)', 0),
(7, 4, '100 и менее (Очень низкое)', 1),
(8, 4, '101-200 (Низкое)', 1),
(9, 4, '201-300 (Среднее)', 1),
(10, 4, '301-500 (Повышенное)', 0.3),
(11, 4, '501-700 (Высокое)', 0),
(12, 4, '700 и более (Очень высокое)', 0),
(13, 6, '100 и менее (Очень низкое)', 1),
(14, 6, '101-200 (Низкое)', 1),
(15, 6, '201-300 (Среднее)', 1),
(16, 6, '301-500 (Повышенное)', 0.3),
(17, 6, '501-700 (Высокое)', 0),
(18, 6, '700 и более (Очень высокое)', 0),
(19, 3, '100 и менее (Очень низкое)', 1.3),
(20, 3, '101-200 (Низкое)', 1.1),
(21, 3, '201-300 (Среднее)', 1),
(22, 3, '301-500 (Повышенное)', 0.5),
(23, 3, '501-700 (Высокое)', 0.3),
(24, 3, '700 и более (Очень высокое)', 0.2),
(25, 2, '100 и менее (Очень низкое)', 1.3),
(26, 2, '101-200 (Низкое)', 1.1),
(27, 2, '201-300 (Среднее)', 1),
(28, 2, '301-500 (Повышенное)', 0.5),
(29, 2, '501-700 (Высокое)', 0.3),
(30, 2, '700 и более (Очень высокое)', 0.2);

-- --------------------------------------------------------

--
-- Структура таблицы `storage`
--

CREATE TABLE `storage` (
  `id` int NOT NULL,
  `id_user` int NOT NULL,
  `id_fertilizer` int NOT NULL,
  `amount` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `storage`
--

INSERT INTO `storage` (`id`, `id_user`, `id_fertilizer`, `amount`) VALUES
(1, 1, 1, 147),
(2, 1, 2, 13970),
(3, 1, 3, 78771),
(4, 3, 1, 1000),
(5, 3, 2, 0),
(6, 3, 3, 500);

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id_user` int NOT NULL,
  `surname` varchar(30) COLLATE utf8_general_ci NOT NULL,
  `name` varchar(30) COLLATE utf8_general_ci NOT NULL,
  `patronymic` varchar(30) COLLATE utf8_general_ci NOT NULL,
  `login` varchar(15) COLLATE utf8_general_ci NOT NULL,
  `password` varchar(25) COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id_user`, `surname`, `name`, `patronymic`, `login`, `password`) VALUES
(1, 'Григорьев', 'Семен', 'Сергеевич', 'admin', 'admin'),
(3, 'Петров', 'Петр', 'Петрович', 'user', '111');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `cultures`
--
ALTER TABLE `cultures`
  ADD PRIMARY KEY (`id_culture`);

--
-- Индексы таблицы `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_culture` (`id_culture`),
  ADD KEY `id_fertilizer` (`id_fertilizer`);

--
-- Индексы таблицы `fertilizers`
--
ALTER TABLE `fertilizers`
  ADD PRIMARY KEY (`id_fertilizer`);

--
-- Индексы таблицы `phoshor_coefficient`
--
ALTER TABLE `phoshor_coefficient`
  ADD PRIMARY KEY (`id`),
  ADD KEY `culture` (`id_culture`);

--
-- Индексы таблицы `potassium_coefficient`
--
ALTER TABLE `potassium_coefficient`
  ADD PRIMARY KEY (`id`),
  ADD KEY `culture` (`id_culture`);

--
-- Индексы таблицы `storage`
--
ALTER TABLE `storage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_fertilizer` (`id_fertilizer`),
  ADD KEY `id_user` (`id_user`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `cultures`
--
ALTER TABLE `cultures`
  MODIFY `id_culture` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `data`
--
ALTER TABLE `data`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT для таблицы `fertilizers`
--
ALTER TABLE `fertilizers`
  MODIFY `id_fertilizer` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `phoshor_coefficient`
--
ALTER TABLE `phoshor_coefficient`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT для таблицы `potassium_coefficient`
--
ALTER TABLE `potassium_coefficient`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT для таблицы `storage`
--
ALTER TABLE `storage`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `data`
--
ALTER TABLE `data`
  ADD CONSTRAINT `data_ibfk_1` FOREIGN KEY (`id_culture`) REFERENCES `cultures` (`id_culture`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `data_ibfk_2` FOREIGN KEY (`id_fertilizer`) REFERENCES `fertilizers` (`id_fertilizer`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `phoshor_coefficient`
--
ALTER TABLE `phoshor_coefficient`
  ADD CONSTRAINT `phoshor_coefficient_ibfk_1` FOREIGN KEY (`id_culture`) REFERENCES `cultures` (`id_culture`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `potassium_coefficient`
--
ALTER TABLE `potassium_coefficient`
  ADD CONSTRAINT `potassium_coefficient_ibfk_1` FOREIGN KEY (`id_culture`) REFERENCES `cultures` (`id_culture`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `storage`
--
ALTER TABLE `storage`
  ADD CONSTRAINT `storage_ibfk_1` FOREIGN KEY (`id_fertilizer`) REFERENCES `fertilizers` (`id_fertilizer`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `storage_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
