<div id="toc" align="center">
  <ul style="list-style: none">
    <summary>
      <h1>Веб-сервис для управления движением денежных средств (ДДС)</h1>
    </summary>
  </ul>
</div>

## Описание

ДДС (движение денежных средств) — это процесс учета, управления и анализа
поступлений и списаний денежных средств компании или частного лица.


## Используемые технологии

![Python](https://img.shields.io/badge/Python-3.14-2B5B84?style=flat&logo=python&logoColor=white&labelColor=1E2229)
![Django](https://img.shields.io/badge/Django-6.1.1-185C37?style=flat&logo=django&logoColor=white&labelColor=1E2229)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-336791?style=flat&logo=postgresql&logoColor=white&labelColor=1E2229)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-29.9.3-1D63ED?style=flat&logo=docker&logoColor=white&labelColor=1E2229)

## Возможности приложения

### Создание записи о движении денежных средств (ДДС)

При создании записи доступны следующие поля:

* **Дата создания записи** — заполняется автоматически, но может быть изменена вручную. 
  * *Пример:* `01.01.2025`
* **Статус** — определяет принадлежность операции (список расширяемый):
  * Бизнес
  * Личное
  * Налог
* **Тип** — направление движения средств (список расширяемый):
  * Пополнение
  * Списание
* **Категория и подкатегория** — иерархическая классификация расходов/доходов (список расширяемый):
  * *Инфраструктура:* `VPS`, `Proxy`
  * *Маркетинг:* `Farpost`, `Avito`
* **Сумма** — количество средств в рублях. 
  * *Пример:* `1 000 р.`
* **Комментарий** *(необязательное поле)* — текстовое описание операции в свободной форме.

### Просмотр списка всех записей

* Вывод таблицы с данными: дата, статус, тип, категория, подкатегория, сумма, комментарий.
* Поддержка фильтрации по дате (с указанием периода дат), статусу, типу, категории и подкатегории.

### Редактирование и удаление записей

* **Редактирование записи** — возможность изменить любую существующую запись.
* **Удаление записи** — возможность удалить любую запись.

### Управление справочниками

* Добавление, редактирование и удаление статусов, типов, категорий и подкатегорий.

### Логические зависимости

* **Подкатегории → Категории:** подкатегории привязаны к конкретным категориям.
* **Категории → Типы:** категории привязаны к определённым типам операций.
  * *Пример:* к типу `Списание` относится категория `Маркетинг`, в которую входят подкатегории `Farpost` и `Avito`.

### Дополнительные возможности
* Автоматическая загрузка курсов валют из внешнего источника (ЦБ РФ) и конвертация сумм.
* Быстрый поиск по записям.
* Выгрузка отфильтрованных данных и финансовой отчётности в формат Excel (`.xlsx`).

## Демонстрация работы проекта


### Добавление справочника
https://github.com/user-attachments/assets/19910b13-5d8d-4f71-80ac-a96a49cdbce5

### Удаление из справочника
Можно удалить несколько значений из списка

https://github.com/user-attachments/assets/1ad2cabc-9c42-48c9-9ec6-4c57a6cd884d

### Добавление с зависимостями

https://github.com/user-attachments/assets/55bb9dc2-4cc4-40b1-8033-94507132b433

### Удаление с зависимостями

https://github.com/user-attachments/assets/5d47318e-1830-4b55-b406-11612a288699

### Добавление транзакции

https://github.com/user-attachments/assets/f26eb031-e5b9-491b-b9ed-d6299cf63be9

### Изменение транзакции

Также можно удалить транзакции

https://github.com/user-attachments/assets/2636670b-2a48-41e3-8108-de497cea57ee

### Фильтрация данных

https://github.com/user-attachments/assets/e539e7f7-1dcf-49b3-bc69-fd78cbe98b05

При нажатии на кнопку "Выгрузить в xlsx" скачается таблица в формате excel
<img width="1433" height="700" alt="image" src="https://github.com/user-attachments/assets/3cab7b3a-62ea-4243-b240-4ab0ed090bae" />

## Запуск проекта

### Скопировать репозиторий
```bash
git clone https://github.com/MRRomenin/DDS.git
```   
```bash
cd DDS
```

В проекте есть .env_example, на основе него нужно собрать конфигурации для запуска БД и Django для файла .env

```bash
cp .env_example .env
```

### Запуск Docker

Далее разворачиваем образ и создаем контейнер
```bash
docker compose up -d --build
```
После запуска сервис будет доступен по адресу: `http://localhost:8000`


---
Запуск проекта локально прошу сюда  [Инструкция по локальному запуску](README_LOCAL_SETUP.md) <img src="https://www.kolobok.us/smiles/standart/declare.gif" align="absmiddle" width="35" alt="secret" />
