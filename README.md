# GribMaths

## Серверная часть

### Перейдите в папку backend
 ```bash
cd backend
```

### Установите виртуальное окружение
 ```bash
python -m venv venv
```
### Активируйте виртуальное окружение
```bash
source venv/Scripts/activate
```

### Установите зависимости
```shell
pip install -r requirements.txt
```

### Создайте папку для хранения базы данных
``` bash
mkdir db
```

### Перейдтие в generator
``` bash
cd generator
```

### Заполните базу данных примерами с помощью генератора
``` bash
python num_gen_to_db.py
```
### Подождите

### Перейдите обратно в backend
``` bash
cd ..
```

### Выполните команду:
``` bash
python main.py
```

## Клиентская часть

### Откройте второй терминал

### Перейдите в папку frontend
```bash
cd frontend
```

### Установите зависимости

```bash
npm install
```

```bash
cp .env.template .env
```

### Запуск сервера

```bash
npm run dev
```

### Перейдите по появившейся ссылке



### Примечание: часть функционала клиентской части выполнена в виде прототипа