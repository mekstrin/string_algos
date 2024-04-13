# Алгоритмы исследования операций, лабораторная работа 1

## ТЗ:

Реализовать и сравнить алгоритмы поиска подстроки в строке.

1) Наивный алгоритм
2) Алгоритм Рабина-Карпа ИЛИ Алгоритм Бойера-Мура-Хорспула (был выбран алгоритм Рабина-Карпа)
3) Алгоритм Кнутта-Мориса-Пратта ИЛИ Алгоритм Ахо-Карасика (был выбран алгоритм Кнутта-Мориса-Пратта)

Необходимо сравнить время работы алгоритма и количество операций сравнения.

## Структура файлов

- benchmarks - тесты
- kmp.py - реализация алгоритма Кнутта-Мориса-Пратта
- naive.py - реализация наивного алгоритма
- rabin_karp.py - реализация алгоритма Рабина-Карпа
- tests.py - запуск и сравнение алгоритмов
- utils.py - загрузка тестов и декоратор для оценивания времени алгоритма (кол-во запусков конфигурируется константой
  NUMBER_OF_STARTS)

## Итоги

Все алгоритмы были реализованы для поиска всех подстрок в строке, 
поэтому в качестве результата получается список индексов начала паттерна в тексте.

- Test: bad_1
  - Naive algo: result - [8], num_of_operations - 18, time in seconds - 1.7e-06.
  - Rabin karp algo: result - [8], num_of_operations - 9, time in seconds - 2.3e-06.
  - KMP algo: result - [8], num_of_operations - 34, time in seconds - 3.3e-06.


- Test: good_1
  - Naive algo: result - [599], num_of_operations - 714, time in seconds - 8.6e-05.
  - Rabin karp algo: result - [599], num_of_operations - 678, time in seconds - 0.0001.
  - KMP algo: result - [599], num_of_operations - 2116, time in seconds - 0.0001.


- Test: bad_2
  - Naive algo: result - [90], num_of_operations - 910, time in seconds - 4.2e-05.
  - Rabin karp algo: result - [90], num_of_operations - 91, time in seconds - 1.2e-05.
  - KMP algo: result - [90], num_of_operations - 320, time in seconds - 1.7e-05.


- Test: good_2
  - Naive algo: result - [610], num_of_operations - 1158, time in seconds - 0.00014.
  - Rabin karp algo: result - [610], num_of_operations - 1074, time in seconds - 0.00018.
  - KMP algo: result - [610], num_of_operations - 3644, time in seconds - 0.00017.


- Test: bad_3
  - Naive algo: result - [900], num_of_operations - 90100, time in seconds - 0.004.
  - Rabin karp algo: result - [900], num_of_operations - 901, time in seconds - 0.00013.
  - KMP algo: result - [900], num_of_operations - 3200, time in seconds - 0.00019.


- Test: good_3
  - Naive algo: result - [1629], num_of_operations - 3554, time in seconds - 0.00054.
  - Rabin karp algo: result - [1629], num_of_operations - 3058, time in seconds - 0.00057.
  - KMP algo: result - [1629], num_of_operations - 11076, time in seconds - 0.00057.


- Test: bad_4
  - Naive algo: result - [4000], num_of_operations - 4001000, time in seconds - 0.19.
  - Rabin karp algo: result - [4000], num_of_operations - 4001, time in seconds - 0.00066.
  - KMP algo: result - [4000], num_of_operations - 17000, time in seconds - 0.001.


- Test: good_4
  - Naive algo: result - [9522], num_of_operations - 10714, time in seconds - 0.0014.
  - Rabin karp algo: result - [9522], num_of_operations - 10623, time in seconds - 0.0016.
  - KMP algo: result - [9522], num_of_operations - 32326, time in seconds - 0.0015.

